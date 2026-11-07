import os, json, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

from services_data_part1 import SERVICES_DATA as p1
from services_data_part2 import SERVICES_DATA_PART2 as p2
from services_data_part3 import SERVICES_DATA_PART3 as p3

from services_config import format_currency
from service_extras import get_reviews_for_service
from service_simulations import render_simulation

ALL_SERVICES = p1 + p2 + p3
print(f"Total base services loaded: {len(ALL_SERVICES)}")

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "r", encoding="utf-8") as f:
    packages_data = json.load(f)

OUTPUT_DIR = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\services"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SLUG_TO_PKG_KEY = {
    'web-development.html': 'web-dev',
    'app-development.html': 'app-dev',
    'ui-ux-design.html': 'ui-ux',
    'graphic-design.html': 'graphic',
    'e-commerce-solutions.html': 'ecommerce',
    'video-editing.html': 'video',
    'content-writing.html': 'content',
    'landing-page-design.html': 'landing',
    'digital-marketing.html': 'digital-mkt',
    'seo-services.html': 'seo',
    'google-ads-bing-ads.html': 'google-ads',
    'meta-ads.html': 'meta-ads',
    'social-media-management.html': 'social',
    'web-analytics.html': 'analytics',
    'cro-conversion-optimization.html': 'cro',
    'email-marketing.html': 'email',
    'legal-data-entry-data-analysis.html': 'legal',
    'gohighlevel-migration-automation.html': 'ghl',
    'zoho-setup-automation.html': 'zoho',
    'crm-data-management-automation.html': 'crm',
    'lead-generation.html': 'leadgen',
    'web-research.html': 'research',
    'excel-cleaning-formatting.html': 'excel',
    'social-media-data-collection.html': 'socialdata'
}

def get_simulation_type(slug):
    if "google-ads" in slug:
        return "google_ads"
    elif "meta-ads" in slug or "social-media-management" in slug:
        return "meta_ads"
    elif "web-development" in slug or "landing-page" in slug or "app-development" in slug or "ui-ux" in slug or "graphic" in slug:
        return "web_dev"
    else:
        return "crm_auto"

