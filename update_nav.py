import os
import re

GALLERY_DIR = "galleries"

HEADER_HTML = '''<header>
  <div class="nav-container">
    <a href="../../index.html" class="logo">mark sinclair<span>.</span>photo</a>
    <nav>
      <ul>
        <li><a href="../../photo-blog/index.html">Photo Blog</a></li>
        <li><a href="../../my-coast-blog/index.html">My Coast Blog</a></li>

        <li>
          <a href="#">Central Coast ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/central-coast/chittaway-bay.html">Chittaway Bay</a></li>
            <li><a href="../../galleries/central-coast/copacabana.html">Copacabana</a></li>
            <li><a href="../../galleries/central-coast/girrakool.html">Girrakool</a></li>
            <li><a href="../../galleries/central-coast/koolewong.html">Koolewong</a></li>
            <li><a href="../../galleries/central-coast/morisset.html">Morisset Abandoned Hospital</a></li>
            <li><a href="../../galleries/central-coast/mt-wondabyne.html">Mt Wondabyne</a></li>
            <li><a href="../../galleries/central-coast/pink-caves.html">Pink Caves</a></li>
            <li><a href="../../galleries/central-coast/soldiers-beach.html">Soldiers Beach</a></li>
            <li><a href="../../galleries/central-coast/somersby-falls.html">Somersby Falls</a></li>
            <li><a href="../../galleries/central-coast/tascott.html">Tascott</a></li>
            <li><a href="../../galleries/central-coast/toowoon-bay.html">Toowoon Bay</a></li>
            <li><a href="../../galleries/central-coast/woy-woy.html">Woy Woy</a></li>
            <li><a href="../../galleries/central-coast/yarramalong.html">Yarramalong</a></li>
          </ul>
        </li>

        <li>
          <a href="#">Travel ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/travel/england.html">England</a></li>
            <li><a href="../../galleries/travel/fiji.html">Fiji</a></li>
            <li><a href="../../galleries/travel/france.html">France</a></li>
            <li><a href="../../galleries/travel/italy.html">Italy</a></li>
            <li><a href="../../galleries/travel/singapore.html">Singapore</a></li>
          </ul>
        </li>

        <li>
          <a href="#">Urban ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/urban/london.html">London</a></li>
            <li><a href="../../galleries/urban/melbourne.html">Melbourne</a></li>
            <li><a href="../../galleries/urban/sydney.html">Sydney</a></li>
            <li><a href="../../galleries/urban/street-art.html">Street Art</a></li>
          </ul>
        </li>

        <li><a href="../../galleries/architecture.html">Architecture</a></li>

        <li>
          <a href="#">Natural World ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/natural-world/flowers.html">Flowers</a></li>
            <li><a href="../../galleries/natural-world/birds.html">Birds</a></li>
          </ul>
        </li>

        <li>
          <a href="#">Night ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/night/astro.html">Astro</a></li>
            <li><a href="../../galleries/night/urban.html">Urban</a></li>
          </ul>
        </li>

        <li>
          <a href="#">Events ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/events/brickman-lego.html">Brickman Lego</a></li>
            <li><a href="../../galleries/events/cars-coffee.html">Central Coast Cars & Coffee</a></li>
          </ul>
        </li>

        <li>
          <a href="#">Sport ▾</a>
          <ul class="dropdown-menu">
            <li><a href="../../galleries/sport/central-coast-mariners.html">CC Mariners</a></li>
          </ul>
        </li>

        <li><a href="../../about.html">About</a></li>
      </ul>
    </nav>
  </div>
</header>'''

for root, _, files in os.walk(GALLERY_DIR):
    for f in files:
        if f.endswith(".html") and root != GALLERY_DIR:
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            new_content = re.sub(r'<header>.*?</header>', HEADER_HTML, content, flags=re.DOTALL)
            with open(path, "w", encoding="utf-8") as file:
                file.write(new_content)
            print(f"Patched navigation in {path}")
