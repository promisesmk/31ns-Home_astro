"""
word_to_blog.py — Word to Astro Blog Pipeline
==============================================
기능:
  1. input/*.docx → 이미지 추출 → WebP 압축 → CDN 저장소 자동 push
  2. 한글 마크다운(index.ko.md) 생성
  3. 영문 마크다운(index.en.md) 생성 (동일 이미지 CDN URL 공유)
  4. SEO 완전 자동화 (description, heroImage, title)
  5. GitHub 용량 최적화 (WebP 압축, 이미지 중복 업로드 없음)

실행: python -X utf8 word_to_blog.py
결과: output/<포스트명>/index.ko.md + index.en.md
"""

import os, io, glob, re, subprocess, time, sys
from datetime import datetime

import mammoth
from markdownify import markdownify as md_convert
from PIL import Image
from deep_translator import GoogleTranslator

# ─── 설정 ──────────────────────────────────────────────
INPUT_DIR      = "input"
OUTPUT_DIR     = "output"
ASSETS_REPO    = "31ns-Home-blog-assets"   # assets 저장소 폴더
GITHUB_USER    = "promisesmk"
REPO_NAME      = "31ns-Home-blog-assets"
CDN_BASE       = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@main"

# 이미지 최적화 설정
IMG_MAX_WIDTH  = 1200   # 최대 너비(px)
IMG_QUALITY    = 75     # WebP 품질 (0~100, 낮을수록 용량↓ 화질↓)
                        # 75 = 고품질 유지하면서 60~70% 용량 절약

# 번역 설정
CHUNK_SIZE     = 2500   # 구글 번역 1회 최대 글자 수
TRANSLATE_DELAY = 0.4   # 요청 간격(초) — 속도 제한 방지
# ───────────────────────────────────────────────────────


# ══════════════════════════════════════════════════════
# 1. 디렉터리 검증
# ══════════════════════════════════════════════════════
def ensure_dirs():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.exists(ASSETS_REPO):
        print(f"[Error] '{ASSETS_REPO}' 폴더가 없습니다. assets 저장소를 clone 해주세요.")
        sys.exit(1)


# ══════════════════════════════════════════════════════
# 2. 이미지 핸들러 (mammoth 콜백)
# ══════════════════════════════════════════════════════
class ImageHandler:
    def __init__(self, post_slug: str):
        self.post_slug  = post_slug
        self.counter    = 1
        self.cdn_urls   = []          # 순서대로 저장 (첫 번째 = heroImage)
        self.dimensions = {}          # cdn_url → (width, height)

        self.save_dir = os.path.join(ASSETS_REPO, post_slug)
        os.makedirs(self.save_dir, exist_ok=True)

    def handle_image(self, image):
        """mammoth 이미지 콜백 — WebP 변환 후 assets 저장소에 저장"""
        with image.open() as stream:
            img = Image.open(io.BytesIO(stream.read()))

        # RGBA/팔레트 → RGB 변환 (WebP 저장 필수)
        if img.mode in ("RGBA", "P", "LA"):
            img = img.convert("RGB")

        # 비율 유지 리사이즈
        if img.width > IMG_MAX_WIDTH:
            ratio = IMG_MAX_WIDTH / img.width
            img = img.resize(
                (IMG_MAX_WIDTH, int(img.height * ratio)),
                Image.Resampling.LANCZOS
            )

        filename = f"img_{self.counter:02d}.webp"
        filepath = os.path.join(self.save_dir, filename)
        img.save(filepath, "WEBP", quality=IMG_QUALITY, method=6)
        self.counter += 1

        cdn_url = f"{CDN_BASE}/{self.post_slug}/{filename}"
        self.cdn_urls.append(cdn_url)
        self.dimensions[cdn_url] = (img.width, img.height)
        return {"src": cdn_url}


# ══════════════════════════════════════════════════════
# 3. 마크다운 후처리 — 이미지 태그를 SEO용 HTML로 교체
# ══════════════════════════════════════════════════════
def replace_images_with_html(markdown: str, dimensions: dict) -> str:
    """
    ![alt](cdn_url) → <img src="..." width="..." height="..." loading="lazy" alt="..." />
    width/height 명시 → CLS(레이아웃 이동) 방지 → Core Web Vitals 향상
    """
    for cdn_url, (w, h) in dimensions.items():
        img_tag = (
            f'<img src="{cdn_url}" width="{w}" height="{h}" '
            f'loading="lazy" alt="Blog Image" />'
        )
        pattern = r'!\[.*?\]\(' + re.escape(cdn_url) + r'\)'
        markdown = re.sub(pattern, img_tag, markdown)
    return markdown


