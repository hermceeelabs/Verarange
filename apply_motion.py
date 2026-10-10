import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Link motion.css
    if 'motion.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="motion.css">\n</head>')

    # Link motion.js
    if 'motion.js' not in content:
        content = content.replace('</body>', '  <script src="motion.js"></script>\n</body>')

    # Add motion-reveal to sections
    def section_replacer(match):
        attrs = match.group(1)
        if 'motion-reveal' not in attrs:
            return f'<section class="{attrs} motion-reveal"'
        return match.group(0)

    content = re.sub(r'<section\s+class="([^"]*)"', section_replacer, content)

    # Add hero-zoom to hero images
    content = content.replace('scale-105 transition-transform duration-1000', 'scale-105 transition-transform duration-1000 hero-zoom')

    # Add floating-widget to bottom widgets
    content = content.replace('class="fixed bottom-20 right-4 z-40', 'class="fixed bottom-20 right-4 z-40 floating-widget')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("All HTML pages upgraded with motion & animations!")
