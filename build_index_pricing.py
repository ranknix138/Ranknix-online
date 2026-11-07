import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

from test_pricing_gen import SERVICES_INFO, format_currency

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "r", encoding="utf-8") as f:
    packages_data = json.load(f)

# Group services by division
divisions = {
    "dev": {
        "label": "Web & App Development",
        "icon": "fa-solid fa-code",
        "keys": ["web-dev", "app-dev", "ui-ux", "graphic", "ecommerce", "video", "content", "landing"]
    },
    "mkt": {
        "label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-chart-line",
        "keys": ["digital-mkt", "seo", "google-ads", "meta-ads", "social", "analytics", "cro", "email"]
    },
    "auto": {
        "label": "Data, CRM & Automation",
        "icon": "fa-solid fa-cubes-stacked",
        "keys": ["legal", "ghl", "zoho", "crm", "leadgen", "research", "excel", "socialdata"]
    }
}

html = []
html.append('<!-- 11. PRICING SECTION (24-SERVICE MASTER INTERACTIVE SHOWCASE) -->')
html.append('<section id="pricing" class="py-24 bg-slate-50/70 relative z-10 border-t border-slate-200/80">')
html.append('  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">')
html.append('    ')
html.append('    <!-- Section Header -->')
html.append('    <div class="text-center max-w-3xl mx-auto mb-10" data-aos="fade-up">')
html.append('      <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold mb-3 shadow-xs">')
html.append('        <i class="fa-solid fa-shield-check text-blue-600"></i>')
html.append('        <span>All-Inclusive Fixed Rates & Zero Hidden Costs</span>')
html.append('      </div>')
html.append('      <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">')
html.append('        Growth Packages Tailored <span class="text-gradient-blue">For Your Scale</span>')
html.append('      </h2>')
html.append('      <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-6">')
html.append('        Explore clear, fixed pricing across all 24 digital services. Every tier includes guaranteed turnaround times, direct Founder supervision by Muhammad Abdullah, and dynamic multi-currency display (PKR, GBP, USD, EUR).')
html.append('      </p>')
html.append('      ')
html.append('      <!-- Dynamic Currency Badge & Quick Selector -->')
html.append('      <div class="inline-flex flex-wrap items-center justify-center gap-2 px-4 py-2 rounded-2xl bg-white border border-slate-200/90 shadow-sm text-xs">')
html.append('        <span class="text-slate-500 font-semibold flex items-center gap-1.5">')
html.append('          <i class="fa-solid fa-globe text-blue-600"></i> Active Currency:')
html.append('        </span>')
html.append('        <div class="inline-flex gap-1">')
html.append('          <button onclick="changeGlobalCurrency(\'PKR\')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="PKR">🇵🇰 ₨ PKR</button>')
html.append('          <button onclick="changeGlobalCurrency(\'GBP\')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="GBP">🇬🇧 £ GBP</button>')
html.append('          <button onclick="changeGlobalCurrency(\'USD\')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="USD">🇺🇸 $ USD</button>')
html.append('          <button onclick="changeGlobalCurrency(\'EUR\')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="EUR">🇪🇺 € EUR</button>')
html.append('        </div>')
html.append('      </div>')
html.append('    </div>')
html.append('')

# Division Switcher Tabs
html.append('    <!-- 1. Division Switcher Tabs (3 Main Categories) -->')
html.append('    <div class="flex justify-center mb-8" data-aos="fade-up">')
html.append('      <div class="inline-flex flex-wrap justify-center p-1.5 rounded-2xl bg-slate-200/80 border border-slate-300/80 shadow-inner gap-1.5 max-w-full">')
html.append('        <button id="div-btn-dev" onclick="selectPricingDivision(\'dev\')" class="pricing-div-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold bg-blue-600 text-white shadow-md transition flex items-center gap-2">')
html.append('          <i class="fa-solid fa-code"></i>')
html.append('          <span>Web & App Dev (01-08)</span>')
html.append('        </button>')
html.append('        <button id="div-btn-mkt" onclick="selectPricingDivision(\'mkt\')" class="pricing-div-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold text-slate-700 hover:text-slate-900 hover:bg-white/60 transition flex items-center gap-2">')
html.append('          <i class="fa-solid fa-chart-line"></i>')
html.append('          <span>Marketing & Ads (09-16)</span>')
html.append('        </button>')
html.append('        <button id="div-btn-auto" onclick="selectPricingDivision(\'auto\')" class="pricing-div-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold text-slate-700 hover:text-slate-900 hover:bg-white/60 transition flex items-center gap-2">')
html.append('          <i class="fa-solid fa-cubes-stacked"></i>')
html.append('          <span>Data & Automation (17-24)</span>')
html.append('        </button>')
html.append('      </div>')
html.append('    </div>')
html.append('')

