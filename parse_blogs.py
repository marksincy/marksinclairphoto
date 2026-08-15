import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

XML_FILES = [
    f for f in os.listdir(".") if f.lower().startswith("squarespace-wordpress-export") and f.lower().endswith(".xml")
]

NAMESPACES = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

def clean_slug(title):
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    return slug.strip('-')

def clean_html_content(raw_html):
    if not raw_html:
        return "<p>No content available.</p>"
    lines = raw_html.strip().split('\n\n')
    formatted = []
    for block in lines:
        block = block.strip()
        if block.startswith('<p') or block.startswith('<div') or block.startswith('<h') or block.startswith('<blockquote'):
            formatted.append(block)
        elif block:
            formatted.append(f"<p>{block.replace(chr(10), '<br />')}</p>")
    return "\n\n".join(formatted)

def render_post_html(title, date_str, category_name, content_html, rel_depth="../"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel_depth}styles.css" />
  <style>
    .article-header {{
      max-width: 740px;
      margin: 4.5rem auto 2.5rem;
      padding: 0 1.5rem;
      text-align: center;
    }}
    .post-category {{
      color: var(--accent);
      font-size: 0.8rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.15em;
      margin-bottom: 1rem;
      display: inline-block;
    }}
    .article-header h1 {{
      font-family: 'Playfair Display', Georgia, serif;
      font-size: clamp(2.4rem, 5vw, 3.6rem);
      font-weight: 400;
      color: var(--text);
      line-height: 1.2;
      margin-bottom: 1.25rem;
    }}
    .post-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .article-content {{
      max-width: 740px;
      margin: 0 auto;
      padding: 0 1.5rem 6rem;
      font-size: 1.1rem;
      line-height: 1.8;
      font-weight: 300;
      color: var(--text-muted);
    }}
    .article-content p {{
      margin-bottom: 1.75rem;
      color: #c7cbd4;
    }}
    .article-content h2, .article-content h3 {{
      font-family: 'Playfair Display', Georgia, serif;
      color: var(--text);
      margin: 2.5rem 0 1rem;
      font-weight: 400;
    }}
    .article-content img {{
      max-width: 100%;
      height: auto;
      border-radius: 6px;
      margin: 2rem 0;
      display: block;
    }}
  </style>
</head>
<body>

  <header>
    <div class="nav-container">
      <a href="{rel_depth}index.html" class="logo">mark sinclair<span>.</span>photo</a>
      <a href="index.html" style="color: var(--text-muted); text-decoration: none; font-size: 0.85rem; letter-spacing: 0.05em;">← Back to Hub</a>
    </div>
  </header>

  <article>
    <div class="article-header">
      <span class="post-category">{category_name}</span>
      <h1>{title}</h1>
      <div class="post-meta">
        <span>{date_str}</span>
      </div>
    </div>

    <div class="article-content">
      {content_html}
    </div>
  </article>

  <footer>
    <p>© 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>

</body>
</html>
"""

def render_blog_hub_html(blog_title, blog_subtitle, posts, rel_depth="../"):
    cards_html = ""
    for post in posts:
        cards_html += f"""
      <article class="photo-card" style="text-align: left; padding: 0;">
        <a href="{post['filename']}" style="text-decoration: none; color: inherit; display: block; padding: 1.75rem;">
          <div style="font-size: 0.75rem; color: var(--accent); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">{post['date']}</div>
          <h3 style="font-family: 'Playfair Display', serif; font-size: 1.35rem; color: var(--text); margin-bottom: 0.75rem;">{post['title']}</h3>
          <p style="color: var(--text-muted); font-size: 0.9rem; font-weight: 300; line-height: 1.5; margin-bottom: 1rem;">{post['snippet']}</p>
          <span style="color: var(--accent); font-size: 0.85rem; font-weight: 500;">Read Story →</span>
        </a>
      </article>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{blog_title} | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel_depth}styles.css" />
