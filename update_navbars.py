import re, os

BASE_DIR = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website"

INDEX_FILE = os.path.join(BASE_DIR, "index.html")
PRICING_FILE = os.path.join(BASE_DIR, "pricing.html")

# 1. Update index.html Header & Nav
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Desktop Nav in index.html
old_nav_pattern = r'<nav class="hidden lg:flex items-center justify-center gap-0\.5 xl:gap-1\.5 mx-auto min-w-0">.*?</nav>'

new_nav_index = """<nav class="hidden lg:flex items-center justify-center gap-0.5 xl:gap-1.5 mx-auto min-w-0">
          <!-- Development Link & Dropdown -->
          <div class="relative group">
            <a href="development.html" class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-code text-blue-600"></i>
              <span>Development</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>Web &amp; App Dev (01–08)</span>
                <span class="text-blue-600 font-bold">8 Services</span>
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
              <div class="px-3 pt-2 mt-1 border-t border-slate-100">
                <a href="development.html" class="w-full py-1.5 px-3 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 text-[11px] font-black text-center flex items-center justify-center gap-1 transition">
                  <span>Explore Division Page</span> &rarr;
                </a>
              </div>
            </div>
          </div>

          <!-- Marketing Link & Dropdown -->
          <div class="relative group">
            <a href="marketing.html" class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-chart-line text-indigo-600"></i>
              <span>Marketing</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>Marketing &amp; Growth (09–16)</span>
                <span class="text-indigo-600 font-bold">8 Services</span>
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
              <div class="px-3 pt-2 mt-1 border-t border-slate-100">
                <a href="marketing.html" class="w-full py-1.5 px-3 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-[11px] font-black text-center flex items-center justify-center gap-1 transition">
                  <span>Explore Division Page</span> &rarr;
                </a>
              </div>
            </div>
          </div>

          <!-- Automation Link & Dropdown -->
          <div class="relative group">
            <a href="automation.html" class="nav-link-item flex items-center gap-1">
              <i class="fa-solid fa-gears text-amber-600"></i>
              <span>Automation</span>
              <i class="fa-solid fa-chevron-down text-[8px] text-slate-400 group-hover:rotate-180 transition-transform"></i>
            </a>
            <div class="absolute left-0 mt-1 w-64 bg-white border border-slate-200/90 rounded-2xl shadow-xl py-2 hidden group-hover:block z-50">
              <div class="px-4 py-1.5 text-[10px] font-black uppercase tracking-wider text-slate-400 border-b border-slate-100 flex items-center justify-between">
                <span>Data &amp; CRM (17–24)</span>
                <span class="text-amber-600 font-bold">8 Services</span>
              </div>
              <a href="services/legal-data-entry-data-analysis.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-scale-balanced text-amber-600 w-4"></i> Legal Data Entry
              </a>
              <a href="services/gohighlevel-migration-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-arrows-rotate text-amber-600 w-4"></i> GoHighLevel Automation
              </a>
              <a href="services/zoho-setup-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-cloud text-amber-600 w-4"></i> Zoho Setup &amp; Sync
              </a>
              <a href="services/crm-data-management-automation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-database text-amber-600 w-4"></i> CRM Data Management
              </a>
              <a href="services/lead-generation.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-bullseye text-amber-600 w-4"></i> Lead Generation
              </a>
              <a href="services/web-research.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-globe text-amber-600 w-4"></i> Web Research
              </a>
              <a href="services/excel-cleaning-formatting.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-file-excel text-amber-600 w-4"></i> Excel Cleanup
              </a>
              <a href="services/social-media-data-collection.html" class="flex items-center gap-2.5 px-4 py-2 text-xs font-bold text-slate-700 hover:bg-blue-50 hover:text-blue-600 transition">
                <i class="fa-solid fa-users text-amber-600 w-4"></i> Social Data Collection
              </a>
              <div class="px-3 pt-2 mt-1 border-t border-slate-100">
                <a href="automation.html" class="w-full py-1.5 px-3 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-700 text-[11px] font-black text-center flex items-center justify-center gap-1 transition">
                  <span>Explore Division Page</span> &rarr;
                </a>
              </div>
            </div>
          </div>

          <!-- Pricing Link -->
          <a href="pricing.html" class="nav-link-item">
            <i class="fa-solid fa-tags text-emerald-600"></i>
            <span>Pricing</span>
          </a>

          <!-- Case Studies Link -->
          <a href="#results" class="nav-link-item">
            <i class="fa-solid fa-trophy text-amber-500"></i>
            <span>Case Studies</span>
          </a>

          <!-- About Link -->
          <a href="#about" class="nav-link-item">
            <i class="fa-solid fa-circle-info text-sky-600"></i>
            <span>About</span>
          </a>

          <!-- Founder Link -->
          <a href="#founder" class="nav-link-item hidden 2xl:inline-flex">
            <i class="fa-solid fa-user-tie text-violet-600"></i>
            <span>Founder</span>
          </a>

          <!-- Reviews Link -->
          <a href="#testimonials" class="nav-link-item hidden 2xl:inline-flex">
            <i class="fa-solid fa-star text-amber-400"></i>
            <span>Reviews</span>
          </a>

          <!-- Contact Link -->
          <a href="#contact" class="nav-link-item">
            <i class="fa-solid fa-phone text-blue-500"></i>
            <span>Contact</span>
          </a>
        </nav>"""

