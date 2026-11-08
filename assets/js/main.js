/**
 * Ranknix Online - Main Interactive Script
 * Auto Geo-Currency Detection (PKR, GBP, USD, EUR) + Counter Animations
 */

const AGENCY_CONFIG = {
  agencyName: "Ranknix Online",
  tagline: "Digital Agency",
  founderName: "Muhammad Abdullah",
  founderExp: "5+ Years Experience in Performance Marketing & Management",
  whatsappNumber: "923359276673", // User's WhatsApp number without leading +
  email: "contact@ranknix.online",
  phone: "+92 335 9276673",
  defaultCurrency: "PKR"
};

// PRICING DATA BY CURRENCY
const PRICING_DATA = {
  // Digital Marketing Plans (Monthly)
  "mkt-starter": {
    PKR: { amount: "₨ 45,000", period: "/ month" },
    GBP: { amount: "£149", period: "/ month" },
    USD: { amount: "$189", period: "/ month" },
    EUR: { amount: "€179", period: "/ month" }
  },
  "mkt-growth": {
    PKR: { amount: "₨ 85,000", period: "/ month" },
    GBP: { amount: "£279", period: "/ month" },
    USD: { amount: "$349", period: "/ month" },
    EUR: { amount: "€329", period: "/ month" }
  },
  "mkt-enterprise": {
    PKR: { amount: "₨ 145,000", period: "/ month" },
    GBP: { amount: "£479", period: "/ month" },
    USD: { amount: "$599", period: "/ month" },
    EUR: { amount: "€569", period: "/ month" }
  },

  // Web & E-Commerce Plans (One-Time)
  "web-starter": {
    PKR: { amount: "₨ 35,000", period: "one-time" },
    GBP: { amount: "£119", period: "one-time" },
    USD: { amount: "$149", period: "one-time" },
    EUR: { amount: "€139", period: "one-time" }
  },
  "web-shopify": {
    PKR: { amount: "₨ 65,000", period: "one-time" },
    GBP: { amount: "£219", period: "one-time" },
    USD: { amount: "$279", period: "one-time" },
    EUR: { amount: "€259", period: "one-time" }
  },
  "web-custom": {
    PKR: { amount: "₨ 125,000", period: "one-time" },
    GBP: { amount: "£419", period: "one-time" },
    USD: { amount: "$529", period: "one-time" },
    EUR: { amount: "€499", period: "one-time" }
  }
};

let currentCurrency = "PKR";

document.addEventListener('DOMContentLoaded', () => {
  initAOS();
  initGeoCurrency();
  initMobileMenu();
  initStatsCounter();
  initPricingSwitcher();
  initFaqAccordion();
  initModal();
  initWhatsAppButtons();
  initLeadForms();
  initMobileBottomNav();
});

// 1. INITIALIZE AOS ANIMATION ON SCROLL
function initAOS() {
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 750,
      easing: 'ease-out-cubic',
      once: true,
      offset: 40
    });
  }
}

// 2. GEO CURRENCY AUTO-DETECTION & SWITCHER
function initGeoCurrency() {
  if (window.RanknixCurrency) {
    window.RanknixCurrency.init();
  }

  const currencyBtns = document.querySelectorAll('[data-set-currency]');
  currencyBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const curr = btn.getAttribute('data-set-currency');
      setCurrency(curr, true);
    });
  });
}

function detectByTimezone() {
  if (window.RanknixCurrency) return;
}

function detectByIP() {
  if (window.RanknixCurrency) return;
}

function setCurrency(currency, isUserChoice = false) {
  if (window.RanknixCurrency) {
    window.RanknixCurrency.setCurrency(currency, isUserChoice);
    currentCurrency = currency;
    return;
  }
}

// 3. MOBILE MENU TOGGLE
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-btn');
  const closeBtn = document.getElementById('mobile-menu-close');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileLinks = document.querySelectorAll('.mobile-nav-link');

  if (!toggleBtn || !mobileMenu) return;

  const toggle = () => {
    mobileMenu.classList.toggle('hidden');
    document.body.classList.toggle('overflow-hidden');
  };

  toggleBtn.addEventListener('click', toggle);
  if (closeBtn) closeBtn.addEventListener('click', toggle);

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    });
  });
}

