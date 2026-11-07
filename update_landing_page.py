import re, json, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

from services_config import SERVICES_INFO
from reviews_marquee import render_reviews_marquee
from build_pricing_track import render_pricing_track_section
from build_unified_services_sec import render_unified_services_section
from build_search_component import render_hero_search_bar

idx_path = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    html = f.read()

print("Original index.html length:", len(html))

# -------------------------------------------------------------
# 1. UPDATE NAVBAR (Add Dropdowns for Development, Marketing, Automation)
# -------------------------------------------------------------
old_nav_pattern = r'<nav class="hidden lg:flex items-center justify-center gap-0\.5 xl:gap-1\.5 mx-auto min-w-0">.*?</nav>'
new_nav = """<nav class="hidden lg:flex items-center justify-center gap-0.5 xl:gap-1.5 mx-auto min-w-0">
          
          <!-- Development Dropdown -->
          <div class="relative group">
            <button onclick="switchServiceCategory('dev'); document.getElementById('services').scrollIntoView({behavior:'smooth'});" class="nav-link-item flex items-center gap-1">
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
            <button onclick="switchServiceCategory('mkt'); document.getElementById('services').scrollIntoView({behavior:'smooth'});" class="nav-link-item flex items-center gap-1">
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
            <button onclick="switchServiceCategory('auto'); document.getElementById('services').scrollIntoView({behavior:'smooth'});" class="nav-link-item flex items-center gap-1">
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

          <a href="#results" class="nav-link-item">
            <i class="fa-solid fa-trophy text-amber-500"></i>
            <span>Case Studies</span>
          </a>
          <a href="#about" class="nav-link-item">
            <i class="fa-solid fa-circle-info text-sky-600"></i>
            <span>About</span>
          </a>
          <a href="#pricing" class="nav-link-item">
            <i class="fa-solid fa-tags text-emerald-600"></i>
            <span>Pricing</span>
          </a>
          <a href="#testimonials" class="nav-link-item">
            <i class="fa-solid fa-star text-amber-400"></i>
            <span>Reviews</span>
          </a>
          <a href="#contact" class="nav-link-item">
            <i class="fa-solid fa-phone text-blue-500"></i>
            <span>Contact</span>
          </a>
        </nav>"""

if re.search(old_nav_pattern, html, re.DOTALL):
    html = re.sub(old_nav_pattern, new_nav, html, count=1)
    print("Updated Navbar with dropdowns successfully!")
else:
    print("WARNING: Could not match old navbar pattern")

# -------------------------------------------------------------
# 2. INSERT LIVE SEARCH BAR INTO HERO (below the CTAs)
# -------------------------------------------------------------
search_bar_html = render_hero_search_bar()
# Find CTAs in hero
cta_marker = '<!-- CTAs (Main Conversion Actions) -->'
if cta_marker in html and "hero-search-input" not in html:
    # Insert right after CTAs block closing div
    # Find the end of the CTA flex container
    cta_pos = html.find(cta_marker)
    closing_div_pos = html.find('</div>', cta_pos)
    # Move past the closing </div>
    next_pos = html.find('</div>', closing_div_pos + 6)
    html = html[:next_pos+6] + "\n" + search_bar_html + "\n" + html[next_pos+6:]
    print("Inserted Hero Search Bar successfully!")
else:
    print("Search bar already present or CTA marker not found")

# -------------------------------------------------------------
# 3. REPLACE 3 STACKED SERVICE SECTIONS WITH UNIFIED #services
# -------------------------------------------------------------
services_sec_html = render_unified_services_section()
pattern_3_sections = r'<section id="dev-services".*?<section id="results"'
m3 = re.search(pattern_3_sections, html, re.DOTALL)
if m3:
    html = html[:m3.start()] + services_sec_html + "\n\n  <section id=\"results\"" + html[m3.end():]
    print("Replaced 3 stacked service sections with unified #services!")
else:
    print("WARNING: Could not match 3 stacked sections")

