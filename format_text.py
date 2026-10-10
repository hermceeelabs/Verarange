import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove dashes
    content = content.replace('&mdash;', ' ')
    content = content.replace('&ndash;', ' ')
    content = content.replace(' — ', ' ')
    content = content.replace(' – ', ' ')
    content = content.replace('—', ' ')
    content = content.replace('–', ' ')

    # Remove leading dashes from testimonial attributions: e.g. >— Morgan or >- Morgan
    content = re.sub(r'>\s*[-—–]\s*', '>', content)

    # 2. Add text-justify to paragraph containers
    content = re.sub(
        r'<p\s+class="([^"]*text-(?:gray|base|sm|xs)[^"]*)"',
        lambda m: f'<p class="{m.group(1)} text-justify"' if 'text-justify' not in m.group(1) else m.group(0),
        content
    )

    # In space-y containers holding paragraph text
    content = content.replace('class="space-y-4 text-gray-700', 'class="space-y-4 text-gray-700 text-justify')
    content = content.replace('class="space-y-5 text-gray-700', 'class="space-y-5 text-gray-700 text-justify')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied justification and removed dashes across all HTML files!")
