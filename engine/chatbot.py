"""
CampusGreenify – AI Chatbot Engine
Rule-based contextual chatbot for sustainability Q&A.
"""

import re

# ============================================================
# RESPONSE TEMPLATES
# ============================================================

RECOMMENDATION_RESPONSES = {
    "solar": {
        "why": "Solar panels are highly recommended for your campus because {climate_reason}. With India receiving 300+ sunny days per year in most regions, solar energy can offset up to 30% of your electricity consumption. Your campus size ({size}) makes it ideal for a rooftop solar installation of significant capacity.",
        "roi": "**Solar ROI Analysis:**\n- **Investment:** {cost_range}\n- **Annual Savings:** ~₹3.6 Lakhs (for medium campus)\n- **Payback Period:** ~4 years\n- **Government Subsidies:** Up to 40% under PM Surya Ghar scheme\n- **Panel Lifespan:** 25+ years\n- **Net ROI over 25 years:** 5-6x the initial investment",
        "benefits": "**Key Benefits of Solar Installation:**\n1. 🔋 30% reduction in electricity bills\n2. 🌍 25% reduction in carbon footprint\n3. 💰 Government subsidies available (up to 40%)\n4. 📈 Net metering allows selling excess power to grid\n5. 🏗️ 25-year panel lifespan with minimal maintenance\n6. 🎓 Enhances campus green reputation and rankings",
        "implement": "**Implementation Roadmap for Solar:**\n1. **Week 1-2:** Conduct solar feasibility & rooftop assessment\n2. **Week 3-4:** Select vendor and finalize panel specifications\n3. **Week 5-8:** Installation of panels and inverters\n4. **Week 9-10:** Net metering setup and grid connection\n5. **Week 11-12:** Testing, commissioning, and IoT dashboard setup\n\n**Pro Tip:** Apply for government subsidies before starting installation."
    },
    "rainwater": {
        "why": "Rainwater harvesting is crucial for your campus because {climate_reason}. Campuses typically have large rooftop areas that can collect thousands of liters of rainwater annually. This reduces your dependency on municipal water supply and helps recharge groundwater.",
        "roi": "**Rainwater Harvesting ROI:**\n- **Investment:** {cost_range}\n- **Annual Savings:** ~₹1.5 Lakhs\n- **Payback Period:** ~3 years\n- **Water Savings:** Up to 35%\n- **Additional Value:** Groundwater recharge, reduced flooding",
        "benefits": "**Key Benefits:**\n1. 💧 35% reduction in water bills\n2. 🌊 Groundwater recharge for long-term water security\n3. 🌧️ Reduces stormwater runoff and campus flooding\n4. 🔧 Low maintenance once installed\n5. ✅ Compliance with green building standards\n6. 🏗️ Mandatory in many states — stay ahead of regulations",
        "implement": "**Implementation Roadmap:**\n1. **Week 1:** Map rooftop catchment areas and runoff patterns\n2. **Week 2-3:** Design storage tanks (underground recommended)\n3. **Week 4-6:** Install filtration and first-flush diverters\n4. **Week 7-8:** Connect to non-potable water supply\n5. **Week 9:** Set up water quality monitoring\n\n**Pro Tip:** Start with the largest building rooftop for maximum collection."
    },
    "smart_energy": {
        "why": "Smart energy monitoring is essential because most campuses waste 15-25% of energy without even knowing it. IoT-based smart meters provide real-time visibility into consumption patterns, helping you identify and eliminate waste instantly.",
        "roi": "**Smart Energy Monitoring ROI:**\n- **Investment:** {cost_range}\n- **Annual Savings:** ~₹2.8 Lakhs\n- **Payback Period:** ~2 years (fastest among all solutions)\n- **Energy Savings:** Up to 20%\n- **Added Value:** Predictive maintenance, anomaly detection",
        "benefits": "**Key Benefits:**\n1. ⚡ 20% energy savings through visibility\n2. 📊 Real-time consumption dashboards\n3. 🔔 Automated alerts for anomalies and waste\n4. 🏆 Fastest ROI among all green solutions\n5. 🧠 Data-driven decision making for future investments\n6. 🔧 Preventive maintenance reduces equipment failures",
        "implement": "**Implementation Roadmap:**\n1. **Week 1:** Audit existing electrical infrastructure\n2. **Week 2-3:** Install smart meters on all major circuits\n3. **Week 4:** Deploy centralized energy dashboard\n4. **Week 5:** Configure automated alerts and reports\n5. **Week 6:** Train facility team on dashboard usage\n\n**Pro Tip:** Start with the top 3 highest-consuming buildings."
    },
    "led": {
        "why": "LED retrofitting offers the quickest and most reliable ROI of any sustainability measure. If your campus still uses conventional lighting, you're spending 60% more on lighting energy than necessary. LEDs also provide better light quality.",
        "roi": "**LED Retrofit ROI:**\n- **Investment:** {cost_range}\n- **Annual Savings:** ~₹1.8 Lakhs\n- **Payback Period:** ~1.5 years (best payback)\n- **Energy Savings:** Up to 60% on lighting\n- **Bulb Lifespan:** 50,000+ hours vs 8,000 for CFL",
        "benefits": "**Key Benefits:**\n1. 💡 Up to 60% lighting energy savings\n2. ⏱️ Quickest payback period (< 2 years)\n3. 🔋 50,000+ hour LED lifespan\n4. 📚 Better light quality improves productivity\n5. 🔧 Near-zero maintenance costs\n6. 🌡️ Less heat generation = lower cooling costs",
        "implement": "**Implementation Roadmap:**\n1. **Week 1:** Audit all lighting fixtures campus-wide\n2. **Week 2-3:** Procure LED fixtures (bulk pricing)\n3. **Week 4-6:** Phase-wise replacement (start with high-usage areas)\n4. **Week 7:** Install occupancy sensors in low-traffic areas\n5. **Week 8:** Smart scheduling for outdoor lighting\n\n**Pro Tip:** Replace high-usage areas first for immediate savings."
    },
    "composting": {
        "why": "Your campus likely generates significant organic waste from canteens and gardens. Composting converts this waste into valuable fertilizer, reducing landfill burden and methane emissions while creating a circular waste economy on campus.",
        "roi": "**Composting System ROI:**\n- **Investment:** {cost_range}\n- **Annual Savings:** ~₹1 Lakh\n- **Payback Period:** ~2.5 years\n- **Waste Reduction:** 50-60% of organic waste\n- **Added Value:** Free compost for landscaping",
        "benefits": "**Key Benefits:**\n1. 🌱 50-60% reduction in organic waste to landfill\n2. 🌿 Free high-quality compost for gardens\n3. 🌍 Reduces methane emissions significantly\n4. 📚 Educational opportunity for students\n5. ✅ Compliance with Swachh Bharat guidelines\n6. 💰 Revenue potential from excess compost",
        "implement": "**Implementation Roadmap:**\n1. **Week 1-2:** Set up waste segregation at source\n2. **Week 3-4:** Install composting units (aerobic/vermicompost)\n3. **Week 5:** Train housekeeping staff\n4. **Week 6-8:** Begin operations and monitoring\n5. **Monthly:** Quality checks and output tracking\n\n**Pro Tip:** Start with vermicomposting — it's simpler and produces higher quality compost."
    },
}

