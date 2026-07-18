// @ts-check
// Deployment trigger: 2026-05-10

import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://31ns.kr',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('.html'),
    }),
  ],
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  i18n: {
    defaultLocale: 'ko',
    locales: ['ko', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
