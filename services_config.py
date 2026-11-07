import sys
sys.stdout.reconfigure(encoding='utf-8')

SERVICES_INFO = {
    # Division 1: Web & App Dev
    "web-dev": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-code",
        "slug": "web-development.html",
        "name": "Web Development",
        "short_name": "Web Dev"
    },
    "app-dev": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-mobile-screen-button",
        "slug": "app-development.html",
        "name": "App Development",
        "short_name": "App Dev"
    },
    "ui-ux": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-pen-nib",
        "slug": "ui-ux-design.html",
        "name": "UI/UX Design",
        "short_name": "UI/UX"
    },
    "graphic": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-palette",
        "slug": "graphic-design.html",
        "name": "Graphic Design",
        "short_name": "Graphic Design"
    },
    "ecommerce": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-bag-shopping",
        "slug": "e-commerce-solutions.html",
        "name": "E-Commerce Solutions",
        "short_name": "E-Commerce"
    },
    "video": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-video",
        "slug": "video-editing.html",
        "name": "Video Editing",
        "short_name": "Video Editing"
    },
    "content": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-feather",
        "slug": "content-writing.html",
        "name": "Content Writing",
        "short_name": "Content Writing"
    },
    "landing": {
        "division": "dev",
        "division_label": "Web & App Development",
        "icon": "fa-solid fa-rocket",
        "slug": "landing-page-design.html",
        "name": "Landing Page Design",
        "short_name": "Landing Pages"
    },
    # Division 2: Marketing & Growth
    "digital-mkt": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-chart-line",
        "slug": "digital-marketing.html",
        "name": "Digital Marketing",
        "short_name": "Digital Mkt"
    },
    "seo": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-magnifying-glass-chart",
        "slug": "seo-services.html",
        "name": "SEO Services",
        "short_name": "SEO Services"
    },
    "google-ads": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-brands fa-google",
        "slug": "google-ads-bing-ads.html",
        "name": "Google Ads & Bing Ads",
        "short_name": "Google Ads"
    },
    "meta-ads": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-brands fa-meta",
        "slug": "meta-ads.html",
        "name": "Meta Ads (FB & IG)",
        "short_name": "Meta Ads"
    },
    "social": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-share-nodes",
        "slug": "social-media-management.html",
        "name": "Social Media Management",
        "short_name": "Social Media"
    },
    "analytics": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-chart-pie",
        "slug": "web-analytics.html",
        "name": "Web Analytics (GA4/GTM)",
        "short_name": "Web Analytics"
    },
    "cro": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-arrow-trend-up",
        "slug": "cro-conversion-optimization.html",
        "name": "CRO Conversion Optimisation",
        "short_name": "CRO Optimization"
    },
    "email": {
        "division": "mkt",
        "division_label": "Performance Marketing & Growth",
        "icon": "fa-solid fa-envelope-open-text",
        "slug": "email-marketing.html",
        "name": "Email Marketing",
        "short_name": "Email Marketing"
    },
    # Division 3: Automation & CRM
    "legal": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-scale-balanced",
        "slug": "legal-data-entry-data-analysis.html",
        "name": "Legal Data Entry & Analysis",
        "short_name": "Legal Data"
    },
    "ghl": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-bolt",
        "slug": "gohighlevel-migration-automation.html",
        "name": "GoHighLevel Migration & Automation",
        "short_name": "GoHighLevel"
    },
    "zoho": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-cubes",
        "slug": "zoho-setup-automation.html",
        "name": "Zoho Setup & Automation",
        "short_name": "Zoho Setup"
    },
    "crm": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-database",
        "slug": "crm-data-management-automation.html",
        "name": "CRM Data Management",
        "short_name": "CRM Data"
    },
    "leadgen": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-bullseye",
        "slug": "lead-generation.html",
        "name": "B2B Lead Generation",
        "short_name": "Lead Generation"
    },
    "research": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-magnifying-glass",
        "slug": "web-research.html",
        "name": "Web Research & Intelligence",
        "short_name": "Web Research"
    },
    "excel": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-file-excel",
        "slug": "excel-cleaning-formatting.html",
        "name": "Excel Cleaning & Formatting",
        "short_name": "Excel Cleanup"
    },
    "socialdata": {
        "division": "auto",
        "division_label": "Data, CRM & Automation",
        "icon": "fa-solid fa-network-wired",
        "slug": "social-media-data-collection.html",
        "name": "Social Media Data Collection",
        "short_name": "Social Data"
    }
}

def format_currency(usd_str):
    if not usd_str or usd_str.lower() == "custom":
        return {
            "pkr": "Custom Quote",
            "usd": "Custom Quote",
            "gbp": "Custom Quote",
            "eur": "Custom Quote"
        }
    clean = str(usd_str).replace(",", "").replace("$", "").strip()
    try:
        val = float(clean)
        pkr = int(round(val * 280, -2))
        gbp = int(round(val * 0.78))
        eur = int(round(val * 0.92))
        usd = int(val)
        return {
            "pkr": f"₨ {pkr:,}",
            "usd": f"${usd:,}",
            "gbp": f"£{gbp:,}",
            "eur": f"€{eur:,}"
        }
    except Exception as e:
        return {
            "pkr": str(usd_str),
            "usd": str(usd_str),
            "gbp": str(usd_str),
            "eur": str(usd_str)
        }

print("services_config.py loaded successfully.")
