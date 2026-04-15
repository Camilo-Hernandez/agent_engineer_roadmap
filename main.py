from src.comparison import build_comparison_table
from src.config import doc
from src.footer import build_footer
from src.header import build_header
from src.readme import write_readme
from src.sections import build_sections_story


def build_pdf():
    """Assemble all sections and generate the PDF."""
    story = []
    story.extend(build_header())
    story.extend(build_comparison_table())
    story.extend(build_footer())
    story.extend(build_sections_story())
    doc.build(story)


def build_outputs():
    """Generate every published output from the shared roadmap content."""
    build_pdf()
    write_readme()


if __name__ == "__main__":
    build_outputs()
