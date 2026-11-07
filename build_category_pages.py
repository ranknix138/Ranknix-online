import os, json, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

from services_config import SERVICES_INFO, format_currency
from services_data_part1 import SERVICES_DATA as p1
from services_data_part2 import SERVICES_DATA_PART2 as p2
from services_data_part3 import SERVICES_DATA_PART3 as p3
from reviews_data import TESTIMONIALS_DATA

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "r", encoding="utf-8") as f:
    packages_data = json.load(f)

BASE_DIR = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website"

CATEGORY_CONFIGS = [
    {
        "id": "development",
        "file": "development.html",
        "title": "Web & App Development Services | Ranknix Online",
        "division_badge": "Division 01: Engineering & Design",
        "h1_prefix": "Custom Web & Mobile App",
        "h1_gradient": "Engineering &amp; Design",
        "subtitle": "High-converting Shopify & WordPress platforms, custom React/Next.js web applications, and production-ready iOS & Android apps built for extreme speed, conversion optimization, and enterprise scalability.",
        "services": p1,
        "num_start": 1,
        "stats": [
            ("100+", "Websites & Apps Delivered", "Custom code & theme builds"),
            ("99", "Google PageSpeed Score", "Mobile Core Web Vitals"),
            ("7 Days", "Avg. Turnaround Time", "Strict milestone delivery"),
            ("4.9★", "Verified Client Rating", "50+ 5-star reviews")
        ],
        "tech_ticker": ["WordPress", "Shopify Plus", "React", "Next.js", "React Native", "Flutter", "Figma", "Tailwind CSS", "WooCommerce", "Node.js"],
        "keys": ["web-dev", "app-dev", "ui-ux", "graphic", "ecommerce", "video", "content", "landing"],
        "sim_type": "web_dev"
    },
    {
        "id": "marketing",
        "file": "marketing.html",
        "title": "Performance Marketing & Paid Ads | Ranknix Online",
        "division_badge": "Division 02: Performance Marketing & Growth",
        "h1_prefix": "Precision Performance Marketing",
        "h1_gradient": "&amp; Paid Traffic That Converts",
        "subtitle": "Data-backed Meta Ads, Google Ads & Bing Ads, technical SEO, and conversion rate optimization designed to acquire high-intent customers at the lowest possible CPA across every global market.",
        "services": p2,
        "num_start": 9,
        "stats": [
            ("150+", "Campaigns Scaled", "Worldwide ad management"),
            ("4.6x", "Avg. Blended ROAS", "Direct response scaling"),
            ("-42%", "Lower CPA Achieved", "Negative KW & CAPI tracking"),
            ("100%", "CAPI Signal Recovery", "Bypasses iOS tracking loss")
        ],
        "tech_ticker": ["Google Ads", "Meta Ads", "TikTok Ads", "Bing Ads", "Google Analytics 4", "Google Tag Manager", "Klaviyo", "Shopify CAPI", "Hotjar", "SEMrush"],
        "keys": ["digital-mkt", "seo", "google-ads", "meta-ads", "social", "analytics", "cro", "email"],
        "sim_type": "google_ads"
    },
    {
        "id": "automation",
        "file": "automation.html",
        "title": "Data, CRM & Workflow Automation | Ranknix Online",
        "division_badge": "Division 03: Data & Back-Office Automation",
        "h1_prefix": "Data, CRM &amp; Workflow",
        "h1_gradient": "Automation Solutions",
        "subtitle": "Streamline your operational pipeline with Zoho CRM setup, GoHighLevel migration, automated lead distribution, verified B2B prospect lists, and clean Excel analytics. Zero manual bottlenecks.",
        "services": p3,
        "num_start": 17,
        "stats": [
            ("200+", "Workflows Automated", "Custom webhook pipelines"),
            ("25+ Hrs", "Saved Weekly per Rep", "Automated CRM follow-ups"),
            ("0%", "Data Bounce Rate", "SMTP verified B2B leads"),
            ("100%", "API & Webhook SLA", "Zero lead leakage")
        ],
        "tech_ticker": ["Zoho CRM", "GoHighLevel", "HubSpot", "Salesforce", "Zapier", "Make.com", "Microsoft Excel", "Google Sheets", "Stripe API", "WhatsApp Business API"],
        "keys": ["legal", "ghl", "zoho", "crm", "leadgen", "research", "excel", "socialdata"],
        "sim_type": "crm_auto"
    }
]

