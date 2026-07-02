"""
CampusGreenify – Custom CSS Theme
Premium green SaaS design injected into Streamlit
"""


def get_custom_css():
    """Return custom CSS for the entire app."""
    return """
    <style>
        /* ===== GOOGLE FONTS ===== */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

        /* ===== ROOT VARIABLES ===== */
        :root {
            --primary: #2E7D32;
            --primary-light: #A5D6A7;
            --primary-lighter: #E8F5E9;
            --primary-dark: #1B5E20;
            --accent: #1976D2;
            --accent-light: #BBDEFB;
            --surface: #F5F7F5;
            --text-primary: #1A1A2E;
            --text-secondary: #5A6070;
            --success: #43A047;
            --warning: #FF9800;
            --danger: #E53935;
            --white: #FFFFFF;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.10);
            --shadow-lg: 0 8px 32px rgba(0,0,0,0.12);
            --shadow-xl: 0 16px 48px rgba(0,0,0,0.14);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 24px;
        }

        /* ===== GLOBAL STYLES ===== */
        html, body, [class*="stApp"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }

        .stApp {
            background: #FFFFFF;
        }

        /* ===== HIDE STREAMLIT DEFAULTS ===== */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}

        /* ===== HERO BANNER ===== */
        .hero-banner {
            background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 40%, #43A047 70%, #66BB6A 100%);
            padding: 3.5rem 2.5rem;
            border-radius: 20px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 12px 40px rgba(46, 125, 50, 0.3);
        }

        .hero-banner::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 70%);
            animation: shimmer 8s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { transform: translateX(-30%) translateY(-30%); }
            50% { transform: translateX(10%) translateY(10%); }
        }

        .hero-banner h1 {
            font-size: 2.8rem !important;
            font-weight: 800 !important;
            margin-bottom: 0.5rem !important;
            color: white !important;
            position: relative;
            letter-spacing: -0.5px;
        }

        .hero-banner p {
            font-size: 1.15rem !important;
            opacity: 0.92;
            font-weight: 400;
            position: relative;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }

        /* ===== STEP PROGRESS BAR ===== */
        .progress-container {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0;
            margin: 1.5rem auto 2rem auto;
            max-width: 700px;
        }

        .progress-step {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            flex: 1;
        }

        .step-circle {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 0.9rem;
            z-index: 2;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .step-circle.active {
            background: linear-gradient(135deg, #2E7D32, #43A047);
            color: white;
            box-shadow: 0 4px 15px rgba(46, 125, 50, 0.4);
            transform: scale(1.1);
        }

        .step-circle.completed {
            background: #2E7D32;
            color: white;
        }

        .step-circle.inactive {
            background: #E0E0E0;
            color: #9E9E9E;
        }

        .step-label {
            font-size: 0.7rem;
            margin-top: 6px;
            font-weight: 500;
            color: var(--text-secondary);
            text-align: center;
        }

        .step-line {
            height: 3px;
            flex: 1;
            margin: 0 -5px;
            margin-bottom: 22px;
            z-index: 1;
        }

        .step-line.completed {
            background: #2E7D32;
        }

        .step-line.inactive {
            background: #E0E0E0;
        }

        /* ===== CARDS ===== */
        .custom-card {
            background: white;
            border-radius: var(--radius-md);
            padding: 1.5rem;
            box-shadow: var(--shadow-md);
            border: 1px solid rgba(0,0,0,0.04);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin-bottom: 1rem;
        }

        .custom-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateY(-2px);
        }

        .custom-card-green {
            border-left: 4px solid #2E7D32;
        }

        .custom-card-blue {
            border-left: 4px solid #1976D2;
        }

        .custom-card-orange {
            border-left: 4px solid #FF9800;
        }

        .custom-card-red {
            border-left: 4px solid #E53935;
        }

        /* ===== METRIC CARDS ===== */
        .metric-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 1.8rem 1.5rem;
            text-align: center;
            box-shadow: var(--shadow-md);
            border: 1px solid rgba(0,0,0,0.04);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .metric-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
        }

        .metric-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--shadow-xl);
        }

        .metric-card .metric-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .metric-card .metric-value {
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 0.25rem;
            letter-spacing: -1px;
        }

        .metric-card .metric-label {
            font-size: 0.85rem;
            color: var(--text-secondary);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .metric-green::before { background: linear-gradient(90deg, #2E7D32, #66BB6A); }
        .metric-blue::before { background: linear-gradient(90deg, #1976D2, #64B5F6); }
        .metric-orange::before { background: linear-gradient(90deg, #F57C00, #FFB74D); }
        .metric-teal::before { background: linear-gradient(90deg, #00796B, #4DB6AC); }

        /* ===== FEATURE CARDS ===== */
        .feature-card {
            background: white;
            border-radius: var(--radius-lg);
            padding: 2rem 1.5rem;
            text-align: center;
            box-shadow: var(--shadow-sm);
            border: 1px solid #F0F0F0;
            transition: all 0.3s ease;
        }

        .feature-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateY(-4px);
            border-color: var(--primary-light);
        }

        .feature-card .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            color: var(--text-primary);
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .feature-card p {
            color: var(--text-secondary);
            font-size: 0.9rem;
            line-height: 1.5;
        }

        /* ===== PRIORITY SELECTOR CARDS ===== */
        .priority-card {
            background: white;
            border: 2px solid #E8E8E8;
            border-radius: var(--radius-md);
            padding: 1.2rem;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
            min-height: 120px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .priority-card:hover {
            border-color: var(--primary-light);
            background: var(--primary-lighter);
        }

        .priority-card.selected {
            border-color: var(--primary);
            background: var(--primary-lighter);
            box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.15);
        }

        .priority-card .priority-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        .priority-card .priority-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        /* ===== RECOMMENDATION CARDS ===== */
        .rec-card {
            background: white;
            border-radius: var(--radius-md);
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: var(--shadow-sm);
            border: 1px solid #F0F0F0;
            border-left: 5px solid var(--primary);
            transition: all 0.3s ease;
        }

        .rec-card:hover {
            box-shadow: var(--shadow-lg);
            transform: translateX(4px);
        }

        .rec-card .rec-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 0.75rem;
        }

        .rec-card .rec-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .rec-card .rec-desc {
            font-size: 0.9rem;
            color: var(--text-secondary);
            line-height: 1.5;
            margin-bottom: 0.75rem;
        }

        .rec-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        .badge-high {
            background: #E8F5E9;
            color: #2E7D32;
        }

        .badge-medium {
            background: #FFF3E0;
            color: #E65100;
        }

        .badge-low {
            background: #E3F2FD;
            color: #1565C0;
        }

        /* ===== PROBLEM AREA CARDS ===== */
        .problem-card {
            border-radius: var(--radius-md);
            padding: 1.2rem;
            text-align: center;
            font-weight: 600;
            font-size: 0.9rem;
        }

        .problem-critical {
            background: #FFEBEE;
            color: #C62828;
            border: 1px solid #FFCDD2;
        }

        .problem-moderate {
            background: #FFF8E1;
            color: #E65100;
            border: 1px solid #FFE082;
        }

        .problem-good {
            background: #E8F5E9;
            color: #2E7D32;
            border: 1px solid #C8E6C9;
        }

        /* ===== SCORE GAUGE ===== */
        .score-container {
            text-align: center;
            padding: 2rem;
        }

        .score-value {
            font-size: 4.5rem;
            font-weight: 900;
            letter-spacing: -3px;
            line-height: 1;
            margin-bottom: 0.25rem;
        }

        .score-label {
            font-size: 1rem;
            color: var(--text-secondary);
            font-weight: 500;
        }

        .score-excellent { color: #2E7D32; }
        .score-good { color: #43A047; }
        .score-moderate { color: #FF9800; }
        .score-poor { color: #E53935; }

        /* ===== CHATBOT ===== */
        .chat-container {
            background: var(--surface);
            border-radius: var(--radius-lg);
            padding: 1rem;
            border: 1px solid #E8E8E8;
        }

        .stChatMessage {
            border-radius: var(--radius-md) !important;
        }

        /* ===== SECTION HEADERS ===== */
        .section-header {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
            letter-spacing: -0.5px;
        }

        .section-subheader {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            font-weight: 400;
        }

        /* ===== BUTTONS ===== */
        .stButton > button {
            border-radius: var(--radius-md) !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
            padding: 0.6rem 2rem !important;
            transition: all 0.3s ease !important;
            border: none !important;
            font-size: 0.95rem !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(46, 125, 50, 0.3) !important;
        }

        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #2E7D32, #43A047) !important;
            color: white !important;
        }

        /* ===== FORM INPUTS ===== */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div > div {
            border-radius: var(--radius-sm) !important;
            border: 1.5px solid #E0E0E0 !important;
            font-family: 'Inter', sans-serif !important;
            transition: border-color 0.3s ease !important;
        }

        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus {
            border-color: #2E7D32 !important;
            box-shadow: 0 0 0 3px rgba(46, 125, 50, 0.1) !important;
        }

        /* ===== EXPANDER ===== */
        .streamlit-expanderHeader {
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
            color: var(--text-primary) !important;
            border-radius: var(--radius-sm) !important;
        }

        /* ===== DIVIDER ===== */
        .green-divider {
            height: 3px;
            background: linear-gradient(90deg, #2E7D32, #A5D6A7, transparent);
            border: none;
            margin: 1.5rem 0;
            border-radius: 2px;
        }

        /* ===== NAV BAR ===== */
        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 1.5rem;
            background: white;
            border-bottom: 1px solid #F0F0F0;
            margin: -1rem -1rem 1.5rem -1rem;
        }

        .navbar-brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .navbar-brand-text {
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--primary);
            letter-spacing: -0.5px;
        }

        .navbar-brand-sub {
            font-size: 0.75rem;
            color: var(--text-secondary);
            font-weight: 400;
        }

        /* ===== DOWNLOAD BUTTON ===== */
        .stDownloadButton > button {
            background: linear-gradient(135deg, #2E7D32, #43A047) !important;
            color: white !important;
            border-radius: var(--radius-md) !important;
            font-weight: 600 !important;
            padding: 0.75rem 2rem !important;
            font-size: 1rem !important;
            border: none !important;
            transition: all 0.3s ease !important;
        }

        .stDownloadButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(46, 125, 50, 0.35) !important;
        }

        /* ===== REPORT PREVIEW ===== */
        .report-preview {
            background: white;
            border: 1px solid #E0E0E0;
            border-radius: var(--radius-lg);
            padding: 2rem;
            box-shadow: var(--shadow-md);
            max-width: 800px;
            margin: 0 auto;
        }

        .report-header {
            text-align: center;
            padding-bottom: 1.5rem;
            border-bottom: 2px solid var(--primary-light);
            margin-bottom: 1.5rem;
        }

        .report-section {
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #F0F0F0;
        }

        .report-section h3 {
            color: var(--primary);
            font-weight: 700;
            margin-bottom: 0.75rem;
        }

        /* ===== ANIMATIONS ===== */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .animate-fade-in {
            animation: fadeIn 0.6s ease-out;
        }

        .animate-fade-in-up {
            animation: fadeInUp 0.6s ease-out;
        }

        /* ===== RESPONSIVE ===== */
        @media (max-width: 768px) {
            .hero-banner h1 {
                font-size: 1.8rem !important;
            }
            .hero-banner {
                padding: 2rem 1.5rem;
            }
            .score-value {
                font-size: 3rem;
            }
        }

        /* ===== TABS STYLING ===== */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: var(--radius-sm) !important;
            font-weight: 600 !important;
            font-family: 'Inter', sans-serif !important;
        }

        .stTabs [aria-selected="true"] {
            background: var(--primary-lighter) !important;
            color: var(--primary) !important;
        }
    </style>
    """
