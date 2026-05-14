import os
import io
import glob
import re
import subprocess
import time
from datetime import datetime
import mammoth
from markdownify import markdownify as md
from PIL import Image
from deep_translator import GoogleTranslator

# Directories
INPUT_DIR = "input"
OUTPUT_DIR = "output"
ASSETS_REPO_DIR = "31ns-Home-blog-assets"
GITHUB_USER = "promisesmk"
REPO_NAME = "31ns-Home-blog-assets"

def ensure_dirs():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    if not os.path.exists(ASSETS_REPO_DIR):
        print(f"[Error] {ASSETS_REPO_DIR} directory not found. Please clone the repository first.")
        exit(1)

class ImageHandler:
    def __init__(self, post_name):
        self.post_name = post_name
        self.counter = 1
        self.image_dimensions = {} # URL -> (width, height)
        
        self.post_assets_dir = os.path.join(ASSETS_REPO_DIR, post_name)
        if not os.path.exists(self.post_assets_dir):
            os.makedirs(self.post_assets_dir)

    def handle_image(self, image):
        with image.open() as image_stream:
            img = Image.open(io.BytesIO(image_stream.read()))
        
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        max_width = 1200
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int((float(img.height) * float(ratio)))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
        filename = f"img_{self.counter:02d}.webp"
        filepath = os.path.join(self.post_assets_dir, filename)
        img.save(filepath, "WEBP", quality=80)
        self.counter += 1
        
        cdn_url = f"https://cdn.jsdelivr.net/gh/{GITHUB_USER}/{REPO_NAME}@main/{self.post_name}/{filename}"
        self.image_dimensions[cdn_url] = (img.width, img.height)
        return {"src": cdn_url}

def generate_frontmatter(title, description, hero_image, lang):
    date_str = datetime.now().strftime("%Y-%m-%d")
    description = description.replace('"', '\\"')
    return f"""---
title: "{title}"
description: "{description}"
date: {date_str}
lang: "{lang}"
tags: ["Astro", "Blog"]
---
"""

def push_assets_to_github():
    print("[Processing] Uploading optimized images to GitHub...")
    try:
        subprocess.run(["git", "add", "."], cwd=ASSETS_REPO_DIR, check=True, stdout=subprocess.DEVNULL)
        status = subprocess.run(["git", "status", "--porcelain"], cwd=ASSETS_REPO_DIR, capture_output=True, text=True)
        if status.stdout.strip() == "":
            print("No new images to push.")
            return
            
        subprocess.run(["git", "commit", "-m", "Auto-add blog images via script"], cwd=ASSETS_REPO_DIR, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "branch", "-M", "main"], cwd=ASSETS_REPO_DIR, check=True, stdout=subprocess.DEVNULL)
        subprocess.run(["git", "push", "-u", "origin", "main"], cwd=ASSETS_REPO_DIR, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[Success] Successfully pushed images to GitHub! (CDN links are now live)")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to push to GitHub. You may need to push manually inside {ASSETS_REPO_DIR} folder.")

def translate_markdown_2pass(markdown_text):
    translator = GoogleTranslator(source='ko', target='en')
    
    # PASS 1: Hide images using placeholders
    images = []
    def image_replacer(match):
        images.append(match.group(0))
        return f"[[IMG_{len(images)-1}]]"
        
    text_without_images = re.sub(r'<img[^>]+>', image_replacer, markdown_text)
    
    # PASS 2: Chunk text safely (approx 3000 chars per chunk to avoid hitting 5k limit)
    chunks = []
    current_chunk = []
    current_length = 0
    
    paragraphs = text_without_images.split('\n\n')
    for p in paragraphs:
        p_len = len(p)
        if current_length + p_len > 3000:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk = [p]
            current_length = p_len
        else:
            current_chunk.append(p)
            current_length += p_len + 2
            
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
        
    # PASS 3: Translate chunks
    translated_chunks = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            # only translate if there's text (skip empty/pure symbols)
            if re.search(r'[a-zA-Z가-힣]', chunk):
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
            else:
                translated_chunks.append(chunk)
        except Exception as e:
            print(f"  [Warning] Translation chunk failed: {e}")
            translated_chunks.append(chunk)
        time.sleep(0.5)
        
    translated_text = '\n\n'.join(translated_chunks)
    
    # PASS 4: Restore images
    for i, img_tag in enumerate(images):
        translated_text = translated_text.replace(f"[[IMG_{i}]]", img_tag)
        translated_text = re.sub(rf'\[\[\s*IMG_{i}\s*\]\]', img_tag, translated_text)
    
    # PASS 5: Structural Repair (Fixing markdown syntax broken by AI Translator)
    translated_text = re.sub(r'\*\*\s+(.*?)\s+\*\*', r'**\1**', translated_text)
    translated_text = re.sub(r'\*\s+(.*?)\s+\*', r'*\1*', translated_text)
    translated_text = translated_text.replace('< img', '<img').replace('/>', ' />')
    
    return translated_text

