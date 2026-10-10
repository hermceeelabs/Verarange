replacements = [
    ('blog.html#post-1', 'journal-western-wedding-guide.html'),
    ('blog.html#post-2', 'journal-what-to-wear-guide.html'),
    ('blog.html#post-3', 'journal-ozarks-elopement-spots.html'),
    ('#post-1', 'journal-western-wedding-guide.html'),
    ('#post-2', 'journal-what-to-wear-guide.html'),
    ('#post-3', 'journal-ozarks-elopement-spots.html'),
    ('<span class="text-[11px] tracking-widest uppercase font-semibold text-brand-cherry cursor-pointer hover:underline">Read Article &rarr;</span>', '<a href="journal-western-wedding-guide.html" class="text-[11px] tracking-widest uppercase font-semibold text-brand-cherry hover:underline">Read Article &rarr;</a>')
]

for filepath in ['index.html', 'blog.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()

    for old, new in replacements:
        c = c.replace(old, new)

    # Make whole card rounded
    c = c.replace('class="group bg-brand-linenLight p-6 border', 'class="group bg-brand-linenLight p-6 rounded-2xl border')
    c = c.replace('class="bg-white border border-brand-linen p-6', 'class="group bg-white border border-brand-linen p-6 rounded-2xl')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)

# In blog.html specifically, wire up the 3 cards' read article buttons
with open('blog.html', 'r', encoding='utf-8') as f:
    blog_content = f.read()

blog_content = blog_content.replace('href="#post-1"', 'href="journal-western-wedding-guide.html"')
blog_content = blog_content.replace('id="post-1">\n          <div>', 'id="post-1" onclick="window.location=\'journal-western-wedding-guide.html\'" class="cursor-pointer">\n          <div>')
blog_content = blog_content.replace('id="post-2">\n          <div>', 'id="post-2" onclick="window.location=\'journal-what-to-wear-guide.html\'" class="cursor-pointer">\n          <div>')
blog_content = blog_content.replace('id="post-3">\n          <div>', 'id="post-3" onclick="window.location=\'journal-ozarks-elopement-spots.html\'" class="cursor-pointer">\n          <div>')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_content)

print("Linked all journal and stories cards directly to their dedicated story pages!")
