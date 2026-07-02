"""
One-time script to re-translate the existing index.ko.md into index.en.md.
Run from: word_to_blog/ directory.
"""
import os, re, time, sys
sys.stdout.reconfigure(encoding='utf-8')
from deep_translator import GoogleTranslator
from datetime import datetime

KO_FILE = r"..\src\content\blog\nRF52805_BLE모듈_개발기술참고문서_이미지포함\index.ko.md"
EN_FILE = r"..\src\content\blog\nRF52805_BLE모듈_개발기술참고문서_이미지포함\index.en.md"

def translate_markdown_2pass(markdown_text):
    translator = GoogleTranslator(source='ko', target='en')

    # PASS 1: Hide images with placeholders
    images = []
    def image_replacer(match):
        images.append(match.group(0))
        return f"[[IMG_{len(images)-1}]]"
    text_without_images = re.sub(r'<img[^>]+>', image_replacer, markdown_text)

    # PASS 2: Build chunks (~3000 chars each)
    chunks, current_chunk, current_length = [], [], 0
    for p in text_without_images.split('\n\n'):
        p_len = len(p)
        if current_length + p_len > 3000:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk, current_length = [p], p_len
        else:
            current_chunk.append(p)
            current_length += p_len + 2
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))

    # PASS 3: Translate
    translated_chunks = []
    total = len(chunks)
    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            if re.search(r'[가-힣]', chunk):
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
                print(f"  [{i+1}/{total}] Translated chunk ({len(chunk)} chars)")
            else:
                translated_chunks.append(chunk)
                print(f"  [{i+1}/{total}] Skipped (no Korean)")
        except Exception as e:
            print(f"  [{i+1}/{total}] Warning: {e}")
            translated_chunks.append(chunk)
        time.sleep(0.5)

    translated_text = '\n\n'.join(translated_chunks)

    # PASS 4: Restore images
    for i, img_tag in enumerate(images):
        translated_text = translated_text.replace(f"[[IMG_{i}]]", img_tag)
        translated_text = re.sub(rf'\[\[\s*IMG_{i}\s*\]\]', img_tag, translated_text)

    # PASS 5: Fix markdown syntax
    translated_text = re.sub(r'\*\*\s+(.*?)\s+\*\*', r'**\1**', translated_text)
    translated_text = re.sub(r'\*\s+(.*?)\s+\*', r'*\1*', translated_text)
    translated_text = translated_text.replace('< img', '<img')

    return translated_text

# --- Main ---
print(f"Reading: {KO_FILE}")
with open(KO_FILE, 'r', encoding='utf-8') as f:
    ko_full = f.read()

# Split frontmatter and body
parts = ko_full.split('---', 2)
body_ko = parts[2].strip() if len(parts) >= 3 else ko_full

print(f"Translating {len(body_ko)} characters of body text...")
body_en = translate_markdown_2pass(body_ko)

# Translate description
desc_match = re.search(r'description:\s*"(.+?)"', ko_full)
desc_ko = desc_match.group(1) if desc_match else ""
try:
    desc_en = GoogleTranslator(source='ko', target='en').translate(desc_ko)
except:
    desc_en = desc_ko

# Build English frontmatter
date_str = datetime.now().strftime("%Y-%m-%d")
frontmatter_en = f'''---
title: "nRF52805 BLE Module Development Technical Reference"
description: "{desc_en}"
date: {date_str}
lang: "en"
tags: ["Astro", "Blog"]
---'''

en_full = frontmatter_en + "\n\n" + body_en

print(f"Writing: {EN_FILE}")
with open(EN_FILE, 'w', encoding='utf-8') as f:
    f.write(en_full)

print("\n[Done] English file re-generated successfully!")
