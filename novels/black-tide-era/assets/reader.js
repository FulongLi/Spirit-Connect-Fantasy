(function () {
  const copy = {
    zh: {
      brand: "灵接幻想",
      archive: "返回番外",
      day: "白天",
      night: "夜间",
      kicker: "番外 · 筹备中",
      title: "黑潮时代",
      subtitle: "Black Tide Era",
      intro: "以 CP2 先生为主角，讲述他的早年生活，以及他亲历黑潮时代的故事。",
      author: "李富龙 著",
      catalogKicker: "章节索引",
      catalogTitle: "中文阅读目录",
      catalogEmpty: "章节尚未发布。",
    },
    en: {
      brand: "Spirit Connect Fantasy",
      archive: "Back to Spin-offs",
      day: "Day",
      night: "Night",
      kicker: "Spin-off · In development",
      title: "Black Tide Era",
      subtitle: "黑潮时代",
      intro: "A side story about CP2's early life and what he lived through during the Black Tide.",
      author: "By Fulong Li",
      catalogKicker: "Chapter Index",
      catalogTitle: "English Index",
      catalogEmpty: "Chapters have yet to be published.",
    },
  };

  const translatedNodes = document.querySelectorAll("[data-i18n]");
  const languageButtons = document.querySelectorAll("button[data-lang]");
  const themeButtons = document.querySelectorAll("button[data-mode]");
  const archiveLink = document.getElementById("archive-link");

  function setLanguage(lang) {
    const text = copy[lang];
    document.body.dataset.lang = lang;
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en";
    document.title = `${text.title} | ${text.brand}`;
    archiveLink.href = `../../?lang=${lang}#extras`;
    translatedNodes.forEach((node) => {
      node.textContent = text[node.dataset.i18n];
    });
    languageButtons.forEach((button) => {
      const active = button.dataset.lang === lang;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    localStorage.setItem("blackTideEraLang", lang);
  }

  function setTheme(theme) {
    document.body.dataset.theme = theme;
    themeButtons.forEach((button) => {
      const active = button.dataset.mode === theme;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    localStorage.setItem("blackTideEraTheme", theme);
  }

  languageButtons.forEach((button) => {
    button.addEventListener("click", () => setLanguage(button.dataset.lang));
  });
  themeButtons.forEach((button) => {
    button.addEventListener("click", () => setTheme(button.dataset.mode));
  });

  const requestedLang = new URLSearchParams(window.location.search).get("lang") ||
    localStorage.getItem("blackTideEraLang") || localStorage.getItem("spiritConnectLang");
  const preferredTheme = localStorage.getItem("blackTideEraTheme") || localStorage.getItem("spiritConnectTheme");
  setLanguage(requestedLang === "en" ? "en" : "zh");
  setTheme(preferredTheme === "day" ? "day" : "night");
})();
