import os
import re
import urllib.request
import xml.etree.ElementTree as ET

# Automatically find any Squarespace XML export files in the current folder
XML_FILES = [
    f for f in os.listdir(".") if f.lower().startswith("squarespace-wordpress-export") and f.lower().endswith(".xml")
]

NAMESPACES = {
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wp': 'http://wordpress.org/export/1.2/'
}

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def download_image(url, save_path):
    if os.path.exists(save_path):
        print(f"  [Skipped] Already exists: {save_path}")
        return True
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"  [Downloaded] {save_path}")
        return True
    except Exception as e:
        print(f"  [Error] Failed to download {url}: {e}")
        return False

def main():
    if not XML_FILES:
        print("No Squarespace XML export files found in this folder.")
        return

    ensure_path = "images/imported"
    ensure_dir(ensure_path)

    image_urls = set()

    for xml_file in XML_FILES:
        print(f"Scanning {xml_file} for image links...")
        tree = ET.parse(xml_file)
        root = tree.getroot()
        channel = root.find('channel')

        for item in channel.findall('item'):
            # 1. Check attachment URLs (media library items)
            attachment_url = item.find('wp:attachment_url', NAMESPACES)
            if attachment_url is not None and attachment_url.text:
                url = attachment_url.text.strip()
                if any(url.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp', '.avif']):
                    image_urls.add(url)

            # 2. Scan HTML content for embedded <img> tags
            content_el = item.find('content:encoded', NAMESPACES)
            if content_el is not None and content_el.text:
                found_imgs = re.findall(r'src="([^"]+\.(?:jpg|jpeg|png|webp|avif)[^"]*)"', content_el.text, re.IGNORECASE)
                for img_url in found_imgs:
                    image_urls.add(img_url)

    print(f"\nFound {len(image_urls)} unique image URLs across your XML files.")
    print("Starting bulk download...\n")

    success_count = 0
    for idx, url in enumerate(image_urls, start=1):
        filename = url.split('/')[-1].split('?')[0] # Clean query parameters from URL
        if not filename:
            filename = f"image-{idx}.jpg"
        
        save_path = os.path.join(ensure_path, filename)
        print(f"({idx}/{len(image_urls)}) Fetching {filename}...")
        if download_image(url, save_path):
            success_count += 1

    print(f"\nDone! Successfully downloaded {success_count} of {len(image_urls)} images into '{ensure_path}/'.")

if __name__ == "__main__":
    main()