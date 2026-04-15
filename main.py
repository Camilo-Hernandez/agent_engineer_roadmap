from src.config import doc
from src.header import build_header
from src.sections import (
    build_section_agent_skills,
    build_section_rag,
    build_section_langchain,
    build_section_mcp,
    build_section_local_llms,
    build_section_multi_agent,
    build_section_multimodal,
    build_section_deploy,
    build_section_superagents,
)
from src.comparison import build_comparison_table
from src.footer import build_footer


def build_pdf():
    """Assemble all sections and generate the PDF."""
    story = []
    story.extend(build_header())
    section_builders = [
        build_section_agent_skills,
        build_section_rag,
        build_section_mcp,
        build_section_langchain,
        build_section_multi_agent,
        build_section_local_llms,
        build_section_multimodal,
        build_section_deploy,
        build_section_superagents,
    ]
    for number, builder in enumerate(section_builders, start=1):
        story.extend(builder(number))
    story.extend(build_comparison_table())
    story.extend(build_footer())
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
