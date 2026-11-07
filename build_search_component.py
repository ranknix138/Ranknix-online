import sys
sys.stdout.reconfigure(encoding='utf-8')

def render_hero_search_bar():
    return """
        <!-- HERO INSTANT 24-SERVICE LIVE SEARCH BAR -->
        <div class="relative max-w-xl mx-auto lg:mx-0 mt-8 mb-6 z-30" data-aos="fade-up" data-aos-delay="250">
          <div class="relative flex items-center">
            <i class="fa-solid fa-magnifying-glass absolute left-4 text-slate-400 text-sm"></i>
            <input type="text" id="hero-search-input" oninput="handleLiveServiceSearch(this.value)" placeholder="Search any service (e.g. Shopify, Google Ads, SEO, Mobile Apps, Video, Zoho...)" class="w-full pl-11 pr-24 py-3.5 rounded-2xl bg-white border-2 border-slate-200/90 shadow-md text-xs sm:text-sm font-semibold text-slate-800 placeholder-slate-400 focus:outline-none focus:border-blue-600 focus:ring-4 focus:ring-blue-100 transition" autocomplete="off">
            <button onclick="submitSearchFirstMatch()" class="absolute right-2 px-3.5 py-1.5 rounded-xl bg-blue-600 text-white text-xs font-bold hover:bg-blue-700 transition shadow-xs">
              Search
            </button>
          </div>

          <!-- Live Search Results Dropdown -->
          <div id="hero-search-results" class="absolute left-0 right-0 mt-2 bg-white rounded-2xl shadow-2xl border border-slate-200/90 hidden z-50 overflow-hidden max-h-80 overflow-y-auto">
            <!-- Populated dynamically via JS -->
          </div>

          <!-- Quick Jump Chips -->
          <div class="flex flex-wrap items-center gap-1.5 mt-2.5 text-[11px] text-slate-500">
            <span class="font-bold text-slate-400 mr-1">Popular:</span>
            <button onclick="quickSelectService('web-dev')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">Web Dev</button>
            <button onclick="quickSelectService('google-ads')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">Google Ads</button>
            <button onclick="quickSelectService('meta-ads')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">Meta Ads</button>
            <button onclick="quickSelectService('ecommerce')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">Shopify</button>
            <button onclick="quickSelectService('seo')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">SEO</button>
            <button onclick="quickSelectService('zoho')" class="px-2.5 py-0.5 rounded-md bg-white border border-slate-200 hover:border-blue-300 hover:bg-blue-50 hover:text-blue-600 font-semibold transition">Zoho CRM</button>
          </div>
        </div>
    """

print("render_hero_search_bar ready!")
