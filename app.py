"""
CampusGreenify – Smart Planner for Eco-Campus
Main Streamlit Application
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import os
from engine.recommendations import generate_recommendations
from engine.impact import calculate_impact_metrics
from engine.chatbot import process_chat_message
from engine.report import generate_pdf_report
from styles.theme import get_custom_css

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="CampusGreenify – Smart Planner for Eco-Campus",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Inject custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# ============================================================
# SESSION STATE INIT
# ============================================================
if "current_step" not in st.session_state:
    st.session_state.current_step = 0
if "campus_profile" not in st.session_state:
    st.session_state.campus_profile = {}
if "priorities" not in st.session_state:
    st.session_state.priorities = []
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "sustainability_score" not in st.session_state:
    st.session_state.sustainability_score = 0
if "problem_areas" not in st.session_state:
    st.session_state.problem_areas = []
if "impact_metrics" not in st.session_state:
    st.session_state.impact_metrics = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def go_to_step(step):
    st.session_state.current_step = step


# ============================================================
# LOGO HELPER
# ============================================================
def render_logo():
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
    if os.path.exists(logo_path):
        return logo_path
    return None


# ============================================================
# PROGRESS BAR
# ============================================================
def render_progress_bar(current):
    steps = ["Campus Input", "Personalize", "AI Dashboard", "Impact Analysis", "Report"]
    html = '<div class="progress-container">'
    for i, label in enumerate(steps):
        step_num = i + 1
        if step_num < current:
            circle_class = "completed"
        elif step_num == current:
            circle_class = "active"
        else:
            circle_class = "inactive"
        html += f'<div class="progress-step"><div class="step-circle {circle_class}">{step_num}</div><div class="step-label">{label}</div></div>'
        if i < len(steps) - 1:
            line_class = "completed" if step_num < current else "inactive"
            html += f'<div class="step-line {line_class}"></div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# STEP 0: LANDING PAGE
# ============================================================
def render_landing():
    logo = render_logo()
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        if logo:
            st.image(logo, width=120)

    st.markdown("""
    <div class="hero-banner">
        <h1>CampusGreenify</h1>
        <p>AI-Powered Sustainability Intelligence for Campuses.<br/>
        Make smarter sustainability decisions with data-driven insights, personalized recommendations, and actionable reports.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Data-Driven Analysis</h3>
            <p>Input your campus data and get AI-powered sustainability scoring with identified problem areas.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h3>AI Recommendations</h3>
            <p>Get personalized sustainability solutions ranked by impact, ROI, and feasibility for your campus.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📄</div>
            <h3>Actionable Reports</h3>
            <p>Download comprehensive PDF reports with action plans, timelines, and projected savings.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_b:
        if st.button("🚀  Get Started", type="primary", use_container_width=True, key="get_started"):
            go_to_step(1)
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color: #5A6070; font-size: 0.85rem;">
        <strong>Trusted by campuses</strong> looking to reduce costs, cut emissions, and build a sustainable future.<br/>
        CampusGreenify — Where sustainability meets intelligence.
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# STEP 1: CAMPUS INPUT FORM
# ============================================================
def render_step1():
    render_progress_bar(1)
    st.markdown('<div class="section-header">📋 Tell us about your campus</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subheader">We need just a few details to generate your personalized sustainability plan.</div>', unsafe_allow_html=True)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            campus_name = st.text_input("Campus Name *", placeholder="e.g., Green Valley University", key="inp_name")
            campus_type = st.selectbox("Campus Type *", ["University", "College", "School", "Corporate Campus", "Government"], key="inp_type")
            location = st.selectbox("Location / Climate Zone *", ["Tropical", "Arid", "Temperate", "Continental", "Coastal"], key="inp_loc")
        with col2:
            campus_size = st.selectbox("Campus Size *", ["Small (< 5 acres)", "Medium (5–20 acres)", "Large (20–50 acres)", "Very Large (> 50 acres)"], key="inp_size")
            main_goal = st.selectbox("Main Sustainability Goal *", ["Reduce Energy Costs", "Water Conservation", "Carbon Neutrality", "Waste Reduction", "Overall Sustainability"], key="inp_goal")
            electricity_bill = st.number_input("Annual Electricity Bill ₹ (Optional)", min_value=0, value=0, step=50000, key="inp_bill", help="Helps us estimate savings more accurately")

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        if st.button("← Back", key="back_1", use_container_width=True):
            go_to_step(0)
            st.rerun()
    with col_c:
        if st.button("Next →", type="primary", key="next_1", use_container_width=True):
            if not campus_name.strip():
                st.error("Please enter a campus name.")
            else:
                st.session_state.campus_profile = {
                    "name": campus_name.strip(),
                    "type": campus_type.lower().replace(" ", "_"),
                    "location": location.lower(),
                    "size": campus_size,
                    "main_goal": main_goal,
                    "electricity_bill": electricity_bill if electricity_bill > 0 else 0,
                }
                go_to_step(2)
                st.rerun()