def render_category_page(cfg):
    cat_id = cfg["id"]
    active_nav = {
        "dev": "bg-blue-50 text-blue-700 font-bold border-blue-200" if cat_id == "development" else "text-slate-700 hover:text-slate-900",
        "mkt": "bg-blue-50 text-blue-700 font-bold border-blue-200" if cat_id == "marketing" else "text-slate-700 hover:text-slate-900",
        "auto": "bg-blue-50 text-blue-700 font-bold border-blue-200" if cat_id == "automation" else "text-slate-700 hover:text-slate-900",
    }

    # Stat Cards
    stat_cards_html = ""
    for val, label, sub in cfg["stats"]:
        stat_cards_html += f"""
        <div class="clean-card rounded-2xl p-5 border border-slate-200/90 shadow-2xs hover:border-blue-300 transition">
          <div class="text-3xl font-black text-slate-900 font-heading mb-1 text-gradient-blue">{val}</div>
          <div class="text-xs font-black text-slate-800 uppercase tracking-wider mb-1">{label}</div>
          <div class="text-[11px] text-slate-500 leading-snug">{sub}</div>
        </div>"""

    # 8 Services Cards Grid
    cards_html = ""
    for idx, s in enumerate(cfg["services"], cfg["num_start"]):
        slug = s['slug'] if s['slug'].endswith('.html') else s['slug'] + '.html'
        # Package key
        from build_all_service_pages import SLUG_TO_PKG_KEY
        pkg_key = SLUG_TO_PKG_KEY.get(slug, 'web-dev')

        name = s['name']
        icon = s['icon']
        desc = s['description'][:140] + "..." if len(s['description']) > 140 else s['description']
        desc = desc.replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")

        tags_html = ""
        if 'platforms' in s:
            tags_html = "".join([f'<span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-600 text-[10px] font-bold">{p}</span>' for p in s['platforms'][:3]])

        wa_url = f"https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{urllib.parse.quote(name)}"

        cards_html += f"""
        <div class="clean-card rounded-3xl p-6 sm:p-7 flex flex-col justify-between border border-slate-200/90 shadow-2xs hover:shadow-xl hover:border-blue-400 transition-all duration-300 group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-xs font-mono font-black text-slate-300 group-hover:text-blue-500 transition-colors">#{idx:02d}</span>
              <div class="w-11 h-11 rounded-2xl bg-blue-50 border border-blue-200/80 text-blue-600 flex items-center justify-center text-lg group-hover:bg-blue-600 group-hover:text-white transition-all shadow-2xs">
                <i class="{icon}"></i>
              </div>
            </div>

            <h3 class="text-lg font-black text-slate-900 font-heading mb-2 group-hover:text-blue-600 transition-colors">
              <a href="services/{slug}">{name}</a>
            </h3>

            <p class="text-xs sm:text-[13px] text-slate-500 leading-relaxed mb-4">
              {desc}
            </p>

            <div class="flex flex-wrap gap-1.5 mb-6">
              {tags_html}
            </div>
          </div>

          <div class="pt-4 border-t border-slate-100 flex items-center gap-2">
            <a href="services/{slug}" class="flex-1 py-2 px-2.5 rounded-xl bg-blue-50 hover:bg-blue-600 text-blue-700 hover:text-white text-xs font-bold text-center transition flex items-center justify-center gap-1 shadow-2xs">
              <span>View Details</span>
              <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </a>
            <a href="pricing.html?service={pkg_key}" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 text-xs font-bold text-center transition shadow-2xs">
              View Pricing
            </a>
            <a href="{wa_url}" target="_blank" class="p-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-600 transition flex items-center justify-center shrink-0" title="Chat on WhatsApp">
              <i class="fa-brands fa-whatsapp text-base"></i>
            </a>
          </div>
        </div>"""

    # Division Pricing Track (8 Services for this division)
    pills_html = ""
    panels_html = ""
    for idx, sk in enumerate(cfg["keys"]):
        s_info = SERVICES_INFO[sk]
        pkg = packages_data.get(sk, {})
        is_first = (idx == 0)
        active_pill_cls = "border-blue-600 bg-blue-50/80 text-blue-700 shadow-xs" if is_first else "border-slate-200/90 bg-white text-slate-700 hover:border-blue-400 hover:bg-slate-50 shadow-2xs"
        hidden_panel_cls = "" if is_first else "hidden"

        pills_html += f"""
        <button id="cat-pill-{sk}" onclick="selectCatPricingService('{sk}')" class="cat-track-pill flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-2xl border text-xs font-bold transition-all cursor-pointer {active_pill_cls}">
          <i class="{s_info['icon']} text-xs text-blue-600"></i>
          <span>{s_info['name']}</span>
        </button>"""

        desc_clean = pkg.get("desc", "").replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")

        # 3 Tiers
        tiers = pkg.get("packages", [])
        tiers_cards = ""
        for t_idx, tier in enumerate(tiers):
            t_name = tier.get("name", "")
            t_tag = tier.get("tag", "")
            t_price_usd = tier.get("price_usd", "Custom")
            t_period = tier.get("period", "")
            t_desc = tier.get("card_desc", "").replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")
            t_features = tier.get("features", [])
            t_delivery = tier.get("delivery", "⏱ Turnaround by scope")
            is_pop = tier.get("popular", False) or (t_idx == 1)

            rates = format_currency(t_price_usd)
            period_text = f"/{t_period}" if t_period else ("One-time" if "custom" not in rates['usd'].lower() else "Custom Scope")

            wa_text = f"Hi Ranknix Online! I want to get started with the {s_info['name']} - {t_name} package ({rates['pkr']}). Please share onboarding details."
            wa_link = f"https://wa.me/923088163940?text={urllib.parse.quote(wa_text)}"

            if is_pop:
                card_border = "border-2 border-blue-600 shadow-xl relative scale-100 lg:-translate-y-2"
                badge_html = '<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-[11px] font-black uppercase tracking-wider shadow-md">⭐ Most Popular Tier</div>'
                btn_cls = "bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20"
                wa_icon_color = "text-white"
            else:
                card_border = "border border-slate-200/90 shadow-2xs relative"
                badge_html = ""
                btn_cls = "bg-slate-900 hover:bg-blue-600 text-white shadow-xs"
                wa_icon_color = "text-emerald-400"

            feats_li = "".join([f'<li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-blue-600 mt-0.5 shrink-0 text-xs sm:text-sm"></i><span class="leading-snug">{f.replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")}</span></li>' for f in t_features])

            tiers_cards += f"""
            <div class="clean-card rounded-3xl p-7 sm:p-8 flex flex-col justify-between {card_border}">
              {badge_html}
              <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                  <span class="text-xs font-black uppercase tracking-wider text-blue-600">{t_name}</span>
                  <span class="text-[11px] font-bold text-slate-500 bg-slate-100 px-2.5 py-0.5 rounded-full">{t_delivery}</span>
                </div>
                <h4 class="text-lg font-black text-slate-900 font-heading mb-1">{t_tag}</h4>
                <p class="text-xs text-slate-500 mb-6 leading-relaxed">{t_desc}</p>
                
                <div class="mb-6 pb-6 border-b border-slate-100">
                  <div class="flex items-baseline gap-1.5">
                    <span class="dynamic-price text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight" data-pkr="{rates['pkr']}" data-usd="{rates['usd']}" data-gbp="{rates['gbp']}" data-eur="{rates['eur']}">{rates['pkr']}</span>
                    <span class="text-xs font-bold text-slate-500">{period_text}</span>
                  </div>
                  <span class="text-[11px] text-slate-400 block mt-1">Direct Founder Supervision &bull; Full Asset Rights</span>
                </div>

                <ul class="space-y-3 mb-8 text-xs sm:text-[13px] text-slate-700">
                  {feats_li}
                </ul>
              </div>

              <div class="pt-4 border-t border-slate-100 flex flex-col gap-2">
                <a href="{wa_link}" target="_blank" class="w-full py-3.5 px-4 rounded-xl font-black text-xs sm:text-sm transition flex items-center justify-center gap-2 {btn_cls}">
                  <i class="fa-brands fa-whatsapp text-base {wa_icon_color}"></i>
                  <span>Order via WhatsApp</span>
                </a>
                <a href="services/{s_info['slug']}#pricing" class="w-full py-2 px-3 text-center text-xs font-bold text-slate-500 hover:text-blue-600 transition flex items-center justify-center gap-1">
                  <span>View Dedicated Service Page &rarr;</span>
                </a>
              </div>
            </div>"""

        panels_html += f"""
        <div id="cat-panel-{sk}" class="cat-pricing-panel {hidden_panel_cls}">
          <div class="clean-card rounded-2xl p-6 sm:p-7 mb-8 border border-slate-200/90 shadow-2xs flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-2xl bg-blue-50 border border-blue-200 text-blue-600 flex items-center justify-center text-xl shrink-0">
                <i class="{s_info['icon']}"></i>
              </div>
              <div>
                <h3 class="text-xl sm:text-2xl font-black text-slate-900 font-heading">{s_info['name']} Packages</h3>
                <p class="text-slate-600 text-xs sm:text-sm max-w-2xl mt-1 leading-relaxed">{desc_clean}</p>
              </div>
            </div>
            <a href="services/{s_info['slug']}" class="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 hover:text-blue-600 text-xs font-bold transition flex items-center gap-1.5 shadow-2xs shrink-0">
              <span>View Full Scope</span>
              <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </a>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {tiers_cards}
          </div>
        </div>"""

    # Double pills for smooth loop
    pills_marquee = pills_html * 2

    # Reviews (Pick 3 reviews for this division)
    reviews_slice = TESTIMONIALS_DATA[:3] if cat_id == "development" else (TESTIMONIALS_DATA[4:7] if cat_id == "marketing" else TESTIMONIALS_DATA[10:13])
    reviews_cards = ""
    for r in reviews_slice:
        reviews_cards += f"""
        <div class="clean-card rounded-2xl p-6 sm:p-7 flex flex-col justify-between border border-slate-200/90 shadow-2xs hover:shadow-md transition">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="flex items-center gap-1 text-amber-400 text-sm">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
              </div>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 text-[10px] font-bold border border-emerald-200">
                <i class="fa-solid fa-circle-check text-[9px]"></i> Verified Client
              </span>
            </div>
            <p class="text-slate-700 text-xs sm:text-sm leading-relaxed italic mb-6">"{r['text']}"</p>
          </div>
          <div class="pt-4 border-t border-slate-100 flex items-center gap-3">
            <div class="relative shrink-0">
              <img src="{r['avatar']}" alt="{r['name']}" class="w-11 h-11 rounded-full object-cover border-2 border-blue-100 shadow-2xs">
              <span class="absolute bottom-0 right-0 w-3 h-3 rounded-full bg-emerald-500 border-2 border-white"></span>
            </div>
            <div class="overflow-hidden">
              <h5 class="text-xs font-black text-slate-900 leading-tight truncate">{r['name']} {r['flag']}</h5>
              <span class="text-[11px] text-slate-500 block truncate">{r['role']}</span>
              <span class="text-[10px] text-blue-600 font-mono block">{r['country']}</span>
            </div>
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{cfg["title"]}</title>
  <meta name="description" content="{cfg["subtitle"]}">
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
          Ranknix Official Division
        </span>
        <span class="hidden sm:inline text-slate-300">
          {cfg["division_badge"]} overseen directly by Founder Muhammad Abdullah
        </span>
      </div>
      <div class="flex items-center gap-4 text-slate-300 ml-auto">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20your%20{cfg['id']}%20services." target="_blank" class="hover:text-emerald-400 transition flex items-center gap-1.5">
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

        <!-- Center: Navigation Links with Active Indicator -->
        <nav class="hidden lg:flex items-center justify-center gap-1 xl:gap-2 mx-auto min-w-0">
          <a href="index.html" class="nav-link-item">
            <i class="fa-solid fa-house text-slate-400"></i>
            <span>Home</span>
          </a>

          <!-- Development Dropdown -->
          <div class="relative group">
            <a href="development.html" class="nav-link-item flex items-center gap-1.5 {active_nav['dev']}">
              <i class="fa-solid fa-code text-blue-600"></i>
              <span>Development</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
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
            <a href="marketing.html" class="nav-link-item flex items-center gap-1.5 {active_nav['mkt']}">
              <i class="fa-solid fa-chart-line text-indigo-600"></i>
              <span>Marketing</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
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
            <a href="automation.html" class="nav-link-item flex items-center gap-1.5 {active_nav['auto']}">
              <i class="fa-solid fa-gears text-amber-600"></i>
              <span>Automation</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
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
          <a href="pricing.html" class="nav-link-item font-extrabold text-blue-600 bg-blue-50/70 border border-blue-200/60 rounded-xl px-3 py-1.5 hover:bg-blue-600 hover:text-white transition shadow-2xs">
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
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20your%20{cfg['id']}%20services." target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 text-xs font-bold transition flex items-center gap-1.5">
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
    <a href="development.html" class="block py-2 text-blue-600 font-bold"><i class="fa-solid fa-code mr-2"></i> Development Services (8)</a>
    <a href="marketing.html" class="block py-2 text-indigo-600 font-bold"><i class="fa-solid fa-chart-line mr-2"></i> Marketing &amp; Ads (8)</a>
    <a href="automation.html" class="block py-2 text-amber-600 font-bold"><i class="fa-solid fa-gears mr-2"></i> CRM &amp; Automation (8)</a>
    <a href="pricing.html" class="block py-2 text-emerald-600 font-bold"><i class="fa-solid fa-tags mr-2"></i> Pricing &amp; Packages</a>
    <a href="index.html#results" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-trophy mr-2"></i> Case Studies</a>
    <a href="index.html#testimonials" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-star mr-2"></i> Client Reviews</a>
    <a href="#contact" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-phone mr-2"></i> Contact</a>
  </div>

  <!-- HERO SECTION -->
  <section class="relative pt-10 pb-16 md:pt-16 md:pb-20 overflow-hidden bg-gradient-to-b from-blue-50/50 via-white to-white border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs text-slate-500 mb-6 font-medium">
        <a href="index.html" class="hover:text-blue-600 transition flex items-center gap-1">
          <i class="fa-solid fa-house text-[10px]"></i>
          <span>Home</span>
        </a>
        <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
        <span class="text-blue-600 font-bold">{cfg["division_badge"]}</span>
      </nav>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Left: Hero Copy -->
        <div class="lg:col-span-7">
          <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-blue-100/80 text-blue-800 text-xs font-extrabold uppercase tracking-wider mb-4 border border-blue-200/60 shadow-2xs">
            <i class="fa-solid fa-shield-check text-blue-600"></i>
            <span>{cfg["division_badge"]}</span>
          </div>
          
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight leading-[1.15] mb-5">
            {cfg["h1_prefix"]} <span class="text-gradient-blue">{cfg["h1_gradient"]}</span>
          </h1>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
            {cfg["subtitle"]}
          </p>

          <!-- CTAs -->
          <div class="flex flex-wrap items-center gap-3.5 mb-8">
            <a href="#services-grid" class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-black text-sm shadow-md shadow-blue-500/25 transition flex items-center gap-2">
              <i class="fa-solid fa-grid-2"></i>
              <span>Explore 8 Services Below &darr;</span>
            </a>
            <a href="#division-pricing" class="px-6 py-3.5 rounded-xl bg-white hover:bg-slate-50 border-2 border-slate-200 text-slate-800 font-bold text-sm shadow-2xs transition flex items-center gap-2">
              <i class="fa-solid fa-tags text-blue-600"></i>
              <span>View Packages</span>
            </a>
            <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20ready%20to%20discuss%20a%20{cfg['id']}%20project." target="_blank" class="px-4 py-3.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-700 font-bold text-sm transition flex items-center gap-1.5 shadow-2xs">
              <i class="fa-brands fa-whatsapp text-emerald-600 text-lg"></i>
              <span>WhatsApp</span>
            </a>
          </div>

          <div class="flex items-center gap-3 text-xs text-slate-500">
            <div class="flex -space-x-2">
              <span class="w-7 h-7 rounded-full bg-blue-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">UK</span>
              <span class="w-7 h-7 rounded-full bg-emerald-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">US</span>
              <span class="w-7 h-7 rounded-full bg-amber-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">UAE</span>
              <span class="w-7 h-7 rounded-full bg-indigo-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">PK</span>
            </div>
            <span class="font-semibold text-slate-700">Trusted by Ambitious Brands Across 60+ Countries</span>
          </div>
        </div>

        <!-- Right: 4 Stat Cards Grid -->
        <div class="lg:col-span-5 grid grid-cols-2 gap-3.5">
          {stat_cards_html}
        </div>
      </div>
    </div>
  </section>

  <!-- TECHNOLOGIES TICKER -->
  <div class="py-4 bg-slate-900 text-white overflow-hidden border-y border-slate-800">
    <div class="marquee-wrapper relative w-full overflow-hidden">
      <div class="marquee-content flex gap-8 items-center text-xs font-mono font-bold tracking-wider" style="animation: scrollInfinite 35s linear infinite; width: max-content;">
        {"".join([f'<span class="flex items-center gap-2 text-slate-300"><i class="fa-solid fa-cube text-blue-400"></i> {tech}</span>' for tech in cfg["tech_ticker"] * 3])}
      </div>
    </div>
  </div>

  <!-- THE 8 SERVICES GRID (THE ACTUAL CARDS PREVIOUSLY ON LANDING PAGE) -->
  <section id="services-grid" class="py-20 sm:py-24 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-14" data-aos="fade-up">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Specialized Capabilities</span>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          8 Core Specializations <span class="text-gradient-blue">In This Division</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Every service is managed with dedicated technical mastery, direct supervision by Founder Muhammad Abdullah, and clear milestone deliverables.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {cards_html}
      </div>

    </div>
  </section>

  <!-- DIVISION PRICING SHOWCASE (MARQUEE TRACK FOR THIS DIVISION) -->
  <section id="division-pricing" class="py-24 bg-slate-50/70 relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-10" data-aos="fade-up">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold mb-3 shadow-2xs">
          <i class="fa-solid fa-tags text-blue-600"></i>
          <span>Transparent Pricing &bull; Fixed Turnaround Times</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Packages &amp; Rates <span class="text-gradient-blue">For Every Need</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-6">
          Click any service in the track below to view complete 3-tier packages (Starter, Growth, Enterprise). All prices switch dynamically to your local currency.
        </p>

        <!-- Dynamic Currency Selector Pills -->
        <div class="inline-flex flex-wrap items-center justify-center gap-2 px-4 py-2 rounded-2xl bg-white border border-slate-200/90 shadow-2xs text-xs">
          <span class="text-slate-500 font-semibold flex items-center gap-1.5">
            <i class="fa-solid fa-globe text-blue-600"></i> Active Currency:
          </span>
          <div class="inline-flex gap-1">
            <button onclick="changeGlobalCurrency('PKR')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="PKR">🇵🇰 ₨ PKR</button>
            <button onclick="changeGlobalCurrency('GBP')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="GBP">🇬🇧 £ GBP</button>
            <button onclick="changeGlobalCurrency('USD')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="USD">🇺🇸 $ USD</button>
            <button onclick="changeGlobalCurrency('EUR')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="EUR">🇪🇺 € EUR</button>
          </div>
        </div>
      </div>

      <!-- Marquee Track for the 8 Services of this Division -->
      <div class="relative mb-8" data-aos="fade-up">
        <div class="marquee-wrapper relative w-full overflow-hidden py-3 bg-white/70 backdrop-blur-sm rounded-2xl border border-slate-200/90 shadow-2xs">
          <div class="marquee-content flex gap-3 hover:[animation-play-state:paused]" style="animation: scrollInfinite 40s linear infinite; width: max-content;">
            {pills_marquee}
          </div>
        </div>
      </div>

      <!-- The 8 Service Panels -->
      <div id="cat-panels-container">
        {panels_html}
      </div>

    </div>
  </section>

  <!-- VERIFIED CLIENT REVIEWS -->
  <section class="py-20 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Verified Testimonials</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          What Clients Say <span class="text-gradient-blue">About This Division</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Authentic feedback from CEOs, CMOs, and brand founders in the UK, USA, UAE, and Pakistan.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {reviews_cards}
      </div>
    </div>
  </section>

  <!-- FINAL CTA BANNER -->
  <section id="contact" class="py-16 sm:py-20 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white relative z-10 overflow-hidden">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <span class="inline-block px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-4 border border-blue-400/30">
        Ready To Accelerate Your Brand?
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
          <a href="development.html" class="hover:text-blue-400 transition">Development</a>
          <a href="marketing.html" class="hover:text-blue-400 transition">Marketing</a>
          <a href="automation.html" class="hover:text-blue-400 transition">Automation</a>
          <a href="pricing.html" class="hover:text-blue-400 transition">Pricing Plans</a>
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
    function selectCatPricingService(slug) {{
      document.querySelectorAll('.cat-track-pill').forEach(btn => {{
        btn.classList.remove('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
        btn.classList.add('border-slate-200/90', 'bg-white', 'text-slate-700');
      }});

      const matchingPills = document.querySelectorAll('#cat-pill-' + slug);
      matchingPills.forEach(p => {{
        p.classList.add('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
        p.classList.remove('border-slate-200/90', 'bg-white', 'text-slate-700');
      }});

      document.querySelectorAll('.cat-pricing-panel').forEach(p => p.classList.add('hidden'));
      const target = document.getElementById('cat-panel-' + slug);
      if (target) {{
        target.classList.remove('hidden');
      }}
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
      const msg = "Hi Ranknix Online! I'm submitting an inquiry for {cfg['h1_prefix']}.\\n\\nName: " + lName + "\\nPhone: " + lPhone + "\\nRequirement: " + lNotes;
      window.open("https://wa.me/923088163940?text=" + encodeURIComponent(msg), '_blank');
      closeModal();
    }}
  </script>
</body>
</html>
"""
    return html

# Generate all 3 category pages
for cfg in CATEGORY_CONFIGS:
    out_file = os.path.join(BASE_DIR, cfg["file"])
    html_content = render_category_page(cfg)
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated {cfg['file']} ({len(html_content)} bytes)")

print("\nSuccessfully built all 3 dedicated category pages!")
