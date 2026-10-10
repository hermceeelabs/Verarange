import re
import json

with open(r'C:/Users/User/.gemini/antigravity/brain/1d9026f7-d7cb-473b-9780-081b81952bab/.system_generated/steps/5/content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# find init_data json
match = re.search(r'<script id="init_data" type="application/json">\s*(\{.*?\})\s*</script>', text)
if match:
    data = json.loads(match.group(1))
    images = []
    # check blockData
    for b in data.get('blockData', []):
        for s in b.get('states', []):
            for mode in ['d', 'm']:
                if mode in s and 'bgImage' in s[mode]:
                    images.append(s[mode]['bgImage'])
        for mode in ['d', 'm']:
            if mode in b and 'bgImage' in b[mode]:
                images.append(b[mode]['bgImage'])
    # check elementData
    for el in data.get('elementData', []):
        if 'c' in el and 'key' in el['c']:
            images.append(el['c'])
    print(f"Extracted {len(images)} image records")
    seen = set()
    cleaned = []
    for img in images:
        k = img.get('key')
        if k and k not in seen:
            seen.add(k)
            cleaned.append({
                'title': img.get('title', ''),
                'aspect_ratio': img.get('aspect_ratio', 1.5),
                'url': f"https://static.showit.com/1200/{k}"
            })
    with open('extracted_images.json', 'w') as out:
        json.dump(cleaned, out, indent=2)
    print("Saved extracted_images.json:")
    for item in cleaned:
        print(item['title'], '->', item['url'])
