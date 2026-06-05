#!/usr/bin/env python3
"""Batch-update blog articles: add author bio + fix JSON-LD author."""
import glob
import re

BLOG_DIR = "/home/omeo_urke/silverstrength/blog"

AUTHOR_BIO = '''<div class="author-bio" style="background:#f0f4e8;border-left:4px solid #2d5016;padding:24px;margin:40px 0;border-radius:8px;">
  <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
    <img src="/team/sarah-mitchell.jpg" alt="Sarah Mitchell, Senior Health Writer" style="width:64px;height:64px;border-radius:50%;object-fit:cover;" loading="lazy" onerror="this.style.display='none'">
    <div>
      <p style="margin:0;font-weight:700;color:#1a1a2e;font-size:16px;">Written by <a href="/about" style="color:#2d5016;text-decoration:underline;">Sarah Mitchell</a></p>
      <p style="margin:4px 0 0;color:#555;font-size:14px;">Senior Health &amp; Wellness Writer &middot; Certified Health Education Specialist (CHES)</p>
    </div>
  </div>
  <p style="margin:12px 0 0;color:#444;font-size:14px;line-height:1.6;">Sarah has over 8 years of experience writing about senior health and fitness. She holds a degree in Health Sciences and is passionate about helping older adults live active, independent lives. All content is reviewed for accuracy against current medical guidelines and peer-reviewed research.</p>
</div>

'''

ORG_AUTHOR = '"author": {"@type": "Organization", "name": "SilverStrength Club"}'
PERSON_AUTHOR = '"author": {"@type": "Person", "name": "Sarah Mitchell", "jobTitle": "Senior Health & Wellness Writer", "url": "https://www.silverstrength.club/about"}'

updated = 0
skipped = 0
errors = 0

for filepath in sorted(glob.glob(f"{BLOG_DIR}/*.html")):
    if filepath.endswith("index.html"):
        continue
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        modified = False
        
        # 1. Fix JSON-LD author
        if ORG_AUTHOR in content:
            content = content.replace(ORG_AUTHOR, PERSON_AUTHOR)
            modified = True
        
        # 2. Insert author bio before Related Articles
        if "Related Articles" in content and "author-bio" not in content:
            match = re.search(r'(<h2[^>]*>.*?Related Articles.*?</h2>)', content, re.DOTALL)
            if match:
                insert_point = match.start()
                content = content[:insert_point] + AUTHOR_BIO + content[insert_point:]
                modified = True
        
        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            updated += 1
        else:
            skipped += 1
    
    except Exception as e:
        errors += 1
        print(f"ERROR {filepath}: {e}")

print(f"Updated: {updated}")
print(f"Skipped: {skipped}")
print(f"Errors: {errors}")
print(f"Total: {updated + skipped + errors}")