content = re.sub(old_nav_pattern, new_nav_index, content, flags=re.DOTALL)

# Update Mobile Menu in index.html
old_mobile_menu = r'<div id="mobile-menu" class="hidden md:hidden.*?</div>\s*</div>\s*</header>'
new_mobile_menu = """<div id="mobile-menu" class="hidden md:hidden bg-white border-b border-slate-200 px-6 py-5 shadow-xl transition-all">
      <div class="flex flex-col gap-3 text-sm font-semibold text-slate-800">
        <a href="development.html" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span class="flex items-center gap-2"><i class="fa-solid fa-code text-blue-600"></i> Web &amp; App Development</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="marketing.html" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span class="flex items-center gap-2"><i class="fa-solid fa-chart-line text-indigo-600"></i> Performance Marketing</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="automation.html" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span class="flex items-center gap-2"><i class="fa-solid fa-gears text-amber-600"></i> Data, CRM &amp; Automation</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="pricing.html" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span class="flex items-center gap-2"><i class="fa-solid fa-tags text-emerald-600"></i> Pricing Plans (All 24 Services)</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#results" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span>Case Studies &amp; Results</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#about" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span>About Ranknix Online</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#founder" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span>Founder (Muhammad Abdullah)</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#testimonials" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span>Client Reviews</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#faq" class="mobile-nav-link hover:text-blue-600 py-2 border-b border-slate-100 flex items-center justify-between">
          <span>FAQs</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        <a href="#contact" class="mobile-nav-link hover:text-blue-600 py-2 flex items-center justify-between">
          <span>Contact</span>
          <i class="fa-solid fa-chevron-right text-xs text-slate-400"></i>
        </a>
        
        <!-- Mobile Currency Selection -->
        <div class="pt-2 border-t border-slate-100">
          <span class="text-xs text-slate-400 uppercase font-bold block mb-2">Change Currency:</span>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <button data-set-currency="PKR" class="p-2 rounded-lg border border-slate-200 font-bold hover:bg-blue-50">🇵🇰 PKR (₨)</button>
            <button data-set-currency="GBP" class="p-2 rounded-lg border border-slate-200 font-bold hover:bg-blue-50">🇬🇧 GBP (£)</button>
            <button data-set-currency="USD" class="p-2 rounded-lg border border-slate-200 font-bold hover:bg-blue-50">🇺🇸 USD ($)</button>
            <button data-set-currency="EUR" class="p-2 rounded-lg border border-slate-200 font-bold hover:bg-blue-50">🇪🇺 EUR (€)</button>
          </div>
        </div>

        <div class="flex flex-col gap-2.5 pt-3">
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20%F0%9F%91%8B%20I'm%20interested%20in%20your%20services." target="_blank" class="w-full py-2.5 rounded-xl bg-emerald-600 text-white font-bold text-center flex items-center justify-center gap-2 shadow-md">
            <i class="fa-brands fa-whatsapp text-lg"></i>
            <span>Chat on WhatsApp</span>
          </a>
          <button class="open-audit-modal w-full py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-center shadow-md">
            Claim Free Consultation
          </button>
        </div>
      </div>
    </div>
  </header>"""

content = re.sub(old_mobile_menu, new_mobile_menu, content, flags=re.DOTALL)

