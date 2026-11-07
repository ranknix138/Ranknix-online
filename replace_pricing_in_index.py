import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\index.html", "r", encoding="utf-8") as f:
    idx = f.read()

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\generated_pricing_section.html", "r", encoding="utf-8") as f:
    new_pricing = f.read()

pattern = r'<section id="pricing".*?</section>'
m = re.search(pattern, idx, re.DOTALL)
if not m:
    print("ERROR: Could not find <section id='pricing' ...> in index.html!")
    sys.exit(1)

old_sec = m.group(0)
print(f"Old pricing section length: {len(old_sec)}")
print(f"New pricing section length: {len(new_pricing)}")

updated_idx = idx[:m.start()] + new_pricing + idx[m.end():]

# Now let's check if the JS switcher functions are in index.html or main.js
# Let's ensure the JS functions are embedded right before </body> in index.html or in main.js
js_snippet = """
<!-- RANKNIX 24-SERVICE PRICING ENGINE & GLOBAL CURRENCY JS -->
<script>
function selectPricingDivision(divId) {
  document.querySelectorAll('.pricing-div-btn').forEach(btn => {
    btn.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
    btn.classList.add('text-slate-700');
  });
  const activeDivBtn = document.getElementById('div-btn-' + divId);
  if (activeDivBtn) {
    activeDivBtn.classList.add('bg-blue-600', 'text-white', 'shadow-md');
    activeDivBtn.classList.remove('text-slate-700');
  }

  document.querySelectorAll('.service-pills-bar').forEach(bar => bar.classList.add('hidden'));
  const activePillsBar = document.getElementById('service-pills-' + divId);
  if (activePillsBar) {
    activePillsBar.classList.remove('hidden');
    const firstPill = activePillsBar.querySelector('.service-pill-btn');
    if (firstPill) {
      const svcKey = firstPill.id.replace('pill-', '');
      selectPricingService(svcKey);
    }
  }
}

function selectPricingService(svcKey) {
  document.querySelectorAll('.service-pill-btn').forEach(p => {
    p.classList.remove('bg-blue-600', 'text-white', 'shadow-md', 'border-blue-600');
    p.classList.add('bg-white', 'text-slate-700', 'border-slate-200/90');
  });
  const activePill = document.getElementById('pill-' + svcKey);
  if (activePill) {
    activePill.classList.add('bg-blue-600', 'text-white', 'shadow-md', 'border-blue-600');
    activePill.classList.remove('bg-white', 'text-slate-700', 'border-slate-200/90');
    
    const parentBar = activePill.closest('.service-pills-bar');
    if (parentBar && parentBar.classList.contains('hidden')) {
      document.querySelectorAll('.service-pills-bar').forEach(b => b.classList.add('hidden'));
      parentBar.classList.remove('hidden');
      const divId = parentBar.id.replace('service-pills-', '');
      document.querySelectorAll('.pricing-div-btn').forEach(btn => {
        btn.classList.remove('bg-blue-600', 'text-white', 'shadow-md');
        btn.classList.add('text-slate-700');
      });
      const divBtn = document.getElementById('div-btn-' + divId);
      if (divBtn) {
        divBtn.classList.add('bg-blue-600', 'text-white', 'shadow-md');
        divBtn.classList.remove('text-slate-700');
      }
    }
  }

  const mobileSelect = document.getElementById('mobile-pricing-select');
  if (mobileSelect) {
    mobileSelect.value = svcKey;
  }

  document.querySelectorAll('.pricing-panel').forEach(panel => {
    panel.classList.add('hidden');
  });
  const targetPanel = document.getElementById('panel-' + svcKey);
  if (targetPanel) {
    targetPanel.classList.remove('hidden');
  }
}

function changeGlobalCurrency(curr) {
  try {
    localStorage.setItem('ranknix_currency', curr);
  } catch (e) {}

  document.querySelectorAll('[data-curr-pill]').forEach(pill => {
    if (pill.getAttribute('data-curr-pill') === curr) {
      pill.classList.add('bg-blue-600', 'text-white');
      pill.classList.remove('text-slate-700');
    } else {
      pill.classList.remove('bg-blue-600', 'text-white');
      pill.classList.add('text-slate-700');
    }
  });

  const activeLabel = document.getElementById('active-currency-label');
  if (activeLabel) {
    const icons = { PKR: '🇵🇰 PKR', GBP: '🇬🇧 GBP', USD: '🇺🇸 USD', EUR: '🇪🇺 EUR' };
    activeLabel.textContent = icons[curr] || curr;
  }

  document.querySelectorAll('.dynamic-price').forEach(el => {
    const val = el.getAttribute('data-' + curr.toLowerCase());
    if (val) el.textContent = val;
  });

  if (typeof setCurrency === 'function') {
    setCurrency(curr, true);
  }
}

// Auto-run on load
document.addEventListener('DOMContentLoaded', function() {
  const saved = localStorage.getItem('ranknix_currency') || 'PKR';
  changeGlobalCurrency(saved);

  // Check URL hash for direct service link, e.g. #pricing-google-ads
  if (window.location.hash) {
    const h = window.location.hash.toLowerCase();
    const svcKeys = [
      'web-dev', 'app-dev', 'ui-ux', 'graphic', 'ecommerce', 'video', 'content', 'landing',
      'digital-mkt', 'seo', 'google-ads', 'meta-ads', 'social', 'analytics', 'cro', 'email',
      'legal', 'ghl', 'zoho', 'crm', 'leadgen', 'research', 'excel', 'socialdata'
    ];
    for (const k of svcKeys) {
      if (h.includes(k)) {
        selectPricingService(k);
        break;
      }
    }
  }
});
</script>
"""

if "function selectPricingDivision" not in updated_idx:
    updated_idx = updated_idx.replace("</body>", js_snippet + "\n</body>")

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\index.html", "w", encoding="utf-8") as f:
    f.write(updated_idx)

print("Successfully updated index.html with the new 24-service interactive pricing showcase!")
