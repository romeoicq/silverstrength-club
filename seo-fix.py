#!/usr/bin/env python3
"""Fix SilverStrength SEO and usability issues across all pages."""
import os
import re

SITE_DIR = "/home/omeo_urke/silverstrength"

# ============================================================
# IMPROVED CSS - Homepage (has hero, features, grid, card, cta)
# ============================================================
HOMEPAGE_CSS = """*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 20px; scroll-behavior: smooth; }
body { font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif; line-height: 1.7; color: #1a1a2e; background: #faf9f6; }
a { color: #2d6a4f; text-decoration: none; font-weight: 600; }
a:hover { text-decoration: underline; }
a:focus-visible { outline: 2px solid #2d6a4f; outline-offset: 3px; border-radius: 2px; }
img { max-width: 100%; height: auto; }
.featured-img { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; margin-top: 1.5rem; border-radius: 10px; overflow: hidden; }
.featured-img img { width: 100%; height: auto; display: block; border-radius: 10px; aspect-ratio: 2/1; object-fit: cover; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }
nav { background: #1a1a2e; padding: 1rem 0; position: sticky; top: 0; z-index: 100; }
nav .container { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.5rem; }
nav a { color: #e0e0e0; font-size: 0.9rem; padding: 0.5rem 0.7rem; border-radius: 4px; display: inline-flex; align-items: center; min-height: 44px; }
nav a:hover { color: #b7e4c7; text-decoration: none; background: rgba(255,255,255,0.08); }
nav .logo { font-size: 1.2rem; font-weight: 700; color: #b7e4c7; }
.hero { background: linear-gradient(135deg, #1a1a2e 0%, #2d6a4f 100%); color: white; padding: 5rem 0 4rem; text-align: center; }
.hero h1 { font-size: 2.8rem; line-height: 1.2; margin-bottom: 1rem; font-weight: 800; }
.hero p { font-size: 1.1rem; max-width: 700px; margin: 0 auto 2rem; color: #d8f3dc; }
.btn { display: inline-block; background: #95d5b2; color: #1a1a2e; padding: 0.8rem 2rem; border-radius: 8px; font-weight: 700; font-size: 1rem; transition: background 0.2s; min-height: 44px; line-height: 1.4; }
.btn:hover { background: #74c69d; text-decoration: none; }
.features { padding: 4rem 0; }
.features h2 { text-align: center; font-size: 2rem; margin-bottom: 2.5rem; color: #1a1a2e; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.card { background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 2px 12px rgba(0,0,0,0.06); transition: transform 0.2s; }
.card:hover { transform: translateY(-3px); }
.card h3 { font-size: 1.3rem; margin-bottom: 0.8rem; color: #2d6a4f; }
.card p { font-size: 0.9rem; color: #555; margin-bottom: 1rem; max-width: 70ch; }
.card a { font-size: 0.85rem; }
.cta { background: #2d6a4f; color: white; padding: 3.5rem 0; text-align: center; }
.cta h2 { font-size: 2rem; margin-bottom: 0.8rem; }
.cta p { font-size: 1rem; margin-bottom: 1.5rem; opacity: 0.9; }
.cta .btn { background: #d8f3dc; color: #1a1a2e; }
.cta .btn:hover { background: #b7e4c7; }
footer { background: #1a1a2e; color: #999; padding: 2rem 0; text-align: center; font-size: 0.8rem; }
footer a { color: #95d5b2; }
@media (max-width: 768px) { html { font-size: 19px; } .hero h1 { font-size: 2.2rem; } .hero { padding: 3.5rem 0 3rem; } .features h2 { font-size: 1.6rem; } .cta h2 { font-size: 1.6rem; } }
@media (max-width: 600px) { html { font-size: 18px; } .hero h1 { font-size: 1.8rem; } nav .container { justify-content: center; } nav a { font-size: 0.8rem; padding: 0.4rem 0.5rem; } .hero { padding: 3rem 0 2.5rem; } .features h2 { font-size: 1.4rem; } .features { padding: 2.5rem 0; } .grid { gap: 1.2rem; } }
@media (max-width: 400px) { nav a { font-size: 0.75rem; padding: 0.35rem 0.4rem; } .hero h1 { font-size: 1.5rem; } }"""