# ══════════════════════════════════════════════════════
# 4. 번역 엔진 (2-Pass: 번역 → 마크다운 문법 복구)
# ══════════════════════════════════════════════════════
def translate_ko_to_en(markdown_text: str) -> str:
    """
    Pass 1 — 이미지 태그를 플레이스홀더로 교체 (번역 오염 방지)
    Pass 2 — 문단 단위 청크 구성
    Pass 3 — 구글 번역 API 호출
    Pass 4 — 이미지 태그 복원
    Pass 5 — 마크다운 문법 수리 (번역기가 깨뜨리는 ** * 등 복구)
    """
    translator = GoogleTranslator(source='ko', target='en')

    # ── Pass 1: 이미지 숨기기
    images = []
    def hide_image(m):
        images.append(m.group(0))
        return f"⟦IMG{len(images)-1}⟧"   # 번역기가 건드리기 어려운 기호 사용

    text = re.sub(r'<img[^>]+/>', hide_image, markdown_text)

    # ── Pass 2: 청크 구성
    chunks, current, cur_len = [], [], 0
    for para in text.split('\n\n'):
        plen = len(para)
        if cur_len + plen > CHUNK_SIZE:
            if current:
                chunks.append('\n\n'.join(current))
            current, cur_len = [para], plen
        else:
            current.append(para)
            cur_len += plen + 2
    if current:
        chunks.append('\n\n'.join(current))

    total = len(chunks)
    print(f"  → 총 {total}개 청크 번역 시작...")

    # ── Pass 3: 번역
    translated_chunks = []
    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if not chunk:
            continue
        # 한글이 없으면 번역 불필요 (영문 기술 용어, URL 등)
        if not re.search(r'[가-힣]', chunk):
            translated_chunks.append(chunk)
            continue
        try:
            result = translator.translate(chunk)
            translated_chunks.append(result if result else chunk)
            if (i + 1) % 10 == 0:
                print(f"  → {i+1}/{total} 청크 완료")
        except Exception as e:
            print(f"  [경고] 청크 {i+1} 번역 실패: {e}")
            translated_chunks.append(chunk)
        time.sleep(TRANSLATE_DELAY)

    translated = '\n\n'.join(translated_chunks)

    # ── Pass 4: 이미지 복원
    for i, tag in enumerate(images):
        # 번역기가 플레이스홀더를 약간 변형할 수 있으므로 유연하게 매칭
        translated = re.sub(rf'⟦\s*IMG\s*{i}\s*⟧', tag, translated)
        translated = translated.replace(f"⟦IMG{i}⟧", tag)

    # ── Pass 5: 마크다운 문법 복구
    # 번역기가 ** bold ** → **bold**로 공백을 넣는 경우 수정
    translated = re.sub(r'\*\*\s+(.+?)\s+\*\*', r'**\1**', translated)
    translated = re.sub(r'\*\s+(.+?)\s+\*', r'*\1*', translated)
    # 번역기가 ## 제목 뒤 줄바꿈을 없애는 경우
    translated = re.sub(r'(#{1,6})\s*(.+)', r'\1 \2', translated)

    return translated


# ══════════════════════════════════════════════════════
# 5. Front Matter 생성 (SEO 완전 자동화)
# ══════════════════════════════════════════════════════
def make_frontmatter(title: str, description: str, lang: str) -> str:
    """
    Astro content.config.ts 스키마에 맞게 frontmatter 생성
    필수 필드: title, description, date, lang, tags
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    # YAML에서 따옴표 이스케이프
    title       = title.replace('"', '\\"')
    description = description.replace('"', '\\"')
    return f"""---
