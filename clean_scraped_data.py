import json, sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Clean scraped_packages.json
with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "r", encoding="utf-8") as f:
    data = json.load(f)

data["socialdata"]["packages"][2]["features"] = [
    "Unlimited volume & custom queries",
    "All major platforms (Instagram, LinkedIn, X, TikTok, YouTube)",
    "Custom data pipeline & API / Webhook delivery",
    "Clean formatting (CSV, Excel, Google Sheets, JSON)",
    "Dedicated data analyst & Founder Muhammad Abdullah oversight",
    "Priority turnaround & 100% data verification"
]

with open(r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\scraped_packages.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Cleaned scraped_packages.json socialdata tier 3!")

# 2. Re-run build_index_pricing.py
import subprocess
subprocess.run(["python", r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\build_index_pricing.py"], check=True)
subprocess.run(["python", r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\replace_pricing_in_index.py"], check=True)

# 3. Clean any comments in index.html mentioning Rafirit Station
idx_path = r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

idx_content = idx_content.replace("Rafirit Station", "Ranknix Online").replace("rafiritstation.com", "ranknix.online").replace("Dhaka (Head Office)", "Lahore & Global Operations")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(idx_content)

print("Updated index.html cleanly!")

# 4. Re-run build_all_service_pages.py
subprocess.run(["python", r"C:\Users\Abdullah\.gemini\antigravity\scratch\marketing-agency-website\build_all_service_pages.py"], check=True)
print("Regenerated all 24 service sub-pages cleanly!")
