(function () {
    const STORAGE_KEY = 'academico-theme';
    const root = document.documentElement;
    const toggleBtn = document.getElementById('themeToggle');

    function applyTheme(theme) {
        root.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
        if (toggleBtn) {
            toggleBtn.textContent = theme === 'dark' ? 'Modo Claro' : 'Modo Escuro';
        }
    }

    const savedTheme = localStorage.getItem(STORAGE_KEY);
    if (savedTheme === 'dark' || savedTheme === 'light') {
        applyTheme(savedTheme);
    } else {
        applyTheme('light');
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', function () {
            const currentTheme = root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
            applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
        });
    }

    document.addEventListener('keydown', function (event) {
        if (event.ctrlKey && event.shiftKey && event.key.toLowerCase() === 'd') {
            event.preventDefault();
            const currentTheme = root.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
            applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
        }
    });
})();