# Mobile Dropdown Jump
html.append('    <!-- Mobile Dropdown Selector for Quick Jump -->')
html.append('    <div class="md:hidden mb-6 px-2">')
html.append('      <label for="mobile-pricing-select" class="block text-xs font-bold text-slate-500 mb-1.5">Jump to Service Packages:</label>')
html.append('      <select id="mobile-pricing-select" onchange="selectPricingService(this.value)" class="w-full px-4 py-2.5 rounded-xl bg-white border border-slate-200 text-slate-800 text-xs font-bold shadow-xs focus:ring-2 focus:ring-blue-600">')
for div_id, div_data in divisions.items():
    html.append(f'        <optgroup label="{div_data["label"]}">')
    for sk in div_data["keys"]:
        s_info = SERVICES_INFO[sk]
        html.append(f'          <option value="{sk}">{s_info["name"]}</option>')
    html.append('        </optgroup>')
html.append('      </select>')
html.append('    </div>')
html.append('')

# Service Pills for each division
html.append('    <!-- 2. Service Pills Containers (One per division) -->')
for div_id, div_data in divisions.items():
    hidden_cls = "" if div_id == "dev" else "hidden"
    html.append(f'    <div id="service-pills-{div_id}" class="service-pills-bar {hidden_cls} flex flex-wrap items-center justify-center gap-2 sm:gap-2.5 mb-10" data-aos="fade-up">')
    for sk in div_data["keys"]:
        s_info = SERVICES_INFO[sk]
        active_pill_cls = "bg-blue-600 text-white shadow-md border-blue-600" if sk == "web-dev" else "bg-white text-slate-700 hover:bg-blue-50/70 hover:border-blue-300 border-slate-200/90 shadow-2xs"
        html.append(f'      <button id="pill-{sk}" onclick="selectPricingService(\'{sk}\')" class="service-pill-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-[13px] font-bold border transition-all flex items-center gap-2 {active_pill_cls}">')
        html.append(f'        <i class="{s_info["icon"]} text-xs"></i>')
        html.append(f'        <span>{s_info["name"]}</span>')
        html.append('      </button>')
    html.append('    </div>')
html.append('')

# Service Packages Panels (24 total)
html.append('    <!-- 3. The 24 Service Package Panels -->')
html.append('    <div id="all-service-panels" class="relative min-h-[500px]">')

