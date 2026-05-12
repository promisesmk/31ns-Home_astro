import sharp from 'sharp';
import fs from 'fs/promises';
import path from 'path';
import mammoth from 'mammoth';

const CONFIG = {
    inbox: './src/content/temp_inbox',
    outImageDir: './src/assets/images/blog',
    maxWidth: 1200,
    quality: 80
};

async function ensureDirectory(dir) {
    try {
        await fs.access(dir);
    } catch {
        await fs.mkdir(dir, { recursive: true });
    }
}

async function processWordFiles() {
    const files = await fs.readdir(CONFIG.inbox);
    const docxFiles = files.filter(file => file.endsWith('.docx'));

    for (const file of docxFiles) {
        console.log(`\n📄 워드 파일 처리 중: ${file}`);
        const inputPath = path.join(CONFIG.inbox, file);
        const fileName = path.parse(file).name;
        
        let imageCounter = 1;

        // 워드에서 이미지 추출 및 HTML 변환
        const result = await mammoth.convertToHtml({ path: inputPath }, {
            convertImage: mammoth.images.inline(async (element) => {
                const extension = element.contentType.split("/")[1];
                const imageFileName = `${fileName}-img-${imageCounter++}.${extension}`;
                const imagePath = path.join(CONFIG.inbox, imageFileName);
                
                const buffer = await element.read();
                await fs.writeFile(imagePath, buffer);
                
                return { src: imageFileName }; // 임시 경로 반환
            })
        });

        const htmlPath = path.join(CONFIG.inbox, `${fileName}.html`);
        await fs.writeFile(htmlPath, result.value);
        console.log(`✅ 워드 텍스트 추출 완료: ${fileName}.html`);
        console.log(`✅ 이미지 ${imageCounter - 1}개 추출 완료.`);
    }
}

async function processImages() {
    const files = await fs.readdir(CONFIG.inbox);
    const imageFiles = files.filter(file => /\.(jpg|jpeg|png|gif)$/i.test(file));

    if (imageFiles.length === 0) {
        console.log('처리할 이미지가 없습니다.');
        return;
    }

    console.log(`\n🖼️ ${imageFiles.length}개의 이미지 최적화를 시작합니다...`);
    await ensureDirectory(CONFIG.outImageDir);

    for (const file of imageFiles) {
        const inputPath = path.join(CONFIG.inbox, file);
        const fileName = path.parse(file).name;
        const outputPath = path.join(CONFIG.outImageDir, `${fileName}.webp`);

        await sharp(inputPath)
            .resize({ width: CONFIG.maxWidth, withoutEnlargement: true })
            .webp({ quality: CONFIG.quality })
            .toFile(outputPath);

        console.log(`✅ 최적화 완료: ${file} -> ${fileName}.webp`);
    }
}

async function main() {
    try {
        await processWordFiles();
        await processImages();
        console.log('\n✨ 모든 전처리가 완료되었습니다! 이제 제가 내용을 체계화할 준비가 되었습니다.');
    } catch (err) {
        console.error('에러 발생:', err);
    }
}

main();