# Add 3 Specialization Divisions Gateway section on landing page (between tech marquee and results)
gateway_sec = """
  <!-- ============================================================== -->
  <!-- 4. CORE SPECIALIZATION DIVISIONS (Clean Gateway to Dedicated Pages) -->
  <!-- ============================================================== -->
  <section class="py-16 sm:py-20 bg-white relative z-10 border-b border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="text-center max-w-3xl mx-auto mb-12">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-xs font-bold mb-3 shadow-2xs">
          <i class="fa-solid fa-layer-group text-blue-600"></i>
          <span>Three Dedicated Practice Divisions</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Explore Our <span class="text-gradient-blue">Core Capabilities</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed max-w-2xl mx-auto">
          Ranknix Online operates 3 specialized engineering and marketing divisions. Click any division below or in the top navigation to view its full services, portfolio deliverables, and packages.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-7">
        
        <!-- Division 01 Card -->
        <div class="clean-card rounded-3xl p-7 sm:p-8 flex flex-col justify-between border-2 border-blue-100 hover:border-blue-500 hover:shadow-xl transition-all duration-300 group bg-gradient-to-b from-white to-blue-50/30">
          <div>
            <div class="flex items-center justify-between mb-5">
              <span class="text-xs font-black uppercase tracking-wider text-blue-600 bg-blue-50 px-3 py-1 rounded-full border border-blue-200">Division 01</span>
              <div class="w-12 h-12 rounded-2xl bg-blue-600 text-white flex items-center justify-center text-xl shadow-md group-hover:scale-110 transition-transform">
                <i class="fa-solid fa-code"></i>
              </div>
            </div>
            <h3 class="text-2xl font-black text-slate-900 font-heading mb-3 group-hover:text-blue-600 transition-colors">
              Web &amp; App Development
            </h3>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-6">
              Shopify Plus, WordPress, custom React &amp; Next.js platforms, mobile apps (Flutter &amp; React Native), and high-converting landing pages engineered for speed and conversion.
            </p>
            <div class="flex flex-wrap gap-1.5 mb-6">
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">Shopify</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">WordPress</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">React Native</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">UI/UX Figma</span>
            </div>
          </div>
          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2">
            <a href="development.html" class="w-full py-3 px-4 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-black text-xs sm:text-sm text-center transition flex items-center justify-center gap-2 shadow-md shadow-blue-500/20">
              <span>Explore Development Division (8 Services)</span>
              <i class="fa-solid fa-arrow-right text-xs"></i>
            </a>
            <a href="pricing.html?service=web-dev" class="w-full py-2 text-center text-xs font-bold text-slate-500 hover:text-blue-600 transition">
              View Dev Pricing Packages &rarr;
            </a>
          </div>
        </div>

        <!-- Division 02 Card -->
        <div class="clean-card rounded-3xl p-7 sm:p-8 flex flex-col justify-between border-2 border-indigo-100 hover:border-indigo-500 hover:shadow-xl transition-all duration-300 group bg-gradient-to-b from-white to-indigo-50/30">
          <div>
            <div class="flex items-center justify-between mb-5">
              <span class="text-xs font-black uppercase tracking-wider text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full border border-indigo-200">Division 02</span>
              <div class="w-12 h-12 rounded-2xl bg-indigo-600 text-white flex items-center justify-center text-xl shadow-md group-hover:scale-110 transition-transform">
                <i class="fa-solid fa-chart-line"></i>
              </div>
            </div>
            <h3 class="text-2xl font-black text-slate-900 font-heading mb-3 group-hover:text-indigo-600 transition-colors">
              Performance Marketing &amp; Paid Ads
            </h3>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-6">
              Data-driven Google &amp; Bing Ads, Meta Ads (Facebook &amp; Instagram), TikTok campaigns, technical SEO, and Conversion Rate Optimization with direct founder oversight.
            </p>
            <div class="flex flex-wrap gap-1.5 mb-6">
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">Google Ads</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">Meta CAPI</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">SEO Rank</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">GA4 Analytics</span>
            </div>
          </div>
          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2">
            <a href="marketing.html" class="w-full py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-black text-xs sm:text-sm text-center transition flex items-center justify-center gap-2 shadow-md shadow-indigo-500/20">
              <span>Explore Marketing Division (8 Services)</span>
              <i class="fa-solid fa-arrow-right text-xs"></i>
            </a>
            <a href="pricing.html?service=google-ads" class="w-full py-2 text-center text-xs font-bold text-slate-500 hover:text-indigo-600 transition">
              View Marketing Pricing Packages &rarr;
            </a>
          </div>
        </div>

        <!-- Division 03 Card -->
        <div class="clean-card rounded-3xl p-7 sm:p-8 flex flex-col justify-between border-2 border-amber-100 hover:border-amber-500 hover:shadow-xl transition-all duration-300 group bg-gradient-to-b from-white to-amber-50/30">
          <div>
            <div class="flex items-center justify-between mb-5">
              <span class="text-xs font-black uppercase tracking-wider text-amber-700 bg-amber-50 px-3 py-1 rounded-full border border-amber-200">Division 03</span>
              <div class="w-12 h-12 rounded-2xl bg-amber-600 text-white flex items-center justify-center text-xl shadow-md group-hover:scale-110 transition-transform">
                <i class="fa-solid fa-gears"></i>
              </div>
            </div>
            <h3 class="text-2xl font-black text-slate-900 font-heading mb-3 group-hover:text-amber-600 transition-colors">
              CRM, Data &amp; Automation
            </h3>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-6">
              Zoho CRM deployment, GoHighLevel agency migrations, automated sales workflows, verified B2B lead generation lists, and custom Excel cleaning pipelines. Zero manual bottlenecks.
            </p>
            <div class="flex flex-wrap gap-1.5 mb-6">
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">Zoho CRM</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">GoHighLevel</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">B2B Leads</span>
              <span class="px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 text-[11px] font-bold">Zapier &amp; Make</span>
            </div>
          </div>
          <div class="pt-4 border-t border-slate-100 flex flex-col gap-2">
            <a href="automation.html" class="w-full py-3 px-4 rounded-xl bg-amber-600 hover:bg-amber-700 text-white font-black text-xs sm:text-sm text-center transition flex items-center justify-center gap-2 shadow-md shadow-amber-500/20">
              <span>Explore Automation Division (8 Services)</span>
              <i class="fa-solid fa-arrow-right text-xs"></i>
            </a>
            <a href="pricing.html?service=zoho" class="w-full py-2 text-center text-xs font-bold text-slate-500 hover:text-amber-600 transition">
              View Automation Pricing Packages &rarr;
            </a>
          </div>
        </div>

      </div>

    </div>
  </section>
"""

