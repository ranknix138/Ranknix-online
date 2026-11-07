import json, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')

from services_config import SERVICES_INFO, format_currency

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "r", encoding="utf-8") as f:
    packages_data = json.load(f)

def render_pricing_track_section():
    # Build the pills list (duplicated for infinite loop)
    def render_pill(sk, s_info):
        active_cls = "active-track-pill border-blue-600 bg-blue-50/80 text-blue-700 shadow-xs" if sk == "web-dev" else "border-slate-200/90 bg-white text-slate-700 hover:border-blue-400 hover:bg-slate-50 shadow-2xs"
        return f"""
        <button id="track-pill-{sk}" onclick="selectTrackService('{sk}')" class="track-pill flex-shrink-0 flex items-center gap-2 px-4 py-2.5 rounded-2xl border text-xs font-bold transition-all cursor-pointer {active_cls}">
          <i class="{s_info['icon']} text-xs text-blue-600"></i>
          <span>{s_info['name']}</span>
        </button>
        """

    pills_single = "".join([render_pill(sk, s_info) for sk, s_info in SERVICES_INFO.items()])
    # 2 copies for infinite smooth marquee
    marquee_pills_html = pills_single * 2

    # Render 24 panels
    panels_html = []
    for idx, (sk, s_info) in enumerate(SERVICES_INFO.items()):
        pkg = packages_data.get(sk, {})
        is_active = (sk == "web-dev")
        hidden_cls = "" if is_active else "hidden"
        desc_clean = pkg.get("desc", "").replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")

        panel = f"""
        <!-- PANEL: {sk} -->
        <div id="track-panel-{sk}" class="track-pricing-panel {hidden_cls} transition-all duration-300">
          
          <!-- Selected Service Header -->
          <div class="clean-card rounded-2xl p-6 sm:p-7 mb-8 border border-slate-200/90 shadow-2xs flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-2xl bg-blue-50 border border-blue-200 text-blue-600 flex items-center justify-center text-xl shrink-0">
                <i class="{s_info['icon']}"></i>
              </div>
              <div>
                <div class="flex items-center gap-2 mb-1">
                  <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-800 text-[10px] font-extrabold uppercase tracking-wider">{s_info['division_label']}</span>
                  <span class="text-xs text-slate-400 font-bold">Service #{idx+1:02d} of 24</span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-slate-900 font-heading">{s_info['name']} Packages</h3>
                <p class="text-slate-600 text-xs sm:text-sm max-w-2xl mt-1 leading-relaxed">{desc_clean}</p>
              </div>
            </div>
            <div class="shrink-0 flex items-center gap-2.5">
              <a href="services/{s_info['slug']}" class="px-4 py-2 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 hover:text-blue-600 text-xs font-bold transition flex items-center gap-1.5 shadow-2xs">
                <span>View Full Scope</span>
                <i class="fa-solid fa-arrow-right text-[10px]"></i>
              </a>
            </div>
          </div>

          <!-- 3-Tier Pricing Grid -->
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        """

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

            panel += f"""
            <!-- Tier {t_idx+1}: {t_name} -->
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
            </div>
            """

        panel += """
          </div>
        </div>
        """
        panels_html.append(panel)

    all_panels = "\n".join(panels_html)

    html = f"""
  <!-- 10. PRICING SECTION (AUTO-SCROLLING 24-SERVICE MARQUEE + DYNAMIC 3-TIER PACKAGES) -->
  <section id="pricing" class="py-24 bg-slate-50/70 relative z-10 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-8" data-aos="fade-up">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold mb-3 shadow-2xs">
          <i class="fa-solid fa-tags text-blue-600"></i>
          <span>Transparent Pricing &bull; Fixed Turnaround Times</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Growth Packages Tailored <span class="text-gradient-blue">For Your Scale</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-6">
          Click any service in the moving track below to immediately see its transparent rates. All prices switch dynamically to your local currency.
        </p>

        <!-- Dynamic Currency Selector Pills -->
        <div class="inline-flex flex-wrap items-center justify-center gap-2 px-4 py-2 rounded-2xl bg-white border border-slate-200/90 shadow-2xs text-xs">
          <span class="text-slate-500 font-semibold flex items-center gap-1.5">
            <i class="fa-solid fa-globe text-blue-600"></i> Region Currency:
          </span>
          <div class="inline-flex gap-1">
            <button onclick="changeGlobalCurrency('PKR')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="PKR">🇵🇰 ₨ PKR</button>
            <button onclick="changeGlobalCurrency('GBP')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="GBP">🇬🇧 £ GBP</button>
            <button onclick="changeGlobalCurrency('USD')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="USD">🇺🇸 $ USD</button>
            <button onclick="changeGlobalCurrency('EUR')" class="curr-pill px-2.5 py-1 rounded-lg font-bold text-slate-700 hover:bg-slate-100 transition" data-curr-pill="EUR">🇪🇺 € EUR</button>
          </div>
        </div>
      </div>

      <!-- AUTO-SCROLLING 24-SERVICE MARQUEE TRACK (SINGLE ROW, SLOW & SMOOTH) -->
      <div class="relative mb-8" data-aos="fade-up">
        <div class="flex items-center justify-between mb-2 px-2">
          <span class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
            <i class="fa-solid fa-arrows-left-right text-blue-600"></i> 24 Services Track (Hover to Pause &bull; Click to View Packages)
          </span>
          <div class="flex items-center gap-1.5 text-xs">
            <button onclick="scrollTrackPrev()" class="p-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-blue-50 hover:text-blue-600 transition shadow-2xs" title="Previous Service">
              <i class="fa-solid fa-chevron-left text-xs"></i>
            </button>
            <button onclick="scrollTrackNext()" class="p-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-blue-50 hover:text-blue-600 transition shadow-2xs" title="Next Service">
              <i class="fa-solid fa-chevron-right text-xs"></i>
            </button>
          </div>
        </div>

        <div id="pricing-marquee-container" class="marquee-wrapper relative w-full overflow-hidden py-3 bg-white/70 backdrop-blur-sm rounded-2xl border border-slate-200/90 shadow-2xs">
          <div id="pricing-track" class="marquee-content flex gap-3 hover:[animation-play-state:paused]" style="animation: scrollInfinite 55s linear infinite; width: max-content;">
            {marquee_pills_html}
          </div>
        </div>
      </div>

      <!-- THE 24 SERVICE PANELS -->
      <div id="track-panels-container">
        {all_panels}
      </div>

    </div>
  </section>
    """
    return html

print("render_pricing_track_section ready!")
