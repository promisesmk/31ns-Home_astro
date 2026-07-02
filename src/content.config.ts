import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    lang: z.enum(['ko', 'en']),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

const faq = defineCollection({
  loader: glob({
    pattern: '**/*.md',
    base: './src/content/faq',
    id: ({ entry }) => entry.replace(/\.md$/, ''),
  }),
  schema: z.object({
    title: z.string(),
    seoTitle: z.string(),
    description: z.string(),
    category: z.string(),
    tags: z.array(z.string()).default([]),
    date: z.coerce.date().optional(),
    lang: z.enum(['ko', 'en']).default('ko'),
    slug: z.string(),
  }),
});

export const collections = { blog, faq };
