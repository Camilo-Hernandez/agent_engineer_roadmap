from reportlab.platypus import Spacer, Paragraph, HRFlowable

from .config import styles, MUTED_GRAY


def build_footer():
    """Closing note and footer."""
    return [
        Spacer(1, 12),
        Paragraph(
            "<b>Ventaja de la ruta gratuita:</b> La especializacion paga de IBM "
            "no cubre Agent Skills (estandar abierto), fine-tuning/deployment "
            "local de modelos open-weight, ni superagentes personales "
            "(OpenClaw/MaxClaw). Estos tres temas son criticos para privacidad "
            "de datos, reduccion de costos, modelos especializados, y asistentes "
            "autonomos que funcionan con cualquier LLM.",
            styles["WN"],
        ),
        Spacer(1, 14),
        HRFlowable(
            width="40%", thickness=0.5,
            color=MUTED_GRAY, spaceAfter=6, hAlign="CENTER",
        ),
        Paragraph(
            "Compilado en marzo 2026. Todos los recursos listados son "
            "gratuitos al momento de publicacion.",
            styles["FN"],
        ),
    ]
