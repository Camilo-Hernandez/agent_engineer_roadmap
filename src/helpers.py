from reportlab.platypus import HRFlowable, Paragraph, Spacer

from .config import DIVIDER_COLOR, TAG_COLORS, styles


def section_divider(title, number):
    """Create a section header with a horizontal rule."""
    return [
        Spacer(1, 6),
        HRFlowable(
            width="100%",
            thickness=0.5,
            color=DIVIDER_COLOR,
            spaceAfter=2,
        ),
        Paragraph(f"{number}. {title}", styles["SH"]),
    ]


def make_link(url: str):
    """Convert a URL into a clickable ReportLab link."""
    if url.startswith("http"):
        return f'<a href="{url}" color="#2980b9">{url}</a>'
    return f'<a href="https://{url}" color="#2980b9">https://{url}</a>'


def resource_block(title, description, urls, tags=None):
    """Create a resource entry with title, description, URLs, and optional tags."""
    tag_html = ""
    if tags:
        for tag_label in tags:
            tag_color = TAG_COLORS.get(tag_label, TAG_COLORS["GRATUITO"])
            tag_html += f' <font color="{tag_color}" size="8">[{tag_label}]</font>'
    items = [
        Paragraph(f"&#9654; {title}{tag_html}", styles["RT"]),
        Paragraph(description, styles["RD"]),
    ]
    for url in urls:
        items.append(Paragraph(f"&#8594; {make_link(url)}", styles["UL"]))
    return items