</head>
<body>

  <header>
    <div class="nav-container">
      <a href="{rel_depth}index.html" class="logo">mark sinclair<span>.</span>photo</a>
      <a href="{rel_depth}index.html" style="color: var(--text-muted); text-decoration: none; font-size: 0.85rem;">← Return Home</a>
    </div>
  </header>

  <section class="page-header">
    <h1>{blog_title}</h1>
    <p>{blog_subtitle}</p>
  </section>

  <main class="gallery-container">
    <div class="gallery-grid">
      {cards_html if cards_html else '<p style="color: var(--text-muted);">No posts found.</p>'}
    </div>
  </main>

  <footer>
    <p>© 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>
</body>
</html>
"""

def is_strict_my_coast_post(slug, title):
    """Strictly matches true My Coast Series entries."""
    s = slug.lower()
    t = title.lower()
    return s.startswith("my-coast-") or s.startswith("mycoast-") or bool(re.match(r'^[a-z]\s+is\s+for\b', t))

def main():
    if not XML_FILES:
        print("No Squarespace export XML files found.")
        return

    xml_path = XML_FILES[0]
    print(f"Re-parsing posts with strict separation from: {xml_path}\n")

    tree = ET.parse(xml_path)
    root = tree.getroot()
    channel = root.find('channel')

    # Wipe existing html posts in both folders to remove misfiled files
    for target in ["photo-blog", "my-coast-blog"]:
        os.makedirs(target, exist_ok=True)
        for f in os.listdir(target):
            if f.endswith(".html") and f != "index.html":
                os.remove(os.path.join(target, f))

    photo_posts = []
    my_coast_posts = []
    processed_slugs = set()

    for item in channel.findall('item'):
        post_type = item.find('wp:post_type', NAMESPACES)
        status = item.find('wp:status', NAMESPACES)

        if post_type is not None and post_type.text != 'post':
            continue
        if status is not None and status.text != 'publish':
            continue

        title_el = item.find('title')
        title = title_el.text.strip() if title_el is not None and title_el.text else "Untitled Post"

        slug = clean_slug(title)
        if slug in processed_slugs:
            continue
        processed_slugs.add(slug)

        pub_date_el = item.find('pubDate')
        date_str = ""
        if pub_date_el is not None and pub_date_el.text:
            try:
                dt = datetime.strptime(pub_date_el.text[:25], "%a, %d %b %Y %H:%M:%S")
                date_str = dt.strftime("%B %d, %Y")
            except Exception:
                date_str = pub_date_el.text

        content_el = item.find('content:encoded', NAMESPACES)
        raw_content = content_el.text if content_el is not None and content_el.text else ""

        # Strict routing logic
        if is_strict_my_coast_post(slug, title):
            target_dir = "my-coast-blog"
            category_tag = "My Coast Series"
        else:
            target_dir = "photo-blog"
            category_tag = "Photo Essay"

        clean_text = re.sub(r'<[^>]+>', '', raw_content)
        snippet = (clean_text[:140] + '...') if len(clean_text) > 140 else clean_text

        filename = f"{slug}.html"
        filepath = os.path.join(target_dir, filename)

        formatted_content = clean_html_content(raw_content)
        post_html = render_post_html(title, date_str, category_tag, formatted_content, rel_depth="../")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(post_html)

        entry = {
            "title": title,
            "date": date_str,
            "filename": filename,
            "snippet": snippet
        }

        if target_dir == "my-coast-blog":
            my_coast_posts.append(entry)
            print(f"[My Coast Blog] → {filename}")
        else:
            photo_posts.append(entry)
            print(f"[Photo Blog]    → {filename}")

    # Rebuild Index Pages
    photo_hub = render_blog_hub_html(
        "Photo Blog",
        "Reflections on street walks, gear experiments, and documentary essays.",
        photo_posts,
        rel_depth="../"
    )
    with open("photo-blog/index.html", "w", encoding="utf-8") as f:
        f.write(photo_hub)

    coast_hub = render_blog_hub_html(
        "My Coast Blog",
        "The dedicated A–Z documentary exploration across the NSW Central Coast.",
        my_coast_posts,
        rel_depth="../"
    )
    with open("my-coast-blog/index.html", "w", encoding="utf-8") as f:
        f.write(coast_hub)

    print(f"\nSorted: {len(photo_posts)} Photo Blog essays and {len(my_coast_posts)} My Coast posts.")

if __name__ == "__main__":
    main()