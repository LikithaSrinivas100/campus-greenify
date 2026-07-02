"""
CampusGreenify – PDF Report Generator
Generates downloadable sustainability assessment reports using FPDF2.
"""

import io
import os
import re
from datetime import datetime
from fpdf import FPDF


def _sanitize(text):
    """Sanitize text for latin-1 PDF encoding."""
    if not isinstance(text, str):
        text = str(text)
    # Replace ₹ with Rs.
    text = text.replace('\u20b9', 'Rs.')
    # Replace en-dash and em-dash
    text = text.replace('\u2013', '-').replace('\u2014', '-')
    # Replace smart quotes
    text = text.replace('\u2018', "'").replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    # Remove emojis and other non-latin1 characters
    text = text.encode('latin-1', 'replace').decode('latin-1')
    return text


class CampusGreenifyReport(FPDF):
    """Custom PDF report for CampusGreenify."""

    def __init__(self):
        super().__init__()
        self.primary_color = (46, 125, 50)       # #2E7D32
        self.primary_light = (165, 214, 167)      # #A5D6A7
        self.accent_color = (25, 118, 210)        # #1976D2
        self.dark_text = (26, 26, 46)             # #1A1A2E
        self.light_text = (90, 96, 112)           # #5A6070
        self.white = (255, 255, 255)
        self.light_bg = (245, 247, 245)           # #F5F7F5
        self.danger = (229, 57, 53)               # #E53935
        self.warning = (255, 152, 0)              # #FF9800
        self.success = (67, 160, 71)              # #43A047

    def header(self):
        """Custom header for each page."""
        # Green bar at top
        self.set_fill_color(*self.primary_color)
        self.rect(0, 0, 210, 8, 'F')

        # Brand name
        self.set_y(12)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(*self.primary_color)
        self.cell(0, 5, 'CampusGreenify', align='L')

        # Date
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*self.light_text)
        self.cell(0, 5, datetime.now().strftime('%B %d, %Y'), align='R')

        self.ln(10)

    def footer(self):
        """Custom footer for each page."""
        self.set_y(-15)
        self.set_font('Helvetica', '', 8)
        self.set_text_color(*self.light_text)
        self.cell(0, 10, f'CampusGreenify Sustainability Report  |  Page {self.page_no()}/{{nb}}', align='C')

    def add_cover_page(self, campus_profile, sustainability_score):
        """Add a professional cover page."""
        self.add_page()
        self.alias_nb_pages()

        # Large green banner
        self.set_fill_color(*self.primary_color)
        self.rect(0, 0, 210, 120, 'F')

        # Gradient overlay effect (lighter stripe)
        self.set_fill_color(67, 160, 71)
        self.rect(0, 90, 210, 30, 'F')

        # Title
        self.set_y(30)
        self.set_font('Helvetica', 'B', 28)
        self.set_text_color(*self.white)
        self.cell(0, 12, 'Sustainability Assessment', align='C')
        self.ln(14)

        self.set_font('Helvetica', '', 14)
        self.cell(0, 8, 'Report', align='C')
        self.ln(20)

        # Campus name
        self.set_font('Helvetica', 'B', 20)
        campus_name = campus_profile.get('name', 'Campus')
        self.cell(0, 10, campus_name, align='C')
        self.ln(12)

        # Tagline
        self.set_font('Helvetica', '', 11)
        self.set_text_color(200, 230, 200)
        self.cell(0, 6, 'AI-Powered Sustainability Intelligence by CampusGreenify', align='C')

        # Score section below banner
        self.set_y(135)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*self.dark_text)
        self.cell(0, 10, 'Sustainability Score', align='C')
        self.ln(12)

        # Score value
        self.set_font('Helvetica', 'B', 48)
        if sustainability_score >= 70:
            self.set_text_color(*self.success)
        elif sustainability_score >= 50:
            self.set_text_color(*self.warning)
        else:
            self.set_text_color(*self.danger)
        self.cell(0, 20, f'{sustainability_score}/100', align='C')
        self.ln(22)

        # Score interpretation
        self.set_font('Helvetica', '', 11)
        self.set_text_color(*self.light_text)
        if sustainability_score >= 70:
            interpretation = "Your campus has a strong sustainability foundation. Focus on optimization."
        elif sustainability_score >= 50:
            interpretation = "Your campus has moderate sustainability. Significant improvements are achievable."
        else:
            interpretation = "Your campus has substantial room for sustainability improvement."
        self.cell(0, 6, interpretation, align='C')

        # Report metadata
        self.set_y(220)
        self.set_font('Helvetica', '', 9)
        self.set_text_color(*self.light_text)
        self.cell(0, 5, f'Generated on: {datetime.now().strftime("%B %d, %Y at %I:%M %p")}', align='C')
        self.ln(5)
        self.cell(0, 5, f'Campus Type: {campus_profile.get("type", "N/A")}  |  Location: {campus_profile.get("location", "N/A")}  |  Size: {campus_profile.get("size", "N/A")}', align='C')

    def add_section_header(self, title, subtitle=""):
        """Add a styled section header."""
        self.ln(5)
        # Green accent bar
        self.set_fill_color(*self.primary_color)
        self.rect(10, self.get_y(), 4, 10, 'F')

        self.set_x(18)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(*self.dark_text)
        self.cell(0, 10, title)
        self.ln(10)

        if subtitle:
            self.set_x(18)
            self.set_font('Helvetica', '', 9)
            self.set_text_color(*self.light_text)
            self.cell(0, 5, subtitle)
            self.ln(8)
        else:
            self.ln(3)

    def add_campus_profile(self, campus_profile, priorities):
        """Add campus profile section."""
        self.add_page()
        self.add_section_header("Campus Profile", "Overview of your campus sustainability assessment inputs")

        # Profile table
        profile_items = [
            ("Campus Name", campus_profile.get("name", "N/A")),
            ("Campus Type", campus_profile.get("type", "N/A")),
            ("Location / Climate", campus_profile.get("location", "N/A")),
            ("Campus Size", campus_profile.get("size", "N/A")),
            ("Main Sustainability Goal", campus_profile.get("main_goal", "N/A")),
        ]

        bill = campus_profile.get("electricity_bill", 0)
        if bill:
            profile_items.append(("Annual Electricity Bill", f"Rs. {bill:,.0f}"))

        for i, (label, value) in enumerate(profile_items):
            if i % 2 == 0:
                self.set_fill_color(*self.light_bg)
            else:
                self.set_fill_color(*self.white)

            self.set_font('Helvetica', 'B', 10)
            self.set_text_color(*self.light_text)
            self.cell(60, 8, f'  {label}', fill=True)
            self.set_font('Helvetica', '', 10)
            self.set_text_color(*self.dark_text)
            self.cell(0, 8, f'  {value}', fill=True)
            self.ln(8)

        # Priorities
        if priorities:
            self.ln(5)
            self.set_font('Helvetica', 'B', 11)
            self.set_text_color(*self.dark_text)
            self.cell(0, 8, 'Selected Priorities:')
            self.ln(8)

            for priority in priorities:
                self.set_font('Helvetica', '', 10)
                self.set_text_color(*self.primary_color)
                self.cell(8, 6, '>')
                self.set_text_color(*self.dark_text)
                self.cell(0, 6, f' {_sanitize(priority)}')
                self.ln(6)

    def add_recommendations(self, recommendations):
        """Add recommendations section."""
        self.add_page()
        self.add_section_header("Smart Recommendations", "AI-generated sustainability solutions prioritized for your campus")

        for i, rec in enumerate(recommendations[:6]):
            # Check if we need a new page
            if self.get_y() > 230:
                self.add_page()

            # Recommendation card
            y_start = self.get_y()

            # Priority badge color
            if rec.get("priority") == "High Priority":
                badge_color = self.success
            elif rec.get("priority") == "Medium Priority":
                badge_color = self.warning
            else:
                badge_color = self.accent_color

            # Card background
            self.set_fill_color(*self.light_bg)
            self.rect(10, y_start, 190, 35, 'F')

            # Green left border
            self.set_fill_color(*self.primary_color)
            self.rect(10, y_start, 3, 35, 'F')

            # Title
            self.set_xy(16, y_start + 2)
            self.set_font('Helvetica', 'B', 11)
            self.set_text_color(*self.dark_text)
            title = rec["title"].encode('latin-1', 'replace').decode('latin-1')
            self.cell(120, 7, f'{i+1}. {title}')

            # Priority badge
            self.set_font('Helvetica', 'B', 8)
            self.set_text_color(*badge_color)
            self.cell(0, 7, rec.get("priority", ""), align='R')

            # Description
            self.set_xy(16, y_start + 10)
            self.set_font('Helvetica', '', 9)
            self.set_text_color(*self.light_text)
            desc = rec["description"][:120] + "..." if len(rec["description"]) > 120 else rec["description"]
            self.multi_cell(180, 4, desc)

            # Metrics row
            self.set_xy(16, y_start + 24)
            self.set_font('Helvetica', '', 8)

            self.set_text_color(*self.primary_color)
            self.cell(45, 5, f'ROI: {rec["payback_years"]}yr payback')
            self.cell(45, 5, _sanitize(f'Investment: {rec["cost_range"]}'))
            self.set_text_color(*self.accent_color)
            self.cell(45, 5, f'Energy: -{rec["savings_percent"]}%')
            self.cell(0, 5, f'CO2: -{rec["co2_reduction"]}%')

            self.set_y(y_start + 38)

    def add_impact_analysis(self, impact_metrics):
        """Add impact analysis section."""
        self.add_page()
        self.add_section_header("Impact Analysis", "Projected savings and environmental impact from recommended solutions")

        # Summary metrics in boxes
        metrics = [
            ("Cost Savings", f"Rs. {impact_metrics['cost_savings']:,.0f}/yr", self.primary_color),
            ("Energy Savings", f"{impact_metrics['energy_savings']}%", self.accent_color),
            ("Water Savings", f"{impact_metrics['water_savings']}%", (0, 121, 107)),
            ("CO2 Reduction", f"{impact_metrics['co2_reduction']}%", self.success),
        ]

        x_start = 12
        box_width = 44
        for label, value, color in metrics:
            self.set_fill_color(*color)
            self.rect(x_start, self.get_y(), box_width, 25, 'F')

            self.set_xy(x_start, self.get_y() + 3)
            self.set_font('Helvetica', 'B', 14)
            self.set_text_color(*self.white)
            self.cell(box_width, 8, value, align='C')

            self.set_xy(x_start, self.get_y() + 10)
            self.set_font('Helvetica', '', 8)
            self.cell(box_width, 5, label, align='C')

            x_start += box_width + 4

        self.ln(30)

        # Breakdown table
        self.add_section_header("Savings Breakdown", "Per-recommendation projected annual savings")

        # Table header
        self.set_fill_color(*self.primary_color)
        self.set_text_color(*self.white)
        self.set_font('Helvetica', 'B', 9)
        self.cell(70, 8, '  Recommendation', fill=True)
        self.cell(35, 8, 'Annual Savings', fill=True, align='C')
        self.cell(25, 8, 'Energy', fill=True, align='C')
        self.cell(25, 8, 'Water', fill=True, align='C')
        self.cell(35, 8, 'Payback', fill=True, align='C')
        self.ln(8)

        for i, item in enumerate(impact_metrics.get("breakdown", [])):
            if i % 2 == 0:
                self.set_fill_color(*self.light_bg)
            else:
                self.set_fill_color(*self.white)

            self.set_text_color(*self.dark_text)
            self.set_font('Helvetica', '', 9)

            title = item["title"].encode('latin-1', 'replace').decode('latin-1')
            self.cell(70, 7, f'  {title}', fill=True)
            self.cell(35, 7, f'Rs. {item["annual_savings"]:,}', fill=True, align='C')
            self.cell(25, 7, f'{item["energy_savings"]}%', fill=True, align='C')
            self.cell(25, 7, f'{item["water_savings"]}%', fill=True, align='C')
            self.cell(35, 7, f'{item["payback_years"]} years', fill=True, align='C')
            self.ln(7)

        # 5-year timeline
        self.ln(10)
        self.add_section_header("5-Year Savings Projection", "Progressive implementation timeline")

        # Timeline table
        self.set_fill_color(*self.accent_color)
        self.set_text_color(*self.white)
        self.set_font('Helvetica', 'B', 9)
        self.cell(38, 8, '  Year', fill=True)
        self.cell(38, 8, 'Adoption', fill=True, align='C')
        self.cell(50, 8, 'Annual Savings', fill=True, align='C')
        self.cell(55, 8, 'Cumulative Savings', fill=True, align='C')
        self.ln(8)

        for i, item in enumerate(impact_metrics.get("timeline", [])):
            if i % 2 == 0:
                self.set_fill_color(*self.light_bg)
            else:
                self.set_fill_color(*self.white)

            self.set_text_color(*self.dark_text)
            self.set_font('Helvetica', '', 9)
            self.cell(38, 7, f'  {item["year"]}', fill=True)
            self.cell(38, 7, f'{item["adoption_percent"]}%', fill=True, align='C')
            self.cell(50, 7, f'Rs. {item["annual_savings"]:,}', fill=True, align='C')
            self.set_font('Helvetica', 'B', 9)
            self.cell(55, 7, f'Rs. {item["cumulative_savings"]:,}', fill=True, align='C')
            self.ln(7)

    def add_action_plan(self, recommendations):
        """Add action plan section."""
        self.add_page()
        self.add_section_header("Action Plan", "Recommended implementation timeline and steps")

        phases = [
            ("Phase 1: Quick Wins (Month 1-3)", recommendations[:2]),
            ("Phase 2: Core Implementation (Month 3-6)", recommendations[2:4]),
            ("Phase 3: Advanced Solutions (Month 6-12)", recommendations[4:6]),
        ]

        for phase_title, phase_recs in phases:
            if not phase_recs:
                continue

            if self.get_y() > 230:
                self.add_page()

            self.set_font('Helvetica', 'B', 11)
            self.set_text_color(*self.primary_color)
            self.cell(0, 8, phase_title)
            self.ln(8)

            for rec in phase_recs:
                self.set_font('Helvetica', 'B', 10)
                self.set_text_color(*self.dark_text)
                title = rec["title"].encode('latin-1', 'replace').decode('latin-1')
                self.cell(0, 6, f'  > {title}')
                self.ln(6)

                # Implementation steps
                for step in rec.get("implementation_steps", [])[:3]:
                    self.set_font('Helvetica', '', 9)
                    self.set_text_color(*self.light_text)
                    step_text = step.encode('latin-1', 'replace').decode('latin-1')
                    self.cell(0, 5, f'      - {step_text}')
                    self.ln(5)

                self.ln(3)

            self.ln(5)

        # Final note
        self.ln(10)
        self.set_fill_color(*self.primary_light)
        self.rect(10, self.get_y(), 190, 20, 'F')
        self.set_xy(15, self.get_y() + 3)
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(*self.primary_color)
        self.cell(0, 6, 'Ready to get started?')
        self.set_xy(15, self.get_y() + 8)
        self.set_font('Helvetica', '', 9)
        self.set_text_color(*self.dark_text)
        self.cell(0, 6, 'CampusGreenify can help you implement these recommendations with expert guidance and monitoring.')


def generate_pdf_report(campus_profile, priorities, recommendations, sustainability_score, impact_metrics):
    """
    Generate a complete PDF report and return as bytes.

    Args:
        campus_profile: Dict with campus information
        priorities: List of selected priorities
        recommendations: List of ranked recommendations
        sustainability_score: Int score 0-100
        impact_metrics: Dict with impact analysis results

    Returns:
        bytes: PDF file content
    """
    pdf = CampusGreenifyReport()

    # Cover page
    pdf.add_cover_page(campus_profile, sustainability_score)

    # Campus profile
    pdf.add_campus_profile(campus_profile, priorities)

    # Recommendations
    pdf.add_recommendations(recommendations)

    # Impact analysis
    pdf.add_impact_analysis(impact_metrics)

    # Action plan
    pdf.add_action_plan(recommendations)

    # Output to bytes (Streamlit requires bytes, not bytearray)
    return bytes(pdf.output())
