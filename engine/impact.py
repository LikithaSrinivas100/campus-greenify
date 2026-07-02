"""
CampusGreenify – Impact Analysis Engine
Calculates projected savings, CO2 reduction, and generates timeline data.
"""


def calculate_impact_metrics(recommendations, campus_profile):
    """
    Calculate aggregate impact metrics from top recommendations.

    Returns dict with:
    - cost_savings: Annual cost savings in ₹
    - energy_savings: Percentage energy savings
    - water_savings: Percentage water savings
    - co2_reduction: Percentage CO2 reduction
    - breakdown: Per-recommendation savings
    - timeline: 5-year projected savings
    """
    top_recs = recommendations[:6]  # Top 6 recommendations

    # Base electricity bill for calculations
    base_bill = campus_profile.get("electricity_bill", 0)
    if not base_bill or base_bill == 0:
        # Estimate based on campus size
        size_bills = {
            "Small (< 5 acres)": 200000,
            "Medium (5–20 acres)": 500000,
            "Large (20–50 acres)": 1200000,
            "Very Large (> 50 acres)": 2500000,
        }
        base_bill = size_bills.get(campus_profile.get("size", "Medium (5–20 acres)"), 500000)

    # Calculate per-recommendation impact
    breakdown = []
    total_energy_savings = 0
    total_water_savings = 0
    total_co2_reduction = 0
    total_annual_savings = 0

    for rec in top_recs:
        # Scale savings by campus size
        size_multiplier = {
            "Small (< 5 acres)": 0.6,
            "Medium (5–20 acres)": 1.0,
            "Large (20–50 acres)": 1.5,
            "Very Large (> 50 acres)": 2.2,
        }.get(campus_profile.get("size", "Medium (5–20 acres)"), 1.0)

        annual_saving = int(rec["annual_savings"] * size_multiplier)

        breakdown.append({
            "title": rec["title"],
            "icon": rec["icon"],
            "category": rec["category"],
            "annual_savings": annual_saving,
            "energy_savings": rec["savings_percent"],
            "water_savings": rec["water_savings"],
            "co2_reduction": rec["co2_reduction"],
            "payback_years": rec["payback_years"],
            "cost_range": rec["cost_range"],
        })

        total_annual_savings += annual_saving
        total_energy_savings += rec["savings_percent"]
        total_water_savings += rec["water_savings"]
        total_co2_reduction += rec["co2_reduction"]

    # Cap percentages at reasonable values
    total_energy_savings = min(total_energy_savings, 65)
    total_water_savings = min(total_water_savings, 60)
    total_co2_reduction = min(total_co2_reduction, 55)

    # Generate 5-year timeline
    timeline = generate_savings_timeline(total_annual_savings, top_recs)

    return {
        "cost_savings": total_annual_savings,
        "energy_savings": total_energy_savings,
        "water_savings": total_water_savings,
        "co2_reduction": total_co2_reduction,
        "base_bill": base_bill,
        "breakdown": breakdown,
        "timeline": timeline,
        "category_distribution": _category_distribution(breakdown),
    }


def generate_savings_timeline(annual_savings, recommendations):
    """
    Generate 5-year projected savings with progressive implementation.
    Year 1: 30% of full potential (initial implementation)
    Year 2: 60% (most systems operational)
    Year 3: 85% (full deployment)
    Year 4: 95% (optimized)
    Year 5: 100% (mature operation)
    """
    adoption_curve = [0.30, 0.60, 0.85, 0.95, 1.00]
    cumulative = 0

    timeline = []
    for year, adoption in enumerate(adoption_curve, 1):
        year_savings = int(annual_savings * adoption)
        cumulative += year_savings
        timeline.append({
            "year": f"Year {year}",
            "annual_savings": year_savings,
            "cumulative_savings": cumulative,
            "adoption_percent": int(adoption * 100),
        })

    return timeline


def _category_distribution(breakdown):
    """Calculate savings distribution by category."""
    categories = {}
    for item in breakdown:
        cat = item["category"]
        cat_label = {
            "energy": "Energy",
            "water": "Water",
            "waste": "Waste",
            "carbon": "Carbon",
        }.get(cat, cat.title())

        if cat_label not in categories:
            categories[cat_label] = 0
        categories[cat_label] += item["annual_savings"]

    return categories


def get_impact_summary_text(metrics):
    """Generate a text summary of impact metrics for the report."""
    summary = []
    summary.append(f"Annual Cost Savings: ₹{metrics['cost_savings']:,.0f}")
    summary.append(f"Energy Savings: {metrics['energy_savings']}%")
    summary.append(f"Water Savings: {metrics['water_savings']}%")
    summary.append(f"CO₂ Reduction: {metrics['co2_reduction']}%")
    summary.append(f"5-Year Cumulative Savings: ₹{metrics['timeline'][-1]['cumulative_savings']:,.0f}")
    return "\n".join(summary)
