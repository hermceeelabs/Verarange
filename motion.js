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

  // Header transparency & Maroon scroll transition
  const header = document.getElementById('siteHeader');
  if (header) {
    const handleScroll = () => {
      if (window.scrollY > 40) {
        header.classList.remove('header-transparent');
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
        header.classList.add('header-transparent');
      }
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Trigger on load
  }
});
