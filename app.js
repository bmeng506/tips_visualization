// app.js

// Smooth-scroll to a chart card by ID
function scrollToCard(cardId) {
    const el = document.getElementById(cardId);
    if (!el) return;
    el.scrollIntoView({ behavior: "smooth", block: "start" });
  }
  
  // View mode filters (all / overview / time / money)
  function setupFilters() {
    const buttons = Array.from(document.querySelectorAll(".pill-button"));
    const cards = Array.from(document.querySelectorAll(".chart-card"));
  
    function applyFilter(group) {
      cards.forEach((card) => {
        const cardGroup = card.getAttribute("data-group");
        if (group === "all" || cardGroup === group) {
          card.classList.remove("hidden");
        } else {
          card.classList.add("hidden");
        }
      });
    }
  
    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        const group = btn.getAttribute("data-filter");
  
        // active styling
        buttons.forEach((b) => b.classList.remove("pill-button--active"));
        btn.classList.add("pill-button--active");
  
        applyFilter(group);
      });
    });
  }
  
  // Insight chips → scroll to relevant chart
  function setupInsightChips() {
    const chips = Array.from(document.querySelectorAll(".insight-chip"));
    chips.forEach((chip) => {
      chip.addEventListener("click", () => {
        const targetId = chip.getAttribute("data-scroll-target");
        scrollToCard(targetId);
      });
    });
  }
  
  // Question selector → scroll to relevant chart
  function setupQuestionSelector() {
    const select = document.getElementById("questionSelector");
    if (!select) return;
  
    const mapping = {
      dist: "card-dist",
      day: "card-day",
      weekend: "card-weekend",
      meal: "card-meal",
      size: "card-size",
      bill: "card-bill",
      summary: "card-summary",
    };
  
    select.addEventListener("change", () => {
      const value = select.value;
      if (value === "none") return;
      const target = mapping[value];
      if (target) {
        scrollToCard(target);
      }
    });
  }
  
  // Lightbox / zoom for images
  function setupLightbox() {
    const lightbox = document.getElementById("lightbox");
    const lightboxImage = document.getElementById("lightboxImage");
    const lightboxCaption = document.getElementById("lightboxCaption");
    const lightboxClose = document.getElementById("lightboxClose");
  
    if (!lightbox || !lightboxImage || !lightboxCaption || !lightboxClose) return;
  
    const images = Array.from(document.querySelectorAll(".chart-image"));
  
    function showLightbox(src, caption) {
      lightboxImage.src = src;
      lightboxCaption.textContent = caption || "";
      lightbox.classList.remove("hidden");
    }
  
    function hideLightbox() {
      lightbox.classList.add("hidden");
      lightboxImage.src = "";
      lightboxCaption.textContent = "";
    }
  
    images.forEach((img) => {
      img.addEventListener("click", () => {
        const src = img.getAttribute("data-full") || img.src;
        const alt = img.alt || "Chart";
        showLightbox(src, alt);
      });
    });
  
    lightboxClose.addEventListener("click", hideLightbox);
  
    const backdrop = lightbox.querySelector(".bg-slate-950\\/80");
    if (backdrop) {
      backdrop.addEventListener("click", hideLightbox);
    }
  
    document.addEventListener("keydown", (evt) => {
      if (evt.key === "Escape" && !lightbox.classList.contains("hidden")) {
        hideLightbox();
      }
    });
  }
  
  // Init
  document.addEventListener("DOMContentLoaded", () => {
    setupFilters();
    setupInsightChips();
    setupQuestionSelector();
    setupLightbox();
  });
  