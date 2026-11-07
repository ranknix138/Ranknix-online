import sys
sys.stdout.reconfigure(encoding='utf-8')

def render_simulation(sim_type, s_name):
    if sim_type == "google_ads":
        return f"""
        <!-- GOOGLE SEARCH LIVE SIMULATION PANEL -->
        <div class="clean-card rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-lg bg-white relative overflow-hidden">
          <div class="flex items-center justify-between pb-4 mb-5 border-b border-slate-100 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-rose-500"></span>
              <span class="w-3 h-3 rounded-full bg-amber-500"></span>
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="text-xs font-mono text-slate-400 ml-2">google.com/search?q=enterprise+solutions</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-[11px] font-bold">
                <i class="fa-solid fa-circle-check"></i> Rank #1 Live Ad
              </span>
              <span class="px-2.5 py-0.5 rounded-full bg-blue-50 border border-blue-200 text-blue-700 text-[11px] font-bold">
                Quality Score: 10/10
              </span>
            </div>
          </div>

          <!-- The Simulated Google Ad -->
          <div class="bg-slate-50/70 p-5 sm:p-6 rounded-2xl border border-slate-200/80">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[10px] font-black bg-emerald-600 text-white tracking-wider uppercase">Sponsored</span>
              <span class="text-xs text-slate-500 font-mono">https://www.yourbrand.com/growth</span>
            </div>
            <h4 class="text-base sm:text-lg font-bold text-blue-700 hover:underline cursor-pointer mb-1.5">
              Ranknix Online Growth Partner | High-ROAS Google & Bing Campaigns
            </h4>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mb-4">
              Stop burning budget on wasted clicks. Ranknix Online builds hyper-targeted Google Search & Performance Max campaigns with strict negative keyword shielding, 4.8% CTR, and direct Founder supervision.
            </p>

            <!-- 4 Sitelinks Grid -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-4 pt-3 border-t border-slate-200/60">
              <div class="p-2.5 rounded-xl bg-white border border-slate-200/80 text-xs font-bold text-blue-700 hover:bg-blue-50 transition cursor-pointer">
                <span>Free Strategy Audit &rarr;</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-0.5">30-min consultation</span>
              </div>
              <div class="p-2.5 rounded-xl bg-white border border-slate-200/80 text-xs font-bold text-blue-700 hover:bg-blue-50 transition cursor-pointer">
                <span>Verified Case Studies &rarr;</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-0.5">3.5x–8x ROAS</span>
              </div>
              <div class="p-2.5 rounded-xl bg-white border border-slate-200/80 text-xs font-bold text-blue-700 hover:bg-blue-50 transition cursor-pointer">
                <span>Transparent Rates &rarr;</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-0.5">PKR, GBP, USD, EUR</span>
              </div>
              <div class="p-2.5 rounded-xl bg-white border border-slate-200/80 text-xs font-bold text-blue-700 hover:bg-blue-50 transition cursor-pointer">
                <span>WhatsApp Onboard &rarr;</span>
                <span class="block text-[10px] text-slate-400 font-normal mt-0.5">24hr setup</span>
              </div>
            </div>

            <!-- Ad Extensions -->
            <div class="flex flex-wrap items-center gap-3 text-xs text-slate-500 pt-2 border-t border-slate-200/60">
              <span class="text-amber-500 font-bold flex items-center gap-1">
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                <span class="text-slate-700 ml-1">5.0 (80+ Client Reviews)</span>
              </span>
              <span>&bull;</span>
              <span class="flex items-center gap-1"><i class="fa-solid fa-shield-check text-blue-600"></i> Certified Google Partner</span>
              <span>&bull;</span>
              <span class="flex items-center gap-1"><i class="fa-solid fa-phone text-emerald-600"></i> Call Extensions Enabled</span>
            </div>
          </div>
        </div>
        """

    elif sim_type == "meta_ads":
        return f"""
        <!-- META ADS LIVE SIMULATION PANEL -->
        <div class="clean-card rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-lg bg-white relative overflow-hidden">
          <div class="flex items-center justify-between pb-4 mb-5 border-b border-slate-100 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-rose-500"></span>
              <span class="w-3 h-3 rounded-full bg-amber-500"></span>
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="text-xs font-mono text-slate-400 ml-2">instagram.com/feed &bull; Meta Advantage+</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-purple-50 border border-purple-200 text-purple-700 text-[11px] font-bold">
                <i class="fa-brands fa-meta"></i> Server-Side CAPI Active
              </span>
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-[11px] font-bold">
                4.6x Average ROAS
              </span>
            </div>
          </div>

          <div class="max-w-md mx-auto bg-slate-50/90 rounded-2xl border border-slate-200/80 p-5 shadow-inner">
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-full bg-gradient-to-tr from-amber-400 via-rose-500 to-purple-600 p-0.5">
                  <div class="w-full h-full bg-white rounded-full flex items-center justify-center font-bold text-xs text-blue-600">R</div>
                </div>
                <div>
                  <h5 class="text-xs font-black text-slate-900 leading-none">YourBrand_Official</h5>
                  <span class="text-[10px] text-slate-400">Sponsored &bull; Direct Response Hook</span>
                </div>
              </div>
              <i class="fa-solid fa-ellipsis text-slate-400 text-xs"></i>
            </div>

            <!-- Ad Creative Card -->
            <div class="rounded-xl overflow-hidden bg-gradient-to-br from-blue-900 via-indigo-900 to-slate-900 text-white p-6 text-center relative mb-3 aspect-[4/3] flex flex-col justify-center items-center">
              <div class="w-14 h-14 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center mb-3 shadow-lg">
                <i class="fa-solid fa-play text-white text-lg ml-0.5"></i>
              </div>
              <span class="text-[10px] font-extrabold uppercase tracking-widest text-blue-300 mb-1">Ranknix High-Converting Creative</span>
              <h4 class="text-lg font-black font-heading leading-tight">Scale From $10k to $100k/mo with Precision Meta Ads</h4>
              <p class="text-[11px] text-slate-300 mt-2">Iterative creative testing &bull; Advantage+ Shopping &bull; 95% CAPI Match Rate</p>
            </div>

            <!-- Interactive CTA Bar -->
            <div class="flex items-center justify-between bg-white p-3 rounded-xl border border-slate-200/80 mb-2">
              <div class="text-left">
                <span class="text-[10px] text-slate-400 block font-mono">RANKNIX.ONLINE/SCALING</span>
                <span class="text-xs font-bold text-slate-800">Claim Your Free Growth Audit</span>
              </div>
              <button class="px-4 py-1.5 rounded-lg bg-blue-600 text-white text-xs font-bold shadow-xs hover:bg-blue-700 transition">
                Shop Now
              </button>
            </div>

            <!-- Live Performance Metrics -->
            <div class="flex items-center justify-between text-[11px] font-bold text-slate-600 px-1 pt-1">
              <span>❤️ 2,480 Likes</span>
              <span>💬 194 Comments</span>
              <span class="text-emerald-600 font-extrabold">ROAS 4.6x</span>
            </div>
          </div>
        </div>
        """

    elif sim_type == "web_dev":
        return f"""
        <!-- PAGESPEED 99 LIVE AUDIT SIMULATION PANEL -->
        <div class="clean-card rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-lg bg-white relative overflow-hidden">
          <div class="flex items-center justify-between pb-4 mb-5 border-b border-slate-100 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-rose-500"></span>
              <span class="w-3 h-3 rounded-full bg-amber-500"></span>
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="text-xs font-mono text-slate-400 ml-2">pagespeed.web.dev/report?url=yourbrand.com</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-[11px] font-bold">
                <i class="fa-solid fa-circle-check"></i> Core Web Vitals Passed
              </span>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-4 gap-6 items-center">
            <!-- 99 Score Circle -->
            <div class="flex flex-col items-center justify-center p-6 rounded-2xl bg-emerald-50/50 border border-emerald-200 text-center">
              <div class="w-24 h-24 rounded-full border-4 border-emerald-500 flex items-center justify-center mb-2 shadow-inner bg-white">
                <span class="text-4xl font-black text-emerald-600 font-heading">99</span>
              </div>
              <span class="text-xs font-black text-emerald-800 uppercase tracking-wider">Performance</span>
              <span class="text-[10px] text-emerald-600 font-medium mt-0.5">Mobile Audit Passed</span>
            </div>

            <!-- Vitals Grid -->
            <div class="md:col-span-3 grid grid-cols-2 sm:grid-cols-3 gap-3">
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">First Contentful Paint</span>
                <span class="text-lg font-black text-emerald-600 font-heading">0.6 s</span>
                <span class="block text-[10px] text-slate-400 font-medium">Fast (Good)</span>
              </div>
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">Largest Contentful Paint</span>
                <span class="text-lg font-black text-emerald-600 font-heading">0.8 s</span>
                <span class="block text-[10px] text-slate-400 font-medium">Fast (Good)</span>
              </div>
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">Total Blocking Time</span>
                <span class="text-lg font-black text-emerald-600 font-heading">0 ms</span>
                <span class="block text-[10px] text-slate-400 font-medium">Fast (Good)</span>
              </div>
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">Cumulative Layout Shift</span>
                <span class="text-lg font-black text-emerald-600 font-heading">0.00</span>
                <span class="block text-[10px] text-slate-400 font-medium">Zero Layout Jitter</span>
              </div>
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">Accessibility</span>
                <span class="text-lg font-black text-blue-600 font-heading">100 / 100</span>
                <span class="block text-[10px] text-slate-400 font-medium">WCAG Compliant</span>
              </div>
              <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200/80">
                <span class="text-[10px] text-slate-500 block uppercase font-bold">SEO Best Practices</span>
                <span class="text-lg font-black text-blue-600 font-heading">100 / 100</span>
                <span class="block text-[10px] text-slate-400 font-medium">Full Schema Built-in</span>
              </div>
            </div>
          </div>
        </div>
        """

    else:
        # Default CRM / Workflow Automation pipeline simulation
        return f"""
        <!-- AUTOMATED WORKFLOW PIPELINE SIMULATION -->
        <div class="clean-card rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-lg bg-white relative overflow-hidden">
          <div class="flex items-center justify-between pb-4 mb-5 border-b border-slate-100 flex-wrap gap-2">
            <div class="flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-rose-500"></span>
              <span class="w-3 h-3 rounded-full bg-amber-500"></span>
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="text-xs font-mono text-slate-400 ml-2">ranknix.online/pipeline &bull; Active Automation Workflow</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-0.5 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-700 text-[11px] font-bold">
                <i class="fa-solid fa-circle-check"></i> 100% Automated Execution
              </span>
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/80 relative">
              <span class="text-[10px] font-black uppercase tracking-wider text-blue-600 mb-1 block">Step 01 &bull; Trigger</span>
              <h5 class="text-xs font-black text-slate-900 mb-1">Inbound Lead Capture</h5>
              <p class="text-[11px] text-slate-600">Meta/Google Ads lead form submitted with verified contact info.</p>
              <span class="inline-block mt-2 text-[10px] font-bold text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded">Execution: &lt; 1s</span>
            </div>

            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 relative">
              <span class="text-[10px] font-black uppercase tracking-wider text-slate-500 mb-1 block">Step 02 &bull; Instant Action</span>
              <h5 class="text-xs font-black text-slate-900 mb-1">WhatsApp & SMS Hook</h5>
              <p class="text-[11px] text-slate-600">Automated personalized WhatsApp greeting + calendar booking link dispatched.</p>
              <span class="inline-block mt-2 text-[10px] font-bold text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded">Execution: 12s</span>
            </div>

            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 relative">
              <span class="text-[10px] font-black uppercase tracking-wider text-slate-500 mb-1 block">Step 03 &bull; CRM Sync</span>
              <h5 class="text-xs font-black text-slate-900 mb-1">Pipeline Deal Created</h5>
              <p class="text-[11px] text-slate-600">Deal entered in Zoho/GHL, assigned to account manager, lead score assigned.</p>
              <span class="inline-block mt-2 text-[10px] font-bold text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded">Status: Synced</span>
            </div>

            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200/80 relative">
              <span class="text-[10px] font-black uppercase tracking-wider text-slate-500 mb-1 block">Step 04 &bull; Closing</span>
              <h5 class="text-xs font-black text-slate-900 mb-1">Contract & Invoice</h5>
              <p class="text-[11px] text-slate-600">Automated Stripe invoice + electronic contract dispatched upon deal close.</p>
              <span class="inline-block mt-2 text-[10px] font-bold text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded">0 Manual Hours</span>
            </div>
          </div>
        </div>
        """

print("service_simulations.py loaded.")
