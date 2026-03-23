"""Clean extracted content - remove Wix framework noise, keep readable text."""
import os
import re

NOISE_PATTERNS = [
    r'^\{',           # JSON objects
    r'^@view-transition',
    r'^\.[\w]+\{',     # CSS rules
    r'^=0&&',
    r'^\(l\+=',
    r'^\{let ',
    r'^l\?0',
    r'^0&&o\[',
    r'Remove the POWr',
    r'^Select from an email',
    r'^The number of different forms',
    r'^Increase the number of form',
    r'^Select the number of people',
    r'^Select your preferred payment',
    r'^Allow users to upload files',
    r'^See all of your form responses',
    r'^Show a message, redirect',
    r'^Design your own customer',
    r'^Keep your forms short',
    r'^Better Reading Instruction$',
    r'^with Dr\. Jan Richardson$',
    r'^Guided Reading and Reading Science$',
    r'^Next Steps/Science of Reading$',
    r'^JACK HARTMANN/JAN RICHARDSON$',
    r"^JAN'S PRODUCTS$",
    r'^COMMON CORE STANDARDS$',
    r'^LITERACY CONSULTANTS$',
    r'^SUCCESS STORIES$',
    r'^LITERACY TIPS$',
    r'^CONFERENCES/WEBINARS$',
    r'^VIDEO CLIPS$',
    r'^RISE RESOURCES$',
    r'^RESOURCES$',
    r'fleetConfig',
    r'thunderbolt',
    r'parastorage',
    r'wixstatic',
    r'componentsLibrariesTopology',
    r'siteAssetsUrl',
    r'ssrPropsUpdates',
    r'compIdToTypeMap',
    r'prefetch.*mpa-prefetch',
    r'metaSiteId',
    r'menuItemIds',
    r'moreSubItem',
    r'hoverState',
    r'dropWrapper',
    r'moreContainerLeft',
    r'lineHeight.*menuBorderY',
    r'PageMountUnmount',
    r'DynamicStructureContainer',
    r'StripColumnsContainer',
    r'MediaContainer',
    r'WRichText',
    r'ClassicSection',
    r'HeaderContainer',
    r'FooterContainer',
    r'VerticalMenu',
    r'StylableButton',
    r'PagesContainer',
    r'PageBackground',
    r'BackgroundGroup',
    r'SkipToContentButton',
    r'Repeater',
    r'^RESEARCH \|',
    r'\| jrreading$',
    r'view-transition',
]


def is_noise(text):
    for pat in NOISE_PATTERNS:
        if re.search(pat, text):
            return True
    if len(text) < 10:
        return True
    # Pure code/minified JS
    if text.count('{') > 3 or text.count('}') > 3:
        return True
    if text.count('===') > 0 or text.count('!==') > 0:
        return True
    if 'parseInt' in text or 'Math.max' in text:
        return True
    return False


def clean_page(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    clean_blocks = []
    current_block = None

    for line in lines:
        line = line.strip()
        # Skip block number headers
        m = re.match(r'^\[(\d+)\]\s*(.*)', line)
        if m:
            text = m.group(2).strip()
            if text and not is_noise(text):
                clean_blocks.append(text)
        elif line and not line.startswith('PAGE:') and not line.startswith('Extracted') and not line.startswith('==='):
            if not is_noise(line):
                # Could be continuation of previous block
                if clean_blocks:
                    clean_blocks[-1] += ' ' + line
                else:
                    clean_blocks.append(line)

    return clean_blocks


def main():
    scrape_dir = 'C:/Users/ginja/reading-specialist'
    content_files = sorted(f for f in os.listdir(scrape_dir)
                           if f.startswith('content_') and f.endswith('.txt'))

    page_order = [
        'content_homepage.txt',
        'content_products.txt',
        'content_resources.txt',
        'content_literacy_tips.txt',
        'content_video_clips.txt',
        'content_success_stories.txt',
        'content_research.txt',
        'content_rise_resources.txt',
        'content_science_of_reading.txt',
        'content_guided_reading_science.txt',
        'content_jack_hartmann.txt',
        'content_consultants.txt',
    ]

    # Use ordered list, fall back to alphabetical for any missing
    ordered = []
    for f in page_order:
        if f in content_files:
            ordered.append(f)
    for f in content_files:
        if f not in ordered:
            ordered.append(f)

    page_titles = {
        'homepage': 'Homepage',
        'products': "Jan's Products",
        'resources': 'Resources',
        'literacy_tips': 'Literacy Tips',
        'video_clips': 'Video Clips',
        'success_stories': 'Success Stories',
        'research': 'Research',
        'rise_resources': 'RISE Resources',
        'science_of_reading': 'Next Steps & Science of Reading',
        'guided_reading_science': 'Guided Reading and Reading Science',
        'jack_hartmann': 'Jack Hartmann / Jan Richardson',
        'consultants': 'Literacy Consultants',
    }

    md_path = os.path.join(scrape_dir, 'WEBSITE_SCRAPE.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Jan Richardson Reading Website - Complete Scrape\n\n")
        f.write("*Source: janrichardsonreading.com*\n")
        f.write("*Scraped: 2026-03-22*\n")
        f.write("*12 pages captured with full JavaScript rendering*\n\n")
        f.write("---\n\n")

        total_blocks = 0
        for fname in ordered:
            filepath = os.path.join(scrape_dir, fname)
            blocks = clean_page(filepath)
            page_name = fname.replace('content_', '').replace('.txt', '')
            title = page_titles.get(page_name, page_name.replace('_', ' ').title())

            f.write(f"## {title}\n\n")
            f.write(f"**URL:** janrichardsonreading.com/{page_name if page_name != 'homepage' else ''}\n\n")

            for block in blocks:
                f.write(f"{block}\n\n")

            f.write("---\n\n")
            total_blocks += len(blocks)
            print(f"{title}: {len(blocks)} clean blocks")

        print(f"\nTotal: {total_blocks} clean content blocks -> WEBSITE_SCRAPE.md")


if __name__ == '__main__':
    main()
