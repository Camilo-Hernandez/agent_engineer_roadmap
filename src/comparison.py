from reportlab.lib.units import inch
from reportlab.platypus import Spacer, Paragraph, Table, TableStyle, HRFlowable

from .config import (
    styles,
    ACCENT_TEAL,
    TABLE_HEADER_BG,
    ALT_ROW_BG,
    DIVIDER_COLOR,
)


def build_comparison_table():
    """Comparison table: IBM paid specialization vs. free roadmap."""

    def cell(text, style_name="CE"):
        return Paragraph(text, styles[style_name])

    no_cover = '<b><font color="#c0392b">NO cubre</font></b>'

    rows = [
        [
            cell("<b>Tema</b>", "CH"),
            cell("<b>IBM (Paga)</b>", "CH"),
            cell("<b>Ruta Gratuita</b>", "CH"),
        ],
        [
            cell("Agent Skills (estandar abierto agentskills.io)"),
            cell(no_cover),
            cell("agentskills.io + Anthropic Academy + skills.sh + agentskill.sh"),
        ],
        [
            cell("RAG pipelines, FAISS, vectores"),
            cell("Cubre"),
            cell("DeepLearning.AI — RAG course"),
        ],
        [
            cell("LangChain + LangGraph"),
            cell("Cubre"),
            cell("LangChain Academy + DeepLearning.AI (3 cursos)"),
        ],
        [
            cell("MCP (Model Context Protocol)"),
            cell("Cubre (FastMCP)"),
            cell("HuggingFace + Anthropic + Microsoft"),
        ],
        [
            cell("LLMs locales: fine-tuning, Ollama, open-weight"),
            cell(no_cover),
            cell("Unsloth + HF TRL + Ollama + Decoding AI Magazine"),
        ],
        [
            cell("Multi-agente (CrewAI, AG2)"),
            cell("Cubre"),
            cell("DeepLearning.AI + docs oficiales"),
        ],
        [cell("Multimodal AI"), cell("Cubre"), cell("DeepLearning.AI short courses")],
        [
            cell("Deploy multi-cloud (AWS, Railway, Fly.io, etc.)"),
            cell("Parcial (Gradio, Flask)"),
            cell("Advent of Agents + AWS Lambda docs + Railway/Render/Fly.io/DO"),
        ],
        [
            cell("Super 24/7 Agents"),
            cell(no_cover),
            cell(
                "OpenClaw + MaxClaw + KimiClaw + KiloClaw + NemoClaw + Perplexity Computer + n8n"
            ),
        ],
    ]

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
    for i in range(1, len(rows)):
        if i % 2 == 0:
            style_commands.append(("BACKGROUND", (0, i), (-1, i), ALT_ROW_BG))
    table.setStyle(TableStyle(style_commands))

    elements = [
        Spacer(1, 16),
        HRFlowable(
            width="100%",
            thickness=1,
            color=ACCENT_TEAL,
            spaceAfter=8,
        ),
        Paragraph(
            "Tabla Resumen: Especializacion Paga de IBM vs. Ruta Gratuita",
            styles["SH"],
        ),
        table,
    ]
    return elements