for idx, (sk, s_info) in enumerate(SERVICES_INFO.items()):
    pkg = packages_data.get(sk, {})
    is_active = (sk == "web-dev")
    panel_hidden = "" if is_active else "hidden"
    
    desc_clean = pkg.get("desc", "").replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")
    
    html.append(f'      <!-- PANEL: {sk} ({s_info["name"]}) -->')
    html.append(f'      <div id="panel-{sk}" class="pricing-panel {panel_hidden} transition-all duration-300">')
    html.append('        ')
    html.append('        <!-- Active Service Mini Header -->')
    html.append('        <div class="clean-card rounded-2xl p-6 sm:p-7 mb-8 border border-slate-200/90 shadow-xs flex flex-col md:flex-row md:items-center justify-between gap-4">')
    html.append('          <div class="flex items-start gap-4">')
    html.append(f'            <div class="w-12 h-12 rounded-2xl bg-blue-50 border border-blue-200 text-blue-600 flex items-center justify-center text-xl shrink-0">')
    html.append(f'              <i class="{s_info["icon"]}"></i>')
    html.append('            </div>')
    html.append('            <div>')
    html.append(f'              <div class="flex items-center gap-2 mb-1">')
    html.append(f'                <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 text-[10px] font-extrabold uppercase tracking-wider">{s_info["division_label"]}</span>')
    html.append(f'                <span class="text-xs text-slate-400 font-bold">Service #{idx+1:02d}</span>')
    html.append('              </div>')
    html.append(f'              <h3 class="text-xl sm:text-2xl font-black text-slate-900 font-heading">{s_info["name"]} Packages</h3>')
    html.append(f'              <p class="text-slate-600 text-xs sm:text-sm max-w-2xl mt-1 leading-relaxed">{desc_clean}</p>')
    html.append('            </div>')
    html.append('          </div>')
    html.append('          <div class="shrink-0 flex items-center gap-3">')
    html.append(f'            <a href="services/{s_info["slug"]}" class="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 hover:text-blue-600 text-xs font-bold transition flex items-center gap-1.5 shadow-2xs">')
    html.append('              <span>Explore Service Page</span>')
    html.append('              <i class="fa-solid fa-arrow-right text-[10px]"></i>')
    html.append('            </a>')
    html.append('          </div>')
    html.append('        </div>')
    html.append('')
    
    # 3-Tier Grid
    html.append('        <!-- 3-Tier Pricing Grid -->')
    html.append('        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">')
    
    tiers = pkg.get("packages", [])
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
        
        # WhatsApp Pre-filled message
        wa_text = f"Hi Ranknix Online! I want to get started with the {s_info['name']} - {t_name} package ({rates['pkr']}). Please share onboarding details."
        import urllib.parse
        wa_link = f"https://wa.me/923088163940?text={urllib.parse.quote(wa_text)}"
        
        # Card styling
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
            
        period_text = f"/{t_period}" if t_period else ("One-time" if "custom" not in rates['usd'].lower() else "Custom Scope")
        
        html.append(f'          <!-- Tier {t_idx+1}: {t_name} -->')
        html.append(f'          <div class="clean-card rounded-3xl p-7 sm:p-8 flex flex-col justify-between {card_border}">')
        if badge_html:
            html.append(f'            {badge_html}')
        html.append('            <div>')
        html.append('              <div class="flex items-center justify-between gap-2 mb-2">')
        html.append(f'                <span class="text-xs font-black uppercase tracking-wider text-blue-600">{t_name}</span>')
        html.append(f'                <span class="text-[11px] font-bold text-slate-500 bg-slate-100 px-2.5 py-0.5 rounded-full">{t_delivery}</span>')
        html.append('              </div>')
        html.append(f'              <h4 class="text-lg font-black text-slate-900 font-heading mb-1">{t_tag}</h4>')
        html.append(f'              <p class="text-xs text-slate-500 mb-6 leading-relaxed">{t_desc}</p>')
        html.append('              ')
        html.append('              <!-- Dynamic Price Display -->')
        html.append('              <div class="mb-6 pb-6 border-b border-slate-100">')
        html.append('                <div class="flex items-baseline gap-1.5">')
        html.append(f'                  <span class="dynamic-price text-3xl sm:text-4xl font-black text-slate-900 font-heading tracking-tight" data-pkr="{rates["pkr"]}" data-usd="{rates["usd"]}" data-gbp="{rates["gbp"]}" data-eur="{rates["eur"]}">{rates["pkr"]}</span>')
        html.append(f'                  <span class="text-xs font-bold text-slate-500">{period_text}</span>')
        html.append('                </div>')
        html.append('                <span class="text-[11px] text-slate-400 block mt-1">Direct Founder Oversight &bull; Full Source Access</span>')
        html.append('              </div>')
        html.append('              ')
        html.append('              <!-- Features Checklist -->')
        html.append('              <ul class="space-y-3 mb-8 text-xs sm:text-[13px] text-slate-700">')
        for feat in t_features:
            feat_clean = feat.replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")
            html.append(f'                <li class="flex items-start gap-2.5">')
            html.append('                  <i class="fa-solid fa-circle-check text-blue-600 mt-0.5 shrink-0 text-xs sm:text-sm"></i>')
            html.append(f'                  <span class="leading-snug">{feat_clean}</span>')
            html.append('                </li>')
        html.append('              </ul>')
        html.append('            </div>')
        html.append('            ')
        html.append('            <!-- Action CTAs -->')
        html.append('            <div class="pt-4 border-t border-slate-100 flex flex-col gap-2">')
        html.append(f'              <a href="{wa_link}" target="_blank" class="w-full py-3.5 px-4 rounded-xl font-black text-xs sm:text-sm transition flex items-center justify-center gap-2 {btn_cls}">')
        html.append(f'                <i class="fa-brands fa-whatsapp text-base {wa_icon_color}"></i>')
        html.append(f'                <span>Get Started via WhatsApp</span>')
        html.append('              </a>')
        html.append(f'              <a href="services/{s_info["slug"]}#pricing" class="w-full py-2 px-3 text-center text-xs font-bold text-slate-500 hover:text-blue-600 transition flex items-center justify-center gap-1">')
        html.append('                <span>View Full Service Scope</span>')
        html.append('                <i class="fa-solid fa-chevron-right text-[10px]"></i>')
        html.append('              </a>')
        html.append('            </div>')
        html.append('          </div>')
    
    html.append('        </div>')
    html.append('      </div>')
    html.append('')

html.append('    </div>')
html.append('  </div>')
html.append('</section>')

generated_html = "\n".join(html)
print(f"Generated pricing section HTML length: {len(generated_html)} chars")
with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\generated_pricing_section.html", "w", encoding="utf-8") as f:
    f.write(generated_html)
print("Saved to generated_pricing_section.html")
