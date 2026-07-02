"""
CampusGreenify – Recommendation Engine
Rule-based AI system for generating personalized sustainability recommendations.
"""

# ============================================================
# RECOMMENDATION DATASET
# ============================================================

RECOMMENDATIONS_DB = [
    {
        "id": "solar",
        "title": "☀️ Solar Panel Installation",
        "icon": "☀️",
        "description": "Install rooftop and ground-mounted solar panels to generate clean, renewable energy. Reduces dependency on grid power and long-term electricity costs significantly.",
        "category": "energy",
        "impact": 9,
        "roi": 8,
        "feasibility": 7,
        "best_climate": ["tropical", "arid"],
        "best_campus": ["university", "college", "corporate", "government", "school"],
        "savings_percent": 30,
        "co2_reduction": 25,
        "water_savings": 0,
        "cost_range": "₹15–40 Lakhs",
        "payback_years": 4,
        "annual_savings": 360000,
        "implementation_steps": [
            "Conduct solar feasibility & rooftop assessment",
            "Select solar panel vendor (monocrystalline recommended)",
            "Install panels with net metering setup",
            "Monitor via IoT-enabled solar dashboard",
            "Apply for government solar subsidies"
        ],
        "benefits": [
            "30% reduction in electricity bills",
            "25-year panel lifespan with minimal maintenance",
            "Government subsidies available (up to 40%)",
            "Enhances campus green image",
            "Net metering allows selling excess power"
        ]
    },
    {
        "id": "rainwater",
        "title": "🌧️ Rainwater Harvesting System",
        "icon": "🌧️",
        "description": "Implement rooftop rainwater collection and filtration systems to reduce water consumption and recharge groundwater tables across the campus.",
        "category": "water",
        "impact": 8,
        "roi": 7,
        "feasibility": 8,
        "best_climate": ["tropical", "coastal", "temperate"],
        "best_campus": ["university", "college", "school"],
        "savings_percent": 5,
        "co2_reduction": 5,
        "water_savings": 35,
        "cost_range": "₹3–10 Lakhs",
        "payback_years": 3,
        "annual_savings": 150000,
        "implementation_steps": [
            "Map rooftop catchment areas and runoff patterns",
            "Design storage tanks (underground/overhead)",
            "Install filtration and first-flush diverters",
            "Connect to non-potable water supply (toilets, gardens)",
            "Set up water quality monitoring"
        ],
        "benefits": [
            "35% reduction in water bills",
            "Groundwater recharge for long-term water security",
            "Reduces stormwater runoff and flooding",
            "Low maintenance once installed",
            "Compliance with green building standards"
        ]
    },
    {
        "id": "smart_energy",
        "title": "⚡ Smart Energy Monitoring",
        "icon": "⚡",
        "description": "Deploy IoT-based smart meters and energy management systems to monitor, analyze, and optimize energy consumption across all campus buildings in real-time.",
        "category": "energy",
        "impact": 7,
        "roi": 9,
        "feasibility": 8,
        "best_climate": ["tropical", "arid", "temperate", "continental", "coastal"],
        "best_campus": ["university", "college", "corporate", "government", "school"],
        "savings_percent": 20,
        "co2_reduction": 15,
        "water_savings": 0,
        "cost_range": "₹5–15 Lakhs",
        "payback_years": 2,
        "annual_savings": 280000,
        "implementation_steps": [
            "Audit existing electrical infrastructure",
            "Install smart meters on all major circuits",
            "Deploy centralized energy dashboard",
            "Set up automated alerts for anomalies",
            "Train facility team on dashboard usage"
        ],
        "benefits": [
            "20% energy savings through visibility",
            "Identify energy waste instantly",
            "Fastest ROI among all green solutions",
            "Data-driven decision making",
            "Preventive maintenance alerts"
        ]
    },
    {
        "id": "led",
        "title": "💡 LED Lighting Retrofit",
        "icon": "💡",
        "description": "Replace all conventional lighting (CFL, tube lights) with energy-efficient LED fixtures and smart lighting controls with occupancy sensors.",
        "category": "energy",
        "impact": 6,
        "roi": 9,
        "feasibility": 9,
        "best_climate": ["tropical", "arid", "temperate", "continental", "coastal"],
        "best_campus": ["university", "college", "corporate", "government", "school"],
        "savings_percent": 15,
        "co2_reduction": 10,
        "water_savings": 0,
        "cost_range": "₹2–8 Lakhs",
        "payback_years": 1.5,
        "annual_savings": 180000,
        "implementation_steps": [
            "Audit all lighting fixtures campus-wide",
            "Replace with appropriate LED fixtures",
            "Install occupancy sensors in low-traffic areas",
            "Add daylight harvesting sensors near windows",
            "Set up smart scheduling for outdoor lighting"
        ],
        "benefits": [
            "Up to 60% lighting energy savings",
            "LED lifespan 50,000+ hours vs 8,000 for CFL",
            "Quickest payback period (< 2 years)",
            "Better light quality improves productivity",
            "Reduced maintenance costs"
        ]
    },
    {
        "id": "composting",
        "title": "🌱 Composting System",
        "icon": "🌱",
        "description": "Set up organic waste composting infrastructure to convert food and garden waste into nutrient-rich compost, reducing landfill dependency and campus waste footprint.",
        "category": "waste",
        "impact": 7,
        "roi": 6,
        "feasibility": 8,
        "best_climate": ["tropical", "temperate", "coastal"],
        "best_campus": ["university", "college", "school"],
        "savings_percent": 5,
        "co2_reduction": 12,
        "water_savings": 5,
        "cost_range": "₹2–6 Lakhs",
        "payback_years": 2.5,
        "annual_savings": 100000,
        "implementation_steps": [
            "Segregate organic waste at source (canteens, gardens)",
            "Set up composting units (aerobic/vermicompost)",
            "Train housekeeping staff on waste segregation",
            "Use compost in campus landscaping",
            "Monitor compost quality and output"
        ],
        "benefits": [
            "50–60% reduction in organic waste to landfill",
            "Free high-quality compost for gardens",
            "Reduces methane emissions from landfills",
            "Educational opportunity for students",
            "Compliance with Swachh Bharat guidelines"
        ]
    },
    {
        "id": "waste_segregation",
        "title": "♻️ Smart Waste Segregation",
        "icon": "♻️",
        "description": "Implement a comprehensive waste segregation system with color-coded bins, awareness campaigns, and partnerships with recycling vendors.",
        "category": "waste",
        "impact": 6,
        "roi": 7,
        "feasibility": 9,
        "best_climate": ["tropical", "arid", "temperate", "continental", "coastal"],
        "best_campus": ["university", "college", "corporate", "government", "school"],
        "savings_percent": 3,
        "co2_reduction": 8,
        "water_savings": 0,
        "cost_range": "₹1–3 Lakhs",
        "payback_years": 1,
        "annual_savings": 80000,
        "implementation_steps": [
            "Install color-coded bins (Wet/Dry/Hazardous/E-waste)",
            "Partner with certified recycling vendors",
            "Run campus-wide awareness campaigns",
            "Appoint waste champions per department",
            "Track and report waste metrics monthly"
        ],
        "benefits": [
            "Revenue from recyclable materials",
            "Lower waste disposal costs",
            "Improved campus cleanliness",
            "Regulatory compliance",
            "Student engagement and awareness"
        ]
    },
    {
        "id": "green_roof",
        "title": "🏗️ Green Roof & Walls",
        "icon": "🏗️",
        "description": "Install vegetated green roofs and vertical green walls on campus buildings to improve insulation, reduce urban heat island effect, and enhance biodiversity.",
        "category": "carbon",
        "impact": 7,
        "roi": 5,
        "feasibility": 6,
        "best_climate": ["temperate", "continental", "tropical"],
        "best_campus": ["university", "corporate"],
        "savings_percent": 10,
        "co2_reduction": 15,
        "water_savings": 10,
        "cost_range": "₹10–30 Lakhs",
        "payback_years": 6,
        "annual_savings": 200000,
        "implementation_steps": [
            "Structural assessment of buildings",
            "Design green roof layers (waterproof, drainage, soil, plants)",
            "Select native, drought-resistant plant species",
            "Install irrigation and maintenance systems",
            "Monitor building temperature and energy savings"
        ],
        "benefits": [
            "15–25% reduction in cooling costs",
            "Absorbs CO₂ and produces oxygen",
            "Reduces urban heat island effect",
            "Increases building lifespan (protects roof membrane)",
            "Beautiful green aesthetic for campus"
        ]
    },
    {
        "id": "ev_charging",
        "title": "🚗 EV Charging Infrastructure",
        "icon": "🚗",
        "description": "Install electric vehicle charging stations across campus to support the transition to clean mobility for students, staff, and visitors.",
        "category": "carbon",
        "impact": 5,
        "roi": 5,
        "feasibility": 7,
        "best_climate": ["tropical", "arid", "temperate", "continental", "coastal"],
        "best_campus": ["university", "corporate", "government"],
        "savings_percent": 5,
        "co2_reduction": 10,
        "water_savings": 0,
        "cost_range": "₹5–20 Lakhs",
        "payback_years": 5,
        "annual_savings": 120000,
        "implementation_steps": [
            "Survey parking areas for optimal charger placement",
            "Install Level 2 and DC fast chargers",
            "Integrate with solar panels for green charging",
            "Set up payment/booking app for users",
            "Partner with EV manufacturers for subsidies"
        ],
        "benefits": [
            "Supports India's EV adoption goals",
            "Revenue from charging fees",
            "Reduces campus Scope 3 emissions",
            "Attracts eco-conscious students and staff",
            "Future-proofs campus infrastructure"
        ]
    },
    {
        "id": "greywater",
        "title": "💧 Greywater Recycling",
        "icon": "💧",
        "description": "Install greywater treatment and recycling systems to reuse water from sinks, showers, and laundry for toilet flushing and landscaping irrigation.",
        "category": "water",
        "impact": 8,
        "roi": 6,
        "feasibility": 6,
        "best_climate": ["arid", "tropical"],
        "best_campus": ["university", "college", "corporate"],
        "savings_percent": 5,
        "co2_reduction": 3,
        "water_savings": 40,
        "cost_range": "₹8–20 Lakhs",
        "payback_years": 4,
        "annual_savings": 200000,
        "implementation_steps": [
            "Audit water usage and greywater generation points",
            "Design treatment system (filtration + UV/chlorination)",
            "Install dual plumbing for greywater distribution",
            "Connect to toilet flush and irrigation systems",
            "Monitor water quality and system performance"
        ],
        "benefits": [
            "40% reduction in freshwater consumption",
            "Significant water bill savings",
            "Reduces load on sewage treatment",
            "Ideal for water-scarce regions",
            "Compliance with water recycling mandates"
        ]
    },
    {
        "id": "smart_hvac",
        "title": "🌡️ Smart HVAC Optimization",
        "icon": "🌡️",
        "description": "Upgrade heating, ventilation, and air conditioning systems with smart controls, VFDs, and AI-based scheduling to dramatically reduce energy consumption.",
        "category": "energy",
        "impact": 8,
        "roi": 7,
        "feasibility": 6,
        "best_climate": ["temperate", "continental", "arid", "tropical"],
        "best_campus": ["university", "corporate", "government"],
        "savings_percent": 25,
        "co2_reduction": 20,
        "water_savings": 0,
        "cost_range": "₹10–35 Lakhs",
        "payback_years": 3.5,
        "annual_savings": 400000,
        "implementation_steps": [
            "HVAC energy audit across all buildings",
            "Install variable frequency drives (VFDs) on AHUs",
            "Deploy smart thermostats with occupancy sensing",
            "Implement AI-based scheduling algorithms",
            "Set up centralized BMS (Building Management System)"
        ],
        "benefits": [
            "25–35% HVAC energy savings",
            "Improved occupant thermal comfort",
            "Extended equipment lifespan",
            "Reduced peak demand charges",
            "Real-time monitoring and control"
        ]
    },
]

