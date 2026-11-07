import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT

pdf_path = r"c:\Users\Atharva Meharkure\Desktop\MAEHK PORTFOLIO\resume.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    leftMargin=36,
    rightMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

# Colors
C_PRIMARY = colors.HexColor("#111111")
C_ACCENT = colors.HexColor("#E8451E")
C_MUTED = colors.HexColor("#4B5563")
C_LINE = colors.HexColor("#D1D5DB")
C_BG_LIGHT = colors.HexColor("#F9FAFB")

# Custom Styles
title_style = ParagraphStyle(
    'DocTitle',
    fontName='Helvetica-Bold',
    fontSize=22,
    leading=26,
    textColor=C_PRIMARY,
    alignment=TA_CENTER
)

sub_style = ParagraphStyle(
    'DocSub',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=C_ACCENT,
    alignment=TA_CENTER
)

contact_style = ParagraphStyle(
    'DocContact',
    fontName='Helvetica',
    fontSize=9,
    leading=13,
    textColor=C_MUTED,
    alignment=TA_CENTER
)

sec_head = ParagraphStyle(
    'SecHead',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=14,
    textColor=C_PRIMARY,
    spaceAfter=4,
    textTransform='uppercase'
)

item_title = ParagraphStyle(
    'ItemTitle',
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=13,
    textColor=C_PRIMARY
)

item_sub = ParagraphStyle(
    'ItemSub',
    fontName='Helvetica-Bold',
    fontSize=9,
    leading=12,
    textColor=C_ACCENT
)

item_date = ParagraphStyle(
    'ItemDate',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=C_MUTED,
    alignment=TA_RIGHT
)

body_text = ParagraphStyle(
    'BodyText',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#27272A")
)

bullet_text = ParagraphStyle(
    'BulletText',
    fontName='Helvetica',
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#27272A"),
    leftIndent=10
)

story = []

# Header
story.append(Paragraph("MAHEK GHODMARE", title_style))
story.append(Spacer(1, 3))
story.append(Paragraph("DATA ANALYST &bull; AI BUSINESS ANALYST &bull; FOUNDER", sub_style))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "Nagpur, MH &bull; Symbiosis Institute of Technology (SIT Nagpur) &bull; "
    "<font color='#E8451E'>github.com/mahekghodmare</font> &bull; "
    "linkedin.com/in/mahekghodmare",
    contact_style
))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1.5, color=C_PRIMARY, spaceBefore=0, spaceAfter=8))

# Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", sec_head))
story.append(Paragraph(
    "Data Science and AI/ML undergraduate at <b>Symbiosis Institute of Technology, Nagpur</b> with practical experience in statistical modeling, exploratory data analysis, and autonomous AI agents. Strong analytical rigor paired with a founder's mindset, having ideated and built consumer brand ventures (CALYVRA & FIZZKEY). Proven track record in predictive analytics, RFM customer clustering, and IEEE signal compression research.",
    body_text
))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_LINE, spaceBefore=0, spaceAfter=8))

# Education
story.append(Paragraph("EDUCATION", sec_head))
edu_data = [
    [
        Paragraph("<b>B.Tech in Data Science & Artificial Intelligence / Machine Learning</b><br/><font color='#4B5563'>Symbiosis Institute of Technology (SIT), Nagpur</font>", body_text),
        Paragraph("2023 &ndash; 2027<br/><i>Nagpur, Maharashtra</i>", item_date)
    ]
]
t_edu = Table(edu_data, colWidths=[400, 140])
t_edu.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_edu)
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_LINE, spaceBefore=0, spaceAfter=8))

# Technical Skills
story.append(Paragraph("TECHNICAL PROFICIENCIES", sec_head))
skills_data = [
    [Paragraph("<b>Programming & Querying:</b>", body_text), Paragraph("Python (Pandas, NumPy, Scikit-Learn, Plotly, Seaborn), SQL, SQLite", body_text)],
    [Paragraph("<b>Analytics & Modeling:</b>", body_text), Paragraph("Exploratory Data Analysis (EDA), RFM Segmentation, K-Means Clustering, A/B Testing", body_text)],
    [Paragraph("<b>AI & Automation:</b>", body_text), Paragraph("Autonomous Agentic AI, Multi-step Tool Calling, LLM Prompt Orchestration", body_text)],
    [Paragraph("<b>BI & Visualization:</b>", body_text), Paragraph("Tableau, Power BI, Streamlit Dashboards, Interactive Plotly Reports", body_text)],
    [Paragraph("<b>Tools & Versioning:</b>", body_text), Paragraph("Git, GitHub, Jupyter Notebooks, VS Code, REST APIs, FastAPI", body_text)]
]
t_skills = Table(skills_data, colWidths=[150, 390])
t_skills.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('LEFTPADDING', (0,0), (-1,-1), 0),
    ('RIGHTPADDING', (0,0), (-1,-1), 0)
]))
story.append(t_skills)
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_LINE, spaceBefore=0, spaceAfter=8))

