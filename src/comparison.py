from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, Spacer, Table, TableStyle

from .config import ACCENT_TEAL, ALT_ROW_BG, DIVIDER_COLOR, TABLE_HEADER_BG, styles
from .content import get_roadmap_content


def build_comparison_table():
    """Comparison table: IBM paid specialization vs. free roadmap."""

    def cell(text, style_name="CE"):
        return Paragraph(text, styles[style_name])

    def format_cell(text):
        if text == "NO cubre":
            return '<b><font color="#c0392b">NO cubre</font></b>'
        return text

    content = get_roadmap_content().comparison
    rows = [[cell(f"<b>{header}</b>", "CH") for header in content.headers]]
    rows.extend([[cell(format_cell(value)) for value in row] for row in content.rows])

    col_widths = [1.55 * inch, 1.55 * inch, 3.5 * inch]
    table = Table(rows, colWidths=col_widths, repeatRows=1)

    style_commands = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_BG),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("GRID", (0, 0), (-1, -1), 0.5, DIVIDER_COLOR),
    ]
    for index in range(1, len(rows)):
        if index % 2 == 0:
            style_commands.append(("BACKGROUND", (0, index), (-1, index), ALT_ROW_BG))
    table.setStyle(TableStyle(style_commands))

    return [
        Spacer(1, 16),
        HRFlowable(
            width="100%",
            thickness=1,
            color=ACCENT_TEAL,
            spaceAfter=8,
        ),
        Paragraph(content.title, styles["SH"]),
        table,
    ]
