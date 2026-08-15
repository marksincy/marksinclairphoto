import os

PAGES = {
    "galleries/central-coast": [
        ("chittaway-bay.html", "Chittaway Bay", "Central Coast", "Lakeside morning light, calm waters, and local foreshore walks."),
        ("copacabana.html", "Copacabana", "Central Coast", "Dramatic headland perspectives, swell patterns, and coastal shelf textures."),
        ("girrakool.html", "Girrakool", "Central Coast", "Bush trails, waterfalls, and ancient rock engravings in Brisbane Water National Park."),
        ("koolewong.html", "Koolewong", "Central Coast", "Still waters, marina silhouettes, and misty dawn light across the ridge."),
        ("morisset.html", "Morisset Abandoned Hospital", "Central Coast", "Documentary architecture, weathered textures, and historical ruins."),
        ("mt-wondabyne.html", "Mt Wondabyne", "Central Coast", "Trig station outlooks, sweeping national park ridges, and astro views."),
        ("pink-caves.html", "Pink Caves", "Central Coast", "Geological sea caves, vibrant tidal hues, and raw ocean power."),
        ("soldiers-beach.html", "Soldiers Beach", "Central Coast", "Norah Head reef shelves, early morning surf breaks, and coastal drama."),
        ("somersby-falls.html", "Somersby Falls", "Central Coast", "Cascading rainforest tiers, wet sandstone reflections, and forest canopy light."),
        ("tascott.html", "Tascott", "Central Coast", "Brisbane Water waterfront stillness, rail corridors, and shifting coastal tones."),
        ("toowoon-bay.html", "Toowoon Bay", "Central Coast", "Protected horseshoe cove, turquoise tides, and classic beachside life."),
        ("woy-woy.html", "Woy Woy", "Central Coast", "Pelican feeds, oyster leases, channel light, and tidal rhythms."),
        ("yarramalong.html", "Yarramalong", "Central Coast", "Rural valley pastures, historic churches, and rolling hinterland mist.")
    ],
    "galleries/travel": [
        ("england.html", "England", "Travel", "Streets, heritage architecture, and moody atmospheres across London and regional towns."),
        ("fiji.html", "Fiji", "Travel", "Island documentary work, turquoise waters, and Pacific light."),
        ("france.html", "France", "Travel", "Candid moments, Parisian street corners, and architectural geometry."),
        ("italy.html", "Italy", "Travel", "Cobbled alleys, historical ruins, and rich coastal textures."),
        ("singapore.html", "Singapore", "Travel", "Tropical modernist architecture, night transit, and vibrant street corners.")
    ],
    "galleries/urban": [
        ("london.html", "London", "Urban & Street", "Underground commutes, dynamic street scenes, and historic alleyway shadows."),
        ("melbourne.html", "Melbourne", "Urban & Street", "Laneway grit, tramlines, and layered city compositions."),
        ("sydney.html", "Sydney", "Urban & Street", "Barangaroo glass, Martin Place shadow lines, and harbour geometry."),
        ("street-art.html", "Street Art", "Urban & Street", "Urban canvasses, spray-painted murals, and textured wall art.")
    ],
    "galleries/natural-world": [
        ("flowers.html", "Flowers", "Natural World", "Botanical details, organic macro geometry, and vibrant natural palettes."),
        ("birds.html", "Birds", "Natural World", "Native birdlife, avian motion, and coastal wildlife captures.")
    ],
    "galleries/night": [
        ("astro.html", "Astro", "Night", "Milky Way sweeps, dark sky captures across Brisbane Water NP, and star trails."),
        ("urban.html", "Urban Night", "Night", "Neon reflections, late night transit, and long exposure light trails.")
    ],
    "galleries/events": [
        ("brickman-lego.html", "Brickman Lego", "Events", "Intricate scale builds, architectural recreations, and macro details."),
        ("cars-coffee.html", "Central Coast Cars & Coffee", "Events", "Classic vintage chrome, automotive curves, and enthusiast culture.")
    ],
    "galleries/sport": [
        ("central-coast-mariners.html", "Central Coast Mariners", "Sport", "Matchday intensity, terrace atmosphere, and stadium floodlight action.")
    ]
}

def generate_gallery_html(title, category, description, rel_depth="../../"):
    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__TITLE__ | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="__REL_DEPTH__styles.css" />