# Default responses for recommendations not in the detailed templates
DEFAULT_RESPONSES = {
    "why": "This recommendation was selected based on your campus profile ({campus_name}, {campus_type}) and your sustainability goals. It scores highly on our impact-ROI-feasibility matrix for campuses similar to yours.",
    "roi": "**ROI Overview:**\n- **Investment:** {cost_range}\n- **Payback Period:** ~{payback_years} years\n- **Annual Savings:** ~₹{annual_savings}\n- This solution offers a strong return on investment with measurable impact within the first year.",
    "benefits": "**Key Benefits:**\n- Reduces environmental impact\n- Cost savings over long term\n- Improves campus sustainability score\n- Enhances compliance readiness\n- Aligns with your goal: {main_goal}",
    "implement": "**General Implementation Steps:**\n1. Conduct detailed feasibility assessment\n2. Select vendors and get quotations\n3. Plan phased implementation\n4. Execute installation/deployment\n5. Monitor and optimize performance\n\nWould you like more specific guidance for this recommendation?"
}

# General sustainability Q&A
GENERAL_QA = {
    "sustainability score": "Your sustainability score is calculated based on multiple factors including your campus type, location, current practices, and identified gaps. A higher score means fewer sustainability gaps. The score considers energy efficiency, water management, waste handling, and carbon footprint.",
    "get started": "The best way to start is to focus on the **top 2 recommendations** shown in your dashboard. These are prioritized for maximum impact and ROI. Start with the quickest-win solution (usually LED retrofitting or smart energy monitoring) to build momentum.",
    "budget": "For a typical medium-sized campus, a comprehensive sustainability program requires ₹15-50 Lakhs initially, with most solutions paying for themselves within 2-4 years. Start with high-ROI solutions like LED retrofitting and smart energy monitoring.",
    "compliance": "Key compliance frameworks for Indian campuses include:\n- **GRIHA** (Green Rating for Integrated Habitat Assessment)\n- **IGBC** (Indian Green Building Council)\n- **BEE Star Rating** for buildings\n- **Swachh Bharat** waste management guidelines\n- **NAAC** sustainability criteria for academic institutions",
    "carbon footprint": "A typical Indian campus (medium-sized) produces 500-2000 tonnes of CO₂ annually. The biggest contributors are:\n1. Electricity consumption (60-70%)\n2. Transportation (15-20%)\n3. Waste decomposition (5-10%)\n4. Water heating (5%)\n\nOur recommendations target these in priority order.",
    "help": "I can help you with:\n- **Why** a recommendation was made\n- **ROI** and financial analysis\n- **Benefits** of each solution\n- **Implementation** steps and timelines\n- **General sustainability** questions\n\nTry asking: \"Why solar?\" or \"What's the ROI for LED?\" or \"How to start?\"",
}