# Experience
story.append(Paragraph("PRACTICAL EXPERIENCE & VENTURES", sec_head))

# Maincrafts
exp_data = [
    [
        Paragraph("<b>Data Science & Analytics Intern</b> &bull; Maincrafts Technology", item_title),
        Paragraph("Internship", item_date)
    ]
]
t_exp = Table(exp_data, colWidths=[420, 120])
t_exp.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_exp)
story.append(Paragraph("&bull; Executed end-to-end data cleansing, statistical inference, and predictive machine learning models on real-world datasets.", bullet_text))
story.append(Paragraph("&bull; Built reporting pipelines and visual analytics charts translating business indicators into actionable executive summaries.", bullet_text))
story.append(Spacer(1, 5))

# Ventures
venture_data = [
    [
        Paragraph("<b>Founder & Product Strategist</b> &bull; CALYVRA & FIZZKEY", item_title),
        Paragraph("2024 &ndash; Present", item_date)
    ]
]
t_ven = Table(venture_data, colWidths=[420, 120])
t_ven.setStyle(TableStyle([('LEFTPADDING', (0,0), (-1,-1), 0), ('RIGHTPADDING', (0,0), (-1,-1), 0)]))
story.append(t_ven)
story.append(Paragraph("&bull; <b>CALYVRA:</b> Conceptualized card-themed 10ml luxury pocket extrait de parfum with collectible editions and D2C marketing strategy.", bullet_text))
story.append(Paragraph("&bull; <b>FIZZKEY:</b> Engineered a 6-month GTM roadmap for functional sparkling adaptogen beverage with localized contract canning analysis.", bullet_text))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_LINE, spaceBefore=0, spaceAfter=8))

# Featured Projects
story.append(Paragraph("KEY PROJECTS & RESEARCH", sec_head))

# Project 1
story.append(Paragraph("<b>Vriksha AI Agent &mdash; Autonomous Multi-Step Reasoning Engine</b> | <i>Python, Agentic AI, Tool Execution</i>", item_title))
story.append(Paragraph("&bull; Built an autonomous AI agent with scratchpad reasoning, tool integration, and self-directed task replanning protocols.", bullet_text))
story.append(Paragraph("&bull; GitHub: github.com/mahekghodmare/Vriksha-Ai-agent-project-", bullet_text))
story.append(Spacer(1, 4))

# Project 2
story.append(Paragraph("<b>Shopper Spectrum &mdash; Customer RFM Segmentation</b> | <i>Python, Scikit-Learn, K-Means, Plotly</i>", item_title))
story.append(Paragraph("&bull; Analyzed 4,300+ customer profiles across Recency, Frequency, Monetary metrics; isolated 4 distinct commercial personas with 94.8% clustering cohesion.", bullet_text))
story.append(Spacer(1, 4))

# Project 3
story.append(Paragraph("<b>Titanic Multivariate Exploratory Data Analysis Dashboard</b> | <i>Python, Seaborn, Pandas, Plotly</i>", item_title))
story.append(Paragraph("&bull; Uncovered demographic survival determinants, class hierarchies, and family cohort survival factors via interactive visualization pipelines.", bullet_text))
story.append(Paragraph("&bull; GitHub: github.com/mahekghodmare/Data-Science-Analysis-with-Python-", bullet_text))
story.append(Spacer(1, 4))

# Project 4
story.append(Paragraph("<b>TaskFlow &mdash; Agile Workflow & Sprint Velocity Engine</b> | <i>JavaScript, State Management, UX</i>", item_title))
story.append(Paragraph("&bull; Created a responsive agile sprint prioritization board with drag-and-drop state persistence and sub-second velocity tracking.", bullet_text))
story.append(Paragraph("&bull; GitHub: github.com/mahekghodmare/TaskFlow", bullet_text))
story.append(Spacer(1, 4))

# Project 5
story.append(Paragraph("<b>NEXUS-AIC &mdash; ECG Signal Compression Framework</b> | <i>Healthcare AI, Signal Processing (IEEE Paper in progress)</i>", item_title))
story.append(Paragraph("&bull; Designed a Unified Priority Score protecting critical QRS cardiac fiducial markers during high-ratio telemetric transmission.", bullet_text))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=0.5, color=C_LINE, spaceBefore=0, spaceAfter=8))

# Certifications
story.append(Paragraph("CERTIFICATIONS & HONORS", sec_head))
story.append(Paragraph("&bull; <b>Data Science & Analytics Internship Certification</b> &ndash; Maincrafts Technology", bullet_text))
story.append(Paragraph("&bull; <b>Mastering Agentic AI: Prompts to Protocols</b> &ndash; Autonomous Agent Systems Credential", bullet_text))
story.append(Paragraph("&bull; <b>Verified Technical Badges (Credly)</b> &ndash; Computational Thinking & Problem Solving", bullet_text))
story.append(Paragraph("&bull; <b>Technical Symposium Achievement Recognition</b> &ndash; Symbiosis Institute of Technology", bullet_text))

doc.build(story)
print("Resume generated successfully at:", pdf_path)
