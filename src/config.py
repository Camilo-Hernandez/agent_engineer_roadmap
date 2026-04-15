from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

# Colors

DARK_BG = HexColor("#1a1a2e")
ACCENT_BLUE = HexColor("#0f3460")
ACCENT_TEAL = HexColor("#16a085")
MUTED_GRAY = HexColor("#6c757d")
DARK_TEXT = HexColor("#212529")
SECTION_BG = HexColor("#eef2f7")
LINK_COLOR = HexColor("#2980b9")
TABLE_HEADER_BG = HexColor("#1a1a2e")
ALT_ROW_BG = HexColor("#f0f4f8")
TAG_FREE = HexColor("#27ae60")
TAG_OFFICIAL = HexColor("#2980b9")
TAG_COMMUNITY = HexColor("#8e44ad")
TAG_SHORT = HexColor("#7144ad")
WARNING_BG = HexColor("#fdf2e9")
DIVIDER_COLOR = HexColor("#dee2e6")

# Tag shorthand

FREE = TAG_FREE.hexval()
OFFICIAL = TAG_OFFICIAL.hexval()
COMMUNITY = TAG_COMMUNITY.hexval()
SHORT = TAG_SHORT.hexval()

TAG_COLORS = {
    "GRATUITO": FREE,
    "OFICIAL": OFFICIAL,
    "COMUNIDAD": COMMUNITY,
    "OPEN SOURCE": COMMUNITY,
    "CERTIFICADO": COMMUNITY,
    "CREDITOS GRATIS": COMMUNITY,
    "AWS": OFFICIAL,
    "PAGO": OFFICIAL,
    "GOOGLE CLOUD": COMMUNITY,
    "RAPIDO": SHORT,
    "TIER GRATIS": FREE,
}

# Document setup

OUTPUT_PATH = "hoja_de_ruta_ia_agents_engineer.pdf"
README_PATH = "README.md"

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=letter,
    topMargin=0.6 * inch,
    bottomMargin=0.6 * inch,
    leftMargin=0.7 * inch,
    rightMargin=0.7 * inch,
)

# Styles

styles = getSampleStyleSheet()

CUSTOM_STYLES = [
    (
        "MT",
        dict(
            parent=styles["Title"],
            fontSize=26,
            leading=32,
            textColor=DARK_BG,
            spaceAfter=4,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        ),
    ),
    (
        "ST",
        dict(
            parent=styles["Normal"],
            fontSize=12,
            leading=16,
            textColor=MUTED_GRAY,
            spaceAfter=20,
            alignment=TA_CENTER,
            fontName="Helvetica",
        ),
    ),
    (
        "AU",
        dict(
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK_TEXT,
            spaceAfter=2,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        ),
    ),
    (
        "AE",
        dict(
            parent=styles["Normal"],
            fontSize=9,
            leading=12,
            textColor=LINK_COLOR,
            spaceAfter=16,
            alignment=TA_CENTER,
            fontName="Helvetica",
        ),
    ),
    (
        "SH",
        dict(
            parent=styles["Heading1"],
            fontSize=16,
            leading=20,
            textColor=ACCENT_BLUE,
            spaceBefore=18,
            spaceAfter=8,
            fontName="Helvetica-Bold",
        ),
    ),
    (
        "BD",
        dict(
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK_TEXT,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontName="Helvetica",
        ),
    ),
    (
        "RT",
        dict(
            parent=styles["Normal"],
            fontSize=11,
            leading=15,
            textColor=DARK_BG,
            spaceBefore=6,
            spaceAfter=2,
            fontName="Helvetica-Bold",
        ),
    ),
    (
        "RD",
        dict(
            parent=styles["Normal"],
            fontSize=9.5,
            leading=13,
            textColor=MUTED_GRAY,
            spaceAfter=4,
            leftIndent=12,
            fontName="Helvetica",
        ),
    ),
    (
        "UL",
        dict(
            parent=styles["Normal"],
            fontSize=9,
            leading=12,
            textColor=LINK_COLOR,
            spaceAfter=8,
            leftIndent=12,
            fontName="Helvetica-Oblique",
        ),
    ),
    (
        "FN",
        dict(
            parent=styles["Normal"],
            fontSize=8,
            leading=10,
            textColor=MUTED_GRAY,
            alignment=TA_CENTER,
            fontName="Helvetica",
        ),
    ),
    (
        "CE",
        dict(
            parent=styles["Normal"],
            fontSize=8.5,
            leading=11,
            textColor=DARK_TEXT,
            fontName="Helvetica",
        ),
    ),
    (
        "CH",
        dict(
            parent=styles["Normal"],
            fontSize=8.5,
            leading=11,
            textColor=white,
            fontName="Helvetica-Bold",
        ),
    ),
    (
        "CN",
        dict(
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK_TEXT,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
            fontName="Helvetica-Oblique",
            leftIndent=16,
            rightIndent=16,
            backColor=SECTION_BG,
            borderPadding=(8, 8, 8, 8),
        ),
    ),
    (
        "WN",
        dict(
            parent=styles["Normal"],
            fontSize=10,
            leading=14,
            textColor=DARK_TEXT,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
            fontName="Helvetica-Oblique",
            leftIndent=16,
            rightIndent=16,
            backColor=WARNING_BG,
            borderPadding=(8, 8, 8, 8),
        ),
    ),
]

for name, config in CUSTOM_STYLES:
    styles.add(ParagraphStyle(name, **config))
