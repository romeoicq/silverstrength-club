# SilverStrength Club — AGENTS.md

## Project Overview
SilverStrength Club is a static HTML website for senior health and fitness (65+ audience). All pages are self-contained HTML files with inline CSS — no build system, no framework, no JavaScript dependencies.

## Tech Stack
- **Hosting**: Netlify (manual ZIP deployment)
- **Build**: None — raw HTML files
- **CSS**: Inline `<style>` blocks, no external CSS
- **Fonts**: system-ui stack, no external font loading
- **Images**: Unsplash photography, 2:1 aspect ratio, `loading="lazy"`
- **Analytics**: Google Tag Manager (GTM-MV4CJLH4)

## Key Conventions

### HTML Structure
- Each page has: sticky dark nav → gradient page-header → featured-img div → content section → related articles → footer
- Nav HTML is duplicated across every page (inline, no partials)
- CSS is in `<style>` blocks in `<head>`, not external
- All pages are mobile-responsive (600px breakpoint)

### Naming
- Root pages: `kebab-case.html` (e.g., `mobility-fall-prevention.html`)
- Blog articles: `blog/kebab-case.html` (e.g., `blog/balance-exercises-seniors.html`)
- All internal links omit `.html` on Netlify (auto-normalizes), but source files use `.html` extension

### SEO Requirements
Every page MUST have:
- `<title>` (55-60 chars with " — SilverStrength Club" suffix)
- `<meta name="description">` (150-160 chars)
- `<link rel="canonical">` pointing to Netlify URL
- Open Graph: og:title, og:description, og:image, og:url, og:site_name, og:type, og:locale
- Twitter Card: twitter:card, twitter:title, twitter:description, twitter:image
- `<meta name="robots" content="index, follow, max-image-preview:large">`
- JSON-LD: BreadcrumbList + Article (blog posts) + Organization (homepage)
- Google Tag Manager (head script + noscript body tag)
- Full favicon set: favicon.svg, apple-touch-icon.png (180x180), icon-192x192.png, icon-512x512.png, favicon.ico
- og:title and twitter:title must exactly match <title> (including " — SilverStrength Club" suffix)

### Content Standards
- Minimum 5 h2 sections per article
- Minimum 150 lines of HTML per article
- ALL images from unsplash.com with `?w=800&q=80&fit=crop`
- Featured images in `<div class="featured-img">` between page-header and content
- Body text: 18px+ base, 1.7 line height, high contrast (#1a1a2e on #faf9f6)
- Decision-intent content: include "Best X for Seniors" or buying-guide sections

### Writing Voice
Every article should sound like a knowledgeable friend talking to seniors, not a textbook or blogspam:
- Use contractions ("it's", "you'll", "don't")
- Strip AI vocab: delve, pivotal, testament, underscore, vibrant (figurative), nestled, transformative, groundbreaking
- Replace "serves as"/"stands as"/"represents a" with "is"/"are"
- No signposting: no "let's dive in", "let's explore"
- No generic conclusions: end with specific next steps
- Vary sentence rhythm — mix short and long sentences
- Have opinions — it's OK to say "this is worth trying"

### Deployment
```bash
# Deploy via Netlify ZIP API
~/.hermes/scripts/deploy-silverstrength.sh
```

### Common Pitfalls
1. Do NOT use `read_file()` output to write HTML — it adds line numbers. Use direct string content.
2. Do NOT use `patch` tool on blog/index.html — special chars break it. Use execute_code with `from hermes_tools import terminal`.
3. Every article needs a UNIQUE Unsplash photo ID — no duplicates across articles.
4. Featured image goes between `</section>` (page-header) and `<section class="content">`, not inside content.
5. Blog cards must be in order: date → h3 → post-thumb → post-text (not the reverse).
6. All links use `/blog/slug.html` not `/articles/slug.html`.