# ============================================================
# GOAL CATEGORY MAPPING
# ============================================================

GOAL_CATEGORY_MAP = {
    "Reduce Energy Costs": "energy",
    "Water Conservation": "water",
    "Carbon Neutrality": "carbon",
    "Waste Reduction": "waste",
    "Overall Sustainability": "overall",
}

PRIORITY_CATEGORY_MAP = {
    "🔌 Reduce Electricity Cost": "energy",
    "💧 Reduce Water Wastage": "water",
    "📊 Improve Sustainability Score": "overall",
    "✅ Compliance Readiness": "compliance",
    "🌍 Reduce Carbon Footprint": "carbon",
}

SIZE_MULTIPLIER = {
    "Small (< 5 acres)": 0.8,
    "Medium (5–20 acres)": 1.0,
    "Large (20–50 acres)": 1.3,
    "Very Large (> 50 acres)": 1.6,
}

# ============================================================
# SCORING ENGINE
# ============================================================

def calculate_recommendation_score(rec, campus_profile, priorities):
    """
    Calculate composite score for a recommendation based on campus profile.

    Formula: Score = (Impact × 0.30) + (ROI × 0.25) + (GoalAlignment × 0.25) + (Feasibility × 0.20)
    Plus context-specific boosts.
    """
    # Base composite score (normalized to 10)
    base_score = (
        rec["impact"] * 0.30 +
        rec["roi"] * 0.25 +
        rec["feasibility"] * 0.20
    )

    # Goal alignment score
    goal_alignment = 0
    main_goal_category = GOAL_CATEGORY_MAP.get(campus_profile.get("main_goal", ""), "overall")

    if main_goal_category == "overall":
        goal_alignment = 6  # Moderate boost for all
    elif rec["category"] == main_goal_category:
        goal_alignment = 10  # Perfect match
    else:
        goal_alignment = 3  # Partial relevance

    base_score += goal_alignment * 0.25

    # ---- CONTEXT BOOSTS ----

    # Climate match boost
    location = campus_profile.get("location", "").lower()
    if location in rec["best_climate"]:
        base_score += 2.0

    # Campus type match boost
    campus_type = campus_profile.get("type", "").lower()
    if campus_type in rec["best_campus"]:
        base_score += 1.5

    # Priority alignment boost
    for priority in priorities:
        p_category = PRIORITY_CATEGORY_MAP.get(priority, "")
        if p_category == rec["category"]:
            base_score += 1.0
        elif p_category == "overall":
            base_score += 0.5
        elif p_category == "compliance":
            # Compliance boosts waste and carbon recommendations
            if rec["category"] in ["waste", "carbon"]:
                base_score += 0.75

    # Size factor — larger campuses benefit more from infrastructure
    size = campus_profile.get("size", "Medium (5–20 acres)")
    size_mult = SIZE_MULTIPLIER.get(size, 1.0)
    if rec["id"] in ["solar", "smart_hvac", "green_roof", "ev_charging", "greywater"]:
        base_score += (size_mult - 0.8) * 2  # Boost for larger campuses

    # High electricity bill boost
    bill = campus_profile.get("electricity_bill", 0)
    if bill and bill > 500000 and rec["category"] == "energy":
        base_score += 1.5
    elif bill and bill > 300000 and rec["category"] == "energy":
        base_score += 0.75

    return round(base_score, 2)


