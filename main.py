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
    story.extend(build_section_agent_skills())
    story.extend(build_section_rag())
    story.extend(build_section_langchain())
    story.extend(build_section_mcp())
    story.extend(build_section_local_llms())
    story.extend(build_section_multi_agent())
    story.extend(build_section_multimodal())
    story.extend(build_section_deploy())
    story.extend(build_section_superagents())
    story.extend(build_comparison_table())
    story.extend(build_footer())
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
