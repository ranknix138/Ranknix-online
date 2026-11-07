import sys
sys.stdout.reconfigure(encoding='utf-8')
from reviews_data import TESTIMONIALS_DATA

def render_reviews_single_row_marquee():
    def render_card(r):
        return f"""
        <div class="review-card flex-shrink-0 w-[340px] sm:w-[380px] p-6 rounded-2xl bg-white border border-slate-200/90 shadow-2xs hover:shadow-lg hover:border-blue-400 transition-all duration-300 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-1 text-amber-400 text-xs">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
              </div>
              <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 text-[10px] font-bold border border-emerald-200">
                <i class="fa-solid fa-circle-check text-[9px]"></i> Verified Client
              </span>
            </div>
            <p class="text-slate-600 text-xs sm:text-[13px] leading-relaxed italic mb-5">
              "{r['text']}"
            </p>
          </div>
          <div class="pt-3.5 border-t border-slate-100 flex items-center gap-3">
            <div class="relative shrink-0">
              <img src="{r['avatar']}" alt="{r['name']}" class="w-11 h-11 rounded-full object-cover border-2 border-blue-100 shadow-2xs">
              <span class="absolute bottom-0 right-0 w-3 h-3 rounded-full bg-emerald-500 border-2 border-white"></span>
            </div>
            <div class="overflow-hidden">
              <h4 class="text-xs font-black text-slate-900 leading-tight truncate">{r['name']} {r['flag']}</h4>
              <span class="text-[11px] text-slate-500 block truncate">{r['role']}</span>
              <span class="text-[10px] text-blue-600 font-mono block">{r['country']}</span>
            </div>
          </div>
        </div>
        """

    # All 18 reviews duplicated for infinite seamless marquee loop
    all_cards_html = "".join([render_card(r) for r in TESTIMONIALS_DATA]) * 2

    html = f"""
  <!-- 7. REVIEWS & TESTIMONIALS (SINGLE CONTINUOUS AUTO-SCROLLING MARQUEE LINE) -->
  <section id="testimonials" class="py-20 sm:py-24 bg-slate-50/70 relative z-10 border-t border-slate-200/80 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-10">
      <div class="text-center max-w-3xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-blue-50 border border-blue-200/80 text-blue-700 text-xs font-bold mb-3 shadow-2xs">
          <i class="fa-solid fa-star text-amber-500"></i>
          <span>150+ Projects Delivered Across 60+ Countries</span>
        </div>
        <h2 class="text-3xl sm:text-4xl md:text-5xl font-black text-slate-900 font-heading tracking-tight mb-3">
          Trusted By Ambitious Brands <span class="text-gradient-blue">Around The World</span>
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed max-w-2xl mx-auto">
          From high-growth startups in London and Austin to market leaders in Dubai and Pakistan — here is what founders and CMOs say about partnering with Ranknix Online.
        </p>
      </div>
    </div>

    <!-- EXACTLY ONE SINGLE CONTINUOUS MARQUEE LINE (Smooth Infinite Scroll) -->
    <div class="marquee-wrapper relative w-full overflow-hidden py-3">
      <div class="marquee-content flex gap-6 hover:[animation-play-state:paused]" style="animation: scrollInfinite 60s linear infinite; width: max-content;">
        {all_cards_html}
      </div>
    </div>

    <!-- Bottom Metric Bar -->
    <div class="max-w-4xl mx-auto px-4 mt-10 text-center">
      <div class="inline-flex flex-wrap items-center justify-center gap-4 sm:gap-8 px-6 py-3 rounded-2xl bg-white border border-slate-200 shadow-2xs text-xs font-bold text-slate-700">
        <span class="flex items-center gap-1.5 text-amber-500">
          <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
          <span class="text-slate-900 font-black ml-1">4.9 / 5.0</span>
        </span>
        <span class="text-slate-300 hidden sm:inline">|</span>
        <span>🇬🇧 99% UK &amp; Western SLA On-Time Delivery</span>
        <span class="text-slate-300 hidden sm:inline">|</span>
        <span>💬 Direct 24/7 Founder WhatsApp Access</span>
      </div>
    </div>
  </section>
    """
    return html

print("render_reviews_single_row_marquee ready!")
