/**
 * Vera Range Motion Engine
 * Lightweight, high-performance IntersectionObserver animation driver
 */
document.addEventListener('DOMContentLoaded', () => {
  // Page load fade-in
  document.body.classList.add('page-loaded');

  // Scroll reveal observer
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -80px 0px',
    threshold: 0.1
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('motion-visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.motion-reveal, .motion-scale').forEach(el => {
    revealObserver.observe(el);
  });

  // Smooth parallax on hero images if present
  const heroImg = document.querySelector('.hero-zoom');
  if (heroImg) {
    window.addEventListener('scroll', () => {
      const scrollY = window.pageYOffset;
      if (scrollY < window.innerHeight) {
        heroImg.style.transform = `scale(1.04) translateY(${scrollY * 0.2}px)`;
      }
    }, { passive: true });
  }

  // Active scroll detector: Transparent when idle/not scrolling, solid maroon during active scroll
  const header = document.getElementById('siteHeader');
  if (header) {
    let scrollTimer = null;

    const setHeaderSolid = () => {
      header.classList.remove('header-transparent');
      header.classList.add('header-scrolled');
    };

    const setHeaderTransparent = () => {
      header.classList.remove('header-scrolled');
      header.classList.add('header-transparent');
    };

    // Ensure it starts transparent
    setHeaderTransparent();

    window.addEventListener('scroll', () => {
      // While scrolling, make it solid maroon
      setHeaderSolid();

      // Reset timer: when scrolling stops for 1.2s, smoothly return to transparent
      if (scrollTimer !== null) {
        clearTimeout(scrollTimer);
      }
      scrollTimer = setTimeout(() => {
        setHeaderTransparent();
      }, 1200);
    }, { passive: true });
  }
});
