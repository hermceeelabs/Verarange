/**
 * Vera Range Photography - Theme Engine (Light / Dark Mode)
 * Luxury Western Palette with Smooth Transitions & LocalStorage Persistence
 */
(function() {
  const THEME_KEY = 'vr_theme_preference';

  // Apply saved theme immediately to prevent flash of wrong theme
  function getPreferredTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved) return saved;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
    updateToggleButtons(theme);
  }

  function updateToggleButtons(theme) {
    document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
      const icon = btn.querySelector('[data-lucide], i, svg');
      const label = btn.querySelector('.theme-label');
      if (theme === 'dark') {
        btn.setAttribute('aria-label', 'Switch to Light Mode');
        btn.setAttribute('title', 'Switch to Light Mode');
        if (label) label.textContent = 'Light';
      } else {
        btn.setAttribute('aria-label', 'Switch to Dark Mode');
        btn.setAttribute('title', 'Switch to Dark Mode');
        if (label) label.textContent = 'Dark';
      }
    });
    if (window.lucide) {
      window.lucide.createIcons();
    }
  }

  window.toggleTheme = function() {
    const isDark = document.documentElement.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    localStorage.setItem(THEME_KEY, newTheme);
    applyTheme(newTheme);
  };

  // Initial immediate application
  const initialTheme = getPreferredTheme();
  applyTheme(initialTheme);

  // Hook up event listeners once DOM is ready
  document.addEventListener('DOMContentLoaded', () => {
    applyTheme(getPreferredTheme());
    document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        window.toggleTheme();
      });
    });
  });
})();