// 4. ANIMATED NUMBER COUNTERS (STATS)
function initStatsCounter() {
  const statElements = document.querySelectorAll('[data-counter-target]');
  if (!statElements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        obs.unobserve(el);

        const target = parseFloat(el.getAttribute('data-counter-target'));
        const prefix = el.getAttribute('data-prefix') || '';
        const suffix = el.getAttribute('data-suffix') || '';
        const decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
        const duration = 1800;
        const startTime = performance.now();

        const updateCount = (now) => {
          const elapsed = now - startTime;
          const progress = Math.min(elapsed / duration, 1);
          const easeOut = 1 - Math.pow(1 - progress, 3);
          const current = (target * easeOut).toFixed(decimals);

          el.textContent = `${prefix}${current}${suffix}`;

          if (progress < 1) {
            requestAnimationFrame(updateCount);
          } else {
            el.textContent = `${prefix}${target}${suffix}`;
          }
        };

        requestAnimationFrame(updateCount);
      }
    });
  }, { threshold: 0.2 });

  statElements.forEach(el => observer.observe(el));
}

// 5. PRICING TAB SWITCHER
function initPricingSwitcher() {
  const btnMarketing = document.getElementById('tab-marketing');
  const btnDev = document.getElementById('tab-dev');
  const contentMarketing = document.getElementById('pricing-marketing');
  const contentDev = document.getElementById('pricing-dev');

  if (!btnMarketing || !btnDev || !contentMarketing || !contentDev) return;

  btnMarketing.addEventListener('click', () => {
    btnMarketing.classList.add('bg-blue-600', 'text-white', 'shadow-md');
    btnMarketing.classList.remove('text-slate-600', 'hover:text-slate-900');
    btnDev.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
    btnDev.classList.add('text-slate-600', 'hover:text-slate-900');

    contentMarketing.classList.remove('hidden');
    contentDev.classList.add('hidden');
  });

  btnDev.addEventListener('click', () => {
    btnDev.classList.add('bg-blue-600', 'text-white', 'shadow-md');
    btnDev.classList.remove('text-slate-600', 'hover:text-slate-900');
    btnMarketing.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
    btnMarketing.classList.add('text-slate-600', 'hover:text-slate-900');

    contentDev.classList.remove('hidden');
    contentMarketing.classList.add('hidden');
  });
}

// 6. FAQ ACCORDION
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach((item, index) => {
    const trigger = item.querySelector('.faq-trigger');
    const content = item.querySelector('.faq-content');
    const icon = item.querySelector('.faq-icon');

    if (!trigger || !content) return;

    // Open first FAQ by default for instant engagement
    if (index === 0) {
      content.classList.add('active');
      if (icon) icon.classList.add('rotate-180');
    }

    trigger.addEventListener('click', () => {
      const isOpen = content.classList.contains('active');

      document.querySelectorAll('.faq-content').forEach(c => c.classList.remove('active'));
      document.querySelectorAll('.faq-icon').forEach(i => i.classList.remove('rotate-180'));

      if (!isOpen) {
        content.classList.add('active');
        if (icon) icon.classList.add('rotate-180');
      }
    });
  });
}

// 7. AUDIT MODAL
function initModal() {
  const modal = document.getElementById('audit-modal');
  const openBtns = document.querySelectorAll('.open-audit-modal');
  const closeBtns = document.querySelectorAll('.close-audit-modal');

  if (!modal) return;

  const openModal = () => {
    modal.classList.remove('hidden');
    setTimeout(() => modal.classList.remove('opacity-0'), 10);
    document.body.classList.add('overflow-hidden');
  };

  const closeModal = () => {
    modal.classList.add('opacity-0');
    setTimeout(() => {
      modal.classList.add('hidden');
      document.body.classList.remove('overflow-hidden');
    }, 250);
  };

  openBtns.forEach(btn => btn.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  }));

  closeBtns.forEach(btn => btn.addEventListener('click', closeModal));

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
}

// 8. DIRECT WHATSAPP ACTION BUTTONS
function initWhatsAppButtons() {
  const directBtns = document.querySelectorAll('[data-whatsapp-service]');
  
  directBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const service = btn.getAttribute('data-whatsapp-service') || 'General Inquiry';
      const plan = btn.getAttribute('data-whatsapp-plan') || '';
      
      let message = `Hi ${AGENCY_CONFIG.agencyName}! 👋 I am interested in: *${service}*`;
      if (plan) {
        message += ` (Plan: ${plan} in ${currentCurrency})`;
      }
      message += `. Please share details and procedure to start.`;

      const encodedMsg = encodeURIComponent(message);
      window.open(`https://wa.me/${AGENCY_CONFIG.whatsappNumber}?text=${encodedMsg}`, '_blank');
    });
  });
}

