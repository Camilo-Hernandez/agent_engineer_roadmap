from reportlab.platypus import Paragraph

from .config import styles
from .content import get_roadmap_content
from .helpers import section_divider, resource_block


def build_sections_story():
    elements = []
    for number, section in enumerate(get_roadmap_content().sections, start=1):
        elements.extend(section_divider(section.title, number))
        for block in section.blocks:
            style_name = "BD"
            if block.kind == "heading":
                style_name = "BD"
                elements.append(Paragraph(f"<b>{block.text}</b>", styles[style_name]))
                continue
            elements.append(Paragraph(block.text, styles[style_name]))
        for resource in section.resources:
            elements.extend(
                resource_block(
                    title=resource.title,
                    description=resource.description,
                    urls=resource.urls,
                    tags=resource.tags,
                )
            )
    return elements
