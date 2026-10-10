import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix Hero Badge (the uploaded screenshot):
    # Remove the dot and change font to maroon on soft linen/ivory pill
    old_badge_pattern = r'<div class="inline-flex items-center gap-3 px-4 py-1\.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 mb-8">\s*<span class="w-2 h-2 rounded-full bg-brand-olive animate-pulse"></span>\s*<span class="text-\[11px\] tracking-widest-plus uppercase font-medium text-white/90">(.*?)</span>\s*</div>'
    new_badge = r'<div class="inline-flex items-center px-6 py-2 rounded-full bg-[#FAFAF7]/90 backdrop-blur-md border border-white/30 shadow-sm mb-8"><span class="text-[11px] tracking-widest-plus uppercase font-semibold text-[#491211]">\1</span></div>'
    content = re.sub(old_badge_pattern, new_badge, content)

    # 2. Add rounded borders to ALL CTA buttons
    # Replace rounded-none or add rounded-full
    content = content.replace('rounded-none', 'rounded-full')
    
    # Generic button roundings
    content = re.sub(
        r'(class="[^"]*(?:px-7 py-3|px-8 py-3|px-9 py-4|py-3\.5|py-4)[^"]*(?:bg-brand-cherry|bg-white|border-brand-cherry|border-2)[^"]*)"',
        lambda m: m.group(0) if 'rounded-' in m.group(1) else m.group(0).replace(m.group(1), m.group(1) + ' rounded-full'),
        content
    )
    content = content.replace('header-cta-btn', 'header-cta-btn rounded-full')
    content = content.replace('rounded-none', 'rounded-full')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files with rounded buttons and cleaned hero badge!")
