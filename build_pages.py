import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import the 3 service data files
from services_data_part1 import SERVICES_DATA as p1
from services_data_part2 import SERVICES_DATA_PART2 as p2
from services_data_part3 import SERVICES_DATA_PART3 as p3

ALL_SERVICES = p1 + p2 + p3
print(f"Total services loaded: {len(ALL_SERVICES)}")

OUTPUT_DIR = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\services"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_service_html(s):
    slug = s["slug"]
    name = s["name"]
    num = s["num"]
    category = s["category"]
    cat_badge_class = s.get("cat_badge_class", "badge-dev")
    cat_icon = s.get("cat_icon", "fa-solid fa-code")
    icon = s["icon"]
    icon_bg = s.get("icon_bg", "bg-blue-100 text-blue-600")
    h1_prefix = s["h1_prefix"]
    h1_gradient = s["h1_gradient"]
    description = s["description"]
    stats = s["stats"]
    platforms = s["platforms"]
    deliverables = s["deliverables"]
    pricing = s["pricing"]
    faqs = s["faqs"]

    # Pre-render stats HTML
    stats_html = ""
    for val, lbl in stats:
        stats_html += f"""
        <div class="clean-card rounded-2xl p-5 text-center flex flex-col justify-center items-center">
          <span class="text-3xl sm:text-4xl font-black text-slate-900 font-heading mb-1 tracking-tight text-gradient-blue">{val}</span>
          <span class="text-xs sm:text-sm font-bold text-slate-600">{lbl}</span>
        </div>"""

    # Pre-render platform pills
    platform_pills = ""
    for p in platforms:
        platform_pills += f'<span class="hero-tech-pill"><i class="fa-solid fa-circle-check text-blue-600 text-[10px]"></i><span>{p}</span></span>\n'

    # Pre-render deliverables
    deliverables_html = ""
    for d in deliverables:
        deliverables_html += f"""
        <div class="clean-card rounded-2xl p-6 sm:p-7 flex flex-col justify-between" data-aos="fade-up">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-blue-50 border border-blue-200/80 text-blue-600 flex items-center justify-center text-xl mb-5 shadow-xs">
              <i class="{d['icon']}"></i>
            </div>
            <h3 class="text-lg font-black text-slate-900 font-heading mb-2.5">{d['title']}</h3>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">{d['desc']}</p>
          </div>
        </div>"""

    # Pre-render pricing cards
    pricing_html = f"""
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Starter Tier -->
        <div class="clean-card rounded-3xl p-8 flex flex-col justify-between border-2 border-slate-200" data-aos="fade-up">
          <div>
            <span class="inline-block px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-black tracking-wide uppercase mb-3">
              {pricing['starter']['name']}
            </span>
            <div class="my-4">
              <span class="text-4xl font-black text-slate-900 font-heading dynamic-price" data-pkr="{pricing['starter']['pkr']}" data-gbp="{pricing['starter']['gbp']}" data-usd="{pricing['starter']['usd']}" data-eur="{pricing['starter']['eur']}">{pricing['starter']['pkr']}</span>
              <span class="text-xs font-bold text-slate-500 block mt-1">Starting investment</span>
            </div>
            <ul class="space-y-3 pt-4 border-t border-slate-100 mb-8 text-xs sm:text-sm text-slate-700">
              {"".join(f'<li class="flex items-start gap-2.5"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span>{f}</span></li>' for f in pricing['starter']['features'])}
            </ul>
          </div>
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20interested%20in%20the%20{pricing['starter']['name']}%20tier%20for%20{name}." target="_blank" class="w-full py-3.5 rounded-xl border-2 border-slate-300 hover:border-blue-600 bg-white hover:bg-blue-50 text-slate-800 hover:text-blue-700 text-xs font-black tracking-wide transition text-center flex items-center justify-center gap-2">
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>Order via WhatsApp</span>
          </a>
        </div>

        <!-- Growth Tier (Recommended) -->
        <div class="clean-card rounded-3xl p-8 flex flex-col justify-between border-2 border-blue-600 shadow-xl relative" data-aos="fade-up" data-aos-delay="100">
          <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-[11px] font-black uppercase tracking-wider shadow-md">
            Most Popular
          </div>
          <div>
            <span class="inline-block px-3 py-1 rounded-full bg-blue-100 text-blue-800 text-xs font-black tracking-wide uppercase mb-3">
              {pricing['growth']['name']}
            </span>
            <div class="my-4">
              <span class="text-4xl font-black text-slate-900 font-heading dynamic-price" data-pkr="{pricing['growth']['pkr']}" data-gbp="{pricing['growth']['gbp']}" data-usd="{pricing['growth']['usd']}" data-eur="{pricing['growth']['eur']}">{pricing['growth']['pkr']}</span>
              <span class="text-xs font-bold text-slate-500 block mt-1">Accelerated growth package</span>
            </div>
            <ul class="space-y-3 pt-4 border-t border-slate-100 mb-8 text-xs sm:text-sm text-slate-700">
              {"".join(f'<li class="flex items-start gap-2.5"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span class="font-semibold">{f}</span></li>' for f in pricing['growth']['features'])}
            </ul>
          </div>
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20interested%20in%20the%20{pricing['growth']['name']}%20tier%20for%20{name}." target="_blank" class="w-full py-3.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white text-xs font-black tracking-wide shadow-lg shadow-blue-500/25 btn-shimmer transition text-center flex items-center justify-center gap-2">
            <i class="fa-brands fa-whatsapp text-white text-base"></i>
            <span>Get Started Now &rarr;</span>
          </a>
        </div>

        <!-- Enterprise Tier -->
        <div class="clean-card rounded-3xl p-8 flex flex-col justify-between border-2 border-slate-200" data-aos="fade-up" data-aos-delay="200">
          <div>
            <span class="inline-block px-3 py-1 rounded-full bg-slate-100 text-slate-700 text-xs font-black tracking-wide uppercase mb-3">
              {pricing['enterprise']['name']}
            </span>
            <div class="my-4">
              <span class="text-4xl font-black text-slate-900 font-heading dynamic-price" data-pkr="{pricing['enterprise']['pkr']}" data-gbp="{pricing['enterprise']['gbp']}" data-usd="{pricing['enterprise']['usd']}" data-eur="{pricing['enterprise']['eur']}">{pricing['enterprise']['pkr']}</span>
              <span class="text-xs font-bold text-slate-500 block mt-1">Comprehensive scale & custom</span>
            </div>
            <ul class="space-y-3 pt-4 border-t border-slate-100 mb-8 text-xs sm:text-sm text-slate-700">
              {"".join(f'<li class="flex items-start gap-2.5"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span>{f}</span></li>' for f in pricing['enterprise']['features'])}
            </ul>
          </div>
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20interested%20in%20the%20{pricing['enterprise']['name']}%20tier%20for%20{name}." target="_blank" class="w-full py-3.5 rounded-xl border-2 border-slate-300 hover:border-blue-600 bg-white hover:bg-blue-50 text-slate-800 hover:text-blue-700 text-xs font-black tracking-wide transition text-center flex items-center justify-center gap-2">
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>Discuss Custom Scope</span>
          </a>
        </div>
      </div>
    """

    # Pre-render FAQs
    faqs_html = ""
    for idx, f in enumerate(faqs, 1):
        faqs_html += f"""
        <div class="faq-item clean-card rounded-2xl overflow-hidden">
          <button class="faq-trigger w-full px-6 py-5 text-left font-bold text-slate-900 text-base flex items-center justify-between gap-4">
            <span class="flex items-center gap-3">
              <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-black shrink-0">{idx}</span>
              <span>{f['q']}</span>
            </span>
            <i class="faq-icon fa-solid fa-chevron-down text-xs text-slate-400 transition-transform"></i>
          </button>
          <div class="faq-content {'hidden' if idx > 1 else ''} px-6 pb-6 text-slate-600 text-sm leading-relaxed border-t border-slate-100 pt-4">
            {f['a']}
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} Services | Ranknix Online - Digital Agency</title>
  <meta name="description" content="{description[:160]}">
  <link rel="icon" type="image/png" href="../assets/images/logo.png">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            primary: '#0284c7',
            secondary: '#2563eb',
            dark: '#0f172a',
            surface: '#f8fafc',
          }},
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            heading: ['Outfit', 'sans-serif'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Google Fonts & Font Awesome 6 -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="bg-white text-slate-800 antialiased font-sans selection:bg-blue-600 selection:text-white">

  <!-- 1. TOP ANNOUNCEMENT BAR -->
  <div class="bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 text-white text-[11px] sm:text-xs py-2 px-4 border-b border-blue-900/40 relative z-50">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-black bg-blue-500 text-white uppercase tracking-wider">
          Ranknix Official Service
        </span>
        <span class="hidden sm:inline text-slate-300">
          Professional {name} overseen by Founder Muhammad Abdullah
        </span>
      </div>
      <div class="flex items-center gap-4 text-slate-300 ml-auto">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{name}." target="_blank" class="hover:text-emerald-400 transition flex items-center gap-1 font-bold">
          <i class="fa-brands fa-whatsapp text-emerald-400"></i>
          <span>+92 308 8163940</span>
        </a>
        <span class="text-slate-600 hidden md:inline">|</span>
        <a href="mailto:contact@ranknix.online" class="hover:text-blue-400 transition hidden md:flex items-center gap-1">
          <i class="fa-solid fa-envelope text-blue-400"></i>
          <span>contact@ranknix.online</span>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. NAVIGATION BAR -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 transition-all shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-[68px]">
        
        <!-- Left: Brand Logo Lockup -->
        <a href="../index.html" class="flex items-center gap-2.5 sm:gap-3 group shrink-0">
          <img src="../assets/images/logo.png" alt="Ranknix Online Logo" class="h-10 sm:h-11 w-auto transition-transform group-hover:scale-105">
          <div class="flex flex-col justify-center -space-y-1">
            <span class="text-lg sm:text-[21px] font-black tracking-tight text-slate-900 font-heading leading-tight whitespace-nowrap">
              Ranknix
            </span>
            <span class="text-lg sm:text-[21px] font-black tracking-tight text-blue-600 font-heading leading-tight whitespace-nowrap">
              Online
            </span>
            <span class="logo-agency-text pt-0.5 leading-none">
              DIGITAL AGENCY
            </span>
          </div>
        </a>

        <!-- Center: Navigation Links -->
        <nav class="hidden lg:flex items-center justify-center gap-1 xl:gap-2 mx-auto">
          <a href="../index.html" class="nav-link-item">
            <i class="fa-solid fa-arrow-left text-slate-400"></i>
            <span>Back to Home</span>
          </a>
          <a href="../index.html#dev-services" class="nav-link-item">
            <i class="fa-solid fa-grid-2 text-blue-600"></i>
            <span>All Services</span>
          </a>
          <a href="../index.html#results" class="nav-link-item">
            <i class="fa-solid fa-trophy text-amber-500"></i>
            <span>Case Studies</span>
          </a>
          <a href="../index.html#about" class="nav-link-item">
            <i class="fa-solid fa-circle-info text-sky-600"></i>
            <span>About</span>
          </a>
          <a href="#pricing" class="nav-link-item">
            <i class="fa-solid fa-tags text-emerald-600"></i>
            <span>Pricing</span>
          </a>
          <a href="#faq" class="nav-link-item">
            <i class="fa-solid fa-circle-question text-violet-600"></i>
            <span>FAQs</span>
          </a>
          <a href="#contact" class="nav-link-item">
            <i class="fa-solid fa-phone text-blue-500"></i>
            <span>Contact</span>
          </a>
        </nav>

        <!-- Right Side: Currency, WhatsApp & Free Consultation -->
        <div class="hidden md:flex items-center gap-2 shrink-0 ml-auto pl-3 border-l border-slate-200">
          
          <!-- Currency Selector Dropdown -->
          <div class="relative group shrink-0">
            <button class="flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-slate-50 border border-slate-200 text-slate-700 text-xs font-bold hover:bg-slate-100 transition shadow-xs whitespace-nowrap">
              <i class="fa-solid fa-globe text-blue-600 text-xs"></i>
              <span id="active-currency-label">PKR</span>
              <i class="fa-solid fa-chevron-down text-[9px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute right-0 mt-1 w-44 bg-white border border-slate-200 rounded-xl shadow-xl py-1 hidden group-hover:block z-50">
              <div class="px-3 py-1.5 text-[10px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-100">
                Select Currency
              </div>
              <button onclick="changePageCurrency('PKR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 flex items-center justify-between transition">
                <span>🇵🇰 Pakistan (PKR)</span>
                <span class="font-bold text-slate-500">₨</span>
              </button>
              <button onclick="changePageCurrency('GBP')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 flex items-center justify-between transition">
                <span>🇬🇧 United Kingdom (GBP)</span>
                <span class="font-bold text-slate-500">£</span>
              </button>
              <button onclick="changePageCurrency('USD')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 flex items-center justify-between transition">
                <span>🇺🇸 United States (USD)</span>
                <span class="font-bold text-slate-500">$</span>
              </button>
              <button onclick="changePageCurrency('EUR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 flex items-center justify-between transition">
                <span>🇪🇺 Europe (EUR)</span>
                <span class="font-bold text-slate-500">€</span>
              </button>
            </div>
          </div>

          <!-- WhatsApp Button -->
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{name}." target="_blank" class="px-2.5 py-1.5 rounded-lg border border-emerald-500/40 bg-emerald-50 hover:bg-emerald-100 text-emerald-700 text-xs font-bold flex items-center gap-1.5 transition shrink-0 whitespace-nowrap">
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>WhatsApp</span>
          </a>

          <!-- Free Consultation CTA -->
          <button onclick="openModal()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white text-xs font-bold shadow-md shadow-blue-500/25 btn-shimmer transition shrink-0 whitespace-nowrap flex items-center gap-1">
            <span>Free Consultation</span>
            <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </button>
        </div>

        <!-- Mobile Toggle Button -->
        <div class="md:hidden flex items-center gap-2">
          <button onclick="openModal()" class="px-2.5 py-1.5 rounded-lg bg-blue-600 text-white text-xs font-bold">
            Consultation
          </button>
          <button id="mobile-toggle-btn" class="p-2 rounded-lg bg-slate-100 text-slate-800">
            <i class="fa-solid fa-bars text-lg"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- Mobile Drawer Menu -->
    <div id="mobile-drawer" class="hidden md:hidden bg-white border-b border-slate-200 px-6 py-4 shadow-xl">
      <div class="flex flex-col gap-3 text-sm font-bold text-slate-800">
        <a href="../index.html" class="py-2 border-b border-slate-100 flex items-center justify-between">
          <span>← Back to Home</span>
        </a>
        <a href="../index.html#dev-services" class="py-2 border-b border-slate-100 flex items-center justify-between">
          <span>All 24 Services</span>
        </a>
        <a href="#pricing" class="py-2 border-b border-slate-100 flex items-center justify-between">
          <span>Pricing Packages</span>
        </a>
        <a href="#faq" class="py-2 border-b border-slate-100 flex items-center justify-between">
          <span>Frequently Asked Questions</span>
        </a>
        <a href="#contact" class="py-2 flex items-center justify-between">
          <span>Contact Ranknix</span>
        </a>
        <div class="pt-2 border-t border-slate-100 grid grid-cols-2 gap-2 text-xs">
          <button onclick="changePageCurrency('PKR')" class="p-2 rounded-lg border border-slate-200 font-bold">🇵🇰 PKR (₨)</button>
          <button onclick="changePageCurrency('GBP')" class="p-2 rounded-lg border border-slate-200 font-bold">🇬🇧 GBP (£)</button>
          <button onclick="changePageCurrency('USD')" class="p-2 rounded-lg border border-slate-200 font-bold">🇺🇸 USD ($)</button>
          <button onclick="changePageCurrency('EUR')" class="p-2 rounded-lg border border-slate-200 font-bold">🇪🇺 EUR (€)</button>
        </div>
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{name}." target="_blank" class="w-full py-2.5 rounded-xl bg-emerald-600 text-white font-bold text-center mt-2 flex items-center justify-center gap-2">
          <i class="fa-brands fa-whatsapp text-lg"></i>
          <span>Chat on WhatsApp</span>
        </a>
      </div>
    </div>
  </header>

  <!-- 3. SERVICE HERO SECTION -->
  <section class="relative pt-10 pb-16 md:pt-16 md:pb-20 overflow-hidden bg-gradient-to-b from-blue-50/70 via-white to-white border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs font-semibold text-slate-500 mb-6">
        <a href="../index.html" class="hover:text-blue-600 transition">Home</a>
        <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
        <a href="../index.html#dev-services" class="hover:text-blue-600 transition">Services</a>
        <i class="fa-solid fa-chevron-right text-[10px] text-slate-400"></i>
        <span class="text-blue-600 font-bold">{name}</span>
      </nav>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Left: Hero Copy -->
        <div class="lg:col-span-7">
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-blue-100 text-blue-800 text-xs font-black tracking-wide uppercase mb-4">
            <i class="{cat_icon}"></i>
            <span>Division {num} • {category}</span>
          </div>

          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 font-heading tracking-tight leading-tight mb-5">
            {h1_prefix} <br class="hidden sm:inline">
            <span class="text-gradient-blue">{h1_gradient}</span>
          </h1>

          <p class="text-slate-600 text-base sm:text-lg leading-relaxed mb-8 max-w-2xl">
            {description}
          </p>

          <!-- CTAs -->
          <div class="flex flex-wrap items-center gap-3.5 mb-10">
            <button onclick="openModal()" class="px-6 sm:px-8 py-3.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm shadow-lg shadow-blue-500/25 btn-shimmer transition flex items-center gap-2">
              <span>Claim Free Consultation &rarr;</span>
            </button>
            <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'd%20like%20to%20inquire%20about%20{name}." target="_blank" class="px-6 py-3.5 rounded-xl border-2 border-emerald-500 bg-emerald-50 hover:bg-emerald-100 text-emerald-800 font-bold text-sm transition flex items-center gap-2">
              <i class="fa-brands fa-whatsapp text-emerald-600 text-lg"></i>
              <span>Direct WhatsApp Chat</span>
            </a>
          </div>

          <!-- Technologies Ticker/Pills -->
          <div>
            <span class="text-[11px] font-black uppercase tracking-wider text-slate-400 block mb-2.5">
              Tools & Platforms We Master for this Service:
            </span>
            <div class="flex flex-wrap gap-2">
              {platform_pills}
            </div>
          </div>
        </div>

        <!-- Right: 4 Stat Cards Grid -->
        <div class="lg:col-span-5">
          <div class="clean-card rounded-3xl p-6 sm:p-8 bg-gradient-to-br from-white via-slate-50 to-blue-50/40 border-2 border-slate-200">
            <div class="flex items-center gap-3 mb-6 pb-4 border-b border-slate-200">
              <div class="w-12 h-12 rounded-2xl {icon_bg} flex items-center justify-center text-xl shadow-xs">
                <i class="{icon}"></i>
              </div>
              <div>
                <h4 class="text-base font-black text-slate-900 font-heading leading-tight">{name} Track Record</h4>
                <p class="text-xs font-semibold text-slate-500">Verified institutional performance metrics</p>
              </div>
            </div>

            <!-- The 4 Stat Cards -->
            <div class="grid grid-cols-2 gap-4">
              {stats_html}
            </div>

            <div class="mt-6 pt-5 border-t border-slate-200/80 flex items-center justify-between text-xs font-bold text-slate-600">
              <span class="flex items-center gap-1.5">
                <i class="fa-solid fa-shield-halved text-emerald-600"></i>
                <span>Direct Founder Oversight</span>
              </span>
              <span class="text-blue-600 font-black">Muhammad Abdullah</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </section>

  <!-- 4. DELIVERABLES / WHAT WE BUILD -->
  <section class="py-20 bg-white relative z-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="section-badge {cat_badge_class} mb-3">
          <i class="{icon}"></i> Complete Deliverables
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-4">
          What Ranknix Online <span class="text-gradient-blue">Builds & Delivers</span>
        </h2>
        <p class="text-slate-600 text-base">
          Every project includes institutional-grade architecture, strict quality assurance, and zero shortcuts.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
        {deliverables_html}
      </div>

    </div>
  </section>

  <!-- 5. WHY RANKNIX BEATS OTHER AGENCIES -->
  <section class="py-20 bg-slate-50/60 relative z-10 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">The Ranknix Advantage</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-4">
          Why Brands Choose Us Over <span class="text-gradient-blue">Generic Agencies & Freelancers</span>
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        <!-- Freelancers -->
        <div class="clean-card rounded-2xl p-7 bg-white border border-slate-200">
          <div class="w-10 h-10 rounded-xl bg-red-100 text-red-600 flex items-center justify-center font-bold text-lg mb-4">
            <i class="fa-solid fa-xmark"></i>
          </div>
          <h4 class="text-lg font-black text-slate-900 mb-2">Cheap Freelancers</h4>
          <ul class="space-y-3 text-xs sm:text-sm text-slate-600">
            <li class="flex items-start gap-2"><i class="fa-solid fa-xmark text-red-500 mt-1 shrink-0"></i><span>Unreliable delivery and ghosting midway through projects.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-xmark text-red-500 mt-1 shrink-0"></i><span>No understanding of business conversion psychology.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-xmark text-red-500 mt-1 shrink-0"></i><span>Zero warranty or post-launch technical support.</span></li>
          </ul>
        </div>

        <!-- Traditional Agencies -->
        <div class="clean-card rounded-2xl p-7 bg-white border border-slate-200">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center font-bold text-lg mb-4">
            <i class="fa-solid fa-triangle-exclamation"></i>
          </div>
          <h4 class="text-lg font-black text-slate-900 mb-2">Traditional Agencies</h4>
          <ul class="space-y-3 text-xs sm:text-sm text-slate-600">
            <li class="flex items-start gap-2"><i class="fa-solid fa-minus text-amber-500 mt-1 shrink-0"></i><span>Bloated retainers and slow 6-week turnaround times.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-minus text-amber-500 mt-1 shrink-0"></i><span>Your project is handed off to junior interns.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-minus text-amber-500 mt-1 shrink-0"></i><span>Design teams that don't know performance marketing.</span></li>
          </ul>
        </div>

        <!-- Ranknix Online -->
        <div class="clean-card rounded-2xl p-7 bg-gradient-to-b from-blue-50/60 to-white border-2 border-blue-600 shadow-lg relative">
          <div class="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold text-lg mb-4 shadow-md shadow-blue-500/20">
            <i class="fa-solid fa-check"></i>
          </div>
          <h4 class="text-lg font-black text-slate-900 mb-2">Ranknix Online</h4>
          <ul class="space-y-3 text-xs sm:text-sm text-slate-700 font-semibold">
            <li class="flex items-start gap-2"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span>Code + Marketing unified under one high-performing team.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span>Strict milestone deadlines with transparent weekly progress.</span></li>
            <li class="flex items-start gap-2"><i class="fa-solid fa-check text-blue-600 mt-1 shrink-0"></i><span>Personal oversight by Muhammad Abdullah (5+ Years Experience).</span></li>
          </ul>
        </div>

      </div>

    </div>
  </section>

  <!-- 6. 4-STEP DELIVERY PROCESS -->
  <section class="py-20 bg-white relative z-10 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-16">
        <span class="section-badge {cat_badge_class} mb-3">
          <i class="fa-solid fa-arrow-progress"></i> Delivery Process
        </span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-4">
          How We Deliver <span class="text-gradient-blue">Excellence in 4 Steps</span>
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
        
        <div class="clean-card rounded-2xl p-6 text-center">
          <span class="w-12 h-12 rounded-2xl bg-blue-100 text-blue-700 font-black text-lg flex items-center justify-center mx-auto mb-4">01</span>
          <h4 class="font-black text-slate-900 text-base mb-2">Deep Discovery</h4>
          <p class="text-xs text-slate-600 leading-relaxed">We audit your current assets, target audience, and competitors to map out a clear technical scope.</p>
        </div>

        <div class="clean-card rounded-2xl p-6 text-center">
          <span class="w-12 h-12 rounded-2xl bg-blue-100 text-blue-700 font-black text-lg flex items-center justify-center mx-auto mb-4">02</span>
          <h4 class="font-black text-slate-900 text-base mb-2">Strategic Architecture</h4>
          <p class="text-xs text-slate-600 leading-relaxed">We wireframe user journeys, outline technical schemas, and agree on exact project deliverables.</p>
        </div>

        <div class="clean-card rounded-2xl p-6 text-center">
          <span class="w-12 h-12 rounded-2xl bg-blue-100 text-blue-700 font-black text-lg flex items-center justify-center mx-auto mb-4">03</span>
          <h4 class="font-black text-slate-900 text-base mb-2">Build & Rigorous QA</h4>
          <p class="text-xs text-slate-600 leading-relaxed">We write clean code, test across devices, optimize load speeds, and verify tracking accuracy.</p>
        </div>

        <div class="clean-card rounded-2xl p-6 text-center">
          <span class="w-12 h-12 rounded-2xl bg-blue-100 text-blue-700 font-black text-lg flex items-center justify-center mx-auto mb-4">04</span>
          <h4 class="font-black text-slate-900 text-base mb-2">Launch & Scaling</h4>
          <p class="text-xs text-slate-600 leading-relaxed">Full deployment with complete administrative handover, video tutorials, and dedicated warranty support.</p>
        </div>

      </div>

    </div>
  </section>

  <!-- 7. PRICING PACKAGES (DYNAMIC CURRENCY SUPPORT) -->
  <section id="pricing" class="py-20 bg-slate-50/60 relative z-10 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Transparent Investment</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Pricing Packages Tailored for <span class="text-gradient-blue">{name}</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base">
          Transparent rates with automatic currency conversion for clients in Pakistan, UK, USA, and Europe.
        </p>
      </div>

      {pricing_html}

    </div>
  </section>

  <!-- 8. FREQUENTLY ASKED QUESTIONS -->
  <section id="faq" class="py-20 bg-white relative z-10 border-t border-slate-200/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center mb-14">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Frequently Asked Questions</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Questions About <span class="text-gradient-blue">{name}?</span>
        </h2>
      </div>

      <div class="space-y-4">
        {faqs_html}
      </div>

    </div>
  </section>

  <!-- 9. FINAL HIGH-CONVERTING CTA BANNER -->
  <section id="contact" class="py-16 sm:py-20 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white relative overflow-hidden">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      
      <span class="inline-block px-3.5 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-black tracking-wide uppercase mb-4 border border-blue-400/30">
        Ready to Scale?
      </span>
      
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-black font-heading tracking-tight mb-6">
        Let's Build & Scale Your <span class="text-blue-400">{name}</span> Together
      </h2>
      
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto mb-10 leading-relaxed">
        Speak directly with Founder Muhammad Abdullah or our senior specialists. We'll analyze your requirements and deliver a detailed action plan within 24 hours.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-4">
        <button onclick="openModal()" class="px-8 py-4 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-black text-sm shadow-xl shadow-blue-500/30 btn-shimmer transition">
          Claim Free Consultation &rarr;
        </button>
        <a href="https://wa.me/923088163940?text=Hi%20Muhammad%20Abdullah!%20I'm%20ready%20to%20discuss%20{name}%20for%20my%20business." target="_blank" class="px-7 py-4 rounded-xl border-2 border-emerald-400 bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 font-black text-sm transition flex items-center gap-2">
          <i class="fa-brands fa-whatsapp text-emerald-400 text-xl"></i>
          <span>Direct WhatsApp (+92 308 8163940)</span>
        </a>
      </div>

    </div>
  </section>

  <!-- 10. AGENCY FOOTER -->
  <footer class="border-t border-slate-200 bg-slate-900 pt-16 pb-12 text-slate-400 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 mb-12">
        
        <!-- Brand Col -->
        <div class="lg:col-span-2">
          <a href="../index.html" class="flex items-center gap-3 mb-4">
            <img src="../assets/images/logo.png" alt="Ranknix Online" class="h-11 w-auto">
            <div class="flex flex-col justify-center -space-y-1">
              <span class="text-xl font-black text-white font-heading">Ranknix</span>
              <span class="text-xl font-black text-blue-500 font-heading">Online</span>
              <span class="logo-agency-text pt-0.5 leading-none">DIGITAL AGENCY</span>
            </div>
          </a>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed max-w-sm mb-6">
            Ranknix Online is a premier worldwide digital agency uniting cutting-edge engineering with high-ROAS performance marketing.
          </p>
          <p class="text-xs text-slate-500">
            Founder & CEO: <strong>Muhammad Abdullah</strong> (5+ Years Experience)
          </p>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Web & App Dev</h4>
          <ul class="space-y-2.5 text-xs text-slate-400">
            <li><a href="web-development.html" class="hover:text-white transition">Web Development</a></li>
            <li><a href="app-development.html" class="hover:text-white transition">App Development</a></li>
            <li><a href="ui-ux-design.html" class="hover:text-white transition">UI/UX Design</a></li>
            <li><a href="e-commerce-solutions.html" class="hover:text-white transition">E-Commerce Solutions</a></li>
            <li><a href="landing-page-design.html" class="hover:text-white transition">Landing Page Design</a></li>
          </ul>
        </div>

        <!-- Marketing Links -->
        <div>
          <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Marketing & Ads</h4>
          <ul class="space-y-2.5 text-xs text-slate-400">
            <li><a href="digital-marketing.html" class="hover:text-white transition">Digital Marketing</a></li>
            <li><a href="meta-ads.html" class="hover:text-white transition">Meta (FB & IG) Ads</a></li>
            <li><a href="google-ads-bing-ads.html" class="hover:text-white transition">Google & Bing Ads</a></li>
            <li><a href="seo-services.html" class="hover:text-white transition">SEO Services</a></li>
            <li><a href="web-analytics.html" class="hover:text-white transition">Web Analytics & CAPI</a></li>
          </ul>
        </div>

        <!-- Contact Col -->
        <div>
          <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-4">Direct Contact</h4>
          <ul class="space-y-2.5 text-xs text-slate-400">
            <li class="text-white font-bold">Muhammad Abdullah (CEO)</li>
            <li>WhatsApp: +92 308 8163940</li>
            <li>Email: contact@ranknix.online</li>
            <li class="pt-2">
              <a href="https://wa.me/923088163940" target="_blank" class="text-emerald-400 font-bold hover:underline flex items-center gap-1.5">
                <i class="fa-brands fa-whatsapp"></i> Chat on WhatsApp
              </a>
            </li>
          </ul>
        </div>

      </div>

      <div class="pt-8 border-t border-slate-800 text-center text-xs text-slate-500">
        &copy; 2026 Ranknix Online. All rights reserved. Built with performance & conversion first.
      </div>

    </div>
  </footer>

  <!-- AUDIT & STRATEGY MODAL -->
  <div id="service-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 relative shadow-2xl border border-slate-200">
      <button onclick="closeModal()" class="absolute top-5 right-5 text-slate-400 hover:text-slate-700 text-lg">
        <i class="fa-solid fa-xmark"></i>
      </button>

      <div class="mb-6">
        <span class="inline-block px-3 py-1 rounded-full bg-blue-100 text-blue-800 text-xs font-black uppercase mb-2">Free Consultation</span>
        <h3 class="text-2xl font-black text-slate-900 font-heading">Discuss Your {name} Project</h3>
        <p class="text-slate-600 text-xs sm:text-sm mt-1">Fill out the brief form below and our team will get back to you within 24 hours.</p>
      </div>

      <form onsubmit="handleFormSubmit(event)" class="space-y-4">
        <input type="hidden" id="service-name" value="{name}">
        <div>
          <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Your Full Name</label>
          <input type="text" id="lead-name" required placeholder="e.g. Ali Ahmed / John Smith" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-blue-600 focus:outline-none text-sm">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 uppercase mb-1">WhatsApp or Phone Number</label>
          <input type="text" id="lead-phone" required placeholder="e.g. +92 300 1234567" class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-blue-600 focus:outline-none text-sm">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 uppercase mb-1">Business Website or Goals</label>
          <textarea id="lead-notes" rows="3" placeholder="Briefly describe what you want to achieve..." class="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-blue-600 focus:outline-none text-sm"></textarea>
        </div>
        <button type="submit" class="w-full py-3.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm shadow-md transition">
          Send Strategy Request &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- EMBEDDED JAVASCRIPT FOR CURRENCY & INTERACTION -->
  <script>
    // 1. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-toggle-btn');
    const mobileDrawer = document.getElementById('mobile-drawer');
    if (mobileBtn && mobileDrawer) {{
      mobileBtn.addEventListener('click', () => {{
        mobileDrawer.classList.toggle('hidden');
      }});
    }}

    // 2. FAQ Accordion
    document.querySelectorAll('.faq-trigger').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const parent = btn.parentElement;
        const content = parent.querySelector('.faq-content');
        const icon = btn.querySelector('.faq-icon');
        const isHidden = content.classList.contains('hidden');

        // close other items
        document.querySelectorAll('.faq-content').forEach(c => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach(i => i.classList.remove('rotate-180'));

        if (isHidden) {{
          content.classList.remove('hidden');
          if (icon) icon.classList.add('rotate-180');
        }}
      }});
    }});

    // 3. Dynamic Currency Selector
    function changePageCurrency(curr) {{
      localStorage.setItem('ranknix_currency', curr);
      const label = document.getElementById('active-currency-label');
      if (label) label.textContent = curr;

      document.querySelectorAll('.dynamic-price').forEach(el => {{
        const price = el.getAttribute('data-' + curr.toLowerCase());
        if (price) el.textContent = price;
      }});
    }}

    // Load saved or auto currency
    document.addEventListener('DOMContentLoaded', () => {{
      const saved = localStorage.getItem('ranknix_currency') || 'PKR';
      changePageCurrency(saved);
    }});

    // 4. Modal Handlers
    function openModal() {{
      const m = document.getElementById('service-modal');
      if (m) m.classList.remove('hidden');
    }}
    function closeModal() {{
      const m = document.getElementById('service-modal');
      if (m) m.classList.add('hidden');
    }}

    // 5. Lead Form Submission via WhatsApp
    function handleFormSubmit(e) {{
      e.preventDefault();
      const sName = document.getElementById('service-name').value;
      const lName = document.getElementById('lead-name').value;
      const lPhone = document.getElementById('lead-phone').value;
      const lNotes = document.getElementById('lead-notes').value;

      const text = encodeURIComponent("Hi Ranknix Online! 🚀\\n\\n*New Project Inquiry:* " + sName + "\\n*Name:* " + lName + "\\n*Phone:* " + lPhone + "\\n*Details:* " + lNotes);
      window.open("https://wa.me/923088163940?text=" + text, '_blank');
      closeModal();
    }}
  </script>

</body>
</html>
"""
    return html

# Generate all 24 files
count = 0
for s in ALL_SERVICES:
    slug = s["slug"]
    file_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
    html_content = generate_service_html(s)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    count += 1
    print(f"[{count:02d}/24] Created: {slug}.html ({len(html_content)} bytes)")

print(f"\nSUCCESS! All {count} service pages created in {OUTPUT_DIR}")
