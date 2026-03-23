"""Extract text content from scraped Wix HTML pages."""
import re
import html
import os
import json

SKIP_WORDS = ['function(', 'var ', 'margin:', 'padding:', 'display:',
              'window.', 'document.', 'return ', 'typeof', 'undefined',
              'createElement', 'appendChild', 'querySelector', 'addEventListener',
              'prototype', 'constructor', 'Object.', 'Array.', 'String.',
              'font-family', 'font-size', 'line-height', 'text-align',
              'background-color', 'border-radius', 'box-shadow']


def should_skip(text):
    return any(s in text for s in SKIP_WORDS)


def clean_html(raw):
    raw = raw.replace('\\n', '\n').replace('\\"', '"').replace('\\/', '/')
    raw = raw.replace('\\u003c', '<').replace('\\u003e', '>')
    raw = raw.replace('\\u0026', '&').replace('\\u0027', "'")
    clean = re.sub(r'<[^>]+>', ' ', html.unescape(raw))
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean


def extract_wix_content(html_content):
    texts = []

    # 1) Text between HTML tags
    for m in re.finditer(r'>([^<]{15,})<', html_content):
        t = html.unescape(m.group(1)).strip()
        if not should_skip(t):
            texts.append(t)

    # 2) JSON "text" fields
    for m in re.finditer(r'"text"\s*:\s*"((?:[^"\\]|\\.){20,})"', html_content):
        clean = clean_html(m.group(1))
        if len(clean) > 15 and not should_skip(clean):
            texts.append(clean)

    # 3) JSON "html" fields (Wix rich text content)
    for m in re.finditer(r'"html"\s*:\s*"((?:[^"\\]|\\.){20,})"', html_content):
        clean = clean_html(m.group(1))
        if len(clean) > 15 and not should_skip(clean):
            texts.append(clean)

    # 4) JSON "label" and "title" fields
    for m in re.finditer(r'"(?:label|title|alt|description)"\s*:\s*"((?:[^"\\]|\\.){10,})"', html_content):
        clean = clean_html(m.group(1))
        if len(clean) > 10 and not should_skip(clean):
            texts.append(clean)

    # 5) Look for Wix masterPage data
    for m in re.finditer(r'"plainText"\s*:\s*"((?:[^"\\]|\\.){10,})"', html_content):
        clean = clean_html(m.group(1))
        if len(clean) > 10 and not should_skip(clean):
            texts.append(clean)

    # Deduplicate preserving order
    seen = set()
    unique = []
    for t in texts:
        key = t[:150]
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return unique


def main():
    scrape_dir = os.path.dirname(os.path.abspath(__file__))
    files = sorted(f for f in os.listdir(scrape_dir)
                   if f.startswith('scrape_') and f.endswith('.html'))

    all_content = {}
    for fname in files:
        filepath = os.path.join(scrape_dir, fname)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        extracted = extract_wix_content(content)
        page_name = fname.replace('scrape_', '').replace('.html', '')
        all_content[page_name] = extracted

        # Save individual text file
        out_path = os.path.join(scrape_dir, f'content_{page_name}.txt')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"PAGE: {page_name}\n")
            f.write(f"Extracted text blocks: {len(extracted)}\n")
            f.write("=" * 60 + "\n\n")
            for i, text in enumerate(extracted):
                f.write(f"[{i+1}] {text}\n\n")

        print(f"{page_name}: {len(extracted)} text blocks -> content_{page_name}.txt")

    # Save combined markdown
    md_path = os.path.join(scrape_dir, 'WEBSITE_SCRAPE.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("# Jan Richardson Reading Website — Full Scrape\n\n")
        f.write("*Scraped: 2026-03-22*\n")
        f.write("*Source: janrichardsonreading.com (all pages)*\n\n")
        f.write("---\n\n")
        for page_name, blocks in all_content.items():
            f.write(f"## {page_name.replace('_', ' ').title()}\n\n")
            f.write(f"*{len(blocks)} content blocks extracted*\n\n")
            for i, text in enumerate(blocks):
                f.write(f"{text}\n\n")
            f.write("---\n\n")

    print(f"\nCombined -> WEBSITE_SCRAPE.md")


if __name__ == '__main__':
    main()
