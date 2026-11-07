import os
import json

SERVICES_DATA = [
    # 01
    {
        "slug": "web-development",
        "num": "01",
        "name": "Web Development",
        "category": "Web & App Development",
        "cat_badge_class": "badge-dev",
        "cat_icon": "fa-solid fa-code",
        "icon": "fa-solid fa-globe",
        "icon_bg": "bg-blue-100 text-blue-600",
        "tagline": "WordPress, Shopify, Next.js & Custom Web Engineering",
        "h1_prefix": "Websites That Turn Visitors Into",
        "h1_gradient": "Paying Customers & High Revenue",
        "description": "Slow, cookie-cutter templates kill conversions. At Ranknix Online, we engineer high-speed, modern websites optimized for Google PageSpeed 99+, mobile responsiveness, and maximum checkout conversion rates.",
        "stats": [
            ("100+", "Websites Delivered"),
            ("99", "PageSpeed Score"),
            ("7 Days", "Avg. Delivery"),
            ("4.9★", "Client Rating")
        ],
        "platforms": ["WordPress", "Shopify Plus", "Next.js", "React", "WooCommerce", "WIX Studio", "Tailwind CSS", "Webflow"],
        "deliverables": [
            {
                "title": "Custom Responsive Design",
                "desc": "Bespoke UI/UX designed specifically for your brand identity. Zero generic templates, 100% pixel-perfect on mobile, tablet, and ultra-wide screens.",
                "icon": "fa-solid fa-mobile-screen"
            },
            {
                "title": "Lightning 99 PageSpeed Score",
                "desc": "Built with lean semantic markup, compressed WebP media, and CDN edge caching to achieve sub-second load times that keep visitors engaged.",
                "icon": "fa-solid fa-bolt"
            },
            {
                "title": "Built-In SEO & Technical Architecture",
                "desc": "Schema markup, clean canonical URLs, OpenGraph metadata, XML sitemaps, and robots.txt pre-configured for instant Google indexation.",
                "icon": "fa-solid fa-magnifying-glass"
            },
            {
                "title": "High-Converting Checkout & Lead Funnels",
                "desc": "Frictionless checkout paths, one-click WhatsApp integration, sticky CTAs, and automated lead capture pipelines that multiply inbound inquiries.",
                "icon": "fa-solid fa-cart-shopping"
            },
            {
                "title": "Tracking & Analytics Integration",
                "desc": "Complete server-side tracking setup: Meta Conversions API (CAPI), Google Tag Manager, GA4, and Google Ads Conversion Tracking pre-installed.",
                "icon": "fa-solid fa-chart-line"
            },
            {
                "title": "Client Handover & Video Training",
                "desc": "You retain 100% full administrative ownership of your code, domain, and hosting, accompanied by custom recorded video walkthroughs for easy updates.",
                "icon": "fa-solid fa-shield-halved"
            }
        ],
        "pricing": {
            "starter": {"name": "Business Starter", "pkr": "₨ 35,000", "gbp": "£119", "usd": "$149", "eur": "€139", "features": ["5 Custom Designed Pages", "Mobile Responsive & SEO Ready", "Fast 5-7 Day Delivery", "WhatsApp & Contact Forms", "1 Month Post-Launch Support"]},
            "growth": {"name": "E-Commerce / Growth", "pkr": "₨ 65,000", "gbp": "£219", "usd": "$279", "eur": "€259", "features": ["Up to 15 Pages / Product Catalog", "Shopify / WooCommerce / Custom", "Payment Gateways & Cart Setup", "GA4 & Meta CAPI Integration", "2 Months Priority Support"]},
            "enterprise": {"name": "Custom Web App / Scale", "pkr": "₨ 125,000", "gbp": "£419", "usd": "$529", "eur": "€499", "features": ["Full Stack Next.js / Custom React", "Database & API Integrations", "Sub-Second Edge Performance", "Custom Dynamic Workflows", "Dedicated Senior Developer Oversight"]}
        },
        "faqs": [
            {"q": "How long does a website take to build and launch?", "a": "Standard corporate websites take 5 to 7 business days. Complex e-commerce stores take 10 to 14 days, and full custom web applications take 3 to 5 weeks. Every project adheres to strict milestone deadlines."},
            {"q": "Do I get full ownership of my website and domain?", "a": "Yes, absolutely! 100% of the code, domain, hosting credentials, and design assets belong to you upon project completion. We never lock clients into proprietary systems."},
            {"q": "Will my website load fast on mobile devices in Pakistan and internationally?", "a": "Yes. Every website we build is tested on Google PageSpeed Insights and GTmetrix to hit 90+ to 99 performance scores with compressed assets and global CDN edge routing."},
            {"q": "Can Ranknix Online manage my hosting and ongoing maintenance?", "a": "Yes. We offer continuous managed hosting, daily backups, security monitoring, and content updates so you can focus entirely on running your business."}
        ]
    },
    # 02
    {
        "slug": "app-development",
        "num": "02",
        "name": "App Development",
        "category": "Web & App Development",
        "cat_badge_class": "badge-dev",
        "cat_icon": "fa-solid fa-code",
        "icon": "fa-solid fa-mobile-screen",
        "icon_bg": "bg-sky-100 text-sky-600",
        "tagline": "Cross-Platform iOS & Android Mobile Engineering",
        "h1_prefix": "Scalable iOS & Android Apps Built from",
        "h1_gradient": "One Robust High-Performance Codebase",
        "description": "Build high-speed, native-feeling mobile applications for Apple iOS and Google Android simultaneously. We use React Native and Flutter to cut your development costs in half while delivering institutional stability.",
        "stats": [
            ("30+", "Apps Launched"),
            ("2", "Platforms, 1 Codebase"),
            ("4-6 wks", "Fast MVP Delivery"),
            ("4.9★", "Client Rating")
        ],
        "platforms": ["React Native", "Flutter", "iOS (Swift)", "Android (Kotlin)", "Firebase", "Node.js Backend", "GraphQL", "REST APIs"],
        "deliverables": [
            {"title": "Dual-Platform iOS & Android Deploy", "desc": "One single robust codebase deployed seamlessly to the Apple App Store and Google Play Store.", "icon": "fa-brands fa-apple"},
            {"title": "Fluid 60fps Native Performance", "desc": "Smooth gestures, zero lag transitions, and optimized battery consumption engineered for high retention.", "icon": "fa-solid fa-gauge-high"},
            {"title": "Cloud Backend & Push Notifications", "desc": "Scalable Firebase / Node.js infrastructure with instant push notifications, authentication, and offline sync.", "icon": "fa-solid fa-cloud"},
            {"title": "In-App Purchases & Payment Gateways", "desc": "Stripe, Apple Pay, Google Pay, and regional payment integrations with instant receipt validation.", "icon": "fa-solid fa-credit-card"},
            {"title": "App Store Optimization & Approval Guarantee", "desc": "Full handling of App Store review guidelines, metadata, screenshots, and compliance for guaranteed launch approval.", "icon": "fa-solid fa-circle-check"},
            {"title": "Post-Launch Monitoring & Bug-Free Warranty", "desc": "Continuous crash reporting with Sentry, real-time user monitoring, and immediate patch deployment.", "icon": "fa-solid fa-shield-virus"}
        ],
        "pricing": {
            "starter": {"name": "MVP Mobile App", "pkr": "₨ 95,000", "gbp": "£319", "usd": "$399", "eur": "€379", "features": ["Cross-Platform iOS & Android", "Core Features & User Auth", "Push Notifications & Cloud DB", "App Store Submission Assistance", "1 Month Warranty"]},
            "growth": {"name": "Commercial App", "pkr": "₨ 185,000", "gbp": "£619", "usd": "$789", "eur": "€739", "features": ["Full Custom UI/UX Design", "Payment Gateways & Subscriptions", "Admin Dashboard & Analytics", "Real-Time Chat / API Sync", "3 Months Priority Support"]},
            "enterprise": {"name": "Enterprise Scale App", "pkr": "₨ 320,000", "gbp": "£1,080", "usd": "$1,360", "eur": "€1,280", "features": ["Complex Multi-Role Architecture", "Custom High-Volume Backend", "SLA Guarantees & Security Audits", "Dedicated Engineering Team", "Full Source Code & IP Transfer"]}
        },
        "faqs": [
            {"q": "Do I need separate apps for iOS and Android?", "a": "No! With modern frameworks like React Native and Flutter, we build one unified codebase that compiles natively into both Apple iOS and Google Android apps, saving you over 50% in cost and time."},
            {"q": "Do you handle App Store and Google Play publishing?", "a": "Yes. We take care of all store assets, privacy policies, API permissions, and submission requirements to ensure quick store approval."},
            {"q": "Can you integrate custom APIs and existing databases?", "a": "Yes. We regularly connect mobile apps to existing ERPs, CRMs, Shopify stores, and custom REST or GraphQL backends."},
            {"q": "What happens after the app is published?", "a": "We provide warranty support and monitoring, ensuring any OS updates (iOS/Android) keep your app running smoothly."}
        ]
    }
]

print("Base setup ready!")
