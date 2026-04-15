from reportlab.platypus import Spacer, Paragraph, HRFlowable

from .config import styles, DIVIDER_COLOR


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


def make_link(url_text):
    """Convert display URLs into clickable <a href> links. Handles '|' separated multi-URLs."""
    parts = [p.strip() for p in url_text.split("|")]
    linked = []
    for part in parts:
        if part.startswith("http"):
            linked.append(f'<a href="{part}" color="#2980b9">{part}</a>')
        elif "(" in part:
            domain = part.split("(")[0].strip()
            note = "(" + part.split("(")[1]
            linked.append(
                f'<a href="https://{domain}" color="#2980b9">'
                f"https://{domain}</a> {note}"
            )
        else:
            linked.append(
                f'<a href="https://{part}" color="#2980b9">https://{part}</a>'
            )
    return "  |  ".join(linked)


def resource_block(title, description, url, tags=None):
    """Create a resource entry with title, description, URL, and optional tags."""
    tag_html = ""
    if tags:
        for tag_label, tag_color in tags:
            tag_html += f' <font color="{tag_color}" size="8">[{tag_label}]</font>'
    parts = [p.strip() for p in url.split("|")]
    items = [
        Paragraph(f"&#9654; {title}{tag_html}", styles["RT"]),
        Paragraph(description, styles["RD"]),
    ]
    for part in parts:
        link_html = make_link(part)
        items.append(Paragraph(f"&#8594; {link_html}", styles["UL"]))
    return items
