import os
import re

GALLERY_DIR = "galleries"
VALID_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".avif"}

def clean_title(filename):
    name, _ = os.path.splitext(filename)
    name = re.sub(r'[-_]+', ' ', name).strip()
    return name.title()

def main():
    if not os.path.exists(GALLERY_DIR):
        print(f"Directory {GALLERY_DIR} not found.")
        return

    updated_pages = 0

    for root, dirs, files in os.walk(GALLERY_DIR):
        for f in files:
            if not f.endswith(".html") or f == "architecture.html":
                continue

            html_path = os.path.join(root, f)
            rel_folder = os.path.relpath(root, GALLERY_DIR)
            category = rel_folder.replace(os.sep, "/")

            img_folder = os.path.join("images", category)
            if not os.path.exists(img_folder):
                continue

            page_slug = os.path.splitext(f)[0]
            # Match images whose filename starts with or contains the subpage slug/name
            all_imgs = sorted([
                img for img in os.listdir(img_folder)
                if os.path.splitext(img)[1].lower() in VALID_EXTS
            ])
            
            # Filter to relevant images (or use all images in the folder if fewer than 20)
            matched_imgs = [img for img in all_imgs if page_slug in img.lower()]
            if not matched_imgs:
                matched_imgs = all_imgs

            if not matched_imgs:
                continue

            cards_html = []
            for img in matched_imgs:
                img_rel = f"../../images/{category}/{img}"
                title = clean_title(img)
                card = f"""      <article class="photo-card" onclick="openLightbox('{img_rel}', '{title}', '{category.title()}')">
        <div class="img-wrapper">
          <img src="{img_rel}" alt="{title}" loading="lazy" />
        </div>
        <div class="photo-meta">
          <h3>{title}</h3>
          <span class="photo-gear">Gallery</span>
        </div>
      </article>"""
                cards_html.append(card)

            new_grid_content = "\n".join(cards_html)

            with open(html_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace content inside <div class="gallery-grid">...</div>
            pattern = r'(<div class="gallery-grid"[^>]*>)(.*?)(</div>\s*</main>)'
            replacement = f"\\1\n{new_grid_content}\n    \\3"
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

            with open(html_path, "w", encoding="utf-8") as file:
                file.write(new_content)

            print(f"Updated {html_path} with {len(matched_imgs)} images.")
            updated_pages += 1

    print(f"\nDone! Populated {updated_pages} gallery pages.")

if __name__ == "__main__":
    main()