# ============================================================
# STEP 2: PERSONALIZE
# ============================================================
def render_step2():
    render_progress_bar(2)
    st.markdown('<div class="section-header">🎯 What matters most to your campus?</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subheader">Select your top priorities to get tailored recommendations. You can skip this step.</div>', unsafe_allow_html=True)

    priorities_options = [
        ("🔌", "Reduce Electricity Cost"),
        ("💧", "Reduce Water Wastage"),
        ("📊", "Improve Sustainability Score"),
        ("✅", "Compliance Readiness"),
        ("🌍", "Reduce Carbon Footprint"),
    ]

    selected = st.multiselect(
        "Select your priorities (choose one or more):",
        [f"{icon} {label}" for icon, label in priorities_options],
        key="priority_select",
        default=st.session_state.priorities if st.session_state.priorities else [],
    )

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        if st.button("← Back", key="back_2", use_container_width=True):
            go_to_step(1)
            st.rerun()
    with col_b:
        if st.button("Skip →", key="skip_2", use_container_width=True):
            st.session_state.priorities = []
            _generate_results()
            go_to_step(3)
            st.rerun()
    with col_c:
        if st.button("Next →", type="primary", key="next_2", use_container_width=True):
            st.session_state.priorities = selected
            _generate_results()
            go_to_step(3)
            st.rerun()


def _generate_results():
    """Run recommendation engine and impact calculations."""
    recs, score, problems = generate_recommendations(
        st.session_state.campus_profile,
        st.session_state.priorities,
    )
    st.session_state.recommendations = recs
    st.session_state.sustainability_score = score
    st.session_state.problem_areas = problems
    st.session_state.impact_metrics = calculate_impact_metrics(
        recs, st.session_state.campus_profile
    )