def get_climate_reason(location):
    """Get climate-specific reasoning text."""
    reasons = {
        "tropical": "your tropical climate provides abundant sunshine and rainfall, making it ideal for both solar energy and water harvesting",
        "arid": "your arid climate has excellent solar irradiance levels, making solar installations highly efficient, and water conservation is critical",
        "temperate": "your temperate climate offers moderate conditions suitable for a balanced mix of sustainability solutions",
        "continental": "your continental climate with temperature extremes makes HVAC optimization and building insulation particularly impactful",
        "coastal": "your coastal location provides opportunities for both wind energy potential and rainwater harvesting from higher rainfall",
    }
    return reasons.get(location.lower(), "your location and climate conditions make this solution highly effective")


def process_chat_message(user_message, campus_profile, recommendations):
    """
    Process a user message and return an appropriate response.

    Uses keyword matching to determine intent and context.
    """
    msg = user_message.lower().strip()

    # Check for general Q&A matches first
    for key, response in GENERAL_QA.items():
        if key in msg:
            return response

    # Determine question type
    question_type = _detect_question_type(msg)

    # Determine which recommendation is being asked about
    target_rec = _detect_target_recommendation(msg, recommendations)

    if target_rec:
        return _get_recommendation_response(target_rec, question_type, campus_profile)

    # If no specific recommendation detected, check for category questions
    category = _detect_category(msg)
    if category:
        return _get_category_response(category, recommendations, campus_profile)

    # Greeting detection
    if any(greet in msg for greet in ["hello", "hi", "hey", "greetings", "good"]):
        return f"Hello! 👋 I'm your CampusGreenify AI assistant. I can help you understand the sustainability recommendations for **{campus_profile.get('name', 'your campus')}**.\n\nTry asking:\n- \"Why is solar recommended?\"\n- \"What's the ROI for LED?\"\n- \"How to implement composting?\"\n- \"What should we prioritize?\""

    # Thank you
    if any(word in msg for word in ["thank", "thanks", "great", "awesome", "perfect"]):
        return "You're welcome! 😊 Feel free to ask any other questions about your sustainability recommendations. I'm here to help you make the best decisions for your campus!"

    # Fallback
    return _get_fallback_response(campus_profile, recommendations)


def _detect_question_type(msg):
    """Detect what type of question is being asked."""
    if any(word in msg for word in ["why", "reason", "purpose", "need"]):
        return "why"
    elif any(word in msg for word in ["roi", "return", "investment", "cost", "price", "money", "save", "savings", "payback", "budget"]):
        return "roi"
    elif any(word in msg for word in ["benefit", "advantage", "pros", "good", "help", "value"]):
        return "benefits"
    elif any(word in msg for word in ["how", "implement", "install", "step", "start", "plan", "guide", "timeline", "roadmap"]):
        return "implement"
    return "why"  # Default to explaining why


