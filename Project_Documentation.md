# CampusGreenify – Smart Planner for Eco-Campus
## Comprehensive Project Documentation
**Prepared by:** Project Management Team
**Date:** July 2, 2026

---

## 1. Executive Summary
**CampusGreenify** is an AI-powered sustainability decision platform designed specifically for educational institutions and corporate campuses. Built as a scalable, responsive web application, it helps campuses navigate the complexities of sustainability planning by providing data-driven, personalized recommendations, interactive impact analyses, and actionable reports.

This document serves as the complete project reference guide, detailing the architecture, workflow, AI logic, and business value of the CampusGreenify MVP.

## 2. Problem Statement
Campuses globally are facing increasing pressure to adopt sustainable practices due to regulatory compliance, rising operational costs, and the demand for eco-conscious environments. However, decision-makers often struggle with:
*   **Where to start:** Overwhelming number of sustainability options.
*   **What to prioritize:** Lack of clarity on which initiatives offer the best Return on Investment (ROI) and environmental impact.
*   **Decision Paralysis:** Most planning relies on guesswork rather than data-driven intelligence.

## 3. The Solution: CampusGreenify
CampusGreenify solves these challenges using an AI-powered decision intelligence engine. By asking minimal, high-impact questions about the campus profile, the platform generates a tailored sustainability roadmap. 

**Key Value Propositions (B2B SaaS Positioning):**
*   **Reduce Operational Costs:** Direct focus on high-ROI energy and water savings.
*   **Improve Compliance:** Helps campuses align with frameworks like GRIHA, IGBC, and Swachh Bharat.
*   **Enable Smarter Decisions:** Eliminates guesswork through data visualization and rule-based AI scoring.

---

## 4. Architecture & Technology Stack

The MVP is built with a modern, lightweight, single-process architecture focused on performance and seamless user experience.

### Core Technologies
*   **Frontend & Routing:** Streamlit (Python-based framework)
*   **Backend Logic:** Python 3.11 (Engine Modules)
*   **Data Visualization:** Plotly (Interactive charts)
*   **Report Generation:** FPDF2 (PDF generation)
*   **Styling:** Custom CSS injection for a premium, green SaaS design system.

### Project Structure
```text
Campus-Greenify/
├── app.py                      # Main application & UI flow controller
├── requirements.txt            # Dependencies (streamlit, plotly, fpdf2, Pillow)
├── .streamlit/config.toml      # Theme configuration
├── assets/logo.png             # Brand assets
├── styles/theme.py             # Custom CSS injection for premium UI
└── engine/                     # Core Business Logic Modules
    ├── recommendations.py      # AI Scoring Engine & Dataset
    ├── impact.py               # Financial & Environmental impact calculators
    ├── chatbot.py              # Context-aware Assistant Logic
    └── report.py               # PDF Document Generator
```

---

## 5. Application Workflow (The 5-Step Process)

The application utilizes Streamlit's `session_state` to manage a seamless, single-page wizard flow.

### Step 1: Campus Profile Input
A low-friction form designed to capture essential data points without overwhelming the user:
*   Campus Name & Type (University, Corporate, etc.)
*   Location / Climate Zone (Crucial for recommendation accuracy)
*   Campus Size & Main Sustainability Goal
*   Annual Electricity Bill (Optional, for precise ROI calculation)

### Step 2: Personalization
Users define their strategic priorities (e.g., Reduce Electricity Cost, Compliance Readiness, Reduce Carbon Footprint). This data heavily influences the recommendation engine's weighting.

### Step 3: AI Sustainability Dashboard
The core value delivery screen containing:
*   **Sustainability Score:** A 0-100 gauge indicating the current baseline and room for improvement.
*   **Problem Areas:** Color-coded (Critical, Moderate, On Track) identification of gaps.
*   **Smart Recommendations:** Ranked action items (e.g., Solar Installation, Smart HVAC, LED Retrofitting) detailing implementation steps and ROI.
*   **AI Assistant (Chatbot):** A contextual chatbot ready to answer "Why?", "What is the ROI?", and "How to implement?" for any recommendation.

### Step 4: Impact Analysis
Interactive data visualization demonstrating the projected outcomes of implementing the recommendations:
*   **Metric Cards:** Annual Cost Savings (₹), Energy (%), Water (%), and CO₂ (%) reductions.
*   **Charts (Plotly):** Bar charts for savings breakdown, donut charts for category distribution, and a line chart showing a progressive 5-year cumulative savings projection.

### Step 5: Final Report Generation
A comprehensive, downloadable PDF report (generated via `FPDF2`) containing the campus profile, score, ranked recommendations, detailed impact metrics, and a phased action plan.

---

## 6. AI Recommendation Engine Logic

The core intelligence of CampusGreenify resides in `engine/recommendations.py`. It uses a deterministic, rule-based scoring algorithm to ensure recommendations are transparent, explainable, and highly relevant.

### The Scoring Formula
Each of the 10 core sustainability solutions is evaluated against the campus profile using a composite score (out of 10):
`Score = (Impact × 0.3) + (ROI × 0.25) + (GoalAlignment × 0.25) + (Feasibility × 0.2)`

### Contextual Boosts (The "Smart" Factor)
The engine applies dynamic multipliers based on the user's input:
1.  **Climate Match (+2.0):** Solutions like Rainwater Harvesting get boosted in Tropical/Coastal zones.
2.  **Campus Type Match (+1.5):** Solutions tailored for specific institutions (e.g., Green Roofs for Corporate).
3.  **Priority Alignment (+1.0):** Boosts categories the user explicitly cares about.
4.  **Scale Factor:** Larger campuses receive boosts for infrastructure-heavy solutions (Solar, Smart HVAC) due to economies of scale.
5.  **Financial Factor:** High reported electricity bills trigger a boost in energy-saving recommendations.

---

## 7. AI Chatbot Architecture

The integrated AI assistant (`engine/chatbot.py`) provides immediate, contextual support without requiring external API calls (ensuring zero latency and absolute data privacy).
*   **Keyword & Intent Matching:** Analyzes user input to detect the target recommendation (e.g., "Solar", "LED") and the question intent ("Why", "ROI", "Benefits", "How to implement").
*   **Dynamic Templating:** Injects the user's specific campus data (climate, size, goals) into predefined, highly detailed response templates to provide personalized advice.

---

## 8. Future Roadmap (Beyond MVP)

While the MVP delivers complete end-to-end value, future iterations could include:
1.  **Database Integration:** Save user profiles and track implementation progress over time.
2.  **Vendor Marketplace:** Connect campuses directly with verified local vendors for solar, water, and waste management based on the accepted recommendations.
3.  **IoT Integration:** Allow campuses to connect actual smart meters to replace estimated savings with real-time tracking.
4.  **LLM Integration:** Upgrade the rule-based chatbot to a generative AI model (e.g., Google Gemini) for open-ended sustainability consulting.

---
*End of Document*