</head>
<body>

  <header>
    <div class="nav-container">
      <a href="__REL_DEPTH__index.html" class="logo">mark sinclair<span>.</span>photo</a>
      <a href="__REL_DEPTH__index.html" style="color: var(--text-muted); text-decoration: none; font-size: 0.85rem; letter-spacing: 0.05em;">← Return Home</a>
    </div>
  </header>

  <section class="page-header">
    <a href="__REL_DEPTH__index.html" class="breadcrumbs">__CATEGORY__</a>
    <h1>__TITLE__</h1>
    <p>__DESCRIPTION__</p>
  </section>

  <main class="gallery-container">
    <div class="gallery-grid">
      <!-- Add your images below -->
    </div>
  </main>

  <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox()">×</button>
    <div class="lightbox-content">
      <img id="lightboxImg" src="" alt="Full preview" />
      <div class="lightbox-caption">
        <h4 id="lightboxTitle"></h4>
        <p id="lightboxSub"></p>
      </div>
    </div>
  </div>

  <footer>
    <p>© 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>

  <script>
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxTitle = document.getElementById('lightboxTitle');
    const lightboxSub = document.getElementById('lightboxSub');

    function openLightbox(src, title, sub) {
      lightboxImg.src = src;
      lightboxTitle.textContent = title;
      lightboxSub.textContent = sub;
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox(e) {
      if (!e || e.target === lightbox || e.target.classList.contains('lightbox-close')) {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
      }
    }
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeLightbox();
    });
  </script>
</body>
</html>
"""
    return template.replace("__TITLE__", title).replace("__CATEGORY__", category).replace("__DESCRIPTION__", description).replace("__REL_DEPTH__", rel_depth)

def generate_blog_index_html(blog_title, blog_subtitle, rel_depth="../"):
    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__BLOG_TITLE__ | Mark Sinclair Photography</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="__REL_DEPTH__styles.css" />
</head>
<body>

  <header>
    <div class="nav-container">
      <a href="__REL_DEPTH__index.html" class="logo">mark sinclair<span>.</span>photo</a>
      <a href="__REL_DEPTH__index.html" style="color: var(--text-muted); text-decoration: none; font-size: 0.85rem;">← Return Home</a>
    </div>
  </header>

  <section class="page-header">
    <h1>__BLOG_TITLE__</h1>
    <p>__BLOG_SUBTITLE__</p>
  </section>

  <main class="gallery-container">
    <div class="gallery-grid" id="postGrid">
      <!-- Blog post cards will live here -->
    </div>
  </main>

  <footer>
    <p>© 2026 Mark Sinclair Photography. Hosted on GitHub Pages.</p>
  </footer>
</body>
</html>
"""
    return template.replace("__BLOG_TITLE__", blog_title).replace("__BLOG_SUBTITLE__", blog_subtitle).replace("__REL_DEPTH__", rel_depth)

def main():
    # 1. Create Gallery Sub-pages
    for folder, files in PAGES.items():
        os.makedirs(folder, exist_ok=True)
        img_folder = folder.replace("galleries", "images")
        os.makedirs(img_folder, exist_ok=True)
        
        for filename, title, cat, desc in files:
            filepath = os.path.join(folder, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(generate_gallery_html(title, cat, desc, rel_depth="../../"))
            print(f"Created: {filepath}")

    # 2. Create Standalone Architecture Page
    arch_path = "galleries/architecture.html"
    os.makedirs("galleries", exist_ok=True)
    os.makedirs("images/architecture", exist_ok=True)
    with open(arch_path, "w", encoding="utf-8") as f:
        f.write(generate_gallery_html(
            "Architecture",
            "Standalone Gallery",
            "Structural form, geometric patterns, light interplay, and high-rise facades.",
            rel_depth="../"
        ))
    print(f"Created: {arch_path}")

    # 3. Create Photo Blog Hub
    os.makedirs("photo-blog", exist_ok=True)
    with open("photo-blog/index.html", "w", encoding="utf-8") as f:
        f.write(generate_blog_index_html("Photo Blog", "Reflections on street walks, gear experiments, and documentary essays."))
    print("Created: photo-blog/index.html")

    # 4. Create My Coast Blog Hub
    os.makedirs("my-coast-blog", exist_ok=True)
    with open("my-coast-blog/index.html", "w", encoding="utf-8") as f:
        f.write(generate_blog_index_html("My Coast Blog", "The dedicated A–Z documentary exploration across the NSW Central Coast."))
    print("Created: my-coast-blog/index.html")

    print("\nSite scaffold complete! All 22 sub-pages, 2 blog hubs, and matching image folders have been generated.")

if __name__ == "__main__":
    main()