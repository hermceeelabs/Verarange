import glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add text shadow flair to hero headlines
    content = content.replace('text-5xl sm:text-7xl lg:text-8xl font-normal', 'text-5xl sm:text-7xl lg:text-8xl font-normal hero-heading-shadow')
    content = content.replace('text-3xl sm:text-5xl text-brand-cherry', 'text-3xl sm:text-5xl text-brand-cherry text-flair-shadow')
    content = content.replace('text-4xl sm:text-5xl text-brand-cherry', 'text-4xl sm:text-5xl text-brand-cherry text-flair-shadow')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied text flair shadows safely across all pages!")