# ============================================================
# STEP 3: AI DASHBOARD
# ============================================================
def render_step3():
    render_progress_bar(3)
    st.markdown('<div class="section-header">📊 AI Sustainability Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-subheader">Personalized analysis for {st.session_state.campus_profile.get("name", "your campus")}</div>', unsafe_allow_html=True)

    score = st.session_state.sustainability_score
    if score >= 70:
        score_class, score_text = "score-excellent", "Excellent"
    elif score >= 55:
        score_class, score_text = "score-good", "Good"
    elif score >= 40:
        score_class, score_text = "score-moderate", "Moderate"
    else:
        score_class, score_text = "score-poor", "Needs Improvement"

    # Score + Problem Areas row
    col_score, col_problems = st.columns([1, 2])

    with col_score:
        st.markdown(f"""
        <div class="custom-card" style="text-align:center; padding:2rem;">
            <div class="score-label">SUSTAINABILITY SCORE</div>
            <div class="score-value {score_class}">{score}</div>
            <div class="score-label" style="font-size:1.1rem; font-weight:600;">{score_text}</div>
        </div>
        """, unsafe_allow_html=True)

        # Gauge chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            domain={'x': [0, 1], 'y': [0, 1]},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1},
                'bar': {'color': "#2E7D32"},
                'steps': [
                    {'range': [0, 40], 'color': "#FFCDD2"},
                    {'range': [40, 55], 'color': "#FFE0B2"},
                    {'range': [55, 70], 'color': "#FFF9C4"},
                    {'range': [70, 100], 'color': "#C8E6C9"},
                ],
                'threshold': {'line': {'color': "#1B5E20", 'width': 4}, 'thickness': 0.8, 'value': score},
            },
        ))
        fig.update_layout(height=220, margin=dict(l=20, r=20, t=20, b=20), font={'family': 'Inter'})
        st.plotly_chart(fig, use_container_width=True)

    with col_problems:
        st.markdown("**🔍 Problem Areas**")
        prob_cols = st.columns(2)
        for i, area in enumerate(st.session_state.problem_areas):
            with prob_cols[i % 2]:
                if area["status"] == "critical":
                    css_class = "problem-critical"
                elif area["status"] == "moderate":
                    css_class = "problem-moderate"
                else:
                    css_class = "problem-good"
                st.markdown(f"""
                <div class="problem-card {css_class}" style="margin-bottom:0.75rem;">
                    <div style="font-size:1.3rem;">{area['label'].split(' ')[0]}</div>
                    <div>{area['label'].split(' ', 1)[1] if ' ' in area['label'] else area['label']}</div>
                    <div style="font-size:0.8rem; margin-top:4px;">{area['status_label']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('<div class="green-divider"></div>', unsafe_allow_html=True)

    # Recommendations
    st.markdown("**🎯 Smart Recommendations**")
    st.markdown('<div class="section-subheader">Ranked by impact, ROI, and alignment with your goals</div>', unsafe_allow_html=True)

    for rec in st.session_state.recommendations[:6]:
        with st.expander(f"{rec['title']}  —  {rec.get('priority', '')}"):
            c1, c2 = st.columns([2, 1])
            with c1:
                st.write(rec["description"])
                st.markdown("**Implementation Steps:**")
                for step in rec.get("implementation_steps", []):
                    st.markdown(f"- {step}")
            with c2:
                st.metric("Payback Period", f"{rec['payback_years']} years")
                st.metric("Investment", rec["cost_range"])
                st.metric("Energy Savings", f"{rec['savings_percent']}%")
                st.metric("CO₂ Reduction", f"{rec['co2_reduction']}%")
                if rec["water_savings"] > 0:
                    st.metric("Water Savings", f"{rec['water_savings']}%")

    st.markdown('<div class="green-divider"></div>', unsafe_allow_html=True)

    # AI Chatbot
    st.markdown("**🤖 AI Sustainability Assistant**")
    st.markdown("Ask me about any recommendation — *Why?* *ROI?* *Benefits?* *How to implement?*")

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about recommendations... e.g., 'Why solar panels?'"):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = process_chat_message(prompt, st.session_state.campus_profile, st.session_state.recommendations)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        if st.button("← Back", key="back_3", use_container_width=True):
            go_to_step(2)
            st.rerun()
    with col_c:
        if st.button("View Impact Analysis →", type="primary", key="next_3", use_container_width=True):
            go_to_step(4)
            st.rerun()


# ============================================================
# STEP 4: IMPACT ANALYSIS
# ============================================================
def render_step4():
    render_progress_bar(4)
    st.markdown('<div class="section-header">📈 Impact Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subheader">Projected savings and environmental impact from recommended solutions</div>', unsafe_allow_html=True)

    metrics = st.session_state.impact_metrics

    # Metric cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-card metric-green">
            <div class="metric-icon">💰</div>
            <div class="metric-value">₹{metrics['cost_savings']:,.0f}</div>
            <div class="metric-label">Annual Savings</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card metric-blue">
            <div class="metric-icon">⚡</div>
            <div class="metric-value">{metrics['energy_savings']}%</div>
            <div class="metric-label">Energy Savings</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-card metric-teal">
            <div class="metric-icon">💧</div>
            <div class="metric-value">{metrics['water_savings']}%</div>
            <div class="metric-label">Water Savings</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="metric-card metric-orange">
            <div class="metric-icon">🌍</div>
            <div class="metric-value">{metrics['co2_reduction']}%</div>
            <div class="metric-label">CO₂ Reduction</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts
    tab1, tab2, tab3 = st.tabs(["📊 Savings Breakdown", "🍩 Impact Distribution", "📈 5-Year Projection"])

    with tab1:
        breakdown = metrics.get("breakdown", [])
        titles = [b["title"] for b in breakdown]
        savings = [b["annual_savings"] for b in breakdown]
        fig = go.Figure(go.Bar(
            x=savings, y=titles, orientation='h',
            marker=dict(color=savings, colorscale=[[0, '#A5D6A7'], [1, '#1B5E20']]),
            text=[f"₹{s:,.0f}" for s in savings], textposition='auto',
        ))
        fig.update_layout(
            title="Annual Savings by Recommendation",
            xaxis_title="Annual Savings (₹)",
            height=400, margin=dict(l=20, r=20, t=50, b=20),
            font=dict(family="Inter"), plot_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        cat_dist = metrics.get("category_distribution", {})
        fig2 = go.Figure(go.Pie(
            labels=list(cat_dist.keys()), values=list(cat_dist.values()),
            hole=0.5,
            marker=dict(colors=['#2E7D32', '#1976D2', '#FF9800', '#00796B']),
            textinfo='label+percent',
        ))
        fig2.update_layout(
            title="Savings Distribution by Category",
            height=400, font=dict(family="Inter"),
        )
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        timeline = metrics.get("timeline", [])
        years = [t["year"] for t in timeline]
        annual = [t["annual_savings"] for t in timeline]
        cumulative = [t["cumulative_savings"] for t in timeline]
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=years, y=annual, name="Annual Savings", marker_color='#A5D6A7'))
        fig3.add_trace(go.Scatter(x=years, y=cumulative, name="Cumulative Savings", line=dict(color='#2E7D32', width=3), mode='lines+markers'))
        fig3.update_layout(
            title="5-Year Projected Savings",
            yaxis_title="Amount (₹)", height=400,
            font=dict(family="Inter"), plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
        )
        st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_a:
        if st.button("← Back to Dashboard", key="back_4", use_container_width=True):
            go_to_step(3)
            st.rerun()
    with col_c:
        if st.button("Generate Report →", type="primary", key="next_4", use_container_width=True):
            go_to_step(5)
            st.rerun()


# ============================================================
# STEP 5: REPORT
# ============================================================
def render_step5():
    render_progress_bar(5)
    st.markdown('<div class="section-header">📄 Sustainability Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subheader">Download your comprehensive sustainability assessment report</div>', unsafe_allow_html=True)

    profile = st.session_state.campus_profile
    score = st.session_state.sustainability_score
    recs = st.session_state.recommendations
    metrics = st.session_state.impact_metrics
    priorities = st.session_state.priorities

    # Report preview
    st.markdown(f"""
    <div class="report-preview">
        <div class="report-header">
            <h2 style="color:#2E7D32; margin:0;">CampusGreenify</h2>
            <h3 style="color:#1A1A2E; margin:0.5rem 0;">Sustainability Assessment Report</h3>
            <p style="color:#5A6070;">{profile.get('name', 'Campus')}</p>
        </div>
        <div class="report-section">
            <h3>📋 Campus Profile</h3>
            <p><strong>Type:</strong> {profile.get('type', 'N/A').replace('_', ' ').title()} &nbsp;|&nbsp;
            <strong>Location:</strong> {profile.get('location', 'N/A').title()} &nbsp;|&nbsp;
            <strong>Size:</strong> {profile.get('size', 'N/A')}</p>
            <p><strong>Goal:</strong> {profile.get('main_goal', 'N/A')}</p>
        </div>
        <div class="report-section">
            <h3>📊 Sustainability Score: <span style="color:#2E7D32;">{score}/100</span></h3>
        </div>
        <div class="report-section">
            <h3>🎯 Top Recommendations</h3>
            {''.join(f'<p>• <strong>{r["title"]}</strong> — {r.get("priority", "")}</p>' for r in recs[:5])}
        </div>
        <div class="report-section">
            <h3>📈 Impact Summary</h3>
            <p>💰 Annual Savings: <strong>₹{metrics["cost_savings"]:,.0f}</strong> &nbsp;|&nbsp;
            ⚡ Energy: <strong>{metrics["energy_savings"]}%</strong> &nbsp;|&nbsp;
            💧 Water: <strong>{metrics["water_savings"]}%</strong> &nbsp;|&nbsp;
            🌍 CO₂: <strong>{metrics["co2_reduction"]}%</strong></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Generate PDF
    col_a, col_b, col_c = st.columns([1, 1, 1])
    with col_b:
        pdf_bytes = generate_pdf_report(profile, priorities, recs, score, metrics)
        campus_name_safe = profile.get("name", "campus").replace(" ", "_")
        st.download_button(
            label="📥  Download Full PDF Report",
            data=pdf_bytes,
            file_name=f"CampusGreenify_{campus_name_safe}_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary",
        )

    st.markdown("<br>", unsafe_allow_html=True)
    col_a2, col_b2, col_c2 = st.columns([1, 1, 1])
    with col_a2:
        if st.button("← Back to Impact Analysis", key="back_5", use_container_width=True):
            go_to_step(4)
            st.rerun()
    with col_c2:
        if st.button("🔄 Start New Assessment", key="restart", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:#5A6070; font-size:0.85rem; padding:1rem;">
        <strong>CampusGreenify</strong> — AI-Powered Sustainability Intelligence for Campuses<br/>
        Making campuses greener, one decision at a time. 🌿
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MAIN ROUTER
# ============================================================
def main():
    step = st.session_state.current_step
    if step == 0:
        render_landing()
    elif step == 1:
        render_step1()
    elif step == 2:
        render_step2()
    elif step == 3:
        render_step3()
    elif step == 4:
        render_step4()
    elif step == 5:
        render_step5()


if __name__ == "__main__":
    main()
else:
    main()
