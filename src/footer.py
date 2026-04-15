from reportlab.platypus import HRFlowable, Paragraph, Spacer

from .config import MUTED_GRAY, styles
from .content import get_roadmap_content


def build_footer():
    """Closing note and footer."""
    content = get_roadmap_content()
    return [
        Spacer(1, 12),
        Paragraph(f"<b>{content.closing_note}</b>", styles["WN"]),
        Spacer(1, 14),
        HRFlowable(
            width="40%",
            thickness=0.5,
            color=MUTED_GRAY,
            spaceAfter=6,
            hAlign="CENTER",
        ),
        Paragraph(content.publication_note, styles["FN"]),
    ]
