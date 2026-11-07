import os, sys
sys.stdout.reconfigure(encoding='utf-8')

svc_dir = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\services"
files = [f for f in os.listdir(svc_dir) if f.endswith('.html')]

print(f"Scanning all {len(files)} files for quality assurance...")

errors = []
for f_name in files:
    path = os.path.join(svc_dir, f_name)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check sections
    for sec_id in ['id="campaigns"', 'id="simulation"', 'id="pricing"', 'id="reviews"', 'id="faq"', 'id="contact"']:
        if sec_id not in content:
            errors.append(f"{f_name} missing {sec_id}")
            
    # Check for forbidden reference names
    if "rafirit" in content.lower():
        errors.append(f"{f_name} mentions 'rafirit'!")
    if "dhaka" in content.lower():
        errors.append(f"{f_name} mentions 'dhaka'!")

if not errors:
    print("ALL 24 SERVICE SUB-PAGES PASSED QA! Zero forbidden terms, all sections present!")
else:
    print(f"Found {len(errors)} issues:")
    for e in errors[:10]:
        print("  -", e)

# Also check index.html and pricing.html
with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\pricing.html", "r", encoding="utf-8") as f:
    price_content = f.read()

print("index.html mentions rafirit?", "rafirit" in idx_content.lower())
print("pricing.html mentions rafirit?", "rafirit" in price_content.lower())
print("pricing.html has 24 panels?", price_content.count('class="track-pricing-panel') == 24)
print("pricing.html pricing section present?", 'id="pricing"' in price_content)