# -------------------------------------------------------------
# 4. REMOVE "LIVE IN 60+ COUNTRIES" BADGES FROM #about
# -------------------------------------------------------------
about_pattern = r'<section id="about".*?</section>'
m_about = re.search(about_pattern, html, re.DOTALL)
if m_about:
    new_about = """<section id="about" class="py-20 bg-white relative overflow-hidden border-t border-slate-200/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      
      <div class="max-w-4xl mx-auto text-center" data-aos="fade-up">
        <span class="inline-block px-3.5 py-1 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold uppercase tracking-wider mb-3">
          About Ranknix Online
        </span>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight leading-tight mb-6">
          The World's Most Complete <br><span class="text-gradient-blue">Digital Agency</span>
        </h2>
        
        <p class="text-slate-600 text-base sm:text-lg leading-relaxed mb-6">
          Founded in Pakistan and serving ambitious clients worldwide, <strong>Ranknix Online</strong> is a global full-service digital agency trusted by businesses across <strong>60+ countries</strong>. We combine world-class engineering, high-converting design, and revenue-focused performance marketing under one unified roof.
        </p>
        <p class="text-slate-500 text-sm sm:text-base leading-relaxed mb-10 max-w-3xl mx-auto">
          From startups in the US, UK, UAE, and Australia to e-commerce brands in Europe and Asia — we deliver results that matter in every timezone. Direct access to Founder Muhammad Abdullah, zero generic templates, guaranteed code ownership, and transparent growth.
        </p>

        <!-- 4 Pillars Grid -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10 text-left">
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 shadow-2xs">
            <span class="text-xs font-black text-blue-600 uppercase font-mono block mb-1">01 / Oversight</span>
            <h4 class="text-sm font-bold text-slate-900 mb-1">Direct Founder Access</h4>
            <p class="text-[11px] text-slate-500 leading-snug">Personal supervision by Muhammad Abdullah on every project.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 shadow-2xs">
            <span class="text-xs font-black text-blue-600 uppercase font-mono block mb-1">02 / Ownership</span>
            <h4 class="text-sm font-bold text-slate-900 mb-1">100% Asset Rights</h4>
            <p class="text-[11px] text-slate-500 leading-snug">Full source code, hosting, and ad accounts always remain yours.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 shadow-2xs">
            <span class="text-xs font-black text-blue-600 uppercase font-mono block mb-1">03 / Global Scale</span>
            <h4 class="text-sm font-bold text-slate-900 mb-1">Every Timezone</h4>
            <p class="text-[11px] text-slate-500 leading-snug">Active support across UK, USA, UAE, and European business hours.</p>
          </div>
          <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200/80 shadow-2xs">
            <span class="text-xs font-black text-blue-600 uppercase font-mono block mb-1">04 / Clarity</span>
            <h4 class="text-sm font-bold text-slate-900 mb-1">Fixed Multi-Currency</h4>
            <p class="text-[11px] text-slate-500 leading-snug">Zero surprise invoices. Transparent PKR, GBP, USD, and EUR rates.</p>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-wrap items-center justify-center gap-3.5">
          <a href="https://wa.me/923088163940?text=Hi%20Ranknix%20Online!%20I'd%20like%20to%20work%20with%20you." target="_blank" class="px-6 py-3.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-black text-sm shadow-md shadow-blue-500/25 transition flex items-center gap-2">
            <i class="fa-solid fa-rocket"></i>
            <span>Work With Us</span>
          </a>
          <a href="#services" class="px-6 py-3.5 rounded-xl bg-white hover:bg-slate-50 border border-slate-200 text-slate-800 font-bold text-sm shadow-2xs transition flex items-center gap-2">
            <i class="fa-solid fa-grid-2 text-blue-600"></i>
            <span>Explore All 24 Services</span>
          </a>
        </div>
      </div>

    </div>
  </section>"""
    html = html[:m_about.start()] + new_about + html[m_about.end():]
    print("Replaced #about with clean, compact version (removed 60+ countries badges grid)!")

# -------------------------------------------------------------
# 5. REPLACE #testimonials WITH MARQUEE (18 VERIFIED REVIEWS)
# -------------------------------------------------------------
testimonials_pattern = r'<section id="testimonials".*?</section>'
m_test = re.search(testimonials_pattern, html, re.DOTALL)
if m_test:
    html = html[:m_test.start()] + render_reviews_marquee() + html[m_test.end():]
    print("Replaced #testimonials with 18-review auto-scrolling marquee!")
else:
    print("WARNING: Could not match #testimonials")

