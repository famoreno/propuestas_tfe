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
        "interesado": ("INTERESADO", "status-interested"),
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

    def count_project_statuses(categories):

            counts = {
                "asignado": 0,
                "solicitado": 0,
                "interesado": 0,
            }

            for category in categories:
                for project in load_projects(category):

                    variants = project.get("variants", [])

                    items = variants if variants else [project]

                    for item in items:
                        status = item.get("status", "disponible").lower()

                        if status in counts:
                            counts[status] += 1

            return counts

    def calculate_capacity(categories):

        capacity = 0.0

        for category in categories:
            for project in load_projects(category):

                variants = project.get("variants", [])

                items = variants if variants else [project]

                for item in items:

                    status = item.get(
                        "status",
                        "disponible"
                    ).lower()

                    if status != "asignado":
                        continue

                    cotutor = item.get(
                        "cotutor",
                        project.get("cotutor")
                    )

                    if cotutor and str(cotutor).lower() != "none":
                        capacity += 0.5
                    else:
                        capacity += 1.0

        return capacity

    @env.macro
    def capacity_card(max_capacity=5):

        categories = [
            "robotica",
            "automatizacion",
            "vision",
            "salud",
        ]

        counts = count_project_statuses(categories)

        assigned = counts["asignado"]
        requested = counts["solicitado"]
        interested = counts["interesado"]

        capacity = calculate_capacity(categories)

        capacity_percent = min(
            (capacity / max_capacity) * 100,
            100
        )

        return dedent(f"""
        <div class="tfe-card tfe-capacity">

        <div class="capacity-title">
            CAPACIDAD
        </div>

        <div class="capacity-states">

            <div class="capacity-state">
            <span class="capacity-box capacity-box--assigned"></span>
            <span><strong>{assigned}</strong> asignados</span>
            </div>

            <div class="capacity-state">
            <span class="capacity-box capacity-box--requested"></span>
            <span><strong>{requested}</strong> solicitados</span>
            </div>

            <div class="capacity-state">
            <span class="capacity-box capacity-box--interested"></span>
            <span><strong>{interested}</strong> interesados</span>
            </div>

        </div>

        <div class="capacity-total">
            <span>TOTAL</span>
            <strong>{capacity:g} / {max_capacity}</strong>
        </div>

        <div class="capacity-bar">
            <span style="width: {capacity_percent}%"></span>
        </div>

        </div>
        """).strip()
    
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
        cotutor = metadata.get("cotutor")
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

        cotutor_html = ""

        # En proyectos normales se muestra junto al código.
        # En proyectos con variantes se muestra en cada variante.
        if (
            not variants
            and cotutor
            and str(cotutor).lower() != "none"
        ):
            cotutor_html = (
                f'<span class="project-cotutor">'
                f'Cotutor: {cotutor}'
                f'</span>'
            )

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

                # Cotutor específico de la variante.
                # Si no está definido, hereda el cotutor general del proyecto.
                variant_cotutor = variant.get(
                    "cotutor",
                    metadata.get("cotutor")
                )

                cotutor_variant_html = ""

                if (
                    variant_cotutor
                    and str(variant_cotutor).lower() != "none"
                ):
                    cotutor_variant_html = (
                        f'<span class="project-variant-cotutor">'
                        f'Cotutor: {variant_cotutor}'
                        f'</span>'
                    )

                rows.append(
                    f'<div class="project-variant-name">'
                    f'<span>{variant_name}</span>'
                    f'{cotutor_variant_html}'
                    f'</div>'
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
        {cotutor_html}
        <span class="project-status {status_class}">{status_text}</span>

        <div class="project-header__tags">
            <span class="project-type">{project_type}</span>
            {keyword_html}
        </div>

        {variants_html}
        </div>
        """).strip()