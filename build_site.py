import os

GALLERIES = {
    "central-coast": {
        "title": "Central Coast",
        "description": "Coastal rock shelves, tidal estuaries, and headlands across 13 regional locations.",
        "pages": [
            ("chittaway-bay", "Chittaway Bay", "Estuary light, pelicans, and quiet foreshore trails along Tuggerah Lake."),
            ("copacabana", "Copacabana", "Headland views, ocean swells, and golden hour along the coast."),
            ("girrakool", "Girrakool", "Sandstone cascades, rainforest gullies, and ancient engravings."),
            ("koolewong", "Koolewong", "Waterfront reflections, calm marinas, and resilience across Brisbane Water."),
            ("morisset", "Morisset Abandoned Hospital", "Weathered architecture, encroaching bushland, and quiet history."),
            ("mt-wondabyne", "Mt Wondabyne", "Granite peaks, panoramic ridgelines, and remote dark-sky trails."),
            ("pink-caves", "Pink Caves", "Vibrant coastal sandstone formations and tidal rock shelves."),
            ("soldiers-beach", "Soldiers Beach", "Dramatic rock shelves, rolling surf, and sunrise horizons near Norah Head."),
            ("somersby-falls", "Somersby Falls", "Fern-lined tiers, misty cascades, and filtered forest light."),
            ("tascott", "Tascott", "Morning mist, railway reflections, and still waters on Brisbane Water."),
            ("toowoon-bay", "Toowoon Bay", "Protected turquoise waters, gentle reefs, and pastel skies."),
            ("woy-woy", "Woy Woy", "Channel jetties, pelican perches, and daily life along the peninsula."),
            ("yarramalong", "Yarramalong", "Rural valleys, misty paddocks, and country backroads.")
        ]
    },
    "travel": {
        "title": "Travel",
        "description": "Historic streets, Mediterranean textures, and island light across destinations abroad.",
        "pages": [
            ("england", "England", "Historic streets, coastal towns, and timeless architecture."),
            ("fiji", "Fiji", "Tropical light, island coastlines, and warm ocean horizons."),
            ("france", "France", "Classic boulevards, café culture, and European light."),
            ("italy", "Italy", "Ancient stone, vibrant piazzas, and Mediterranean textures."),
            ("singapore", "Singapore", "Futuristic geometry, lush urban gardens, and neon nightscapes.")
        ]
    },
    "urban": {
        "title": "Urban",
        "description": "Candid street rhythms, geometric shadows, and city life.",
        "pages": [
            ("london", "London", "Monochrome geometry, commuting crowds, and iconic streetscapes."),
            ("melbourne", "Melbourne", "Laneway textures, tramlines, and shifting light."),
            ("sydney", "Sydney", "Harbour geometry, high-rise shadows, and street rhythm."),
            ("paris", "Paris", "Haussmann architecture, grand boulevards, and timeless street moments."),
            ("venice", "Venice", "Canals, reflections, and moody atmospheric light through historic lanes."),
            ("street-art", "Street Art", "Murals, urban colour, and ephemeral public expression.")
        ]
    },
    "natural-world": {
        "title": "Natural World",
        "description": "Botanical symmetry, macro textures, and native birdlife.",
        "pages": [
            ("flowers", "Flowers", "Macro textures, botanical symmetry, and natural colour."),
            ("birds", "Birds", "Coastal and bushland birdlife captured in motion and stillness.")
        ]
    },
    "night": {
        "title": "Night",
        "description": "Star trails, deep night skies, and neon-lit streetscapes.",
        "pages": [
            ("astro", "Astro", "Star trails, Milky Way cores, and dark-sky landscapes."),
            ("urban", "Urban Night", "Neon reflections, quiet streets, and city lights after dark.")
        ]
    },
    "events": {
        "title": "Events",
        "description": "Automotive culture, scale models, and community gatherings.",
        "pages": [
            ("brickman-lego", "Brickman Lego", "Intricate scale models, vibrant colour, and playful craft."),
            ("cars-coffee", "Central Coast Cars & Coffee", "Classic chrome, vintage bodywork, and early morning automotive culture.")
        ]
    },
    "sport": {
        "title": "Sport",
        "description": "Pitchside matchday tension and stadium atmosphere.",
        "pages": [
            ("central-coast-mariners", "Central Coast Mariners", "Matchday energy, pitchside action, and stadium atmosphere in Gosford.")
        ]
    }
}

