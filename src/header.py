import os

from reportlab.platypus import Spacer, Paragraph, HRFlowable

from .config import styles, ACCENT_TEAL

GMAIL_ICON = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "gmail_icon.png"
)


def build_header():
    """Build the document header with title, subtitle, and author info."""
    return [
        Spacer(1, 20),
        Paragraph("Hoja de Ruta Gratuita", styles["MT"]),
        Paragraph(
            "Transformers, RAG, Agentic AI, Agent Skills, MCP, LLMs Locales y Superagentes",
            styles["ST"],
        ),
        HRFlowable(
            width="60%",
            thickness=2,
            color=ACCENT_TEAL,
            spaceAfter=12,
            spaceBefore=4,
            hAlign="CENTER",
        ),
        Spacer(1, 10),
        Paragraph(
            "Alternativa gratuita a la especializacion paga de IBM "
            '<a href="https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai" color="#2980b9">'
            "<b>RAG and Agentic AI Professional Certificate</b></a> en Coursera. "
            "Estos recursos cubren el mismo conocimiento y más, provenientes "
            "directamente de los creadores de cada herramienta.",
            styles["CN"],
        ),
        Spacer(1, 10),
        Paragraph(
            "Camilo Hernandez Ruiz — Ingeniero de Software y Automatizaciones",
            styles["AU"],
        ),
        Paragraph(
            f'<img src="{GMAIL_ICON}" width="12" height="9" valign="middle"/> '
            '<a href="mailto:camihruiz24+iaroadmap@gmail.com" '
            'color="#2980b9">camihruiz24@gmail.com</a>',
            styles["AE"],
        ),
    ]