# Replace the empty services division placeholder in index.html with the gateway
old_serv_placeholder = r'<!-- ============================================================== -->\s*<!-- 4\. SERVICES DIVISION 1: WEB & APP DEVELOPMENT.*?<!-- 5\. UNIFIED SERVICES SECTION.*?(?=<section id="results")'
if re.search(old_serv_placeholder, content, re.DOTALL):
    content = re.sub(old_serv_placeholder, gateway_sec, content, flags=re.DOTALL)
else:
    # If not found, insert right before <section id="results"
    content = content.replace('<section id="results"', gateway_sec + '\n  <section id="results"')

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated index.html ({len(content)} bytes)")

# 2. Update pricing.html Header & Nav
with open(PRICING_FILE, "r", encoding="utf-8") as f:
    p_content = f.read()

# Update <button ...> to <a href="development.html" ...> etc in pricing.html
p_content = re.sub(
    r'<button class="nav-link-item flex items-center gap-1">\s*<i class="fa-solid fa-code text-blue-600"></i>\s*<span>Development</span>',
    r'<a href="development.html" class="nav-link-item flex items-center gap-1">\n              <i class="fa-solid fa-code text-blue-600"></i>\n              <span>Development</span>',
    p_content
)
p_content = re.sub(
    r'<button class="nav-link-item flex items-center gap-1">\s*<i class="fa-solid fa-chart-line text-indigo-600"></i>\s*<span>Marketing</span>',
    r'<a href="marketing.html" class="nav-link-item flex items-center gap-1">\n              <i class="fa-solid fa-chart-line text-indigo-600"></i>\n              <span>Marketing</span>',
    p_content
)
p_content = re.sub(
    r'<button class="nav-link-item flex items-center gap-1">\s*<i class="fa-solid fa-gears text-amber-600"></i>\s*<span>Automation</span>',
    r'<a href="automation.html" class="nav-link-item flex items-center gap-1">\n              <i class="fa-solid fa-gears text-amber-600"></i>\n              <span>Automation</span>',
    p_content
)

# Update mobile menu in pricing.html
p_content = re.sub(
    r'href="#dev-services"',
    r'href="development.html"',
    p_content
)
p_content = re.sub(
    r'href="#marketing-services"',
    r'href="marketing.html"',
    p_content
)
p_content = re.sub(
    r'href="#automation-services"',
    r'href="automation.html"',
    p_content
)

with open(PRICING_FILE, "w", encoding="utf-8") as f:
    f.write(p_content)

print(f"Successfully updated pricing.html ({len(p_content)} bytes)")