def get_nav(rel_root):
    return f"""  <header>
    <div class="nav-container">
      <a href="{rel_root}index.html" class="logo">mark sinclair<span>.</span>photo</a>
      <nav>
        <ul>
          <li><a href="{rel_root}photo-blog/index.html">Photo Blog</a></li>
          <li><a href="{rel_root}my-coast-blog/index.html">My Coast Blog</a></li>
          <li>
            <a href="{rel_root}galleries/central-coast/index.html">Central Coast ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/central-coast/chittaway-bay.html">Chittaway Bay</a></li>
              <li><a href="{rel_root}galleries/central-coast/copacabana.html">Copacabana</a></li>
              <li><a href="{rel_root}galleries/central-coast/girrakool.html">Girrakool</a></li>
              <li><a href="{rel_root}galleries/central-coast/koolewong.html">Koolewong</a></li>
              <li><a href="{rel_root}galleries/central-coast/morisset.html">Morisset Abandoned Hospital</a></li>
              <li><a href="{rel_root}galleries/central-coast/mt-wondabyne.html">Mt Wondabyne</a></li>
              <li><a href="{rel_root}galleries/central-coast/pink-caves.html">Pink Caves</a></li>
              <li><a href="{rel_root}galleries/central-coast/soldiers-beach.html">Soldiers Beach</a></li>
              <li><a href="{rel_root}galleries/central-coast/somersby-falls.html">Somersby Falls</a></li>
              <li><a href="{rel_root}galleries/central-coast/tascott.html">Tascott</a></li>
              <li><a href="{rel_root}galleries/central-coast/toowoon-bay.html">Toowoon Bay</a></li>
              <li><a href="{rel_root}galleries/central-coast/woy-woy.html">Woy Woy</a></li>
              <li><a href="{rel_root}galleries/central-coast/yarramalong.html">Yarramalong</a></li>
            </ul>
          </li>
          <li>
            <a href="{rel_root}galleries/travel/index.html">Travel ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/travel/england.html">England</a></li>
              <li><a href="{rel_root}galleries/travel/fiji.html">Fiji</a></li>
              <li><a href="{rel_root}galleries/travel/france.html">France</a></li>
              <li><a href="{rel_root}galleries/travel/italy.html">Italy</a></li>
              <li><a href="{rel_root}galleries/travel/singapore.html">Singapore</a></li>
            </ul>
          </li>
          <li>
            <a href="{rel_root}galleries/urban/index.html">Urban ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/urban/london.html">London</a></li>
              <li><a href="{rel_root}galleries/urban/melbourne.html">Melbourne</a></li>
              <li><a href="{rel_root}galleries/urban/sydney.html">Sydney</a></li>
              <li><a href="{rel_root}galleries/urban/paris.html">Paris</a></li>
              <li><a href="{rel_root}galleries/urban/venice.html">Venice</a></li>
              <li><a href="{rel_root}galleries/urban/street-art.html">Street Art</a></li>
            </ul>
          </li>
          <li><a href="{rel_root}galleries/architecture.html">Architecture</a></li>
          <li>
            <a href="#">Natural World ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/natural-world/flowers.html">Flowers</a></li>
              <li><a href="{rel_root}galleries/natural-world/birds.html">Birds</a></li>
            </ul>
          </li>
          <li>
            <a href="#">Night ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/night/astro.html">Astro</a></li>
              <li><a href="{rel_root}galleries/night/urban.html">Urban</a></li>
            </ul>
          </li>
          <li>
            <a href="#">Events ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/events/brickman-lego.html">Brickman Lego</a></li>
              <li><a href="{rel_root}galleries/events/cars-coffee.html">Central Coast Cars & Coffee</a></li>
            </ul>
          </li>
          <li>
            <a href="#">Sport ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/sport/central-coast-mariners.html">Central Coast Mariners</a></li>
            </ul>
          </li>
          <li><a href="{rel_root}about.html">About</a></li>
        </ul>
      </nav>
    </div>
  </header>"""