# -------------------------------------------------------------
# 6. REPLACE #pricing WITH MARQUEE TRACK VERSION
# -------------------------------------------------------------
pricing_pattern = r'<section id="pricing".*?</section>'
m_price = re.search(pricing_pattern, html, re.DOTALL)
if m_price:
    html = html[:m_price.start()] + render_pricing_track_section() + html[m_price.end():]
    print("Replaced #pricing with auto-scrolling 24-service marquee track!")
else:
    print("WARNING: Could not match #pricing")

# -------------------------------------------------------------
# 7. ADD COMPREHENSIVE JAVASCRIPT CONTROLLERS
# -------------------------------------------------------------
js_controllers = """
<!-- JAVASCRIPT CONTROLLERS FOR LIVE SEARCH, UNIFIED SERVICES & PRICING TRACK -->
<script>
// 1. DATA DICTIONARY FOR LIVE SEARCH
const ALL_SERVICES_SEARCH_DATA = [
  { key: 'web-dev', name: 'Web Development', cat: 'Development', url: 'services/web-development.html', icon: 'fa-solid fa-code', keywords: 'wordpress shopify wix react nextjs frontend website speed core vitals' },
  { key: 'app-dev', name: 'App Development', cat: 'Development', url: 'services/app-development.html', icon: 'fa-solid fa-mobile-screen-button', keywords: 'ios android react native flutter mobile app firebase' },
  { key: 'ui-ux', name: 'UI/UX Design', cat: 'Development', url: 'services/ui-ux-design.html', icon: 'fa-solid fa-pen-nib', keywords: 'figma wireframe prototype user interface user experience' },
  { key: 'graphic', name: 'Graphic Design', cat: 'Development', url: 'services/graphic-design.html', icon: 'fa-solid fa-palette', keywords: 'branding logo social banners brand guidelines packaging' },
  { key: 'ecommerce', name: 'E-Commerce Solutions', cat: 'Development', url: 'services/e-commerce-solutions.html', icon: 'fa-solid fa-bag-shopping', keywords: 'shopify store woocommerce checkout upsell payment gateway catalog' },
  { key: 'video', name: 'Video Editing', cat: 'Development', url: 'services/video-editing.html', icon: 'fa-solid fa-video', keywords: 'tiktok reels premiere capcut ugc video ads sound design motion' },
  { key: 'content', name: 'Content Writing', cat: 'Development', url: 'services/content-writing.html', icon: 'fa-solid fa-feather', keywords: 'seo articles copywriting website content blogs technical writing' },
  { key: 'landing', name: 'Landing Page Design', cat: 'Development', url: 'services/landing-page-design.html', icon: 'fa-solid fa-rocket', keywords: 'high converting figma elementor clickfunnels lead gen page sales page' },
  { key: 'digital-mkt', name: 'Digital Marketing', cat: 'Marketing', url: 'services/digital-marketing.html', icon: 'fa-solid fa-chart-line', keywords: 'full funnel growth strategy multi channel roas acquisition' },
  { key: 'seo', name: 'SEO Services', cat: 'Marketing', url: 'services/seo-services.html', icon: 'fa-solid fa-magnifying-glass-chart', keywords: 'search engine optimization google rank backlinks onpage technical schema' },
  { key: 'google-ads', name: 'Google Ads & Bing Ads', cat: 'Marketing', url: 'services/google-ads-bing-ads.html', icon: 'fa-brands fa-google', keywords: 'ppc search ads shopping pmax performance max display cpa roas' },
  { key: 'meta-ads', name: 'Meta Ads (Facebook & Instagram)', cat: 'Marketing', url: 'services/meta-ads.html', icon: 'fa-brands fa-meta', keywords: 'facebook ads instagram advantage plus capi server gtm scaling' },
  { key: 'social', name: 'Social Media Management', cat: 'Marketing', url: 'services/social-media-management.html', icon: 'fa-solid fa-share-nodes', keywords: 'instagram tiktok linkedin content calendar engagement scheduling' },
  { key: 'analytics', name: 'Web Analytics (GA4 & GTM)', cat: 'Marketing', url: 'services/web-analytics.html', icon: 'fa-solid fa-chart-pie', keywords: 'google analytics 4 tag manager conversion tracking data layer ecommerce' },
  { key: 'cro', name: 'CRO Conversion Optimization', cat: 'Marketing', url: 'services/cro-conversion-optimization.html', icon: 'fa-solid fa-arrow-trend-up', keywords: 'conversion rate optimization split testing heatmaps bounce reduction' },
  { key: 'email', name: 'Email Marketing', cat: 'Marketing', url: 'services/email-marketing.html', icon: 'fa-solid fa-envelope-open-text', keywords: 'klaviyo mailchimp flows automation abandoned cart newsletters' },
  { key: 'legal', name: 'Legal Data Entry & Analysis', cat: 'Automation', url: 'services/legal-data-entry-data-analysis.html', icon: 'fa-solid fa-scale-balanced', keywords: 'legal data records analysis confidential case management contracts' },
  { key: 'ghl', name: 'GoHighLevel Migration & Automation', cat: 'Automation', url: 'services/gohighlevel-migration-automation.html', icon: 'fa-solid fa-bolt', keywords: 'ghl crm funnels workflows pipelines snapshot sms automation' },
  { key: 'zoho', name: 'Zoho Setup & Automation', cat: 'Automation', url: 'services/zoho-setup-automation.html', icon: 'fa-solid fa-cubes', keywords: 'zoho crm books creator flow webhook custom modules' },
  { key: 'crm', name: 'CRM Data Management & Automation', cat: 'Automation', url: 'services/crm-data-management-automation.html', icon: 'fa-solid fa-database', keywords: 'hubspot salesforce data cleanup deduplication field mapping' },
  { key: 'leadgen', name: 'B2B Lead Generation', cat: 'Automation', url: 'services/lead-generation.html', icon: 'fa-solid fa-bullseye', keywords: 'prospecting verified email lists linkedin c-suite contacts b2b pipeline' },
  { key: 'research', name: 'Web Research & Intelligence', cat: 'Automation', url: 'services/web-research.html', icon: 'fa-solid fa-magnifying-glass', keywords: 'market research competitor analysis data sourcing directory scraping' },
  { key: 'excel', name: 'Microsoft Excel Cleaning & Formatting', cat: 'Automation', url: 'services/excel-cleaning-formatting.html', icon: 'fa-solid fa-file-excel', keywords: 'spreadsheet cleanup formulas vlookup macros pivot tables formatting' },
  { key: 'socialdata', name: 'Social Media Data Collection', cat: 'Automation', url: 'services/social-media-data-collection.html', icon: 'fa-solid fa-network-wired', keywords: 'data scraping profiles engagement metrics csv json sheets' }
];

// 2. LIVE SEARCH CONTROLLER
function handleLiveServiceSearch(val) {
  const dropdown = document.getElementById('hero-search-results');
  if (!dropdown) return;
  const q = val.trim().toLowerCase();
  if (!q) {
    dropdown.classList.add('hidden');
    dropdown.innerHTML = '';
    return;
  }

  const matches = ALL_SERVICES_SEARCH_DATA.filter(s => 
    s.name.toLowerCase().includes(q) || 
    s.cat.toLowerCase().includes(q) || 
    s.keywords.toLowerCase().includes(q)
  );

  if (matches.length === 0) {
    dropdown.innerHTML = '<div class="p-4 text-center text-xs text-slate-500 font-semibold">No services found for "' + val + '". Try typing "Web", "Ads", "Shopify", or "CRM".</div>';
    dropdown.classList.remove('hidden');
    return;
  }

  let html = '<div class="p-2 space-y-1">';
  matches.forEach(m => {
    html += `
    <div class="flex items-center justify-between p-2.5 rounded-xl hover:bg-blue-50/80 transition group">
      <a href="${m.url}" class="flex items-center gap-3 flex-1 min-w-0">
        <div class="w-8 h-8 rounded-lg bg-blue-100/80 text-blue-600 flex items-center justify-center text-xs shrink-0 group-hover:bg-blue-600 group-hover:text-white transition">
          <i class="${m.icon}"></i>
        </div>
        <div class="truncate">
          <h5 class="text-xs font-black text-slate-900 group-hover:text-blue-600 transition truncate">${m.name}</h5>
          <span class="text-[10px] text-slate-400 font-semibold uppercase tracking-wider">${m.cat}</span>
        </div>
      </a>
      <div class="flex items-center gap-1.5 shrink-0 ml-2">
        <a href="${m.url}" class="px-2.5 py-1 rounded-lg bg-blue-50 text-blue-700 hover:bg-blue-600 hover:text-white text-[11px] font-bold transition">Details &rarr;</a>
        <button onclick="jumpToServicePricing('${m.key}'); document.getElementById('hero-search-results').classList.add('hidden');" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-bold transition">Pricing</button>
      </div>
    </div>`;
  });
  html += '</div>';

  dropdown.innerHTML = html;
  dropdown.classList.remove('hidden');
}

function quickSelectService(key) {
  const match = ALL_SERVICES_SEARCH_DATA.find(s => s.key === key);
  if (match) {
    window.location.href = match.url;
  }
}

function submitSearchFirstMatch() {
  const input = document.getElementById('hero-search-input');
  if (!input) return;
  const q = input.value.trim().toLowerCase();
  if (!q) return;
  const match = ALL_SERVICES_SEARCH_DATA.find(s => 
    s.name.toLowerCase().includes(q) || 
    s.keywords.toLowerCase().includes(q)
  );
  if (match) {
    window.location.href = match.url;
  }
}

// Close search dropdown on outside click
document.addEventListener('click', (e) => {
  const input = document.getElementById('hero-search-input');
  const dropdown = document.getElementById('hero-search-results');
  if (dropdown && !dropdown.contains(e.target) && e.target !== input) {
    dropdown.classList.add('hidden');
  }
});

// 3. UNIFIED SERVICES CATEGORY SWITCHER (#services)
function switchServiceCategory(cat) {
  document.querySelectorAll('.cat-tab-btn').forEach(btn => {
    btn.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
    btn.classList.add('text-slate-700');
  });
  const activeBtn = document.getElementById('cat-tab-' + cat);
  if (activeBtn) {
    activeBtn.classList.add('bg-blue-600', 'text-white', 'shadow-md');
    activeBtn.classList.remove('text-slate-700');
  }

  document.querySelectorAll('.cat-panel').forEach(p => p.classList.add('hidden'));
  const activePanel = document.getElementById('cat-panel-' + cat);
  if (activePanel) {
    activePanel.classList.remove('hidden');
  }
}

// 4. PRICING MARQUEE TRACK CONTROLLER (#pricing)
function selectTrackService(slug) {
  // Update track pill styling
  document.querySelectorAll('.track-pill').forEach(btn => {
    btn.classList.remove('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
    btn.classList.add('border-slate-200/90', 'bg-white', 'text-slate-700');
  });

  const matchingPills = document.querySelectorAll('#track-pill-' + slug);
  matchingPills.forEach(p => {
    p.classList.add('border-blue-600', 'bg-blue-50/80', 'text-blue-700', 'shadow-xs');
    p.classList.remove('border-slate-200/90', 'bg-white', 'text-slate-700');
  });

  // Show target panel
  document.querySelectorAll('.track-pricing-panel').forEach(p => p.classList.add('hidden'));
  const target = document.getElementById('track-panel-' + slug);
  if (target) {
    target.classList.remove('hidden');
  }
}

function jumpToServicePricing(slug) {
  const sec = document.getElementById('pricing');
  if (sec) {
    sec.scrollIntoView({ behavior: 'smooth' });
  }
  selectTrackService(slug);
}

function scrollTrackPrev() {
  const container = document.getElementById('pricing-marquee-container');
  if (container) container.scrollBy({ left: -280, behavior: 'smooth' });
}

function scrollTrackNext() {
  const container = document.getElementById('pricing-marquee-container');
  if (container) container.scrollBy({ left: 280, behavior: 'smooth' });
}
</script>
"""

# Replace old JS snippet if exists, or append before </body>
if "<!-- RANKNIX 24-SERVICE PRICING ENGINE" in html:
    pattern_old_js = r'<!-- RANKNIX 24-SERVICE PRICING ENGINE.*?</body>'
    html = re.sub(pattern_old_js, js_controllers + "\n</body>", html, flags=re.DOTALL)
else:
    html = html.replace("</body>", js_controllers + "\n</body>")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html has been completely updated!")
