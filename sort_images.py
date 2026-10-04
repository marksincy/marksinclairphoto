import os
import re
import shutil
import xml.etree.ElementTree as ET

SOURCE_DIR = "images/imported"

# Mapping category keywords to your exact target folders
CATEGORY_MAPPING = {
    # Central Coast locations
    "chittaway": "images/central-coast",
    "copacabana": "images/central-coast",
    "girrakool": "images/central-coast",
    "koolewong": "images/central-coast",
    "morisset": "images/central-coast",
    "wondabyne": "images/central-coast",
    "pink-caves": "images/central-coast",
    "soldiers": "images/central-coast",
    "somersby": "images/central-coast",
    "tascott": "images/central-coast",
    "toowoon": "images/central-coast",
    "woy": "images/central-coast",
    "yarramalong": "images/central-coast",
    "coast": "images/central-coast",
    "avoca": "images/central-coast",

    # Urban & Travel
    "london": "images/urban",
    "melbourne": "images/urban",
    "sydney": "images/urban",
    "street": "images/urban",
    "england": "images/travel",
    "fiji": "images/travel",
    "france": "images/travel",
    "italy": "images/travel",
    "singapore": "images/travel",

    # Other galleries
    "architecture": "images/architecture",
    "flower": "images/natural-world",
    "bird": "images/natural-world",
    "astro": "images/night",
    "night": "images/night",
    "lego": "images/events",
    "cars": "images/events",
    "mariners": "images/sport"
}

XML_FILES = [
    f for f in os.listdir(".") if f.lower().startswith("squarespace-wordpress-export") and f.lower().endswith(".xml")
]

NAMESPACES = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/'
}

def clean_url_name(url):
    return url.split('/')[-1].split('?')[0]

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Directory {SOURCE_DIR} not found.")
        return

    # Build image-to-category lookup from XML
    image_targets = {}
    for xml_file in XML_FILES:
        print(f"Reading {xml_file}...")
        tree = ET.parse(xml_file)
        root = tree.getroot()
        channel = root.find('channel')

        for item in channel.findall('item'):
            title = (item.find('title').text or "").lower()
            categories = " ".join([c.text.lower() for c in item.findall('category') if c.text])
            combined_context = f"{title} {categories}"

            target_folder = None
            for key, folder in CATEGORY_MAPPING.items():
                if key in combined_context:
                    target_folder = folder
                    break

            if not target_folder:
                continue

            # Attachment URLs
            att = item.find('wp:attachment_url', NAMESPACES)
            if att is not None and att.text:
                fname = clean_url_name(att.text)
                image_targets[fname] = target_folder

            # Embedded content images
            content = item.find('content:encoded', NAMESPACES)
            if content is not None and content.text:
                found = re.findall(r'src="([^"]+\.(?:jpg|jpeg|png|webp|avif)[^"]*)"', content.text, re.IGNORECASE)
                for img_url in found:
                    fname = clean_url_name(img_url)
                    image_targets[fname] = target_folder

    print(f"\nMapped {len(image_targets)} image associations from exports.")
    
    # Sort files
    moved_count = 0
    remaining_files = os.listdir(SOURCE_DIR)

    for filename in remaining_files:
        src_path = os.path.join(SOURCE_DIR, filename)
        if not os.path.isfile(src_path):
            continue

        target_folder = image_targets.get(filename)

        # Fallback keyword match directly against filename if XML missed it
        if not target_folder:
            name_lower = filename.lower()
            for key, folder in CATEGORY_MAPPING.items():
                if key in name_lower:
                    target_folder = folder
                    break

        if target_folder:
            os.makedirs(target_folder, exist_ok=True)
            dest_path = os.path.join(target_folder, filename)
            shutil.copy2(src_path, dest_path)
            moved_count += 1

    print(f"Successfully copied {moved_count} images to gallery folders.")
    print("Unmatched images remain safely stored inside 'images/imported/' for manual review.")

if __name__ == "__main__":
    main()