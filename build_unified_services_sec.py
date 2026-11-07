import json, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')

from services_config import SERVICES_INFO

# Load card details
from services_data_part1 import SERVICES_DATA as p1
from services_data_part2 import SERVICES_DATA_PART2 as p2
from services_data_part3 import SERVICES_DATA_PART3 as p3

ALL_SERVICES = p1 + p2 + p3

def render_unified_services_section():
    dev_cards = ALL_SERVICES[:8]
    mkt_cards = ALL_SERVICES[8:16]
    auto_cards = ALL_SERVICES[16:24]

    def render_card(s, num):
        slug = s['slug'] if s['slug'].endswith('.html') else s['slug'] + '.html'
        pkg_key = s['slug'].replace('.html', '')
        # Map pkg_key to track key
        from build_all_service_pages import SLUG_TO_PKG_KEY
        track_key = SLUG_TO_PKG_KEY.get(slug, 'web-dev')

        name = s['name']
        icon = s['icon']
        desc = s['description'][:140] + "..." if len(s['description']) > 140 else s['description']
        desc = desc.replace("Rafirit Station", "Ranknix Online").replace("Rafirit", "Ranknix Online")

        tags_html = ""
        if 'platforms' in s:
            tags_html = "".join([f'<span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-600 text-[10px] font-bold">{p}</span>' for p in s['platforms'][:3]])

        wa_url = f"https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'm%20inquiring%20about%20{urllib.parse.quote(name)}"

        return f"""
        <div class="clean-card rounded-3xl p-6 sm:p-7 flex flex-col justify-between border border-slate-200/90 shadow-2xs hover:shadow-xl hover:border-blue-400 transition-all duration-300 group">
          <div>
            <div class="flex items-center justify-between mb-4">
              <span class="text-xs font-mono font-black text-slate-300 group-hover:text-blue-500 transition-colors">#{num:02d}</span>
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
            <button onclick="jumpToServicePricing('{track_key}')" class="flex-1 py-2 px-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 text-xs font-bold text-center transition shadow-2xs">
              View Pricing
            </button>
            <a href="{wa_url}" target="_blank" class="p-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-600 transition flex items-center justify-center shrink-0" title="Chat on WhatsApp">
              <i class="fa-brands fa-whatsapp text-base"></i>
            </a>
          </div>
        </div>
        """

    dev_cards_html = "\n".join([render_card(s, i) for i, s in enumerate(dev_cards, 1)])
    mkt_cards_html = "\n".join([render_card(s, i) for i, s in enumerate(mkt_cards, 9)])
    auto_cards_html = "\n".join([render_card(s, i) for i, s in enumerate(auto_cards, 17)])

    html = f"""
  <!-- 5. UNIFIED SERVICES SECTION (ONE COMPACT INTERACTIVE CONTAINER FOR ALL 24 SERVICES) -->
  <section id="services" class="py-20 sm:py-24 bg-white relative z-10 border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto mb-10" data-aos="fade-up">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold mb-3 shadow-2xs">
          <i class="fa-solid fa-grid-2 text-blue-600"></i>
          <span>24 Specialized Agency Capabilities</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Worldwide Full-Service <span class="text-gradient-blue">Digital Agency</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
          Switch between divisions below to explore our core specializations. Every service includes direct oversight by Founder Muhammad Abdullah and guaranteed delivery SLAs.
        </p>

        <!-- Division Switcher Tabs -->
        <div class="flex justify-center mt-8">
          <div class="inline-flex flex-wrap justify-center p-1.5 rounded-2xl bg-slate-100 border border-slate-200 shadow-inner gap-1.5 max-w-full">
            <button id="cat-tab-dev" onclick="switchServiceCategory('dev')" class="cat-tab-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold bg-blue-600 text-white shadow-md transition flex items-center gap-2">
              <i class="fa-solid fa-code"></i>
              <span>Web &amp; App Development (01–08)</span>
            </button>
            <button id="cat-tab-mkt" onclick="switchServiceCategory('mkt')" class="cat-tab-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold text-slate-700 hover:text-slate-900 hover:bg-white/60 transition flex items-center gap-2">
              <i class="fa-solid fa-chart-line"></i>
              <span>Performance Marketing &amp; Growth (09–16)</span>
            </button>
            <button id="cat-tab-auto" onclick="switchServiceCategory('auto')" class="cat-tab-btn px-4 sm:px-6 py-2.5 rounded-xl text-xs sm:text-sm font-extrabold text-slate-700 hover:text-slate-900 hover:bg-white/60 transition flex items-center gap-2">
              <i class="fa-solid fa-cubes-stacked"></i>
              <span>CRM &amp; Automation (17–24)</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Panel 1: Web & App Dev (01-08) -->
      <div id="cat-panel-dev" class="cat-panel grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {dev_cards_html}
      </div>

      <!-- Panel 2: Marketing & Growth (09-16) -->
      <div id="cat-panel-mkt" class="cat-panel hidden grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {mkt_cards_html}
      </div>

      <!-- Panel 3: Automation & CRM (17-24) -->
      <div id="cat-panel-auto" class="cat-panel hidden grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {auto_cards_html}
      </div>

    </div>
  </section>
    """
    return html

print("render_unified_services_section ready!")
