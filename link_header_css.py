import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'header.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="header.css">\n</head>')

    # Logo spans
    content = content.replace('uppercase font-medium">VERA RANGE', 'uppercase font-medium logo-title transition-colors">VERA RANGE')
    content = content.replace('font-semibold -mt-0.5">Photography', 'font-semibold -mt-0.5 logo-sub transition-colors">Photography')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Linked header.css and updated logo spans across all HTML files!")
