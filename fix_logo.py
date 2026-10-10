import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure id="brandLogo" exists on the logo anchor
    content = content.replace('<a href="index.html" class="flex flex-col items-start">', '<a href="index.html" id="brandLogo" class="flex flex-col items-start">')
    content = content.replace('<a href="index.html" class="group flex flex-col items-start">', '<a href="index.html" id="brandLogo" class="group flex flex-col items-start">')

    # Also make sure the logo spans have logo-title and logo-sub
    if 'logo-title' not in content:
        content = content.replace('text-brand-cherry uppercase font-medium', 'text-brand-cherry uppercase font-medium logo-title transition-colors')
        content = content.replace('text-brand-olive font-semibold -mt-0.5', 'text-brand-olive font-semibold -mt-0.5 logo-sub transition-colors')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Brand logo markup normalized across all pages!")