def process_file(docx_path):
    basename = os.path.basename(docx_path)
    filename_without_ext = os.path.splitext(basename)[0]
    
    print(f"\nProcessing: {basename}...")
    handler = ImageHandler(filename_without_ext)
    
    with open(docx_path, "rb") as docx_file:
        result = mammoth.convert_to_html(
            docx_file,
            convert_image=mammoth.images.img_element(handler.handle_image)
        )
        html = result.value
            
    # Markdown Conversion
    markdown_content = md(html, heading_style="ATX")
    
    # Replace markdown images with SEO HTML tags
    for cdn_url, (width, height) in handler.image_dimensions.items():
        html_tag = f'<img src="{cdn_url}" width="{width}" height="{height}" loading="lazy" alt="Blog Image" />'
        pattern = r'!\[.*?\]\(' + re.escape(cdn_url) + r'\)'
        markdown_content = re.sub(pattern, html_tag, markdown_content)
        
    # --- Front Matter Automation ---
    hero_image_url = ""
    if handler.image_dimensions:
        hero_image_url = list(handler.image_dimensions.keys())[0] # First image as thumbnail
        
    # Extract plain text for description
    plain_text = re.sub(r'<[^>]+>', ' ', html)
    plain_text = re.sub(r'\s+', ' ', plain_text)
    description_ko = plain_text[:120].strip() + "..." if len(plain_text) > 120 else plain_text.strip()
    
    # --- Multilingual File Structure ---
    post_output_dir = os.path.join(OUTPUT_DIR, filename_without_ext)
    if not os.path.exists(post_output_dir):
        os.makedirs(post_output_dir)
        
    # 1. Save Korean Version
    frontmatter_ko = generate_frontmatter(filename_without_ext, description_ko, hero_image_url, "ko")
    ko_content = frontmatter_ko + "\n" + markdown_content
    ko_path = os.path.join(post_output_dir, "index.ko.md")
    with open(ko_path, "w", encoding="utf-8") as f:
        f.write(ko_content)
    print(f"[Success] Saved Korean file: {ko_path}")
    
    # 2. Translate and Save English Version
    print("[Processing] Translating to English (Pass 1: Translation, Pass 2: Markdown Repair)...")
    translated_markdown = translate_markdown_2pass(markdown_content)
    
    try:
        description_en = GoogleTranslator(source='ko', target='en').translate(description_ko)
    except:
        description_en = description_ko
        
    frontmatter_en = generate_frontmatter(filename_without_ext + " (EN)", description_en, hero_image_url, "en")
    en_content = frontmatter_en + "\n" + translated_markdown
    en_path = os.path.join(post_output_dir, "index.en.md")
    with open(en_path, "w", encoding="utf-8") as f:
        f.write(en_content)
    print(f"[Success] Saved English file: {en_path}")

    if handler.counter > 1:
        print(f"[Info] Extracted {handler.counter - 1} images.")

def main():
    ensure_dirs()
    docx_files = glob.glob(os.path.join(INPUT_DIR, "*.docx"))
    
    if not docx_files:
        print(f"[Error] No .docx files found in '{INPUT_DIR}' directory.")
        return
        
    for filepath in docx_files:
        process_file(filepath)
        
    push_assets_to_github()
    print("\n[Done] All processes completed! Move the folders in 'output/' to your Astro src/content/blog directory.")

if __name__ == "__main__":
    main()
