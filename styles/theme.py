"""
CampusGreenify – Custom CSS Theme
Premium dark-green SaaS design injected into Streamlit
"""


def get_custom_css():
    """Return custom CSS for the entire app."""
    return """
    <style>
        /* ===== GOOGLE FONTS ===== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* ===== ROOT VARIABLES ===== */
        :root {
            --primary:       #16a34a;
            --primary-dark:  #14532d;
            --primary-mid:   #166534;
            --primary-light: #bbf7d0;
            --primary-bg:    #f0fdf4;
            --accent:        #0ea5e9;
            --accent-light:  #e0f2fe;
            --surface:       #f8fafc;
            --card-bg:       #ffffff;
            --text-primary:  #0f172a;
            --text-secondary:#475569;
            --text-muted:    #94a3b8;
            --border:        #e2e8f0;
            --success:       #22c55e;
            --warning:       #f59e0b;
            --danger:        #ef4444;
            --white:         #ffffff;
            --r-sm: 10px; --r-md: 14px; --r-lg: 18px; --r-xl: 24px; --r-2xl: 32px;
            --sh-sm: 0 1px 3px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.04);
            --sh-md: 0 4px 16px rgba(0,0,0,.07),0 2px 6px rgba(0,0,0,.04);
            --sh-lg: 0 10px 30px rgba(0,0,0,.09),0 4px 10px rgba(0,0,0,.05);
            --sh-xl: 0 20px 50px rgba(0,0,0,.12),0 8px 20px rgba(0,0,0,.06);
            --sh-green: 0 8px 30px rgba(22,163,74,.25);
            --sh-green-lg: 0 16px 50px rgba(22,163,74,.3);
        }

        /* ===== GLOBAL ===== */
        html, body, [class*="stApp"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }
        .stApp { background: #f8fafc; }

        /* ===== HIDE STREAMLIT CHROME ===== */
        #MainMenu, footer, header, .stDeployButton { visibility: hidden; display: none; }
        .block-container { padding-top: 1.5rem !important; padding-bottom: 3rem !important; max-width: 1100px !important; }

        /* ===== TOP NAV ===== */
        .top-nav {
            display: flex; align-items: center; justify-content: space-between;
            background: white; border-radius: var(--r-xl);
            padding: 0.9rem 1.8rem; margin-bottom: 1.8rem;
            box-shadow: var(--sh-sm); border: 1px solid var(--border);
        }
        .nav-brand { display: flex; align-items: center; gap: 0.6rem; }
        .nav-brand-name { font-size: 1.25rem; font-weight: 800; color: var(--primary); letter-spacing: -0.5px; }
        .nav-brand-badge {
            font-size: 0.65rem; font-weight: 700; text-transform: uppercase;
            background: var(--primary-bg); color: var(--primary);
            border: 1px solid var(--primary-light); border-radius: 99px;
            padding: 2px 8px; letter-spacing: 0.5px;
        }
        .nav-tagline { font-size: 0.82rem; color: var(--text-muted); font-weight: 400; }

        /* ===== HERO BANNER ===== */
        .hero-banner {
            background: linear-gradient(135deg, #14532d 0%, #16a34a 60%, #22c55e 100%);
            padding: 4rem 2.5rem 3.5rem;
            border-radius: var(--r-2xl);
            color: white; text-align: center;
            margin-bottom: 2.5rem;
            position: relative; overflow: hidden;
            box-shadow: var(--sh-green-lg);
            border: 1px solid rgba(255,255,255,0.08);
        }
        .hero-banner::before {
            content: '';
            position: absolute; inset: 0;
            background:
                radial-gradient(circle at 20% 50%, rgba(255,255,255,0.07) 0%, transparent 55%),
                radial-gradient(circle at 80% 20%, rgba(255,255,255,0.05) 0%, transparent 45%);
            pointer-events: none;
        }
        .hero-banner::after {
            content: '🌿';
            position: absolute; right: 3rem; top: 50%;
            transform: translateY(-50%);
            font-size: 7rem; opacity: 0.12; pointer-events: none;
        }
        .hero-badge {
            display: inline-block;
            background: rgba(255,255,255,0.15); backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.2);
            color: white; font-size: 0.75rem; font-weight: 600;
            letter-spacing: 1.5px; text-transform: uppercase;
            padding: 6px 16px; border-radius: 99px; margin-bottom: 1.2rem;
        }
        .hero-banner h1 {
            font-size: 3.2rem !important; font-weight: 900 !important;
            letter-spacing: -1.5px; margin-bottom: 1rem !important;
            color: white !important; position: relative; line-height: 1.1;
        }
        .hero-banner p {
            font-size: 1.1rem !important; opacity: 0.88;
            font-weight: 400; position: relative;
            max-width: 580px; margin: 0 auto; line-height: 1.7;
        }
        .hero-stats {
            display: flex; justify-content: center; gap: 2.5rem;
            margin-top: 2rem; position: relative;
        }
        .hero-stat { text-align: center; }
        .hero-stat-value { font-size: 1.8rem; font-weight: 800; color: white; }
        .hero-stat-label { font-size: 0.75rem; color: rgba(255,255,255,0.7); text-transform: uppercase; letter-spacing: 0.5px; }
        .hero-stat-divider { width: 1px; background: rgba(255,255,255,0.2); height: 40px; align-self: center; }

        /* ===== PROGRESS BAR ===== */
        .progress-wrapper {
            background: white; border-radius: var(--r-xl);
            padding: 1rem 1.5rem; margin-bottom: 2rem;
            box-shadow: var(--sh-sm); border: 1px solid var(--border);
        }
        .progress-container {
            display: flex; align-items: center;
            max-width: 700px; margin: 0 auto;
        }
        .progress-step { display: flex; flex-direction: column; align-items: center; flex: 1; position: relative; }
        .step-circle {
            width: 38px; height: 38px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-weight: 700; font-size: 0.85rem; z-index: 2;
            transition: all 0.4s cubic-bezier(.4,0,.2,1);
        }
        .step-circle.active {
            background: linear-gradient(135deg, #16a34a, #22c55e);
            color: white; box-shadow: 0 0 0 5px rgba(22,163,74,.15), var(--sh-green);
            transform: scale(1.15);
        }
        .step-circle.completed { background: #16a34a; color: white; }
        .step-circle.inactive { background: #e2e8f0; color: #94a3b8; }
        .step-label { font-size: 0.68rem; margin-top: 6px; font-weight: 600; color: var(--text-muted); text-align: center; white-space: nowrap; }
        .step-label.active-label { color: var(--primary); }
        .step-line { height: 3px; flex: 1; margin: 0 -4px; margin-bottom: 24px; z-index: 1; transition: background 0.4s ease; }
        .step-line.completed { background: linear-gradient(90deg, #16a34a, #22c55e); }
        .step-line.inactive { background: #e2e8f0; }

        /* ===== SECTION HEADERS ===== */
        .page-header {
            margin-bottom: 1.75rem;
        }
        .page-header h2 {
            font-size: 1.9rem; font-weight: 800; color: var(--text-primary);
            letter-spacing: -0.8px; margin: 0 0 4px 0;
        }
        .page-header p { font-size: 0.95rem; color: var(--text-secondary); margin: 0; }
        .green-line { width: 48px; height: 4px; background: linear-gradient(90deg, #16a34a, #22c55e); border-radius: 4px; margin-bottom: 0.6rem; }

        /* ===== CARDS ===== */
        .card {
            background: white; border-radius: var(--r-lg);
            padding: 1.75rem; box-shadow: var(--sh-md);
            border: 1px solid var(--border);
            transition: all 0.35s cubic-bezier(.165,.84,.44,1);
            position: relative;
        }
        .card:hover { box-shadow: var(--sh-lg); transform: translateY(-3px); }
        .card-green-border { border-left: 4px solid var(--primary); }
        .card-blue-border  { border-left: 4px solid var(--accent); }

        /* ===== FEATURE CARDS (landing) ===== */
        .feature-card {
            background: white; border-radius: var(--r-xl);
            padding: 2.2rem 1.75rem; text-align: center;
            box-shadow: var(--sh-sm); border: 1px solid var(--border);
            transition: all 0.4s cubic-bezier(.25,.8,.25,1);
        }
        .feature-card:hover {
            box-shadow: var(--sh-green); transform: translateY(-6px);
            border-color: var(--primary-light);
        }
        .feature-icon-wrap {
            width: 64px; height: 64px; border-radius: 16px;
            background: var(--primary-bg); display: inline-flex;
            align-items: center; justify-content: center;
            font-size: 1.8rem; margin-bottom: 1.2rem;
            border: 1px solid var(--primary-light);
        }
        .feature-card h3 { font-size: 1.05rem; font-weight: 700; color: var(--text-primary); margin: 0 0 8px 0; }
        .feature-card p  { font-size: 0.88rem; color: var(--text-secondary); margin: 0; line-height: 1.6; }

        /* ===== METRIC CARDS ===== */
        .metric-card {
            background: white; border-radius: var(--r-xl);
            padding: 1.75rem 1.25rem; text-align: center;
            box-shadow: var(--sh-md); border: 1px solid var(--border);
            transition: all 0.4s cubic-bezier(.175,.885,.32,1.275);
            position: relative; overflow: hidden;
        }
        .metric-card::after {
            content: ''; position: absolute;
            bottom: -30px; right: -30px; width: 90px; height: 90px;
            border-radius: 50%; opacity: 0.06;
        }
        .metric-green::after  { background: #16a34a; }
        .metric-blue::after   { background: #0ea5e9; }
        .metric-teal::after   { background: #0d9488; }
        .metric-amber::after  { background: #d97706; }
        .metric-card:hover { transform: translateY(-5px); box-shadow: var(--sh-xl); }
        .metric-card::before {
            content: ''; position: absolute;
            top: 0; left: 0; right: 0; height: 5px;
        }
        .metric-green::before  { background: linear-gradient(90deg,#16a34a,#4ade80); }
        .metric-blue::before   { background: linear-gradient(90deg,#0ea5e9,#7dd3fc); }
        .metric-teal::before   { background: linear-gradient(90deg,#0d9488,#5eead4); }
        .metric-amber::before  { background: linear-gradient(90deg,#d97706,#fcd34d); }
        .metric-icon-wrap {
            width: 52px; height: 52px; border-radius: 14px;
            display: inline-flex; align-items: center;
            justify-content: center; font-size: 1.5rem; margin-bottom: 0.75rem;
        }
        .metric-green .metric-icon-wrap  { background: #dcfce7; }
        .metric-blue  .metric-icon-wrap  { background: #e0f2fe; }
        .metric-teal  .metric-icon-wrap  { background: #ccfbf1; }
        .metric-amber .metric-icon-wrap  { background: #fef3c7; }
        .metric-value {
            font-size: 2rem; font-weight: 800; letter-spacing: -1px;
            margin-bottom: 4px; color: var(--text-primary);
        }
        .metric-label {
            font-size: 0.78rem; color: var(--text-secondary);
            font-weight: 600; text-transform: uppercase; letter-spacing: 0.6px;
        }

        /* ===== SCORE CARD ===== */
        .score-card {
            background: linear-gradient(145deg, #14532d, #16a34a);
            border-radius: var(--r-2xl); padding: 2.5rem;
            text-align: center; color: white;
            box-shadow: var(--sh-green-lg);
            position: relative; overflow: hidden;
        }
        .score-card::before {
            content: '';
            position: absolute; inset: 0;
            background: radial-gradient(circle at 70% 30%, rgba(255,255,255,0.08) 0%, transparent 60%);
        }
        .score-number {
            font-size: 5rem; font-weight: 900; letter-spacing: -4px;
            line-height: 1; color: white; margin: 0.5rem 0;
        }
        .score-title { font-size: 0.78rem; color: rgba(255,255,255,0.7); text-transform: uppercase; letter-spacing: 1px; font-weight: 600; }
        .score-status { font-size: 1.1rem; font-weight: 700; color: rgba(255,255,255,0.9); margin-top: 0.25rem; }
        .score-bar-wrap { background: rgba(255,255,255,0.2); border-radius: 99px; height: 8px; margin: 1rem 0 0.5rem; overflow: hidden; }
        .score-bar { height: 100%; border-radius: 99px; background: rgba(255,255,255,0.9); transition: width 1s ease; }

        /* ===== PROBLEM AREA CARDS ===== */
        .problem-card {
            border-radius: var(--r-lg); padding: 1.1rem;
            text-align: center; margin-bottom: 0.75rem;
            transition: all 0.3s ease;
        }
        .problem-card:hover { transform: translateY(-2px); }
        .problem-critical { background: #fef2f2; border: 1.5px solid #fecaca; color: #b91c1c; }
        .problem-moderate  { background: #fffbeb; border: 1.5px solid #fde68a; color: #b45309; }
        .problem-good      { background: #f0fdf4; border: 1.5px solid #bbf7d0; color: #15803d; }
        .problem-emoji { font-size: 1.5rem; margin-bottom: 4px; }
        .problem-name { font-size: 0.82rem; font-weight: 700; margin: 2px 0; }
        .problem-badge {
            font-size: 0.68rem; font-weight: 600; border-radius: 99px;
            padding: 2px 8px; display: inline-block; margin-top: 4px;
        }
        .badge-crit { background: #fecaca; color: #b91c1c; }
        .badge-mod  { background: #fde68a; color: #b45309; }
        .badge-good { background: #bbf7d0; color: #15803d; }

        /* ===== RECOMMENDATION CARDS ===== */
        .rec-card {
            background: white; border-radius: var(--r-lg);
            padding: 1.5rem; margin-bottom: 1rem;
            box-shadow: var(--sh-sm); border: 1px solid var(--border);
            border-left: 5px solid var(--primary);
            transition: all 0.3s ease;
        }
        .rec-card:hover { box-shadow: var(--sh-green); transform: translateX(4px); border-left-color: #22c55e; }
        .rec-rank {
            display: inline-flex; align-items: center; justify-content: center;
            width: 28px; height: 28px; border-radius: 8px;
            background: var(--primary-bg); color: var(--primary);
            font-size: 0.8rem; font-weight: 800; margin-right: 8px;
            border: 1px solid var(--primary-light);
        }
        .rec-badge {
            display: inline-block; padding: 3px 10px;
            border-radius: 99px; font-size: 0.72rem; font-weight: 700;
        }
        .badge-high   { background: #dcfce7; color: #15803d; }
        .badge-medium { background: #fef3c7; color: #b45309; }
        .badge-low    { background: #dbeafe; color: #1d4ed8; }

        /* ===== BUTTONS ===== */
        .stButton > button {
            border-radius: 99px !important;
            font-weight: 700 !important;
            font-family: 'Inter', sans-serif !important;
            padding: 0.7rem 2rem !important;
            transition: all 0.3s cubic-bezier(.25,.8,.25,1) !important;
            border: none !important;
            font-size: 0.92rem !important;
            letter-spacing: 0.3px !important;
        }
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #16a34a, #22c55e) !important;
            color: white !important;
            box-shadow: var(--sh-green) !important;
        }
        .stButton > button[kind="primary"]:hover {
            transform: translateY(-3px) !important;
            box-shadow: var(--sh-green-lg) !important;
        }
        .stButton > button:not([kind="primary"]):hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--sh-md) !important;
        }

        /* ===== DOWNLOAD BUTTON ===== */
        .stDownloadButton > button {
            background: linear-gradient(135deg, #16a34a, #22c55e) !important;
            color: white !important; border-radius: 99px !important;
            font-weight: 700 !important; padding: 0.8rem 2rem !important;
            font-size: 1rem !important; border: none !important;
            box-shadow: var(--sh-green) !important;
            transition: all 0.3s ease !important;
            font-family: 'Inter', sans-serif !important;
        }
        .stDownloadButton > button:hover {
            transform: translateY(-3px) !important;
            box-shadow: var(--sh-green-lg) !important;
        }

        /* ===== INPUTS ===== */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            border-radius: var(--r-md) !important;
            border: 1.5px solid var(--border) !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.3s ease !important;
            background: #f8fafc !important;
            padding: 0.6rem 0.9rem !important;
        }
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #16a34a !important;
            box-shadow: 0 0 0 3px rgba(22,163,74,.1) !important;
            background: white !important;
        }

        /* ===== TABS ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px; background: #f1f5f9; padding: 6px;
            border-radius: 12px;
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
            font-size: 0.88rem !important;
        }
        .stTabs [aria-selected="true"] {
            background: white !important; color: var(--primary) !important;
            box-shadow: var(--sh-sm) !important;
        }

        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            font-weight: 700 !important;
            font-family: 'Inter', sans-serif !important;
            color: var(--text-primary) !important;
            border-radius: var(--r-md) !important;
            font-size: 0.95rem !important;
        }

        /* ===== DIVIDER ===== */
        .green-divider {
            height: 2px; border: none; margin: 1.75rem 0;
            background: linear-gradient(90deg, #16a34a33, #22c55e66, #16a34a33);
            border-radius: 2px;
        }

        /* ===== REPORT PREVIEW ===== */
        .report-preview {
            background: white; border: 1px solid var(--border);
            border-radius: var(--r-xl); padding: 2.5rem;
            box-shadow: var(--sh-lg); max-width: 840px; margin: 0 auto;
        }
        .report-header {
            text-align: center; padding-bottom: 1.5rem;
            border-bottom: 2px solid var(--primary-light); margin-bottom: 1.5rem;
        }
        .report-section { margin-bottom: 1.25rem; padding-bottom: 1.25rem; border-bottom: 1px solid #f1f5f9; }
        .report-section:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
        .report-section h3 { color: var(--primary); font-weight: 700; margin: 0 0 0.5rem 0; font-size: 1rem; }

        /* ===== CHAT ===== */
        .stChatMessage { border-radius: var(--r-lg) !important; }
        .chat-hint {
            background: var(--primary-bg); border: 1px solid var(--primary-light);
            border-radius: var(--r-lg); padding: 0.9rem 1.2rem;
            font-size: 0.84rem; color: var(--primary-mid);
            margin-bottom: 1rem;
        }

        /* ===== FOOTER ===== */
        .app-footer {
            text-align: center; color: var(--text-muted);
            font-size: 0.8rem; padding: 1.5rem 0 0.5rem;
        }
        .app-footer strong { color: var(--primary); }

        /* ===== ANIMATIONS ===== */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(24px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; } to { opacity: 1; }
        }
        @keyframes pulse-green {
            0%, 100% { box-shadow: 0 0 0 0 rgba(22,163,74,0.3); }
            50%       { box-shadow: 0 0 0 8px rgba(22,163,74,0); }
        }
        .anim-up   { animation: fadeInUp 0.55s ease-out both; }
        .anim-fade { animation: fadeIn 0.45s ease-out both; }
        .anim-d1 { animation-delay: 0.1s; }
        .anim-d2 { animation-delay: 0.2s; }
        .anim-d3 { animation-delay: 0.3s; }
        .anim-d4 { animation-delay: 0.4s; }
        .anim-d5 { animation-delay: 0.5s; }
        .pulse-btn { animation: pulse-green 2.5s infinite; }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .hero-banner h1  { font-size: 2rem !important; }
            .hero-banner::after { display: none; }
            .hero-stats { gap: 1.5rem; }
        }
    </style>
    """
