import glob
import re

footer_template = """  <!-- FOOTER (Unified Across All Pages) -->
  <footer class="bg-brand-cherry text-brand-linenLight py-12 px-6 sm:px-12 my-8">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-8">
      <div class="text-center md:text-left">
        <span class="font-serif tracking-ultra text-2xl text-white uppercase block">VERA RANGE PHOTOGRAPHY</span>
        <p class="text-xs text-brand-linen/80 mt-1 font-light">
          Southwest Missouri &bull; Oklahoma &bull; Arkansas &bull; Worldwide Travel
        </p>
      </div>

      <div class="flex flex-wrap justify-center gap-6 text-xs uppercase tracking-widest text-brand-linen">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <a href="portfolio.html" class="hover:text-white transition-colors">Portfolio</a>
        <a href="about.html" class="hover:text-white transition-colors">About</a>
        <a href="services.html" class="hover:text-white transition-colors">Services</a>
        <a href="blog.html" class="hover:text-white transition-colors">Journal</a>
        <a href="inquire.html" class="hover:text-white transition-colors">Contact</a>
      </div>

      <div class="text-center md:text-right text-[11px] text-brand-linen/70 font-light">
        <p>&copy; Vera Range Photography. All Rights Reserved.</p>
      </div>
    </div>
  </footer>"""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = re.sub(r'<!--\s*(?:FOOTER|Footer).*?</footer>', footer_template, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Unified footer layout and content cleanly across all pages!")
