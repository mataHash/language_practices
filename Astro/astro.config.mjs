// @ts-check
import { defineConfig } from 'astro/config';

import netlify from '@astrojs/netlify';

import preact from '@astrojs/preact';

// https://astro.build/config
export default defineConfig({
  output: 'static',
  site: "https://example.com",
  adapter: netlify(),
  integrations: [preact()]
});