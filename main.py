from pathlib import Path
from textwrap import dedent
from unicodedata import category
import yaml


def define_env(env):

    CATEGORY_PREFIX = {
        "robotica": "ROB",
        "automatizacion": "AUT",
        "vision": "VIS",
        "salud": "SAL",
        "archivo": "ARX",
    }

    STATUS = {
        "disponible": ("DISPONIBLE", "status-free"),
        "asignado": ("ASIGNADO", "status-assigned"),
        "solicitado": ("SOLICITADO", "status-requested"),
        "completado": ("COMPLETADO", "status-closed"),
        "parcial": ("VARIAS OPCIONES", "status-parcial"),
    }

    def load_projects(category):

        folder = (
            Path(env.project_dir)
            / "docs"
            / "contenidos"
            / category
            / "propuestas"
        )

        projects = []

        if not folder.exists():
            return projects

        for path in folder.glob("*.md"):

            text = path.read_text(encoding="utf-8")

            if not text.startswith("---"):
                continue

            parts = text.split("---", 2)

            if len(parts) < 3:
                continue

            metadata = yaml.safe_load(parts[1]) or {}

            metadata["filename"] = path.name
            metadata["path"] = path

            projects.append(metadata)

        projects.sort(
            key=lambda p: p.get("order", 999)
        )

        return projects

    @env.macro
    def project_cards(category):

        projects = load_projects(category)
        prefix = CATEGORY_PREFIX.get(category, "TFE")

        if not projects:

            if category == "archivo":
                return f"""
<div class="empty-category">
  <span class="empty-category__code">{prefix} / 00</span>
  <h2>El archivo está vacío</h2>
  <p>Todavía no se han incorporado trabajos y propuestas de cursos anteriores.</p>
</div>
"""

            return f"""
<div class="empty-category">
  <span class="empty-category__code">{prefix} / 00</span>
  <h2>No hay propuestas disponibles actualmente</h2>
  <p>Las nuevas propuestas se publicarán en esta sección.</p>
</div>
"""

        prefix = CATEGORY_PREFIX.get(category, "TFG")

        result = ['<div class="project-grid">']

        for project in projects:

            number = project.get("order", 0)
            code = f"{prefix}-{number:02d}"

            status_key = project.get(
                "status",
                "disponible"
            ).lower()

            status_text, status_class = STATUS.get(
                status_key,
                ("DISPONIBLE", "status-free")
            )

            title = project.get(
                "title",
                "Proyecto sin título"
            )

            project_type = project.get(
                "type",
                "TFG"
            )

            summary = project.get(
                "summary",
                ""
            )

            keywords = project.get(
                "keywords",
                []
            )

            keyword_html = " ".join(
                f"<code>{keyword}</code>"
                for keyword in keywords
            )

            variants = project.get(
                "variants",
                []
            )

            variants_html = ""

            if variants:
                rows = []

                for variant in variants:

                    variant_name = variant.get("name", "")
                    variant_status = variant.get("status", "disponible").lower()

                    variant_status_text, variant_status_class = STATUS.get(
                        variant_status,
                        ("DISPONIBLE", "status-free")
                    )

                    rows.append(f"""
                        <span>{variant_name}</span>
                        <span class="project-status {variant_status_class}">
                        {variant_status_text}
                        </span>
                        """)

                variants_html = f"""
                    <div class="project-variants">
                    {''.join(rows)}
                    </div>
                    """

            filename = Path(project["filename"]).stem
            href = f"propuestas/{filename}/"

            result.append(f"""
                <a class="project-card" href="{href}">

                <div class="project-card__meta">
                    <span class="project-code">{code}</span>
                    <span class="project-status {status_class}">
                    {status_text}
                    </span>
                </div>

                <h2>{title}</h2>

                <div class="project-card__tags">
                    <span class="project-type">{project_type}</span>
                    {keyword_html}
                </div>

                <p>{summary}</p>

                {variants_html}

                </a>
                """)

        result.append("</div>")

        return "\n".join(result)

    @env.macro
    def project_header():

        page = env.variables.page
        metadata = page.meta

        project_type = metadata.get("type", "TFG")
        status_key = metadata.get("status", "disponible").lower()
        keywords = metadata.get("keywords", [])
        variants = metadata.get("variants", [])
        order = metadata.get("order", 0)

        src_path = page.file.src_path.replace("\\", "/")
        parts = src_path.split("/")

        category = None

        if "contenidos" in parts:
            i = parts.index("contenidos")

            if i + 1 < len(parts):
                category = parts[i + 1]

        prefix = CATEGORY_PREFIX.get(category, "TFE")

        code = f"{prefix}-{order:02d}"

        status_text, status_class = STATUS.get(
            status_key,
            ("DISPONIBLE", "status-free")
        )

        keyword_html = " ".join(
            f"<code>{keyword}</code>"
            for keyword in keywords
        )

        variants_html = ""

        if variants:
            rows = []

            for variant in variants:

                variant_name = variant.get("name", "")
                variant_status = variant.get(
                    "status",
                    "disponible"
                ).lower()

                variant_status_text, variant_status_class = STATUS.get(
                    variant_status,
                    ("DISPONIBLE", "status-free")
                )

                rows.append(
                    f'<span>{variant_name}</span>'
                    f'<span class="project-status {variant_status_class}">'
                    f'{variant_status_text}'
                    f'</span>'
                )

            variants_html = dedent(f"""
            <div class="project-variants project-header__variants">
            {''.join(rows)}
            </div>
            """).strip()

        return dedent(f"""
        <div class="project-header">
        <span class="project-code">{code}</span>
        <span class="project-status {status_class}">{status_text}</span>

        <div class="project-header__tags">
            <span class="project-type">{project_type}</span>
            {keyword_html}
        </div>

        {variants_html}
        </div>
        """).strip()