// 9. LEAD FORMS TO WHATSAPP
function initLeadForms() {
  // Modal Form
  const modalForm = document.getElementById('modal-lead-form');
  if (modalForm) {
    modalForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = modalForm.querySelector('[name="name"]').value.trim();
      const phone = modalForm.querySelector('[name="phone"]').value.trim();
      const business = modalForm.querySelector('[name="business"]').value.trim();
      const service = modalForm.querySelector('[name="service"]').value;
      const budget = modalForm.querySelector('[name="budget"]').value;

      const message = `🚀 *New Consultation Request for Ranknix Online*:\n\n` +
        `👤 *Name:* ${name}\n` +
        `📱 *Phone/WhatsApp:* ${phone}\n` +
        `🏢 *Business/Brand:* ${business || 'N/A'}\n` +
        `🎯 *Service Required:* ${service}\n` +
        `💰 *Estimated Budget:* ${budget} (${currentCurrency})\n\n` +
        `Founder: ${AGENCY_CONFIG.founderName} (Lead Strategist)\n` +
        `Looking forward to discussing the project!`;

      window.open(`https://wa.me/${AGENCY_CONFIG.whatsappNumber}?text=${encodeURIComponent(message)}`, '_blank');
      
      const modal = document.getElementById('audit-modal');
      if (modal) {
        modal.classList.add('hidden');
        document.body.classList.remove('overflow-hidden');
      }
      modalForm.reset();
    });
  }

  // Inline Contact Form
  const inlineForm = document.getElementById('contact-form');
  if (inlineForm) {
    inlineForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = inlineForm.querySelector('[name="name"]').value.trim();
      const phone = inlineForm.querySelector('[name="phone"]').value.trim();
      const service = inlineForm.querySelector('[name="service"]').value;
      const note = inlineForm.querySelector('[name="message"]').value.trim();

      const message = `👋 *New Agency Lead for Ranknix Online*:\n\n` +
        `👤 *Name:* ${name}\n` +
        `📱 *Contact:* ${phone}\n` +
        `🎯 *Service:* ${service}\n` +
        `💱 *Currency Region:* ${currentCurrency}\n` +
        `📝 *Notes:* ${note || 'Interested in consultation'}\n\n` +
        `Attention: ${AGENCY_CONFIG.founderName} & Team`;

      window.open(`https://wa.me/${AGENCY_CONFIG.whatsappNumber}?text=${encodeURIComponent(message)}`, '_blank');
      inlineForm.reset();
    });
  }
}

// 10. MOBILE BOTTOM NAVIGATION ACTIVE TRACKER
function initMobileBottomNav() {
  const mbnLinks = document.querySelectorAll('.mbn-link');
  if (!mbnLinks.length) return;

  const currentPath = window.location.pathname.toLowerCase();
  const isHome = currentPath === '/' || currentPath.endsWith('index.html') || currentPath === '';

  function updateActive() {
    let activeFound = false;

    // Check if scrolled to testimonials on homepage
    if (isHome) {
      const testimonials = document.getElementById('testimonials');
      if (testimonials) {
        const rect = testimonials.getBoundingClientRect();
        if (rect.top <= window.innerHeight * 0.45 && rect.bottom >= window.innerHeight * 0.2) {
          mbnLinks.forEach(l => l.classList.toggle('active', l.dataset.page === 'reviews'));
          return;
        }
      }
    }

    mbnLinks.forEach(link => {
      const page = link.dataset.page;
      let isActive = false;
      if (page === 'home' && isHome && (!window.location.hash || window.location.hash !== '#testimonials')) {
        isActive = true;
      } else if (page === 'development' && currentPath.includes('development')) {
        isActive = true;
      } else if (page === 'marketing' && currentPath.includes('marketing')) {
        isActive = true;
      } else if (page === 'automation' && currentPath.includes('automation')) {
        isActive = true;
      } else if (page === 'pricing' && currentPath.includes('pricing')) {
        isActive = true;
      }

      link.classList.toggle('active', isActive);
      if (isActive) activeFound = true;
    });

    if (!activeFound && isHome) {
      const homeLink = document.querySelector('.mbn-link[data-page="home"]');
      if (homeLink) homeLink.classList.add('active');
    }
  }

  window.addEventListener('scroll', updateActive, { passive: true });
  updateActive();
}

