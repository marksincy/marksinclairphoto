import os

GALLERIES = {
    "central-coast": {
        "title": "Central Coast",
        "pages": [
            ("chittaway-bay", "Chittaway Bay", "Estuary light, pelicans, and quiet foreshore trails along Tuggerah Lake."),
            ("copacabana", "Copacabana", "Headland views, ocean swells, and golden hour along the coast."),
            ("girrakool", "Girrakool", "Sandstone cascades, rainforest gullies, and ancient engravings in Brisbane Water National Park."),
            ("koolewong", "Koolewong", "Waterfront reflections, calm marinas, and resilience across Brisbane Water."),
            ("morisset", "Morisset Abandoned Hospital", "Weathered architecture, encroaching bushland, and quiet history."),
            ("mt-wondabyne", "Mt Wondabyne", "Granite peaks, panoramic ridgelines, and remote trails."),
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
        "pages": [
            ("flowers", "Flowers", "Macro textures, botanical symmetry, and natural colour."),
            ("birds", "Birds", "Coastal and bushland birdlife captured in motion and stillness.")
        ]
    },
    "night": {
        "title": "Night",
        "pages": [
            ("astro", "Astro", "Star trails, Milky Way cores, and dark-sky landscapes."),
            ("urban", "Urban Night", "Neon reflections, quiet streets, and city lights after dark.")
        ]
    },
    "events": {
        "title": "Events",
        "pages": [
            ("brickman-lego", "Brickman Lego", "Intricate scale models, vibrant colour, and playful craft."),
            ("cars-coffee", "Central Coast Cars & Coffee", "Classic chrome, vintage bodywork, and early morning automotive culture.")
        ]
    },
    "sport": {
        "title": "Sport",
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
            <a href="#">Central Coast ▾</a>
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
            <a href="#">Travel ▾</a>
            <ul class="dropdown-menu">
              <li><a href="{rel_root}galleries/travel/england.html">England</a></li>
              <li><a href="{rel_root}galleries/travel/fiji.html">Fiji</a></li>
              <li><a href="{rel_root}galleries/travel/france.html">France</a></li>
              <li><a href="{rel_root}galleries/travel/italy.html">Italy</a></li>
              <li><a href="{rel_root}galleries/travel/singapore.html">Singapore</a></li>
            </ul>
          </li>
          <li>
            <a href="#">Urban ▾</a>
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
        <p style="color: var(--text-muted); font-size: 0.9rem;">Drop your JPEGs into <code>{folder_display}</code> and re-run python script.</p>
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
    <span class="breadcrumbs">{category_title}</span>
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

def main():
    for cat_slug, cat_data in GALLERIES.items():
        cat_title = cat_data["title"]
        for page_slug, page_title, desc in cat_data["pages"]:
            html_dir = os.path.join("galleries", cat_slug)
            img_dir = os.path.join("images", cat_slug, page_slug)
            os.makedirs(html_dir, exist_ok=True)
            os.makedirs(img_dir, exist_ok=True)

            html_path = os.path.join(html_dir, f"{page_slug}.html")
            html_content = build_gallery_html(cat_title, page_title, desc, img_dir, rel_root="../../", is_root_gallery=False)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Built: {html_path}")

    # Architecture
    arch_img_dir = os.path.join("images", "architecture")
    os.makedirs(arch_img_dir, exist_ok=True)
    arch_html = build_gallery_html(
        "Portfolio", 
        "Architecture", 
        "Lines, geometry, and structural forms across modern and historic cities.", 
        arch_img_dir, 
        rel_root="../", 
        is_root_gallery=True
    )
    with open("galleries/architecture.html", "w", encoding="utf-8") as f:
        f.write(arch_html)
    print("Built: galleries/architecture.html")

if __name__ == "__main__":
    main()
