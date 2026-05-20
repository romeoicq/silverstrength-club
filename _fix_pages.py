#!/usr/bin/env python3
"""
Batch fix all SilverStrength pages for AI-friendliness:
1. Add meta author tag
2. Add sized favicon declarations  
3. Fix og:title to include brand
4. Add missing og:type/og:url/og:locale on root content pages
"""
import os
import re

BASE = "/home/omeo_urke/silverstrength"

# Get all html files
html_files = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith('.html') and 'google2' not in f:
            html_files.append(os.path.join(root, f))

html_files.sort()

print(f"Processing {len(html_files)} pages...")

fixes_applied = 0
pages_fixed = 0

for filepath in html_files:
    relpath = os.path.relpath(filepath, BASE)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    modifications = []

    # ---- 1. Add meta author after meta description ----
    if 'meta name="author"' not in content and "meta name='author'" not in content:
        # Find meta description and add author after it
        desc_match = re.search(r'(<meta name="description" content="[^"]*">)', content)
        if desc_match:
            author_tag = '\n<meta name="author" content="SilverStrength Club">'
            content = content.replace(desc_match.group(1), desc_match.group(1) + author_tag)
            modifications.append("+meta author")
        else:
            # Try alternative description tag pattern 
            desc_match2 = re.search(r'(<meta name=\'description\' content=\'[^\']*\'>)', content)
            if desc_match2:
                author_tag = "\n<meta name='author' content='SilverStrength Club'>"
                content = content.replace(desc_match2.group(1), desc_match2.group(1) + author_tag)
                modifications.append("+meta author")

    # ---- 2. Add sized favicon declarations ----
    # Current pattern: favicon.svg and apple-touch-icon
    favicon_block = '''<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/icon-512.png">
<link rel="apple-touch-icon" href="/icon-192.png">'''

    if 'icon-192.png' not in content and 'icon-512.png' not in content:
        # Find the existing favicon link or apple-touch-icon
        existing_pattern = r'<link rel="icon" type="image/svg\+xml" href="/favicon\.svg">'
        if re.search(existing_pattern, content):
            # Replace the existing favicon.svg with the full block
            content = re.sub(existing_pattern, favicon_block, content)
            modifications.append("+sized icons")
        elif '<link rel="apple-touch-icon"' in content:
            # Replace apple-touch-icon with full block
            apple_pattern = r'<link rel="apple-touch-icon"[^>]*>'
            content = re.sub(apple_pattern, favicon_block, content)
            modifications.append("+sized icons")

    # ---- 3. Fix og:title to include brand ----
    og_title_match = re.search(r'<meta property="og:title" content="([^"]*?)">', content)
    title_match = re.search(r'<title>(.*?)</title>', content)
    
    if og_title_match and title_match:
        og_title = og_title_match.group(1)
        title_text = title_match.group(1)
        
        # Only fix if og:title doesn't mention SilverStrength but the page title does
        if 'SilverStrength' not in og_title and 'SilverStrength' in title_text:
            # Extract the brand part from title
            brand_part = ""
            if ' — SilverStrength' in title_text:
                brand_part = " — SilverStrength" + title_text.split(' — SilverStrength')[1]
            elif ' | SilverStrength' in title_text:
                brand_part = " | SilverStrength" + title_text.split(' | SilverStrength')[1]
            elif 'SilverStrength' in title_text:
                # Find SilverStrength in title and extract from there
                ss_idx = title_text.index('SilverStrength')
                brand_part = " — " + title_text[ss_idx:]
            
            if brand_part:
                new_og = og_title + brand_part
                old_tag = f'<meta property="og:title" content="{og_title}">'
                new_tag = f'<meta property="og:title" content="{new_og}">'
                content = content.replace(old_tag, new_tag, 1)
                modifications.append(f"og:title +brand: '{og_title}' -> '{new_og}'")

    # ---- 4. Add missing og:locale ----
    if 'og:locale' not in content:
        # Insert after og:site_name or after last og tag
        site_name_match = re.search(r'(<meta property="og:site_name"[^>]*>)', content)
        if site_name_match:
            locale_tag = '\n<meta property="og:locale" content="en_US">'
            content = content.replace(site_name_match.group(1), site_name_match.group(1) + locale_tag)
            modifications.append("+og:locale")

    # ---- 5. Add missing og:type (for root content pages) ----
    if 'og:type' not in content:
        # Determine if it's an article (blog) or website
        is_blog = '/blog/' in filepath or relpath == 'blog/index.html'
        og_type = 'article' if is_blog else 'website'
        
        # Insert after og:title
        og_title_tag = re.search(r'(<meta property="og:title" content="[^"]*">)', content)
        if og_title_tag:
            type_tag = f'\n<meta property="og:type" content="{og_type}">'
            content = content.replace(og_title_tag.group(1), og_title_tag.group(1) + type_tag)
            modifications.append(f"+og:type={og_type}")

    # ---- 6. Add missing og:url ----
    if 'og:url' not in content:
        # Determine URL based on path
        if relpath == 'index.html':
            url = 'https://silverstrength-club.netlify.app/'
        else:
            url = f'https://silverstrength-club.netlify.app/{relpath}'
        
        # Insert after og:type
        og_type_tag = re.search(r'(<meta property="og:type" content="[^"]*">)', content)
        if og_type_tag:
            url_tag = f'\n<meta property="og:url" content="{url}">'
            content = content.replace(og_type_tag.group(1), og_type_tag.group(1) + url_tag)
            modifications.append(f"+og:url")

    # Check if anything changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        pages_fixed += 1
        for mod in modifications:
            fixes_applied += 1
            print(f"  [{relpath}] {mod}")

print(f"\n=== DONE ===")
print(f"Pages fixed: {pages_fixed}")
print(f"Total fixes: {fixes_applied}")