def _detect_target_recommendation(msg, recommendations):
    """Detect which recommendation the user is asking about."""
    keyword_map = {
        "solar": ["solar", "panel", "photovoltaic", "pv"],
        "rainwater": ["rain", "rainwater", "harvest", "collect water"],
        "smart_energy": ["smart energy", "monitoring", "iot", "meter", "smart meter"],
        "led": ["led", "light", "lighting", "bulb", "lamp"],
        "composting": ["compost", "organic waste", "food waste"],
        "waste_segregation": ["waste", "segregation", "recycle", "recycling", "bin"],
        "green_roof": ["green roof", "roof garden", "vertical garden", "green wall"],
        "ev_charging": ["ev", "electric vehicle", "charging", "charger"],
        "greywater": ["greywater", "grey water", "gray water", "water recycling", "reuse water"],
        "smart_hvac": ["hvac", "air conditioning", "cooling", "heating", "ventilation", "ac"],
    }

    for rec_id, keywords in keyword_map.items():
        if any(kw in msg for kw in keywords):
            for rec in recommendations:
                if rec["id"] == rec_id:
                    return rec
    return None


def _detect_category(msg):
    """Detect if user is asking about a category."""
    if any(word in msg for word in ["energy", "electricity", "power"]):
        return "energy"
    elif any(word in msg for word in ["water", "irrigation"]):
        return "water"
    elif any(word in msg for word in ["waste", "garbage", "trash"]):
        return "waste"
    elif any(word in msg for word in ["carbon", "emission", "co2", "greenhouse"]):
        return "carbon"
    return None


def _get_recommendation_response(rec, question_type, campus_profile):
    """Get response for a specific recommendation and question type."""
    rec_id = rec["id"]

    # Try specific templates first
    if rec_id in RECOMMENDATION_RESPONSES:
        templates = RECOMMENDATION_RESPONSES[rec_id]
    else:
        templates = DEFAULT_RESPONSES

    template = templates.get(question_type, templates.get("why", ""))

    # Fill template variables
    response = template.format(
        climate_reason=get_climate_reason(campus_profile.get("location", "temperate")),
        cost_range=rec.get("cost_range", "₹5–15 Lakhs"),
        size=campus_profile.get("size", "Medium"),
        campus_name=campus_profile.get("name", "your campus"),
        campus_type=campus_profile.get("type", "campus"),
        payback_years=rec.get("payback_years", 3),
        annual_savings=f"{rec.get('annual_savings', 200000):,}",
        main_goal=campus_profile.get("main_goal", "Overall Sustainability"),
    )

    return response


def _get_category_response(category, recommendations, campus_profile):
    """Get response about a category of recommendations."""
    cat_recs = [r for r in recommendations if r["category"] == category]
    cat_labels = {"energy": "Energy", "water": "Water", "waste": "Waste", "carbon": "Carbon"}
    cat_name = cat_labels.get(category, category.title())

    if not cat_recs:
        return f"I don't have specific {cat_name} recommendations for your campus profile at this time."

    response = f"**{cat_name} Recommendations for {campus_profile.get('name', 'your campus')}:**\n\n"
    for i, rec in enumerate(cat_recs, 1):
        response += f"{i}. **{rec['title']}** — Score: {rec['score']}/10 | ROI: {rec['payback_years']}yr payback\n"
    response += f"\nAsk me about any specific recommendation for detailed analysis!"

    return response


def _get_fallback_response(campus_profile, recommendations):
    """Fallback response when no specific match is found."""
    top_rec = recommendations[0] if recommendations else None
    campus_name = campus_profile.get("name", "your campus")

    response = f"I'd be happy to help with sustainability planning for **{campus_name}**! 🌿\n\n"
    response += "Here are some things you can ask me:\n\n"
    if top_rec:
        response += f"- \"Why is **{top_rec['title']}** recommended?\"\n"
        response += f"- \"What's the ROI for {top_rec['title']}?\"\n"
    response += "- \"What are the benefits of solar panels?\"\n"
    response += "- \"How to implement composting?\"\n"
    response += "- \"What's our carbon footprint?\"\n"
    response += "- \"How do I get started?\"\n"

    return response