def build_gallery_html(category_title, page_title, description, local_img_dir, rel_root, is_root_gallery=False):
    cards_html = ""
    if os.path.exists(local_img_dir):
        files = sorted([f for f in os.listdir(local_img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
        for idx, fname in enumerate(files, 1):
            if is_root_gallery:
                img_src = f"../images/architecture/{fname}"
            else:
                cat_name = os.path.basename(os.path.dirname(local_img_dir))
                page_name = os.path.basename(local_img_dir)
                img_src = f"../../images/{cat_name}/{page_name}/{fname}"
            
            caption = os.path.splitext(fname)[0].replace('-', ' ').replace('_', ' ').title()
            cards_html += f"""
      <article class="photo-card" onclick="openLightbox('{img_src}', '{page_title} #{idx}', '{category_title} Series')">
        <div class="img-wrapper">
          <img src="{img_src}" alt="{caption}" loading="lazy" />
        </div>
        <div class="photo-meta">
          <div>
            <h3>{page_title} #{idx}</h3>
            <p style="font-size: 0.8rem; color: var(--text-muted);">{category_title}</p>
          </div>
          <span class="photo-gear">View Full</span>
        </div>
      </article>"""

    if not cards_html:
        folder_display = "images/architecture/" if is_root_gallery else f"images/.../{os.path.basename(local_img_dir)}/"
        cards_html = f"""
      <div style="grid-column: 1 / -1; background: var(--card-bg); border: 1px dashed var(--border); border-radius: 8px; padding: 3rem; text-align: center;">
        <h3 style="font-family: 'Playfair Display', serif; font-weight: 400; margin-bottom: 0.5rem;">Ready for {page_title} Photos</h3>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Drop your JPEGs into <code>{folder_display}</code> and re-run python build_site.py.</p>
      </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title} | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel_root}styles.css" />
</head>
<body>

{get_nav(rel_root)}

  <section class="page-header">
    <a href="index.html" class="breadcrumbs">&larr; Return to {category_title} Hub</a>
    <h1>{page_title}</h1>
    <p>{description}</p>
  </section>

  <main class="gallery-container">
    <div class="gallery-grid">
      {cards_html}
    </div>
  </main>

  <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox()">&times;</button>
    <div class="lightbox-content">
      <img id="lightboxImg" src="" alt="Full preview" />
      <div class="lightbox-caption">
        <h4 id="lightboxTitle"></h4>
        <p id="lightboxSub"></p>
      </div>
    </div>
  </div>

  <footer>
    <p>&copy; 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>

  <script>
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxSub = document.getElementById('lightboxSub');

    function openLightbox(src, title, sub) {{
      lightboxImg.src = src;
      lightboxTitle.textContent = title;
      lightboxSub.textContent = sub;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }}

    function closeLightbox(e) {{
      if (!e || e.target === lightbox || e.target.classList.contains('lightbox-close')) {{
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeLightbox();
    }});
  </script>
</body>
</html>
"""

def build_category_hub(cat_slug, cat_title, description, pages):
    tiles_html = ""
    for page_slug, page_title, page_desc in pages:
        local_img_dir = os.path.join("images", cat_slug, page_slug)
        img_src = ""
        if os.path.exists(local_img_dir):
            files = sorted([f for f in os.listdir(local_img_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))])
            if files:
                # 1. Prefer a file named cover.jpg or starting with cover-
                covers = [f for f in files if "cover" in f.lower()]
                chosen = covers[0] if covers else files[0]
                img_src = f"../../images/{cat_slug}/{page_slug}/{chosen}"

        if not img_src:
            img_src = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80"

        tiles_html += f"""
      <a href="{page_slug}.html" class="portfolio-tile">
        <img class="tile-img" src="{img_src}" alt="{page_title}" loading="lazy" />
        <div class="tile-overlay">
          <span class="tile-tag">{cat_title} Series</span>
          <h2 class="tile-title">{page_title}</h2>
          <p class="tile-desc">{page_desc}</p>
          <span class="tile-action">View Gallery &rarr;</span>
        </div>
      </a>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cat_title} Locations | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../styles.css" />
  <style>
    .gallery-container {{ padding-top: 2.5rem; }}
    .showcase-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
      gap: 1.75rem;
    }}
    .portfolio-tile {{
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      aspect-ratio: 16 / 11;
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      text-decoration: none;
      display: block;
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.35s ease, box-shadow 0.35s ease;
    }}
    .portfolio-tile:hover {{
      transform: translateY(-5px);
      border-color: rgba(255, 255, 255, 0.3);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    }}
    .tile-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .portfolio-tile:hover .tile-img {{ transform: scale(1.05); }}
    .tile-overlay {{
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(10, 11, 14, 0.94) 0%, rgba(10, 11, 14, 0.35) 55%, rgba(10, 11, 14, 0.05) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 1.85rem;
      transition: background 0.35s ease;
    }}
    .portfolio-tile:hover .tile-overlay {{
      background: linear-gradient(to top, rgba(10, 11, 14, 0.98) 0%, rgba(10, 11, 14, 0.45) 60%, rgba(10, 11, 14, 0.1) 100%);
    }}
    .tile-tag {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--accent);
      margin-bottom: 0.35rem;
      font-weight: 500;
    }}
    .tile-title {{
      font-family: 'Playfair Display', Georgia, serif;
      font-size: 1.5rem;
      font-weight: 400;
      color: #fff;
      margin-bottom: 0.3rem;
      line-height: 1.2;
    }}
    .tile-desc {{
      font-size: 0.83rem;
      color: var(--text-muted);
      line-height: 1.4;
      max-width: 95%;
    }}
    .tile-action {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: #fff;
      margin-top: 0.8rem;
      font-weight: 500;
      transition: gap 0.25s ease, color 0.25s ease;
    }}
    .portfolio-tile:hover .tile-action {{
      gap: 0.7rem;
      color: var(--accent);
    }}
  </style>
</head>
<body>

{get_nav(rel_root="../../")}

  <section class="page-header">
    <a href="../../index.html" class="breadcrumbs">&larr; Return to Home</a>
    <h1>{cat_title} Locations</h1>
    <p>{description}</p>
  </section>

  <main class="gallery-container">
    <div class="showcase-grid">
      {tiles_html}
    </div>
  </main>

  <footer>
    <p>&copy; 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>

</body>
</html>
"""

def main():
    for cat_slug, cat_data in GALLERIES.items():
        cat_title = cat_data["title"]
        pages = cat_data["pages"]
        html_dir = os.path.join("galleries", cat_slug)
        os.makedirs(html_dir, exist_ok=True)

        for page_slug, page_title, desc in pages:
            img_dir = os.path.join("images", cat_slug, page_slug)
            os.makedirs(img_dir, exist_ok=True)
            html_path = os.path.join(html_dir, f"{page_slug}.html")
            html_content = build_gallery_html(cat_title, page_title, desc, img_dir, rel_root="../../", is_root_gallery=False)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)

        hub_path = os.path.join(html_dir, "index.html")
        hub_html = build_category_hub(cat_slug, cat_title, cat_data.get("description", ""), pages)
        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(hub_html)

    # Architecture
    arch_img_dir = os.path.join("images", "architecture")
    os.makedirs(arch_img_dir, exist_ok=True)
    arch_html = build_gallery_html("Portfolio", "Architecture", "Lines, geometry, and structural forms across modern and historic cities.", arch_img_dir, rel_root="../", is_root_gallery=True)
    with open("galleries/architecture.html", "w", encoding="utf-8") as f:
        f.write(arch_html)

    print("✓ Site, galleries, and Directory Hubs rebuilt successfully!")

if __name__ == "__main__":
    main()