# ============================================================
# IMPROVED CSS - Article/Content pages
# ============================================================
ARTICLE_CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:20px;scroll-behavior:smooth}
body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;line-height:1.7;color:#1a1a2e;background:#faf9f6}
a{color:#2d6a4f;text-decoration:none;font-weight:600}
a:hover{text-decoration:underline}
a:focus-visible{outline:2px solid #2d6a4f;outline-offset:3px;border-radius:2px}
.container{max-width:1100px;margin:0 auto;padding:0 1.5rem}
nav{background:#1a1a2e;padding:1rem 0;position:sticky;top:0;z-index:100}
nav .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem}
nav a{color:#e0e0e0;font-size:0.9rem;padding:0.5rem 0.7rem;border-radius:4px;display:inline-flex;align-items:center;min-height:44px}
nav a:hover{color:#b7e4c7;text-decoration:none;background:rgba(255,255,255,0.08)}
nav .logo{font-size:1.2rem;font-weight:700;color:#b7e4c7}
.page-header{background:linear-gradient(135deg,#1a1a2e,#2d6a4f);color:white;padding:3rem 0 2.5rem;text-align:center}
.page-header h1{font-size:2.2rem;margin-bottom:0.5rem}
.page-header p{font-size:1rem;color:#d8f3dc;max-width:650px;margin:0 auto}
.content{padding:3rem 0}
.content h2{font-size:1.5rem;color:#2d6a4f;margin:2rem 0 1rem}
.content h3{font-size:1.2rem;color:#1a1a2e;margin:1.5rem 0 0.8rem}
.content p{font-size:0.95rem;color:#444;margin-bottom:1rem;max-width:70ch}
.content ul{font-size:0.95rem;color:#444;margin:0 0 1.5rem 1.5rem;list-style:disc}
.content li{margin-bottom:0.5rem}
.featured-img{max-width:1100px;margin:0 auto;padding:0 1.5rem;margin-top:1.5rem;border-radius:10px;overflow:hidden}
.featured-img img{width:100%;height:auto;display:block;border-radius:10px;aspect-ratio:2/1;object-fit:cover}
.tip-box{background:#d8f3dc;border-radius:10px;padding:1.5rem;margin:1.5rem 0;border-left:4px solid #2d6a4f}
.tip-box strong{color:#2d6a4f}
.back-link{display:inline-block;margin-top:1rem;font-size:0.9rem;color:#2d6a4f}
footer{background:#1a1a2e;color:#999;padding:2rem 0;text-align:center;font-size:0.8rem;margin-top:2rem}
@media(max-width:768px){html{font-size:19px}.page-header h1{font-size:1.8rem}}
@media(max-width:600px){html{font-size:18px}.page-header h1{font-size:1.6rem;padding:2.5rem 0 2rem}nav .container{justify-content:center}nav a{font-size:0.8rem;padding:0.4rem 0.5rem}}
@media(max-width:400px){nav a{font-size:0.75rem;padding:0.35rem 0.4rem}}"""

# ============================================================
# IMPROVED CSS - Blog index pages
# ============================================================
BLOG_CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{font-size:20px;scroll-behavior:smooth}
body{font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;line-height:1.7;color:#1a1a2e;background:#faf9f6}
a{color:#2d6a4f;text-decoration:none;font-weight:600}
a:hover{text-decoration:underline}
a:focus-visible{outline:2px solid #2d6a4f;outline-offset:3px;border-radius:2px}
.container{max-width:1100px;margin:0 auto;padding:0 1.5rem}
nav{background:#1a1a2e;padding:1rem 0;position:sticky;top:0;z-index:100}
nav .container{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem}
nav a{color:#e0e0e0;font-size:0.9rem;padding:0.5rem 0.7rem;border-radius:4px;display:inline-flex;align-items:center;min-height:44px}
nav a:hover{color:#b7e4c7;text-decoration:none;background:rgba(255,255,255,0.08)}
nav .logo{font-size:1.2rem;font-weight:700;color:#b7e4c7}
.page-header{background:linear-gradient(135deg,#1a1a2e,#2d6a4f);color:white;padding:3rem 0 2.5rem;text-align:center}
.page-header h1{font-size:2.2rem;margin-bottom:0.5rem}
.page-header p{font-size:1rem;color:#d8f3dc}
.content{padding:3rem 0}
.content h2{font-size:1.5rem;color:#2d6a4f;margin:2rem 0 1rem}
.post-list{display:grid;gap:1.5rem}
.post-card{background:white;border-radius:10px;padding:1.5rem;box-shadow:0 2px 8px rgba(0,0,0,0.06)}
.post-card h3{font-size:1.2rem;margin-bottom:0.5rem}
.post-card h3 a{color:#1a1a2e}
.post-card h3 a:hover{color:#2d6a4f}
.post-card .date{font-size:0.75rem;color:#888;margin-bottom:0.5rem}
.post-card p{font-size:0.85rem;color:#555;margin-bottom:0.5rem}
.post-card a{font-size:0.85rem}
.post-thumb img{display:block;border-radius:10px;aspect-ratio:2/1;object-fit:cover}
footer{background:#1a1a2e;color:#999;padding:2rem 0;text-align:center;font-size:0.8rem;margin-top:2rem}
@media(max-width:768px){html{font-size:19px}.page-header h1{font-size:1.8rem}}
@media(max-width:600px){html{font-size:18px}.page-header h1{font-size:1.6rem}nav .container{justify-content:center}nav a{font-size:0.8rem;padding:0.4rem 0.5rem}}
@media(max-width:400px){nav a{font-size:0.75rem;padding:0.35rem 0.4rem}}"""

# ============================================================
# DETECT PAGE TYPE AND FIX
# ============================================================

def detect_page_type(html):
    """Detect if a page is homepage, article, or blog index based on content."""
    if re.search(r'class="hero"', html):
        return "homepage"
    if re.search(r'class="post-list"', html):
        return "blog"
    if re.search(r'class="page-header"', html):
        return "article"
    return "unknown"

def replace_style_block(html, new_css):
    """Replace everything between <style> and </style>."""
    return re.sub(
        r'<style>.*?</style>',
        f'<style>{new_css}</style>',
        html,
        count=1,
        flags=re.DOTALL
    )

def fix_homepage_specifics(html):
    """Fix homepage-specific SEO issues."""
    # Fix og:title to match the <title> tag
    html = re.sub(
        r'<meta property="og:title" content="SilverStrength Club">',
        '<meta property="og:title" content="SilverStrength Club — Healthy Aging & Fitness for Seniors 65+">',
        html
    )
    # Fix twitter:title to match
    html = re.sub(
        r'<meta name="twitter:title" content="SilverStrength Club">',
        '<meta name="twitter:title" content="SilverStrength Club — Healthy Aging & Fitness for Seniors 65+">',
        html
    )
    # Fix og:description to match meta description (more keyword-rich)
    html = re.sub(
        r'<meta property="og:description" content="Stay strong, mobile, and independent at any age.">',
        '<meta property="og:description" content="Expert-guided mobility exercises, resistance band workouts, strength training, and nutrition tips for healthy aging. Built for seniors 65+.">',
        html
    )
    # Fix twitter:description to match
    html = re.sub(
        r'<meta name="twitter:description" content="Stay strong, mobile, and independent at any age.">',
        '<meta name="twitter:description" content="Expert-guided mobility exercises, resistance band workouts, strength training, and nutrition tips for healthy aging. Built for seniors 65+.">',
        html
    )
    # Improve H1 to include a primary keyword
    html = html.replace(
        '<h1>Stronger Every Year.<br>Independent For Life.</h1>',
        '<h1>Senior Fitness &amp; Healthy Aging<br>Stronger Every Year. Independent For Life.</h1>'
    )
    # Add og:image:width and og:image:height after og:image
    html = re.sub(
        r'(<meta property="og:image" content="[^"]+">)',
        r'\1\n<meta property="og:image:width" content="800">\n<meta property="og:image:height" content="600">',
        html
    )
    return html

def fix_page(filepath):
    """Fix CSS and SEO issues in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    page_type = detect_page_type(html)
    
    if page_type == "homepage":
        new_css = HOMEPAGE_CSS
        html = fix_homepage_specifics(html)
    elif page_type == "blog":
        new_css = BLOG_CSS
    else:  # article or unknown
        new_css = ARTICLE_CSS
    
    old_html = html
    html = replace_style_block(html, new_css)
    
    if html == old_html:
        return f"NO CHANGE ({page_type})"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return f"UPDATED ({page_type})"

# ============================================================
# RUN
# ============================================================
# Get all HTML files excluding google verification
html_files = []
for root, dirs, files in os.walk(SITE_DIR):
    for f in files:
        if f.endswith('.html'):
            fp = os.path.join(root, f)
            # Skip google verification files
            if 'google' in f and f.endswith('.html'):
                print(f"SKIP (google verify): {f}")
                continue
            html_files.append(fp)

changed = []
nochange = []
for fp in sorted(html_files):
    rel = os.path.relpath(fp, SITE_DIR)
    result = fix_page(fp)
    if "UPDATED" in result:
        changed.append((rel, result))
    else:
        nochange.append((rel, result))

print(f"=== RESULTS ===")
print(f"Total HTML files: {len(html_files)}")
print(f"Updated: {len(changed)}")
print(f"Unchanged: {len(nochange)}")
print()
print("--- Updated files ---")
for rel, result in changed:
    print(f"  {rel}: {result}")
print()
print("--- Unchanged files ---")
for rel, result in nochange:
    print(f"  {rel}: {result}")
