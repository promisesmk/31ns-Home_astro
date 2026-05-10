import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const blog = await getCollection('blog', ({ data }) => !data.draft);
  
  // Sort by date descending
  blog.sort((a, b) => b.data.date.getTime() - a.data.date.getTime());

  return rss({
    title: '31NS-Tech Hardware Lab',
    description: '20년 이상 경력의 RF/하드웨어 전문가가 제공하는 토털 엔지니어링 솔루션',
    site: context.site,
    items: blog.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description,
      link: post.data.lang === 'en' ? `/en/blog/${post.id}/` : `/blog/${post.id}/`,
    })),
    customData: `<language>ko-kr</language>`,
  });
}
