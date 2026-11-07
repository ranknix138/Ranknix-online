import json, os, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

from build_pricing_track import render_pricing_track_section

OUTPUT_PATH = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\pricing.html"

def generate_pricing_page_html():
    pricing_track_sec = render_pricing_track_section()

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pricing Plans &amp; Packages | Ranknix Online - Worldwide Digital Agency</title>
  <meta name="description" content="Explore transparent, fixed-rate packages across all 24 digital services by Ranknix Online. Web & App Development, Performance Marketing, and CRM Automation. Dynamic multi-currency pricing in PKR, GBP, USD, and EUR.">
  <link rel="icon" type="image/png" href="assets/images/logo.png">

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
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body class="bg-white text-slate-800 antialiased font-sans selection:bg-blue-600 selection:text-white">

  <!-- TOP ANNOUNCEMENT BAR -->
  <div class="bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 text-white text-[11px] sm:text-xs py-2 px-4 border-b border-blue-900/40">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-black bg-blue-500/20 text-blue-300 border border-blue-400/30">
          Ranknix Official Rates
        </span>
        <span class="hidden sm:inline text-slate-300">
          Transparent multi-currency pricing overseen by Founder Muhammad Abdullah
        </span>
      </div>
      <div class="flex items-center gap-4 text-slate-300 ml-auto">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20your%20pricing%20packages." target="_blank" class="hover:text-emerald-400 transition flex items-center gap-1.5">
          <i class="fa-brands fa-whatsapp text-emerald-400"></i>
          <span>+92 308 8163940</span>
        </a>
        <span class="text-slate-600 hidden md:inline">|</span>
        <a href="mailto:contact@ranknix.online" class="hover:text-blue-400 transition hidden md:flex items-center gap-1.5">
          <i class="fa-solid fa-envelope text-blue-400"></i>
          <span>contact@ranknix.online</span>
        </a>
      </div>
    </div>
  </div>

  <!-- NAVIGATION BAR -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 transition shadow-2xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16 sm:h-[68px]">

        <!-- Left: Brand Logo Lockup -->
        <a href="index.html" class="flex items-center gap-2.5 sm:gap-3 group shrink-0">
          <img src="assets/images/logo.png" alt="Ranknix Online Logo" class="h-10 sm:h-11 w-auto object-contain">
          <div class="flex flex-col justify-center -space-y-1">
            <span class="text-lg sm:text-[21px] font-black tracking-tight text-slate-900 font-heading">
              Ranknix
            </span>
            <span class="text-lg sm:text-[21px] font-black tracking-tight text-blue-600 font-heading">
              Online
            </span>
            <span class="logo-agency-text pt-0.5 leading-none">
              DIGITAL AGENCY
            </span>
          </div>
        </a>

        <!-- Center: Navigation Links with Dropdowns -->
        <nav class="hidden lg:flex items-center justify-center gap-1 xl:gap-2 mx-auto min-w-0">
          <a href="index.html" class="nav-link-item">
            <i class="fa-solid fa-house text-slate-400"></i>
            <span>Home</span>
          </a>

          <!-- Development Dropdown -->
          <div class="relative group">
            <button class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-code text-blue-600"></i>
              <span>Development</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>Web &amp; App Dev (01–08)</span>
                <span class="text-blue-600">8 Services</span>
              </div>
              <a href="services/web-development.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-code text-blue-600 w-4"></i> Web Development
              </a>
              <a href="services/app-development.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-mobile-screen-button text-blue-600 w-4"></i> App Development
              </a>
              <a href="services/ui-ux-design.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-pen-nib text-blue-600 w-4"></i> UI/UX Design
              </a>
              <a href="services/graphic-design.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-palette text-blue-600 w-4"></i> Graphic Design
              </a>
              <a href="services/e-commerce-solutions.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-bag-shopping text-blue-600 w-4"></i> E-Commerce Solutions
              </a>
              <a href="services/video-editing.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-video text-blue-600 w-4"></i> Video Editing
              </a>
              <a href="services/content-writing.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-feather text-blue-600 w-4"></i> Content Writing
              </a>
              <a href="services/landing-page-design.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-rocket text-blue-600 w-4"></i> Landing Page Design
              </a>
            </div>
          </div>

          <!-- Marketing Dropdown -->
          <div class="relative group">
            <button class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-chart-line text-indigo-600"></i>
              <span>Marketing</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>Marketing &amp; Growth (09–16)</span>
                <span class="text-indigo-600">8 Services</span>
              </div>
              <a href="services/digital-marketing.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-chart-line text-indigo-600 w-4"></i> Digital Marketing
              </a>
              <a href="services/seo-services.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-magnifying-glass-chart text-indigo-600 w-4"></i> SEO Services
              </a>
              <a href="services/google-ads-bing-ads.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-brands fa-google text-indigo-600 w-4"></i> Google &amp; Bing Ads
              </a>
              <a href="services/meta-ads.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-brands fa-meta text-indigo-600 w-4"></i> Meta Ads (FB &amp; IG)
              </a>
              <a href="services/social-media-management.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-share-nodes text-indigo-600 w-4"></i> Social Media Management
              </a>
              <a href="services/web-analytics.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-chart-pie text-indigo-600 w-4"></i> Web Analytics (GA4)
              </a>
              <a href="services/cro-conversion-optimization.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-arrow-trend-up text-indigo-600 w-4"></i> CRO Optimization
              </a>
              <a href="services/email-marketing.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-envelope-open-text text-indigo-600 w-4"></i> Email Marketing
              </a>
            </div>
          </div>

          <!-- Automation Dropdown -->
          <div class="relative group">
            <button class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-gears text-amber-600"></i>
              <span>Automation</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>CRM &amp; Automation (17–24)</span>
                <span class="text-amber-600">8 Services</span>
              </div>
              <a href="services/legal-data-entry-data-analysis.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-scale-balanced text-amber-600 w-4"></i> Legal Data Entry
              </a>
              <a href="services/gohighlevel-migration-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-bolt text-amber-600 w-4"></i> GoHighLevel Automation
              </a>
              <a href="services/zoho-setup-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-cubes text-amber-600 w-4"></i> Zoho Setup &amp; Sync
              </a>
              <a href="services/crm-data-management-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-database text-amber-600 w-4"></i> CRM Data Management
              </a>
              <a href="services/lead-generation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-bullseye text-amber-600 w-4"></i> Lead Generation
              </a>
              <a href="services/web-research.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-magnifying-glass text-amber-600 w-4"></i> Web Research
              </a>
              <a href="services/excel-cleaning-formatting.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-file-excel text-amber-600 w-4"></i> Excel Cleanup
              </a>
              <a href="services/social-media-data-collection.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-network-wired text-amber-600 w-4"></i> Social Data Collection
              </a>
            </div>
          </div>

          <a href="index.html#results" class="nav-link-item">
            <i class="fa-solid fa-trophy text-amber-500"></i>
            <span>Case Studies</span>
          </a>
          <a href="pricing.html" class="nav-link-item active bg-blue-50 text-blue-700 font-bold">
            <i class="fa-solid fa-tags text-blue-600"></i>
            <span>Pricing Plans</span>
          </a>
          <a href="index.html#testimonials" class="nav-link-item">
            <i class="fa-solid fa-star text-amber-400"></i>
            <span>Reviews</span>
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
            <button class="flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-slate-50 border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-100 transition shadow-2xs">
              <i class="fa-solid fa-globe text-blue-600 text-xs"></i>
              <span id="active-currency-label">PKR</span>
              <i class="fa-solid fa-chevron-down text-[9px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </button>
            <div class="absolute right-0 mt-1 w-44 bg-white border border-slate-200 rounded-xl shadow-xl py-1.5 hidden group-hover:block z-50">
              <div class="px-3 py-1.5 text-[10px] font-bold uppercase tracking-wider text-slate-400 border-b border-slate-100">
                Select Currency
              </div>
              <button onclick="changeGlobalCurrency('PKR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇵🇰 Pakistan (PKR)</span>
                <span class="font-bold text-slate-500">₨</span>
              </button>
              <button onclick="changeGlobalCurrency('GBP')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇬🇧 United Kingdom (GBP)</span>
                <span class="font-bold text-slate-500">£</span>
              </button>
              <button onclick="changeGlobalCurrency('USD')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇺🇸 United States (USD)</span>
                <span class="font-bold text-slate-500">$</span>
              </button>
              <button onclick="changeGlobalCurrency('EUR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇪🇺 Europe (EUR)</span>
                <span class="font-bold text-slate-500">€</span>
              </button>
            </div>
          </div>

          <!-- WhatsApp Button -->
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20your%20pricing%20packages." target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 text-xs font-bold transition flex items-center gap-1.5">
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>WhatsApp</span>
          </a>

          <!-- Free Consultation CTA -->
          <button onclick="openModal()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white text-xs font-bold transition shadow-xs flex items-center gap-1.5">
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
  </header>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-drawer" class="hidden md:hidden bg-white border-b border-slate-200 px-6 py-4 shadow-lg space-y-3 text-sm font-semibold">
    <a href="index.html" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-house mr-2"></i> Home</a>
    <a href="pricing.html" class="block py-2 text-blue-600 font-bold"><i class="fa-solid fa-tags mr-2"></i> All Pricing Packages</a>
    <a href="index.html#results" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-trophy mr-2"></i> Case Studies</a>
    <a href="index.html#about" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-circle-info mr-2"></i> About</a>
    <a href="index.html#testimonials" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-star mr-2"></i> Client Reviews</a>
    <a href="#contact" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-phone mr-2"></i> Contact</a>
  </div>

  <!-- BREADCRUMB & PAGE HEADER -->
  <div class="bg-gradient-to-b from-blue-50/50 to-white pt-8 pb-6 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <nav class="flex items-center gap-2 text-xs text-slate-500 font-medium mb-3">
        <a href="index.html" class="hover:text-blue-600 transition flex items-center gap-1">
          <i class="fa-solid fa-house text-[10px]"></i>
          <span>Home</span>
        </a>
        <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
        <span class="text-blue-600 font-bold">Pricing Plans &amp; Packages</span>
      </nav>
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <span class="inline-block px-3 py-0.5 rounded-full bg-blue-100 text-blue-800 text-[10px] font-black uppercase tracking-wider mb-2">Official Agency Rates</span>
          <h1 class="text-2xl sm:text-3xl md:text-4xl font-black text-slate-900 font-heading tracking-tight">
            24 Services &bull; <span class="text-gradient-blue">Transparent Fixed Packages</span>
          </h1>
          <p class="text-xs sm:text-sm text-slate-600 max-w-2xl mt-1">
            Pick any service in the moving track to view Starter, Growth, and Enterprise tiers with guaranteed turnaround times.
          </p>
        </div>
        <div class="shrink-0 flex items-center gap-2">
          <a href="https://wa.me/923088163940?text=Hi%20Muhammad%20Abdullah!%20I'd%20like%20to%20discuss%20a%20custom%20agency%20package." target="_blank" class="px-4 py-2.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-700 font-bold text-xs transition flex items-center gap-1.5 shadow-2xs">
            <i class="fa-brands fa-whatsapp text-emerald-600 text-base"></i>
            <span>Direct Founder WhatsApp</span>
          </a>
        </div>
      </div>
    </div>
  </div>

  <!-- THE 24-SERVICE AUTO-SCROLLING MARQUEE TRACK + 3-TIER PACKAGES SECTION -->
  {pricing_track_sec}

  <!-- PRICING FAQS SECTION -->
  <section class="py-20 bg-white relative z-10 border-t border-slate-200/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-10">
        <span class="text-xs font-black uppercase text-blue-600 tracking-wider">Payment &amp; Terms</span>
        <h2 class="text-2xl sm:text-3xl font-black text-slate-900 font-heading tracking-tight mt-1">
          Frequently Asked Questions About Our Packages
        </h2>
      </div>

      <div class="space-y-3">
        <div class="clean-card rounded-2xl p-5 border border-slate-200/90 shadow-2xs">
          <h4 class="text-sm font-bold text-slate-900 mb-1.5 flex items-center gap-2">
            <i class="fa-solid fa-circle-question text-blue-600"></i> What payment methods do you accept?
          </h4>
          <p class="text-xs text-slate-600 leading-relaxed">
            We accept Stripe (Credit/Debit Card worldwide), Direct Bank Transfer (UK Faster Payments, US ACH / Wire, EU SEPA, UAE IBAN), Payoneer, Wise, and local bank transfer / Raast in Pakistan.
          </p>
        </div>
        <div class="clean-card rounded-2xl p-5 border border-slate-200/90 shadow-2xs">
          <h4 class="text-sm font-bold text-slate-900 mb-1.5 flex items-center gap-2">
            <i class="fa-solid fa-circle-question text-blue-600"></i> Are there any hidden fees or recurring subscriptions?
          </h4>
          <p class="text-xs text-slate-600 leading-relaxed">
            No. Every fixed package is clearly billed as one-time or monthly with zero surprise invoices. Ad spend is paid directly to Google or Meta with zero markup.
          </p>
        </div>
        <div class="clean-card rounded-2xl p-5 border border-slate-200/90 shadow-2xs">
          <h4 class="text-sm font-bold text-slate-900 mb-1.5 flex items-center gap-2">
            <i class="fa-solid fa-circle-question text-blue-600"></i> Can you build a customized multi-service package?
          </h4>
          <p class="text-xs text-slate-600 leading-relaxed">
            Yes, absolutely! If you need both Web Development and Meta/Google Ads scaling, we build a bundled growth proposal with direct founder discounts.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- FINAL CTA BANNER -->
  <section id="contact" class="py-16 sm:py-20 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white relative z-10 overflow-hidden">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <span class="inline-block px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-4 border border-blue-400/30">
        Ready To Scale Your Brand?
      </span>
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-black font-heading tracking-tight mb-4 leading-tight">
        Speak Directly With Founder <br><span class="text-blue-400">Muhammad Abdullah</span>
      </h2>
      <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto mb-8 leading-relaxed">
        We’ll review your business goals, recommend the exact growth package, and provide a comprehensive proposal within 24 hours.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-4">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20ready%20to%20get%20started." target="_blank" class="px-7 py-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-black text-sm shadow-lg shadow-emerald-500/25 transition flex items-center gap-2.5">
          <i class="fa-brands fa-whatsapp text-xl"></i>
          <span>Chat on WhatsApp (+92 308 8163940)</span>
        </a>
        <button onclick="openModal()" class="px-7 py-4 rounded-xl bg-white hover:bg-slate-100 text-slate-900 font-black text-sm shadow-lg transition flex items-center gap-2">
          <i class="fa-solid fa-calendar-check text-blue-600"></i>
          <span>Schedule Strategy Audit</span>
        </button>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-slate-950 text-slate-400 text-xs py-12 border-t border-slate-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-900">
        <div class="flex items-center gap-3">
          <img src="assets/images/logo.png" alt="Ranknix Online Logo" class="h-10 w-auto">
          <div>
            <span class="text-base font-black text-white font-heading">Ranknix Online</span>
            <span class="block text-[11px] text-slate-500">Founder &amp; CEO: Muhammad Abdullah</span>
          </div>
        </div>
        <div class="flex flex-wrap items-center justify-center gap-6 text-xs">
          <a href="index.html" class="hover:text-blue-400 transition">Home</a>
          <a href="pricing.html" class="text-blue-400 font-bold">Pricing Plans</a>
          <a href="index.html#about" class="hover:text-blue-400 transition">About</a>
          <a href="https://wa.me/923088163940" class="hover:text-emerald-400 transition"><i class="fa-brands fa-whatsapp mr-1"></i> WhatsApp</a>
        </div>
      </div>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-600">
        <p>&copy; 2026 Ranknix Online. All rights reserved. Worldwide Digital Agency.</p>
        <p>Operating across Pakistan, UK, USA, UAE, Canada &amp; Europe.</p>
      </div>
    </div>
  </footer>

  <!-- STRATEGY CONSULTATION MODAL -->
  <div id="service-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative border border-slate-200">
      <button onclick="closeModal()" class="absolute top-5 right-5 text-slate-400 hover:text-slate-700 text-lg">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <div class="mb-5">
        <span class="text-xs font-black uppercase text-blue-600 tracking-wider">Free Consultation</span>
        <h3 class="text-2xl font-black text-slate-900 font-heading mt-1">Book Your Growth Audit</h3>
        <p class="text-xs text-slate-500 mt-1">Direct review by Muhammad Abdullah. Response in &lt; 24h.</p>
      </div>
      <form id="service-form" onsubmit="handleModalSubmit(event)" class="space-y-3.5">
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name</label>
          <input type="text" id="lead-name" required placeholder="e.g. James Whitfield / Ali Ahmed" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp / Phone Number</label>
          <input type="text" id="lead-phone" required placeholder="e.g. +44 7911 123456 / +92 300 1234567" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Desired Service / Budget</label>
          <textarea id="lead-notes" rows="3" placeholder="Tell us about your brand, package interest, and target timeline..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none"></textarea>
        </div>
        <button type="submit" class="w-full py-3.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-black text-xs transition shadow-md shadow-blue-500/20">
          Submit Inbound Request via WhatsApp &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- JAVASCRIPT CONTROLLERS -->
  <script>
    function selectTrackService(slug) {{
      document.querySelectorAll('.track-pill').forEach(btn => {{
        btn.classList.remove('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
        btn.classList.add('border-slate-200/90', 'bg-white', 'text-slate-700');
      }});

      const matchingPills = document.querySelectorAll('#track-pill-' + slug);
      matchingPills.forEach(p => {{
        p.classList.add('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
        p.classList.remove('border-slate-200/90', 'bg-white', 'text-slate-700');
      }});

      document.querySelectorAll('.track-pricing-panel').forEach(p => p.classList.add('hidden'));
      const target = document.getElementById('track-panel-' + slug);
      if (target) {{
        target.classList.remove('hidden');
      }}
    }}

    function scrollTrackPrev() {{
      const container = document.getElementById('pricing-marquee-container');
      if (container) container.scrollBy({{ left: -280, behavior: 'smooth' }});
    }}

    function scrollTrackNext() {{
      const container = document.getElementById('pricing-marquee-container');
      if (container) container.scrollBy({{ left: 280, behavior: 'smooth' }});
    }}

    function changeGlobalCurrency(curr) {{
      try {{
        localStorage.setItem('ranknix_currency', curr);
      }} catch (e) {{}}

      document.querySelectorAll('[data-curr-pill]').forEach(pill => {{
        if (pill.getAttribute('data-curr-pill') === curr) {{
          pill.classList.add('bg-blue-600', 'text-white');
          pill.classList.remove('text-slate-700');
        }} else {{
          pill.classList.remove('bg-blue-600', 'text-white');
          pill.classList.add('text-slate-700');
        }}
      }});

      const activeLabel = document.getElementById('active-currency-label');
      if (activeLabel) {{
        const icons = {{ PKR: '🇵🇰 PKR', GBP: '🇬🇧 GBP', USD: '🇺🇸 USD', EUR: '🇪🇺 EUR' }};
        activeLabel.textContent = icons[curr] || curr;
      }}

      document.querySelectorAll('.dynamic-price').forEach(el => {{
        const val = el.getAttribute('data-' + curr.toLowerCase());
        if (val) el.textContent = val;
      }});
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      const saved = localStorage.getItem('ranknix_currency') || 'PKR';
      changeGlobalCurrency(saved);

      // Check URL parameters for selected service e.g. ?service=google-ads
      const params = new URLSearchParams(window.location.search);
      const svcParam = params.get('service') || window.location.hash.replace('#', '');
      if (svcParam) {{
        selectTrackService(svcParam);
      }}

      const toggleBtn = document.getElementById('mobile-toggle-btn');
      const drawer = document.getElementById('mobile-drawer');
      if (toggleBtn && drawer) {{
        toggleBtn.addEventListener('click', () => {{
          drawer.classList.toggle('hidden');
        }});
      }}
    }});

    function openModal() {{
      const m = document.getElementById('service-modal');
      if (m) m.classList.remove('hidden');
    }}
    function closeModal() {{
      const m = document.getElementById('service-modal');
      if (m) m.classList.add('hidden');
    }}
    function handleModalSubmit(e) {{
      e.preventDefault();
      const lName = document.getElementById('lead-name').value;
      const lPhone = document.getElementById('lead-phone').value;
      const lNotes = document.getElementById('lead-notes').value;
      const msg = "Hi Ranknix Online! I'm submitting a pricing inquiry.\\n\\nName: " + lName + "\\nPhone: " + lPhone + "\\nRequirement: " + lNotes;
      window.open("https://wa.me/923088163940?text=" + encodeURIComponent(msg), '_blank');
      closeModal();
    }}
  </script>
</body>
</html>
"""
    return html

content = generate_pricing_page_html()
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated pricing.html successfully ({len(content)} bytes)!")
