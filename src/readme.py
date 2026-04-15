from pathlib import Path

from .config import README_PATH
from .content import get_roadmap_content


def _format_intro(content):
    return (
        f"{content.intro} "
        f"[{content.intro_link_label}]({content.intro_link_url}) "
        f"{content.intro_suffix}"
    )


def render_readme_markdown() -> str:
    content = get_roadmap_content()
    lines = [
        f"# {content.title}",
        "",
        content.subtitle,
        "",
        _format_intro(content),
        "",
        f"**{content.author}**",
        "",
    ]

    lines.append(f"## {content.comparison.title}")
    lines.append("")
    lines.append("| " + " | ".join(content.comparison.headers) + " |")
    lines.append("|" + "---|" * len(content.comparison.headers))
    for row in content.comparison.rows:
        escaped = [cell.replace("|", "\\|") for cell in row]
        lines.append("| " + " | ".join(escaped) + " |")
    lines.extend(
        [
            "",
            f"> {content.closing_note}",
            "",
            content.publication_note,
            "",
        ]
    )

    for number, section in enumerate(content.sections, start=1):
        lines.append(f"## {number}. {section.title}")
        lines.append("")
        for block in section.blocks:
            if block.kind == "heading":
                lines.append(f"### {block.text}")
            else:
                lines.append(block.text)
            lines.append("")
        for resource in section.resources:
            tags = f" [{' | '.join(resource.tags)}]" if resource.tags else ""
            lines.append(f"- **{resource.title}**{tags}")
            lines.append(f"  {resource.description}")
            for url in resource.urls:
                lines.append(f"  - {url}")
            lines.append("")

    return "\n".join(lines)


def write_readme(output_path: str = README_PATH) -> Path:
    path = Path(output_path)
    path.write_text(render_readme_markdown(), encoding="utf-8")
    return path