def generate_recommendations(campus_profile, priorities):
    """
    Generate ranked recommendations based on campus profile and priorities.
    Returns: (recommendations_list, sustainability_score, problem_areas)
    """
    scored = []
    for rec in RECOMMENDATIONS_DB:
        score = calculate_recommendation_score(rec, campus_profile, priorities)
        rec_copy = rec.copy()
        rec_copy["score"] = score
        scored.append(rec_copy)

    # Sort by score descending
    scored.sort(key=lambda x: x["score"], reverse=True)

    # Assign priority labels
    for i, rec in enumerate(scored):
        if i < 2:
            rec["priority"] = "High Priority"
            rec["priority_class"] = "badge-high"
        elif i < 5:
            rec["priority"] = "Medium Priority"
            rec["priority_class"] = "badge-medium"
        else:
            rec["priority"] = "Explore Later"
            rec["priority_class"] = "badge-low"

    # Calculate sustainability score (0-100)
    # Based on how well the campus can improve with top recommendations
    max_possible_score = max(r["score"] for r in scored) if scored else 1
    top_5_avg = sum(r["score"] for r in scored[:5]) / 5 if len(scored) >= 5 else sum(r["score"] for r in scored) / len(scored)

    # Normalize to 0-100 scale
    # Higher score = more room for improvement = lower current sustainability
    raw_score = (top_5_avg / max_possible_score) * 100
    # Invert — if recommendations score high, campus has more gaps
    sustainability_score = max(15, min(85, int(100 - raw_score * 0.4 + 20)))

    # Adjust based on priorities and profile completeness
    if len(priorities) >= 3:
        sustainability_score = max(15, sustainability_score - 5)  # More concerns = lower score
    if campus_profile.get("electricity_bill", 0) and campus_profile["electricity_bill"] > 500000:
        sustainability_score = max(15, sustainability_score - 5)

    # Identify problem areas
    problem_areas = _identify_problem_areas(scored, campus_profile, priorities)

    return scored, sustainability_score, problem_areas


