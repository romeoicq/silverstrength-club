#!/usr/bin/env python3
"""Add author bio block to all blog articles missing it."""
import glob
import os

BLOG_DIR = "/home/omeo_urke/silverstrength/blog"

AUTHOR_BIO = '''
<div class="author-bio" style="margin-top: 40px; padding: 24px; background: #f8f9fa; border-left: 4px solid #2e7d32; border-radius: 8px;">
  <h3 style="margin: 0 0 8px 0; font-size: 1.1rem;">Written by Dr. Annette Verhoeven</h3>
  <p style="margin: 0; color: #555; font-size: 0.95rem; line-height: 1.6;">
    Dr. Annette Verhoeven is a gerontology researcher and healthy aging advocate with over 15 years of experience working with older adults. She specialises in evidence-based approaches to senior fitness, nutrition, and cognitive wellness. Her work focuses on helping people over 60 maintain independence, vitality, and quality of life through science-backed lifestyle strategies.
  </p>
  <p style="margin: 8px 0 0 0; color: #555; font-size: 0.95rem;">
    <em>Medically reviewed content. Sources cited where applicable. Last updated June 2026.</em>
  </p>
</div>
'''

files = glob.glob(os.path.join(BLOG_DIR, "*.html"))
updated = 0
skipped = 0
errors = []

for fpath in sorted(files):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "author-bio" in content:
        skipped += 1
        continue
    
    # Insert author bio before </main>
    if "</main>" in content:
        new_content = content.replace("</main>", AUTHOR_BIO + "\n</main>")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1
        print(f"  ✓ {os.path.basename(fpath)}")
    else:
        errors.append(os.path.basename(fpath))
        print(f"  ✗ {os.path.basename(fpath)} — no </main> tag found")

print(f"\nDone: {updated} updated, {skipped} already had author bio, {len(errors)} errors")
if errors:
    print(f"Errors: {errors}")
