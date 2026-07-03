"""CampusGreenify – Smart Planner for Eco-Campus"""
import streamlit as st
import plotly.graph_objects as go
import os
from engine.recommendations import generate_recommendations
from engine.impact import calculate_impact_metrics
from engine.chatbot import process_chat_message
from engine.report import generate_pdf_report
from styles.theme import get_custom_css

st.set_page_config(page_title="CampusGreenify", page_icon="🌿", layout="wide", initial_sidebar_state="collapsed")
st.markdown(get_custom_css(), unsafe_allow_html=True)

for k, d in [("current_step",0),("campus_profile",{}),("priorities",[]),("recommendations",[]),
             ("sustainability_score",0),("problem_areas",[]),("impact_metrics",{}),("chat_history",[])]:
    if k not in st.session_state: st.session_state[k] = d

def go_to(s): st.session_state.current_step = s

def nav():
    logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
    logo_html = ""
    if os.path.exists(logo_path):
        import base64
        with open(logo_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        logo_html = f'<img src="data:image/png;base64,{b64}" style="height:32px;border-radius:8px;">'
    st.markdown(f"""
    <div class="top-nav">
      <div class="nav-brand">
        {logo_html}
        <span class="nav-brand-name">CampusGreenify</span>
        <span class="nav-brand-badge">MVP</span>
      </div>
      <span class="nav-tagline">🌿 AI-Powered Sustainability Intelligence</span>
    </div>""", unsafe_allow_html=True)

def progress(cur):
    steps = ["Campus","Personalize","Dashboard","Impact","Report"]
    html = '<div class="progress-wrapper"><div class="progress-container">'
    for i, lbl in enumerate(steps):
        n = i+1
        cls = "active" if n==cur else ("completed" if n<cur else "inactive")
        lcls = "active-label" if n==cur else ""
        icon = "✓" if n<cur else str(n)
        html += f'<div class="progress-step"><div class="step-circle {cls}">{icon}</div><div class="step-label {lcls}">{lbl}</div></div>'
        if i < len(steps)-1:
            lc = "completed" if n<cur else "inactive"
            html += f'<div class="step-line {lc}"></div>'
    html += '</div></div>'
    st.markdown(html, unsafe_allow_html=True)

def render_landing():
    nav()
    st.markdown("""
    <div class="hero-banner anim-up">
      <div class="hero-badge">✦ AI-Powered Platform</div>
      <h1>CampusGreenify</h1>
      <p>Transform your campus into an eco-smart hub. Get personalized AI recommendations,<br>projected savings, and a downloadable sustainability roadmap — in minutes.</p>
      <div class="hero-stats">
        <div class="hero-stat"><div class="hero-stat-value">10+</div><div class="hero-stat-label">Green Solutions</div></div>
        <div class="hero-stat-divider"></div>
        <div class="hero-stat"><div class="hero-stat-value">₹870K</div><div class="hero-stat-label">Avg Annual Savings</div></div>
        <div class="hero-stat-divider"></div>
        <div class="hero-stat"><div class="hero-stat-value">65%</div><div class="hero-stat-label">Energy Reduction</div></div>
      </div>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    cards = [
        ("📊","Data-Driven Analysis","Input campus profile → get AI sustainability scoring with identified problem areas.","anim-d1"),
        ("🤖","Smart Recommendations","10 solutions ranked by Impact, ROI & Feasibility tailored to your campus.","anim-d2"),
        ("📄","PDF Action Report","Download a professional sustainability roadmap with phased action plans.","anim-d3"),
    ]
    for col, (icon, title, desc, delay) in zip([c1,c2,c3], cards):
        with col:
            st.markdown(f"""
            <div class="feature-card anim-up {delay}">
              <div class="feature-icon-wrap">{icon}</div>
              <h3>{title}</h3>
              <p>{desc}</p>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _, cb, _ = st.columns([1.5,1,1.5])
    with cb:
        if st.button("🚀  Get Started — It's Free", type="primary", use_container_width=True, key="gs"):
            go_to(1); st.rerun()
    st.markdown('<div class="app-footer">Made with 💚 by Team CampusGreenify · <strong>Sustainability Intelligence Platform</strong></div>', unsafe_allow_html=True)

def render_step1():
    nav(); progress(1)
    st.markdown('<div class="page-header"><div class="green-line"></div><h2>📋 Tell us about your campus</h2><p>Just a few details to generate your personalized sustainability roadmap.</p></div>', unsafe_allow_html=True)
    with st.container():
        c1,c2 = st.columns(2)
        with c1:
            name = st.text_input("Campus Name *", placeholder="e.g. Green Valley University", key="n")
            ctype = st.selectbox("Campus Type *", ["University","College","School","Corporate Campus","Government"], key="t")
            loc = st.selectbox("Climate Zone *", ["Tropical","Arid","Temperate","Continental","Coastal"], key="l")
        with c2:
            size = st.selectbox("Campus Size *", ["Small (< 5 acres)","Medium (5–20 acres)","Large (20–50 acres)","Very Large (> 50 acres)"], key="s")
            goal = st.selectbox("Main Goal *", ["Reduce Energy Costs","Water Conservation","Carbon Neutrality","Waste Reduction","Overall Sustainability"], key="g")
            bill = st.number_input("Annual Electricity Bill ₹ (Optional)", min_value=0, value=0, step=50000, key="b")
    st.markdown("<br>", unsafe_allow_html=True)
    ca,_,cc = st.columns(3)
    with ca:
        if st.button("← Back", key="b1", use_container_width=True): go_to(0); st.rerun()
    with cc:
        if st.button("Next: Set Priorities →", type="primary", key="n1", use_container_width=True):
            if not name.strip(): st.error("Please enter your campus name.")
            else:
                st.session_state.campus_profile = {"name":name.strip(),"type":ctype.lower().replace(" ","_"),"location":loc.lower(),"size":size,"main_goal":goal,"electricity_bill":bill if bill>0 else 0}
                go_to(2); st.rerun()

def render_step2():
    nav(); progress(2)
    st.markdown('<div class="page-header"><div class="green-line"></div><h2>🎯 What matters most to your campus?</h2><p>Select priorities to fine-tune your AI recommendations (or skip to use defaults).</p></div>', unsafe_allow_html=True)
    opts = ["🔌 Reduce Electricity Cost","💧 Reduce Water Wastage","📊 Improve Sustainability Score","✅ Compliance Readiness","🌍 Reduce Carbon Footprint"]
    sel = st.multiselect("Select your top priorities:", opts, key="ps", default=st.session_state.priorities or [])
    st.markdown("<br>", unsafe_allow_html=True)
    ca,cb,cc = st.columns(3)
    with ca:
        if st.button("← Back", key="b2", use_container_width=True): go_to(1); st.rerun()
    with cb:
        if st.button("Skip →", key="sk2", use_container_width=True):
            st.session_state.priorities=[]; _gen(); go_to(3); st.rerun()
    with cc:
        if st.button("Analyse My Campus →", type="primary", key="n2", use_container_width=True):
            st.session_state.priorities=sel; _gen(); go_to(3); st.rerun()

def _gen():
    r,s,p = generate_recommendations(st.session_state.campus_profile, st.session_state.priorities)
    st.session_state.recommendations=r; st.session_state.sustainability_score=s; st.session_state.problem_areas=p
    st.session_state.impact_metrics = calculate_impact_metrics(r, st.session_state.campus_profile)

def render_step3():
    nav(); progress(3)
    score = st.session_state.sustainability_score
    name = st.session_state.campus_profile.get("name","Your Campus")
    st.markdown(f'<div class="page-header"><div class="green-line"></div><h2>📊 AI Dashboard – {name}</h2><p>Your personalised sustainability analysis is ready.</p></div>', unsafe_allow_html=True)

    if score>=70: status,sc="Excellent 🌟","score-excellent"
    elif score>=55: status,sc="Good 👍","score-good"
    elif score>=40: status,sc="Moderate ⚠️","score-moderate"
    else: status,sc="Needs Work 🔴","score-poor"

    col_s, col_p = st.columns([1,2])
    with col_s:
        st.markdown(f"""
        <div class="score-card anim-up">
          <div class="score-title">SUSTAINABILITY SCORE</div>
          <div class="score-number">{score}</div>
          <div class="score-status">{status}</div>
          <div class="score-bar-wrap"><div class="score-bar" style="width:{score}%"></div></div>
          <div style="font-size:0.78rem;color:rgba(255,255,255,0.6);margin-top:4px;">{score}/100 overall rating</div>
        </div>""", unsafe_allow_html=True)

        fig = go.Figure(go.Indicator(mode="gauge+number", value=score, domain={'x':[0,1],'y':[0,1]},
            gauge={'axis':{'range':[0,100],'tickwidth':1},'bar':{'color':'#22c55e'},
                   'steps':[{'range':[0,40],'color':'#fee2e2'},{'range':[40,55],'color':'#fef3c7'},
                             {'range':[55,70],'color':'#dcfce7'},{'range':[70,100],'color':'#bbf7d0'}],
                   'threshold':{'line':{'color':'#14532d','width':3},'thickness':0.8,'value':score}}))
        fig.update_layout(height=200, margin=dict(l=20,r=20,t=10,b=10), font={'family':'Inter'})
        st.plotly_chart(fig, use_container_width=True)

    with col_p:
        st.markdown("**🔍 Campus Problem Areas**")
        pc1,pc2 = st.columns(2)
        for i,area in enumerate(st.session_state.problem_areas):
            with (pc1 if i%2==0 else pc2):
                css = {"critical":"problem-critical","moderate":"problem-moderate","good":"problem-good"}[area["status"]]
                badge_css = {"critical":"badge-crit","moderate":"badge-mod","good":"badge-good"}[area["status"]]
                parts = area['label'].split(' ',1)
                emoji,lbl = (parts[0],parts[1]) if len(parts)>1 else ("",parts[0])
                st.markdown(f"""
                <div class="problem-card {css}">
                  <div class="problem-emoji">{emoji}</div>
                  <div class="problem-name">{lbl}</div>
                  <span class="problem-badge {badge_css}">{area['status_label']}</span>
                </div>""", unsafe_allow_html=True)

    st.markdown('<div class="green-divider"></div>', unsafe_allow_html=True)
    st.markdown("**🎯 Smart Recommendations** — Ranked by AI scoring")
    for i,rec in enumerate(st.session_state.recommendations[:6]):
        bc = {"High Priority":"badge-high","Medium Priority":"badge-medium"}.get(rec.get("priority",""),"badge-low")
        with st.expander(f"#{i+1}  {rec['title']}"):
            c1,c2 = st.columns([2,1])
            with c1:
                st.write(rec["description"])
                st.markdown("**Implementation Steps:**")
                for step in rec.get("implementation_steps",[]): st.markdown(f"- {step}")
                st.markdown(f'**Benefits:** {" · ".join(rec.get("benefits",[])[:3])}')
            with c2:
                st.metric("Payback",f"{rec['payback_years']} yrs")
                st.metric("Investment",rec["cost_range"])
                st.metric("Energy Savings",f"{rec['savings_percent']}%")
                st.metric("CO₂ Cut",f"{rec['co2_reduction']}%")

    st.markdown('<div class="green-divider"></div>', unsafe_allow_html=True)
    st.markdown("**🤖 AI Sustainability Assistant**")
    st.markdown('<div class="chat-hint">💬 Ask me: <em>"Why solar panels?"</em> · <em>"What is the ROI of LED?"</em> · <em>"How to implement rainwater harvesting?"</em></div>', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
    if prompt := st.chat_input("Ask about any recommendation..."):
        st.session_state.chat_history.append({"role":"user","content":prompt})
        with st.chat_message("user"): st.markdown(prompt)
        resp = process_chat_message(prompt, st.session_state.campus_profile, st.session_state.recommendations)
        st.session_state.chat_history.append({"role":"assistant","content":resp})
        with st.chat_message("assistant"): st.markdown(resp)

    st.markdown("<br>", unsafe_allow_html=True)
    ca,_,cc = st.columns(3)
    with ca:
        if st.button("← Back", key="b3", use_container_width=True): go_to(2); st.rerun()
    with cc:
        if st.button("View Impact Analysis →", type="primary", key="n3", use_container_width=True): go_to(4); st.rerun()

def render_step4():
    nav(); progress(4)
    st.markdown('<div class="page-header"><div class="green-line"></div><h2>📈 Impact Analysis</h2><p>Projected financial & environmental benefits from your recommended solutions.</p></div>', unsafe_allow_html=True)
    m = st.session_state.impact_metrics
    c1,c2,c3,c4 = st.columns(4)
    cards_m = [
        (c1,"metric-green","💰",f"₹{m['cost_savings']:,.0f}","Annual Savings"),
        (c2,"metric-blue","⚡",f"{m['energy_savings']}%","Energy Savings"),
        (c3,"metric-teal","💧",f"{m['water_savings']}%","Water Savings"),
        (c4,"metric-amber","🌍",f"{m['co2_reduction']}%","CO₂ Reduction"),
    ]
    for col,cls,icon,val,label in cards_m:
        with col:
            st.markdown(f"""
            <div class="metric-card {cls} anim-up">
              <div class="metric-icon-wrap">{icon}</div>
              <div class="metric-value">{val}</div>
              <div class="metric-label">{label}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    t1,t2,t3 = st.tabs(["📊 Savings Breakdown","🍩 Impact Distribution","📈 5-Year Projection"])
    bd = m.get("breakdown",[])
    with t1:
        titles=[b["title"] for b in bd]; vals=[b["annual_savings"] for b in bd]
        fig=go.Figure(go.Bar(x=vals,y=titles,orientation='h',
            marker=dict(color=vals,colorscale=[[0,'#bbf7d0'],[1,'#14532d']]),
            text=[f"₹{v:,.0f}" for v in vals],textposition='auto'))
        fig.update_layout(title="Annual Savings per Recommendation",xaxis_title="₹ Savings",
            height=380,font=dict(family="Inter"),plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor='rgba(0,0,0,0)')
        fig.update_xaxes(showgrid=True,gridcolor='#f1f5f9')
        st.plotly_chart(fig,use_container_width=True)
    with t2:
        cd=m.get("category_distribution",{})
        fig2=go.Figure(go.Pie(labels=list(cd.keys()),values=list(cd.values()),hole=0.55,
            marker=dict(colors=['#16a34a','#0ea5e9','#d97706','#0d9488']),textinfo='label+percent'))
        fig2.update_layout(title="Category Distribution",height=380,font=dict(family="Inter"))
        st.plotly_chart(fig2,use_container_width=True)
    with t3:
        tl=m.get("timeline",[])
        yrs=[t["year"] for t in tl]; ann=[t["annual_savings"] for t in tl]; cum=[t["cumulative_savings"] for t in tl]
        fig3=go.Figure()
        fig3.add_trace(go.Bar(x=yrs,y=ann,name="Annual Savings",marker_color='#bbf7d0',marker_line_color='#16a34a',marker_line_width=1.5))
        fig3.add_trace(go.Scatter(x=yrs,y=cum,name="Cumulative",line=dict(color='#16a34a',width=3),mode='lines+markers',
            marker=dict(size=8,color='white',line=dict(color='#16a34a',width=2))))
        fig3.update_layout(title="5-Year Savings Projection",yaxis_title="₹ Amount",height=380,
            font=dict(family="Inter"),plot_bgcolor='rgba(0,0,0,0)',legend=dict(orientation="h",yanchor="bottom",y=1.02))
        fig3.update_xaxes(showgrid=False); fig3.update_yaxes(showgrid=True,gridcolor='#f1f5f9')
        st.plotly_chart(fig3,use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    ca,_,cc = st.columns(3)
    with ca:
        if st.button("← Back to Dashboard", key="b4", use_container_width=True): go_to(3); st.rerun()
    with cc:
        if st.button("Generate PDF Report →", type="primary", key="n4", use_container_width=True): go_to(5); st.rerun()

def render_step5():
    nav(); progress(5)
    st.markdown('<div class="page-header"><div class="green-line"></div><h2>📄 Your Sustainability Report</h2><p>Download your complete AI-generated sustainability roadmap.</p></div>', unsafe_allow_html=True)
    p=st.session_state.campus_profile; score=st.session_state.sustainability_score
    recs=st.session_state.recommendations; m=st.session_state.impact_metrics
    rec_items=''.join(f'<p style="margin:4px 0;">• <strong>{r["title"]}</strong> <span style="color:#6b7280;font-size:0.85rem;">— {r.get("priority","")}</span></p>' for r in recs[:5])
    st.markdown(f"""
    <div class="report-preview anim-up">
      <div class="report-header">
        <div style="font-size:2rem;margin-bottom:0.5rem;">🌿</div>
        <h2 style="color:#16a34a;margin:0;font-size:1.5rem;">CampusGreenify</h2>
        <h3 style="color:#0f172a;margin:6px 0;font-weight:600;">Sustainability Assessment Report</h3>
        <p style="color:#64748b;margin:0;">{p.get('name','Campus')}</p>
      </div>
      <div class="report-section">
        <h3>📋 Campus Profile</h3>
        <p style="color:#475569;font-size:0.9rem;margin:0;">
          <strong>Type:</strong> {p.get('type','N/A').replace('_',' ').title()} &nbsp;|&nbsp;
          <strong>Climate:</strong> {p.get('location','N/A').title()} &nbsp;|&nbsp;
          <strong>Size:</strong> {p.get('size','N/A')} &nbsp;|&nbsp;
          <strong>Goal:</strong> {p.get('main_goal','N/A')}
        </p>
      </div>
      <div class="report-section">
        <h3>📊 Sustainability Score: <span style="color:#16a34a;font-size:1.4rem;">{score}/100</span></h3>
      </div>
      <div class="report-section"><h3>🎯 Top Recommendations</h3>{rec_items}</div>
      <div class="report-section">
        <h3>📈 Projected Impact</h3>
        <p style="color:#475569;font-size:0.9rem;margin:0;">
          💰 <strong>₹{m['cost_savings']:,.0f}</strong>/yr savings &nbsp;|&nbsp;
          ⚡ <strong>{m['energy_savings']}%</strong> energy &nbsp;|&nbsp;
          💧 <strong>{m['water_savings']}%</strong> water &nbsp;|&nbsp;
          🌍 <strong>{m['co2_reduction']}%</strong> CO₂
        </p>
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    _,cb,_ = st.columns([1,1,1])
    with cb:
        pdf = generate_pdf_report(p, st.session_state.priorities, recs, score, m)
        fn = f"CampusGreenify_{p.get('name','campus').replace(' ','_')}_Report.pdf"
        st.download_button("📥  Download Full PDF Report", data=pdf, file_name=fn,
                           mime="application/pdf", use_container_width=True, type="primary")

    st.markdown("<br>", unsafe_allow_html=True)
    ca,_,cc = st.columns(3)
    with ca:
        if st.button("← Back", key="b5", use_container_width=True): go_to(4); st.rerun()
    with cc:
        if st.button("🔄 New Assessment", key="restart", use_container_width=True):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()
    st.markdown('<div class="app-footer"><strong>CampusGreenify</strong> · AI-Powered Sustainability Intelligence · Making campuses greener, one decision at a time 🌿</div>', unsafe_allow_html=True)

STEPS = {0:render_landing, 1:render_step1, 2:render_step2, 3:render_step3, 4:render_step4, 5:render_step5}
STEPS[st.session_state.current_step]()