def generate_service_html(s):
    raw_slug = s['slug']
    slug = raw_slug if raw_slug.endswith('.html') else raw_slug + '.html'
    pkg_key = SLUG_TO_PKG_KEY.get(slug, 'web-dev')
    pkg_info = packages_data.get(pkg_key, {})
    
    name = s['name']
    category = s['category']
    cat_icon = s['cat_icon']
    icon = s['icon']
    h1_prefix = s['h1_prefix']
    h1_gradient = s['h1_gradient']
    description = s['description'].replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")
    stats = s['stats']
    deliverables = s['deliverables']
    faqs = s['faqs']
    
    sim_type = get_simulation_type(slug)
    reviews = get_reviews_for_service(pkg_key, name)
    
    # 1. 4 STAT CARDS
    stat_cards_html = ""
    for st in stats:
        if isinstance(st, (list, tuple)):
            st_val = st[0]
            st_label = st[1]
            st_sub = st[2] if len(st) > 2 else "Verified Track Record"
        else:
            st_val = st.get('val', '')
            st_label = st.get('label', '')
            st_sub = st.get('sub', 'Verified Track Record')
        stat_cards_html += f"""
        <div class="clean-card rounded-2xl p-5 border border-slate-200/90 shadow-2xs hover:border-blue-300 transition">
          <div class="text-3xl font-black text-slate-900 font-heading mb-1 text-gradient-blue">{st_val}</div>
          <div class="text-xs font-black text-slate-800 uppercase tracking-wider mb-1">{st_label}</div>
          <div class="text-[11px] text-slate-500 leading-snug">{st_sub}</div>
        </div>"""

    # 2. DELIVERABLES GRID (6 CARDS)
    deliverables_html = ""
    for d in deliverables:
        deliverables_html += f"""
        <div class="clean-card rounded-2xl p-6 sm:p-7 flex flex-col justify-between border border-slate-200/90 shadow-2xs hover:shadow-md transition">
          <div>
            <div class="w-12 h-12 rounded-2xl bg-blue-50 border border-blue-200/80 text-blue-600 flex items-center justify-center text-xl mb-4">
              <i class="{d['icon']}"></i>
            </div>
            <h3 class="text-lg font-black text-slate-900 font-heading mb-2.5">{d['title']}</h3>
            <p class="text-slate-600 text-xs sm:text-sm leading-relaxed">{d['desc']}</p>
          </div>
        </div>"""

    # 3. CAMPAIGN TYPES / SPECIALIZED CAPABILITIES SECTION
    campaign_cards_html = ""
    default_caps = [
        {"num": "01", "ico": "fa-solid fa-chart-line", "title": f"Strategic {name} Architecture", "desc": f"Comprehensive audit, competitor mapping, and execution strategy tailored to your exact business objectives.", "tags": ["Audit", "Competitor Research", "Roadmap"], "metric_label": "Implementation Speed", "metric_val": "< 48 Hours"},
        {"num": "02", "ico": "fa-solid fa-bolt", "title": f"High-Performance Execution", "desc": f"Rigorous production build with strict quality controls, continuous monitoring, and zero technical bloat.", "tags": ["Quality Assurance", "Direct Founder Oversight", "Zero Errors"], "metric_label": "SLA Uptime", "metric_val": "99.9% Uptime"},
        {"num": "03", "ico": "fa-solid fa-arrows-rotate", "title": "Continuous Optimization & Scaling", "desc": f"Data-backed iterative refinements, split testing, and proactive performance reporting to scale revenue.", "tags": ["A/B Testing", "KPI Tracking", "Weekly Reports"], "metric_label": "Client Retention", "metric_val": "94% Repeat"},
        {"num": "04", "ico": "fa-solid fa-headset", "title": "Dedicated Founder Support", "desc": f"Direct WhatsApp access to Muhammad Abdullah and your designated senior technical manager.", "tags": ["WhatsApp SLA", "Direct Access", "Full Source Rights"], "metric_label": "Response Time", "metric_val": "< 15 Mins"}
    ]
    
    if pkg_key == "google-ads":
        default_caps = [
            {"num": "01", "ico": "fa-solid fa-magnifying-glass", "title": "Search Campaigns", "desc": "High-intent text ads shown when prospective customers actively search for your exact solution on Google & Bing. Structured with tight single-theme ad groups, negative keywords, and responsive search ads.", "tags": ["RSA", "DSA", "Call Ads", "Negative KW", "Exact Match"], "metric_label": "Avg. CTR We Achieve", "metric_val": "4.8% – 7.2%"},
            {"num": "02", "ico": "fa-solid fa-bag-shopping", "title": "Shopping Campaigns", "desc": "Visual product listing ads with image, price, and store reviews displayed right at the top of Google. We manage Merchant Center feed optimization, title enrichment, and smart bidding segmentation.", "tags": ["Merchant Center", "Feed Rules", "Smart Shopping", "Standard Shopping"], "metric_label": "Typical ROAS Range", "metric_val": "3.5x – 8.0x"},
            {"num": "03", "ico": "fa-solid fa-image", "title": "Display & Remarketing", "desc": "High-impact visual banner campaigns across 35 million+ websites and YouTube. We build dynamic retargeting funnels that re-engage previous site visitors and abandoners until they convert.", "tags": ["Dynamic Remarketing", "Custom Intent", "In-Market", "Topic Placements"], "metric_label": "Remarketing CPA Drop", "metric_val": "-42% CPA"},
            {"num": "04", "ico": "fa-solid fa-bolt", "title": "Performance Max (PMax)", "desc": "Google's flagship AI campaign combining Search, Shopping, YouTube, Gmail, Maps, and Display into a unified conversion engine with bespoke asset groups and high-value audience signals.", "tags": ["Asset Groups", "Audience Signals", "Search Themes", "Value Bidding"], "metric_label": "Conversion Lift", "metric_val": "+28% vs Standard"}
        ]
    elif pkg_key == "web-dev":
        default_caps = [
            {"num": "01", "ico": "fa-brands fa-wordpress", "title": "Custom WordPress & Elementor", "desc": "Bespoke WordPress architectures with custom post types, Advanced Custom Fields (ACF), and zero reliance on heavy pre-made themes. Easy to edit for your team, secure, and blazing fast.", "tags": ["ACF Pro", "Custom Post Types", "WooCommerce", "Security Hardening"], "metric_label": "PageSpeed Score", "metric_val": "95+ on Mobile"},
            {"num": "02", "ico": "fa-brands fa-shopify", "title": "Shopify & Shopify Plus", "desc": "High-converting storefronts built on Shopify Liquid with custom section architecture, conversion-focused cart drawers, dynamic upsells, and full payment gateway integrations.", "tags": ["Shopify Liquid", "App Optimization", "Checkout Upsells", "Theme 2.0"], "metric_label": "Checkout Conversion Lift", "metric_val": "+34% Avg."},
            {"num": "03", "ico": "fa-brands fa-react", "title": "React, Next.js & Headless", "desc": "Full-stack web applications and headless storefronts with server-side rendering (SSR), API route microservices, and instant client-side routing for enterprise-grade scalability.", "tags": ["Next.js", "React", "Node.js", "Tailwind CSS", "REST/GraphQL"], "metric_label": "First Contentful Paint", "metric_val": "< 0.8s"},
            {"num": "04", "ico": "fa-solid fa-gauge-high", "title": "Core Web Vitals & Speed", "desc": "Deep performance optimization tackling LCP, FID/INP, and CLS. We optimize assets, implement critical CSS paths, lazy-load media, and configure edge CDN caching.", "tags": ["Sub-Second LCP", "Zero CLS", "Asset Minification", "Edge CDN"], "metric_label": "Google Vitals Status", "metric_val": "100% Green Pass"}
        ]
    elif pkg_key == "meta-ads":
        default_caps = [
            {"num": "01", "ico": "fa-brands fa-meta", "title": "Advantage+ Shopping Campaigns", "desc": "Meta's flagship AI scaling architecture. We configure machine-learning catalogs, creative variations, and dynamic audience boundaries to scale without audience fatigue.", "tags": ["ASC", "Dynamic Catalog", "Audience Cap", "Budget Scaling"], "metric_label": "Avg. Blended ROAS", "metric_val": "3.8x – 6.5x"},
            {"num": "02", "ico": "fa-solid fa-video", "title": "Direct-Response Video Hooks", "desc": "High-converting video ad creatives engineered with 3-second pattern interrupts, authentic UGC hooks, product demonstrations, and clear calls-to-action.", "tags": ["UGC Video", "Hook Testing", "Iterative Variations", "CapCut / Premiere"], "metric_label": "Thumbstop Rate", "metric_val": "38%+ (Top 5%)"},
            {"num": "03", "ico": "fa-solid fa-server", "title": "Conversions API (CAPI) & Server-Side", "desc": "100% signal recovery bypasses iOS 14+ tracking loss and ad blockers with robust Meta Conversions API via server GTM and Cloudflare.", "tags": ["Server GTM", "Event Match Quality", "Deduplication", "iOS Resilient"], "metric_label": "Event Match Quality", "metric_val": "9.2 / 10"},
            {"num": "04", "ico": "fa-solid fa-arrows-split-up-and-left", "title": "Retargeting & High-LTV Funnels", "desc": "Segmented custom audiences capturing engaged Instagram followers, video viewers, and abandoners to maximize client lifetime value and lower CPA.", "tags": ["Custom Audiences", "Lookalike 1%", "Cart Abandonment", "VIP Retention"], "metric_label": "Retargeting CPA", "metric_val": "-45% CPA"}
        ]

    for c in default_caps:
        tags_str = "".join([f'<span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-700 text-[10px] font-bold">{t}</span>' for t in c["tags"]])
        campaign_cards_html += f"""
        <div class="clean-card rounded-2xl p-6 sm:p-7 flex flex-col justify-between border border-slate-200/90 shadow-2xs hover:border-blue-300 transition">
          <div>
            <div class="flex items-center justify-between mb-4">
              <div class="w-10 h-10 rounded-xl bg-blue-50 border border-blue-200 text-blue-600 flex items-center justify-center text-lg">
                <i class="{c['ico']}"></i>
              </div>
              <span class="text-xs font-black font-mono text-slate-300">#{c['num']}</span>
            </div>
            <h4 class="text-base sm:text-lg font-black text-slate-900 font-heading mb-2">{c['title']}</h4>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4">{c['desc']}</p>
            <div class="flex flex-wrap gap-1.5 mb-6">{tags_str}</div>
          </div>
          <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
            <span class="text-slate-500 font-semibold">{c['metric_label']}</span>
            <strong class="text-blue-600 font-black font-heading">{c['metric_val']}</strong>
          </div>
        </div>"""

    # 4. PRICING CARDS FROM SCRAPED PACKAGES
    tiers = pkg_info.get("packages", [])
    pricing_cards_html = ""
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
        
        wa_text = f"Hi Ranknix Online! I'm interested in the {name} - {t_name} package ({rates['pkr']}). Please share onboarding details."
        wa_link = f"https://wa.me/923088163940?text={urllib.parse.quote(wa_text)}"
        
        if is_pop:
            card_border = "border-2 border-blue-600 shadow-xl relative scale-100 lg:-translate-y-2"
            badge_html = '<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-[11px] font-black uppercase tracking-wider shadow-md">⭐ Most Popular Tier</div>'
            btn_cls = "bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20"
            wa_icon_color = "text-white"
        else:
            card_border = "border border-slate-200/90 shadow-xs relative"
            badge_html = ""
            btn_cls = "bg-slate-900 hover:bg-blue-600 text-white shadow-xs"
            wa_icon_color = "text-emerald-400"

        feats_li = "".join([f'<li class="flex items-start gap-2.5"><i class="fa-solid fa-circle-check text-blue-600 mt-0.5 shrink-0 text-xs sm:text-sm"></i><span class="leading-snug">{f.replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")}</span></li>' for f in t_features])
        
        pricing_cards_html += f"""
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
              <span class="text-[11px] text-slate-400 block mt-1">Direct Founder Oversight &bull; Guaranteed Turnaround</span>
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
            <button onclick="openModal()" class="w-full py-2 px-3 text-center text-xs font-bold text-slate-500 hover:text-blue-600 transition flex items-center justify-center gap-1">
              <span>Book Strategy Call &rarr;</span>
            </button>
          </div>
        </div>"""

    # 5. VERIFIED CLIENT REVIEWS
    reviews_cards_html = ""
    for r in reviews:
        reviews_cards_html += f"""
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

    # 6. FAQS ACCORDION
    faqs_html = ""
    for f_idx, f in enumerate(faqs, 1):
        faqs_html += f"""
        <div class="faq-item clean-card rounded-2xl overflow-hidden border border-slate-200/90 shadow-2xs mb-3">
          <button class="faq-trigger w-full px-6 py-4 sm:py-5 text-left font-bold text-slate-900 text-sm sm:text-base flex items-center justify-between gap-4 hover:bg-slate-50 transition">
            <span class="flex items-center gap-3">
              <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold shrink-0">Q{f_idx}</span>
              <span>{f['q']}</span>
            </span>
            <i class="faq-icon fa-solid fa-chevron-down text-xs text-slate-400 transition-transform"></i>
          </button>
          <div class="faq-content {'hidden' if f_idx > 1 else ''} px-6 pb-5 text-slate-600 text-xs sm:text-sm leading-relaxed border-t border-slate-100 pt-3">
            {f['a']}
          </div>
        </div>"""

    # Assemble Full Sub-Page HTML
    sim_html = render_simulation(sim_type, name)

    html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} Services | Ranknix Online - Worldwide Digital Agency</title>
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
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Main Stylesheet -->
  <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body class="bg-white text-slate-800 antialiased font-sans selection:bg-blue-600 selection:text-white">

  <!-- TOP ANNOUNCEMENT BAR -->
  <div class="bg-gradient-to-r from-slate-900 via-blue-950 to-slate-900 text-white text-[11px] sm:text-xs py-2 px-4 border-b border-blue-900/40">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-black bg-blue-500/20 text-blue-300 border border-blue-400/30">
          Ranknix Official Service
        </span>
        <span class="hidden sm:inline text-slate-300">
          Professional {name} overseen by Founder Muhammad Abdullah
        </span>
      </div>
      <div class="flex items-center gap-4 text-slate-300 ml-auto">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{urllib.parse.quote(name)}" target="_blank" class="hover:text-emerald-400 transition flex items-center gap-1.5">
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
        <a href="../index.html" class="flex items-center gap-2.5 sm:gap-3 group shrink-0">
          <img src="../assets/images/logo.png" alt="Ranknix Online Logo" class="h-10 sm:h-11 w-auto object-contain">
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

        <!-- Center: Navigation Links -->
        <nav class="hidden lg:flex items-center justify-center gap-1 xl:gap-2 mx-auto">
          <a href="../index.html" class="nav-link-item">
            <i class="fa-solid fa-arrow-left text-slate-400"></i>
            <span>Home</span>
          </a>
          <a href="../pricing.html" class="nav-link-item">
            <i class="fa-solid fa-tags text-emerald-600"></i>
            <span>Pricing &amp; Packages</span>
          </a>
          <a href="#campaigns" class="nav-link-item">
            <i class="fa-solid fa-layer-group text-indigo-600"></i>
            <span>Specializations</span>
          </a>
          <a href="#simulation" class="nav-link-item">
            <i class="fa-solid fa-desktop text-sky-600"></i>
            <span>Live Proof</span>
          </a>
          <a href="#pricing" class="nav-link-item">
            <i class="fa-solid fa-tags text-emerald-600"></i>
            <span>Packages</span>
          </a>
          <a href="#reviews" class="nav-link-item">
            <i class="fa-solid fa-star text-amber-500"></i>
            <span>Reviews</span>
          </a>
          <a href="#faq" class="nav-link-item">
            <i class="fa-solid fa-circle-question text-violet-600"></i>
            <span>FAQs</span>
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
              <button onclick="changePageCurrency('PKR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇵🇰 Pakistan (PKR)</span>
                <span class="font-bold text-slate-500">₨</span>
              </button>
              <button onclick="changePageCurrency('GBP')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇬🇧 United Kingdom (GBP)</span>
                <span class="font-bold text-slate-500">£</span>
              </button>
              <button onclick="changePageCurrency('USD')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇺🇸 United States (USD)</span>
                <span class="font-bold text-slate-500">$</span>
              </button>
              <button onclick="changePageCurrency('EUR')" class="w-full text-left px-3 py-2 text-xs hover:bg-blue-50 text-slate-700 font-semibold flex items-center justify-between">
                <span>🇪🇺 Europe (EUR)</span>
                <span class="font-bold text-slate-500">€</span>
              </button>
            </div>
          </div>

          <!-- WhatsApp Button -->
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{urllib.parse.quote(name)}" target="_blank" class="px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 text-xs font-bold transition flex items-center gap-1.5">
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
    <a href="../index.html" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-arrow-left mr-2"></i> Home</a>
    <a href="../pricing.html" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-tags mr-2 text-emerald-600"></i> Pricing Plans (All 24)</a>
    <a href="#campaigns" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-layer-group mr-2"></i> Specializations</a>
    <a href="#simulation" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-desktop mr-2"></i> Live Proof</a>
    <a href="#pricing" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-tags mr-2"></i> Pricing Packages</a>
    <a href="#reviews" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-star mr-2"></i> Client Reviews</a>
    <a href="#faq" class="block py-2 text-slate-700 hover:text-blue-600"><i class="fa-solid fa-circle-question mr-2"></i> FAQs</a>
    <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
      <span class="text-xs text-slate-500">Currency:</span>
      <div class="flex gap-1 text-xs">
        <button onclick="changePageCurrency('PKR')" class="px-2 py-1 rounded bg-slate-100 font-bold">PKR</button>
        <button onclick="changePageCurrency('GBP')" class="px-2 py-1 rounded bg-slate-100 font-bold">GBP</button>
        <button onclick="changePageCurrency('USD')" class="px-2 py-1 rounded bg-slate-100 font-bold">USD</button>
        <button onclick="changePageCurrency('EUR')" class="px-2 py-1 rounded bg-slate-100 font-bold">EUR</button>
      </div>
    </div>
  </div>

  <!-- SERVICE HERO SECTION -->
  <section class="relative pt-10 pb-16 md:pt-16 md:pb-20 overflow-hidden bg-gradient-to-b from-blue-50/50 via-white to-white border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Breadcrumb -->
      <nav class="flex items-center gap-2 text-xs text-slate-500 mb-6 font-medium">
        <a href="../index.html" class="hover:text-blue-600 transition flex items-center gap-1">
          <i class="fa-solid fa-house text-[10px]"></i>
          <span>Home</span>
        </a>
        <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
        <a href="../index.html#dev-services" class="hover:text-blue-600 transition">
          {category}
        </a>
        <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
        <span class="text-blue-600 font-bold">{name}</span>
      </nav>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <!-- Left: Hero Copy -->
        <div class="lg:col-span-7">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100/80 text-blue-800 text-xs font-extrabold uppercase tracking-wider mb-4 border border-blue-200/60 shadow-2xs">
            <i class="{cat_icon}"></i>
            <span>{category}</span>
          </div>
          
          <h1 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight leading-[1.15] mb-5">
            {h1_prefix} <span class="text-gradient-blue">{h1_gradient}</span>
          </h1>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-8 max-w-2xl">
            {description}
          </p>

          <!-- CTAs -->
          <div class="flex flex-wrap items-center gap-3.5 mb-8">
            <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{urllib.parse.quote(name)}" target="_blank" class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-black text-sm shadow-md shadow-blue-500/25 transition flex items-center gap-2">
              <i class="fa-brands fa-whatsapp text-lg"></i>
              <span>Get Started via WhatsApp</span>
            </a>
            <a href="#pricing" class="px-6 py-3.5 rounded-xl bg-white hover:bg-slate-50 border-2 border-slate-200 text-slate-800 font-bold text-sm shadow-2xs transition flex items-center gap-2">
              <i class="fa-solid fa-tags text-blue-600"></i>
              <span>View 3-Tier Packages</span>
            </a>
          </div>

          <div class="flex items-center gap-3 text-xs text-slate-500">
            <div class="flex -space-x-2">
              <span class="w-7 h-7 rounded-full bg-blue-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">UK</span>
              <span class="w-7 h-7 rounded-full bg-emerald-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">US</span>
              <span class="w-7 h-7 rounded-full bg-amber-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">UAE</span>
              <span class="w-7 h-7 rounded-full bg-indigo-600 text-white font-bold text-[10px] flex items-center justify-center border-2 border-white">PK</span>
            </div>
            <span class="font-semibold text-slate-700">Trusted by 50+ Ambitious Brands Across 60+ Countries</span>
          </div>
        </div>

        <!-- Right: 4 Stat Cards Grid -->
        <div class="lg:col-span-5 grid grid-cols-2 gap-3.5">
          {stat_cards_html}
        </div>
      </div>
    </div>
  </section>

  <!-- SPECIALIZED CAMPAIGNS / ARCHITECTURE SECTION -->
  <section id="campaigns" class="py-20 bg-slate-50/70 relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Specialized Capabilities</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Every Discipline of {name}, <span class="text-gradient-blue">Covered</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          From brand-new setups to complex multi-channel scaling — we execute every discipline with certified technical mastery.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {campaign_cards_html}
      </div>
    </div>
  </section>

  <!-- LIVE SIMULATION & PROOF PANEL SECTION -->
  <section id="simulation" class="py-20 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-10">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Live Production Preview</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          How Your Brand Performs <span class="text-gradient-blue">In The Real World</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          An interactive snapshot of how Ranknix Online builds, optimizes, and scales your {name} infrastructure.
        </p>
      </div>

      {sim_html}
    </div>
  </section>

  <!-- DELIVERABLES GRID -->
  <section class="py-20 bg-slate-50/70 relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Full Scope Breakdown</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          What We Build &amp; <span class="text-gradient-blue">Deliver For You</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Everything included in our end-to-end execution. Zero gaps, zero outsourcing, complete code and asset ownership.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {deliverables_html}
      </div>
    </div>
  </section>

  <!-- PRICING PACKAGES -->
  <section id="pricing" class="py-24 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Transparent Investment</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          {name} <span class="text-gradient-blue">Packages &amp; Rates</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-6">
          Clear, fixed rates with guaranteed turnaround days. Select your preferred currency below to see exact regional pricing.
        </p>

        <!-- Currency Pills inside Sub-Page Pricing -->
        <div class="inline-flex flex-wrap items-center justify-center gap-2 px-4 py-2 rounded-2xl bg-slate-50 border border-slate-200 text-xs">
          <span class="text-slate-500 font-semibold"><i class="fa-solid fa-coins text-blue-600 mr-1"></i> Currency:</span>
          <button onclick="changePageCurrency('PKR')" class="sub-curr-btn px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-white" data-sub-curr="PKR">🇵🇰 PKR</button>
          <button onclick="changePageCurrency('GBP')" class="sub-curr-btn px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-white" data-sub-curr="GBP">🇬🇧 GBP</button>
          <button onclick="changePageCurrency('USD')" class="sub-curr-btn px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-white" data-sub-curr="USD">🇺🇸 USD</button>
          <button onclick="changePageCurrency('EUR')" class="sub-curr-btn px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-white" data-sub-curr="EUR">🇪🇺 EUR</button>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {pricing_cards_html}
      </div>
    </div>
  </section>

  <!-- VERIFIED CLIENT REVIEWS -->
  <section id="reviews" class="py-20 bg-slate-50/70 relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Verified Testimonials</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          What International Clients Say <span class="text-gradient-blue">About Ranknix Online</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Authentic feedback from CEOs, CMOs, and brand founders in the UK, USA, UAE, Canada, and Pakistan.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        {reviews_cards_html}
      </div>
    </div>
  </section>

  <!-- FAQS ACCORDION -->
  <section id="faq" class="py-20 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center max-w-3xl mx-auto mb-12">
        <span class="text-xs sm:text-sm font-extrabold text-blue-600 tracking-wider uppercase mb-2 inline-block">Frequently Asked Questions</span>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Everything You Need To Know <span class="text-gradient-blue">Before Getting Started</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Have more questions? Muhammad Abdullah and our senior technical team are available on WhatsApp 24/7.
        </p>
      </div>

      <div>
        {faqs_html}
      </div>
    </div>
  </section>

  <!-- FINAL CTA BANNER -->
  <section id="contact" class="py-16 sm:py-20 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white relative z-10 overflow-hidden">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <span class="inline-block px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold uppercase tracking-wider mb-4 border border-blue-400/30">
        Start Your {name} Project
      </span>
      <h2 class="text-3xl sm:text-4xl md:text-5xl font-black font-heading tracking-tight mb-4 leading-tight">
        Ready To Accelerate Your Growth With <br><span class="text-blue-400">Ranknix Online</span>?
      </h2>
      <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto mb-8 leading-relaxed">
        Speak directly with Founder Muhammad Abdullah. We’ll analyze your current setup, uncover missed revenue opportunities, and prepare a custom proposal in under 24 hours.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-4">
        <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20ready%20to%20start%20my%20{urllib.parse.quote(name)}%20project." target="_blank" class="px-7 py-4 rounded-xl bg-emerald-500 hover:bg-emerald-600 text-white font-black text-sm shadow-lg shadow-emerald-500/25 transition flex items-center gap-2.5">
          <i class="fa-brands fa-whatsapp text-xl"></i>
          <span>Chat on WhatsApp (+92 308 8163940)</span>
        </a>
        <button onclick="openModal()" class="px-7 py-4 rounded-xl bg-white hover:bg-slate-100 text-slate-900 font-black text-sm shadow-lg transition flex items-center gap-2">
          <i class="fa-solid fa-calendar-check text-blue-600"></i>
          <span>Schedule Free Strategy Call</span>
        </button>
      </div>
    </div>
  </section>

  <!-- AGENCY FOOTER -->
  <footer class="bg-slate-950 text-slate-400 text-xs py-12 border-t border-slate-900">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-8 border-b border-slate-900">
        <div class="flex items-center gap-3">
          <img src="../assets/images/logo.png" alt="Ranknix Online Logo" class="h-10 w-auto">
          <div>
            <span class="text-base font-black text-white font-heading">Ranknix Online</span>
            <span class="block text-[11px] text-slate-500">Founder &amp; CEO: Muhammad Abdullah</span>
          </div>
        </div>
        <div class="flex flex-wrap items-center justify-center gap-6 text-xs">
          <a href="../index.html" class="hover:text-blue-400 transition">Home</a>
          <a href="../index.html#dev-services" class="hover:text-blue-400 transition">All 24 Services</a>
          <a href="../index.html#pricing" class="hover:text-blue-400 transition">Pricing Plans</a>
          <a href="../index.html#about" class="hover:text-blue-400 transition">About Founder</a>
          <a href="https://wa.me/923088163940" class="hover:text-emerald-400 transition"><i class="fa-brands fa-whatsapp mr-1"></i> WhatsApp</a>
        </div>
      </div>
      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-[11px] text-slate-600">
        <p>&copy; 2026 Ranknix Online. All rights reserved. Worldwide Digital Agency.</p>
        <p>Operating across Pakistan, UK, USA, UAE, Canada &amp; Europe.</p>
      </div>
    </div>
  </footer>

  <!-- AUDIT & STRATEGY MODAL -->
  <div id="service-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative border border-slate-200">
      <button onclick="closeModal()" class="absolute top-5 right-5 text-slate-400 hover:text-slate-700 text-lg">
        <i class="fa-solid fa-xmark"></i>
      </button>
      <div class="mb-5">
        <span class="text-xs font-black uppercase text-blue-600 tracking-wider">Free Consultation</span>
        <h3 class="text-2xl font-black text-slate-900 font-heading mt-1">Book Your Strategy Audit</h3>
        <p class="text-xs text-slate-500 mt-1">We’ll review your {name} goals and reply with a custom roadmap in &lt; 24h.</p>
      </div>
      <form id="service-form" onsubmit="handleModalSubmit(event)" class="space-y-3.5">
        <input type="hidden" id="service-name" value="{name}">
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Your Full Name</label>
          <input type="text" id="lead-name" required placeholder="e.g. James Whitfield / Ali Ahmed" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">WhatsApp / Phone Number</label>
          <input type="text" id="lead-phone" required placeholder="e.g. +44 7911 123456 / +92 300 1234567" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 mb-1">Your Business Goal / Requirement</label>
          <textarea id="lead-notes" rows="3" placeholder="Tell us about your brand, budget, and desired timeline..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-xs focus:ring-2 focus:ring-blue-600 focus:outline-none"></textarea>
        </div>
        <button type="submit" class="w-full py-3.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-black text-xs transition shadow-md shadow-blue-500/20">
          Send Inbound Request via WhatsApp &rarr;
        </button>
      </form>
    </div>
  </div>

  <!-- JAVASCRIPT FOR CURRENCY, FAQS & MODAL -->
  <script>
    // FAQ Accordion
    document.querySelectorAll('.faq-trigger').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const content = btn.nextElementSibling;
        const icon = btn.querySelector('.faq-icon');
        const isHidden = content.classList.contains('hidden');
        
        document.querySelectorAll('.faq-content').forEach(c => c.classList.add('hidden'));
        document.querySelectorAll('.faq-icon').forEach(i => i.classList.remove('rotate-180'));
        
        if (isHidden) {{
          content.classList.remove('hidden');
          icon.classList.add('rotate-180');
        }}
      }});
    }});

    // Currency Switcher
    function changePageCurrency(curr) {{
      try {{
        localStorage.setItem('ranknix_currency', curr);
      }} catch (e) {{}}

      const label = document.getElementById('active-currency-label');
      if (label) {{
        const flags = {{ PKR: '🇵🇰 PKR', GBP: '🇬🇧 GBP', USD: '🇺🇸 USD', EUR: '🇪🇺 EUR' }};
        label.textContent = flags[curr] || curr;
      }}

      document.querySelectorAll('[data-sub-curr]').forEach(btn => {{
        if (btn.getAttribute('data-sub-curr') === curr) {{
          btn.classList.add('bg-blue-600', 'text-white');
          btn.classList.remove('text-slate-700');
        }} else {{
          btn.classList.remove('bg-blue-600', 'text-white');
          btn.classList.add('text-slate-700');
        }}
      }});

      document.querySelectorAll('.dynamic-price').forEach(el => {{
        const val = el.getAttribute('data-' + curr.toLowerCase());
        if (val) el.textContent = val;
      }});
    }}

    // Auto-run currency on page load
    document.addEventListener('DOMContentLoaded', () => {{
      const saved = localStorage.getItem('ranknix_currency') || 'PKR';
      changePageCurrency(saved);

      const toggleBtn = document.getElementById('mobile-toggle-btn');
      const drawer = document.getElementById('mobile-drawer');
      if (toggleBtn && drawer) {{
        toggleBtn.addEventListener('click', () => {{
          drawer.classList.toggle('hidden');
        }});
      }}
    }});

    // Modal logic
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
      const sName = document.getElementById('service-name').value;
      const lName = document.getElementById('lead-name').value;
      const lPhone = document.getElementById('lead-phone').value;
      const lNotes = document.getElementById('lead-notes').value;
      const msg = "Hi Ranknix Online! I'm submitting an inquiry for " + sName + ".\\n\\nName: " + lName + "\\nPhone: " + lPhone + "\\nRequirement: " + lNotes;
      window.open("https://wa.me/923088163940?text=" + encodeURIComponent(msg), '_blank');
      closeModal();
    }}
  </script>
</body>
</html>
"""
    return html

# Generate all 24 pages
for idx, s in enumerate(ALL_SERVICES, 1):
    slug_name = s['slug'] if s['slug'].endswith('.html') else s['slug'] + '.html'
    file_path = os.path.join(OUTPUT_DIR, slug_name)
    page_content = generate_service_html(s)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(page_content)
    
    # Also clean up non-html file if it exists
    non_html_path = os.path.join(OUTPUT_DIR, s['slug'].replace('.html', ''))
    if os.path.exists(non_html_path) and non_html_path != file_path:
        try:
            os.remove(non_html_path)
        except:
            pass
    print(f"[{idx:02d}/24] Generated {slug_name} ({len(page_content)} bytes)")

print("\nSuccessfully generated all 24 rich service pages!")
