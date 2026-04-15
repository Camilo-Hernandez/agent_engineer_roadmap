import os

from reportlab.platypus import HRFlowable, Paragraph, Spacer

from .config import ACCENT_TEAL, styles
from .content import get_roadmap_content

GMAIL_ICON = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "assets", "gmail_icon.png"
)


def build_header():
    """Build the document header with title, subtitle, and author info."""
    content = get_roadmap_content()
    return [
        Spacer(1, 20),
        Paragraph(content.title, styles["MT"]),
        Paragraph(content.subtitle, styles["ST"]),
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
            f'{content.intro} <a href="{content.intro_link_url}" color="#2980b9">'
            f"<b>{content.intro_link_label}</b></a> {content.intro_suffix}",
            styles["CN"],
        ),
        Spacer(1, 10),
        Paragraph(
            f'<font name="Helvetica">Creado por </font>{content.author}', styles["AU"]
        ),
        # Paragraph(
        #     f'<img src="{GMAIL_ICON}" width="12" height="9" valign="middle"/> '
        #     '<a href="mailto:camihruiz24+iaroadmap@gmail.com" '
        #     'color="#2980b9">camihruiz24@gmail.com</a>',
        #     styles["AE"],
        # ),
    ]
