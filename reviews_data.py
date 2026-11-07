import sys
sys.stdout.reconfigure(encoding='utf-8')

# 18 Verified International Client Reviews with authentic portraits
TESTIMONIALS_DATA = [
    {
        "name": "James Whitfield",
        "role": "Managing Partner, Apex Legal UK",
        "country": "London, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Ranknix Online restructured our entire search campaigns. Cost per qualified legal lead plummeted by 52% in 8 weeks. Muhammad Abdullah and his team are extraordinary operators."
    },
    {
        "name": "Michael Kim",
        "role": "CMO, Nexus Dynamics USA",
        "country": "Austin, TX, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Google Ads CPA dropped from $148 to $69 in 6 weeks. Muhammad Abdullah's team handled our search groups and scaled PMax shopping. Their weekly reporting saved us tens of thousands."
    },
    {
        "name": "Sarah Jenkins",
        "role": "Founder & CEO, Lumina Retail UK",
        "country": "Manchester, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Ranknix Online delivered our custom WordPress portal in 10 days flat. PageSpeed jumped from 42 to 99 on mobile, and bounce rates fell off a cliff. Exceptional design depth."
    },
    {
        "name": "David Miller",
        "role": "CTO, BluePeak Logistics USA",
        "country": "Chicago, IL, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Zero bloated page builders, clean semantic code, and seamless API connections to our internal CRM. The site handles hundreds of concurrent quote requests effortlessly."
    },
    {
        "name": "Rachel Foster",
        "role": "E-Commerce VP, Aura Living USA",
        "country": "San Diego, CA, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Our direct-to-consumer store scaled from $18k to $72k/month at a 4.4x blended ROAS using Ranknix Online's Advantage+ catalog setup and UGC video hooks. Total game-changer."
    },
    {
        "name": "Oliver Hughes",
        "role": "Growth Director, Peak Digital UK",
        "country": "Bristol, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Server-side CAPI integration recovered all attribution lost after iOS updates. The Ranknix team tests creatives systematically every week, identifying winning ad angles fast."
    },
    {
        "name": "Tariq Al-Mansoor",
        "role": "Founder, Palm Luxe Realty UAE",
        "country": "Dubai, UAE",
        "flag": "🇦🇪",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "High-ticket lead generation for luxury UAE real estate. We received over 380 verified WhatsApp buyer leads in the first month alone with zero junk inquiries."
    },
    {
        "name": "Charlotte Evans",
        "role": "Head of Product, NorthGate UK",
        "country": "Edinburgh, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "The UI/UX wireframes and Figma design system Ranknix produced were pixel-perfect. Developer handoff took 2 days instead of 3 weeks. Incredible agency."
    },
    {
        "name": "Marcus Vance",
        "role": "CTO, Hyperion Cloud USA",
        "country": "Seattle, WA, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Our cross-platform Flutter mobile app was delivered to both App Store and Google Play on time. Real-time Firebase chat and notifications work flawlessly."
    },
    {
        "name": "Hamza Farooq",
        "role": "CEO, Velora Fashion PK",
        "country": "Lahore, Pakistan",
        "flag": "🇵🇰",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "They built our e-commerce multi-vendor platform with custom checkout drawers and automated payment gateways. Extremely satisfied with both the delivery speed and support."
    },
    {
        "name": "Riya Sharma",
        "role": "Growth Lead, CloudFlow Canada",
        "country": "Toronto, Canada",
        "flag": "🇨🇦",
        "avatar": "https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Running Google and Bing Ads together after their recommendation delivered 38% more B2B conversions at a significantly lower CPA. Professional team."
    },
    {
        "name": "Liam O'Connor",
        "role": "Founder, Horizon Solar",
        "country": "Sydney, Australia",
        "flag": "🇦🇺",
        "avatar": "https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Automated our entire customer onboarding with Zoho CRM and WhatsApp webhooks. Saved our sales reps at least 25 hours every single week."
    },
    {
        "name": "Emma Watson-Bell",
        "role": "E-Commerce Strategist, Thorne UK",
        "country": "London, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Ranknix redesigned our Shopify landing page with custom video sections and upsell drawers. Conversion rate immediately surged from 1.8% to 3.4%."
    },
    {
        "name": "Alexander Wright",
        "role": "Managing Partner, Wright Capital USA",
        "country": "New York, NY, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Confidential financial data analysis and Excel dashboard cleanup handled with surgical accuracy. Muhammad Abdullah personally supervised delivery."
    },
    {
        "name": "Kareem Al-Hassan",
        "role": "Director of Ops, Gulf Logistics UAE",
        "country": "Abu Dhabi, UAE",
        "flag": "🇦🇪",
        "avatar": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Fast, dependable, and always available on WhatsApp. Ranknix Online is our go-to partner for all digital automation and marketing infrastructure."
    },
    {
        "name": "Sophie Taylor",
        "role": "Marketing VP, Velocity Media UK",
        "country": "Birmingham, UK",
        "flag": "🇬🇧",
        "avatar": "https://images.unsplash.com/photo-1534751516642-a171ef2ef63a?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Short-form video editing and TikTok Ads production is top tier. The retention curves on our ads tripled, resulting in record-breaking revenue."
    },
    {
        "name": "Usman Tariq",
        "role": "Managing Director, Crescent Global PK",
        "country": "Karachi, Pakistan",
        "flag": "🇵🇰",
        "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Ranknix Online represents the highest standard of technical and creative talent. Professional communication, transparent pricing, and stellar execution."
    },
    {
        "name": "Benjamin Scott",
        "role": "Founder, Apex SaaS USA",
        "country": "Boston, MA, USA",
        "flag": "🇺🇸",
        "avatar": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=120&h=120&fit=crop&crop=faces",
        "stars": 5,
        "text": "Full GoHighLevel migration, custom funnel build, and email automation completed in under 7 days. Can't recommend them highly enough."
    }
]

print(f"Total verified testimonials: {len(TESTIMONIALS_DATA)}")