def _identify_problem_areas(scored_recs, campus_profile, priorities):
    """Identify campus problem areas based on recommendations and inputs."""
    categories = {"energy": [], "water": [], "waste": [], "carbon": []}

    for rec in scored_recs:
        cat = rec["category"]
        if cat in categories:
            categories[cat].append(rec["score"])

    # Calculate average score per category
    category_scores = {}
    for cat, scores in categories.items():
        if scores:
            category_scores[cat] = sum(scores) / len(scores)

    # Map goal to a boost for that category
    main_goal_category = GOAL_CATEGORY_MAP.get(campus_profile.get("main_goal", ""), "overall")

    problem_areas = []
    category_labels = {
        "energy": ("⚡ Energy Management", "Energy consumption and efficiency"),
        "water": ("💧 Water Management", "Water usage and conservation"),
        "waste": ("♻️ Waste Management", "Waste reduction and recycling"),
        "carbon": ("🌍 Carbon Footprint", "Carbon emissions and offset"),
    }

    for cat, (label, desc) in category_labels.items():
        avg_score = category_scores.get(cat, 5)
        # Higher recommendation scores = bigger gap = more critical
        if avg_score > 7 or cat == main_goal_category:
            status = "critical"
            status_label = "🔴 Needs Attention"
        elif avg_score > 5.5:
            status = "moderate"
            status_label = "🟡 Moderate"
        else:
            status = "good"
            status_label = "🟢 On Track"

        # Override based on priorities
        for p in priorities:
            p_cat = PRIORITY_CATEGORY_MAP.get(p, "")
            if p_cat == cat and status != "critical":
                status = "moderate"
                status_label = "🟡 Needs Improvement"

        problem_areas.append({
            "category": cat,
            "label": label,
            "description": desc,
            "status": status,
            "status_label": status_label,
        })

    return problem_areas


def get_recommendation_by_id(rec_id):
    """Get a specific recommendation by its ID."""
    for rec in RECOMMENDATIONS_DB:
        if rec["id"] == rec_id:
            return rec
    return None
