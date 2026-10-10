import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change 'About Miley' to 'About'
    content = content.replace('>About Miley<', '>About<')
    content = content.replace('>About Miley</a>', '>About</a>')

    # 2. Align logo full left and header contents full right
    # Replace header container padding & layout
    content = re.sub(
        r'<div class="max-w-7xl mx-auto px-6 lg:px-12 h-24 flex items-center justify-between">',
        r'<div class="w-full px-6 lg:px-12 h-24 flex items-center justify-between">',
        content
    )

    # Push nav to the right
    content = re.sub(
        r'<nav class="hidden md:flex items-center gap-9',
        r'<nav class="hidden md:flex items-center gap-9 ml-auto mr-8',
        content
    )
    content = re.sub(
        r'<nav class="hidden md:flex items-center gap-10',
        r'<nav class="hidden md:flex items-center gap-9 ml-auto mr-8',
        content
    )

    # 3. Transparent header on top, maroon on scroll
    # We add header-scroll class to header
    content = re.sub(
        r'<header class="sticky top-0 z-50[^"]*"',
        r'<header id="siteHeader" class="sticky top-0 z-50 transition-all duration-500 header-transparent"',
        content
    )

    # Add id="brandLogo" to logo link
    content = content.replace(
        '<a href="index.html" class="group flex flex-col items-start">',
        '<a href="index.html" id="brandLogo" class="group flex flex-col items-start transition-colors duration-500">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all HTML files successfully!")