title: "{title}"
description: "{description}"
date: {date_str}
lang: "{lang}"
tags: ["Hardware", "BLE", "RF", "Embedded"]
draft: false
---
"""


# ══════════════════════════════════════════════════════
# 6. assets 저장소 GitHub push
# ══════════════════════════════════════════════════════
def push_assets():
    print("\n[GitHub] assets 저장소 push 중...")
    try:
        r = subprocess.run(["git", "add", "."], cwd=ASSETS_REPO, capture_output=True)
        status = subprocess.run(
            ["git", "status", "--porcelain"], cwd=ASSETS_REPO,
            capture_output=True, text=True, encoding='utf-8'
        )
        if not status.stdout.strip():
            print("[GitHub] 새 이미지 없음 — push 생략")
            return
        subprocess.run(
            ["git", "commit", "-m", "auto: add blog images"],
            cwd=ASSETS_REPO, capture_output=True
        )
        subprocess.run(
            ["git", "push", "-u", "origin", "main"],
            cwd=ASSETS_REPO, capture_output=True
        )
        print("[GitHub] 이미지 push 완료 ✓")
    except Exception as e:
        print(f"[GitHub] push 실패: {e}\n→ {ASSETS_REPO} 폴더에서 수동 push 하세요.")


# ══════════════════════════════════════════════════════
# 7. docx 파일 1개 처리
# ══════════════════════════════════════════════════════
def process_docx(docx_path: str):
    basename = os.path.basename(docx_path)
    slug     = os.path.splitext(basename)[0]   # 파일명 = 포스트 슬러그
    print(f"\n{'='*60}")
    print(f"처리 중: {basename}")
    print(f"{'='*60}")

    # ── 1. Word → HTML → Markdown 변환
    handler = ImageHandler(slug)
    with open(docx_path, "rb") as f:
        result = mammoth.convert_to_html(
            f, convert_image=mammoth.images.img_element(handler.handle_image)
        )
    html = result.value

    markdown_raw = md_convert(html, heading_style="ATX")
    markdown_ko  = replace_images_with_html(markdown_raw, handler.dimensions)

    img_count = handler.counter - 1
    print(f"  이미지 추출: {img_count}장 → WebP 압축 완료")

    # ── 2. 자동 메타데이터 추출
    # heroImage: 첫 번째 이미지 URL
    hero_url = handler.cdn_urls[0] if handler.cdn_urls else ""

    # description: HTML 순수 텍스트의 첫 160자
    plain = re.sub(r'<[^>]+>', ' ', html)
    plain = re.sub(r'\s+', ' ', plain).strip()
    desc_ko = (plain[:157] + "...") if len(plain) > 160 else plain

    # ── 3. 한글 MD 파일 저장
    out_dir = os.path.join(OUTPUT_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)

    fm_ko = make_frontmatter(slug, desc_ko, "ko")
    ko_path = os.path.join(out_dir, "index.ko.md")
    with open(ko_path, "w", encoding="utf-8") as f:
        f.write(fm_ko + "\n" + markdown_ko)
    print(f"  [완료] 한글 파일: {ko_path}")

    # ── 4. 영문 번역 후 MD 파일 저장
    #       이미지 태그는 그대로 유지 (동일 CDN URL 공유)
    print("  [번역] 한→영 번역 시작...")
    markdown_en = translate_ko_to_en(markdown_ko)

    try:
        desc_en = GoogleTranslator(source='ko', target='en').translate(desc_ko)
    except:
        desc_en = desc_ko

    # 영문 제목: 파일명에서 기술적 의미를 살린 영문 제목으로 번역
    try:
        title_en_raw = slug.replace("_", " ")
        title_en = GoogleTranslator(source='ko', target='en').translate(title_en_raw)
    except:
        title_en = slug + " (EN)"

    fm_en = make_frontmatter(title_en, desc_en, "en")
    en_path = os.path.join(out_dir, "index.en.md")
    with open(en_path, "w", encoding="utf-8") as f:
        f.write(fm_en + "\n" + markdown_en)
    print(f"  [완료] 영문 파일: {en_path}")

    # ── 5. 결과 요약
    print(f"\n  📁 출력 폴더: {out_dir}/")
    print(f"     ├─ index.ko.md  ({os.path.getsize(ko_path)//1024} KB)")
    print(f"     └─ index.en.md  ({os.path.getsize(en_path)//1024} KB)")
    print(f"  🖼  이미지: {img_count}장 → CDN: {CDN_BASE}/{slug}/")


# ══════════════════════════════════════════════════════
# 8. 메인
# ══════════════════════════════════════════════════════
def main():
    ensure_dirs()

    docx_files = glob.glob(os.path.join(INPUT_DIR, "*.docx"))
    if not docx_files:
        print(f"[오류] '{INPUT_DIR}' 폴더에 .docx 파일이 없습니다.")
        return

    for path in docx_files:
        process_docx(path)

    push_assets()

    print(f"\n{'='*60}")
    print("✅ 모든 처리 완료!")
    print(f"   output/ 폴더의 포스트 폴더를 Astro의")
    print(f"   src/content/blog/ 로 옮기면 업로드 끝입니다.")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
