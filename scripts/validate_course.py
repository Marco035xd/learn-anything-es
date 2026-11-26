#!/usr/bin/env python3
"""Valida la estructura y el estado de un curso de Learn Anything."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover - fallo del entorno
    raise SystemExit("Se requiere PyYAML. Instálalo con python3 -m pip install pyyaml") from exc


REQUIRED_FILES = (
    "00-course-outline.yaml",
    "00-source-manifest.yaml",
    "learner-state.yaml",
    "review-queue.yaml",
)

ROUTE_STATUSES = {"active", "provisional", "completed", "skipped"}
MATERIAL_STATUSES = {
    "not_generated",
    "draft",
    "source_checked",
    "fact_checked",
    "pedagogy_checked",
    "verified",
    "frozen",
    "invalidated",
    "legacy_prebuilt",
}
DELIVERY_STATUSES = {"not_started", "in_progress", "completed"}
MASTERY_STATUSES = {
    "unknown",
    "exposed",
    "guided",
    "independent",
    "transferable",
    "durable",
}
READY_PART_STATUSES = {
    "ready",
    "in_progress",
    "completed",
    "source_checked",
    "fact_checked",
    "pedagogy_checked",
    "verified",
    "frozen",
}
SOURCE_MODES = {"agent_researched", "source_bounded", "source_augmented"}
PASSED_REVIEW = {"passed", "complete", "completed"}
COURSE_HOME_NAMES = ("inicio-del-curso.md", "课程入口.md", "00-课程入口.md")
FIXED_OUTLINES = (
    ("Material principal", "Ejemplos y contraejemplos", "Límites fáciles de confundir"),
    ("核心教材", "正例与反例", "容易混淆的边界"),
)
SPANISH_TASK_HEADING = "## Tu turno"
LEGACY_TASK_HEADING = "## 轮到你"
NAVIGATION_LABELS = (
    ("Posición actual:", "当前位置："),
    ("Pregunta central de la lección:", "本课总问题："),
    ("Qué resolvió el segmento anterior:", "上一段已经解决："),
    ("Por qué sigue este segmento:", "这一段为什么接着学："),
    ("Qué explica la fuente en este segmento:", "原教材这一段主要讲："),
    ("Qué podrás hacer al terminar:", "本段结束时你要能做到："),
)
REQUIRED_GRADING_RULES = ("correct", "partially_correct", "incorrect", "ungradable")
REQUIRED_PREFLIGHT = (
    "target_node_is_explicit",
    "source_support_is_sufficient",
    "answer_or_rubric_frozen",
    "options_are_mutually_exclusive",
    "question_is_realistic",
    "learner_has_required_prerequisites",
)
REQUIRED_TEACHING_LAYERS = ("source_layer", "tutor_synthesis", "application_layer")
MASTERY_RANK = {
    "unknown": 0,
    "exposed": 1,
    "guided": 2,
    "independent": 3,
    "transferable": 4,
    "durable": 5,
}


def load_yaml(path: Path, errors: list[str]):
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except Exception as exc:  # noqa: BLE001 - el validador reúne todos los fallos
        errors.append(f"No se pudo leer el YAML: {path}: {exc}")
        return None


def resolve(course_dir: Path, relative_path: str | None) -> Path | None:
    if not relative_path:
        return None
    return (course_dir / relative_path).resolve()


def markdown_frontmatter(text: str) -> dict:
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            data = yaml.safe_load(parts[1])
            return data if isinstance(data, dict) else {}
    return {}


def body_without_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("---\n", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def validate_longform(
    path: Path,
    errors: list[str],
    warnings: list[str],
    require_v4_protocol: bool = False,
) -> None:
    raw_text = path.read_text(encoding="utf-8")
    metadata = markdown_frontmatter(raw_text)
    text = body_without_frontmatter(raw_text)
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    prose_lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
        and not line.lstrip().startswith(("#", "-", "*", ">", "|", "```"))
    ]
    table_lines = [line for line in text.splitlines() if line.lstrip().startswith("|")]

    if SPANISH_TASK_HEADING in text or not chinese_chars:
        words = len(re.findall(r"\b[^\W\d_]+\b", " ".join(prose_lines)))
        if words < 400:
            warnings.append(f"El material podría ser demasiado breve ({words} palabras): {path}")
    elif chinese_chars < 1200:
        warnings.append(
            f"El material podría ser demasiado breve ({chinese_chars} caracteres chinos): {path}"
        )

    if len(prose_lines) < 12:
        errors.append(f"Falta una explicación desarrollada en prosa: {path}")
    if table_lines and len(table_lines) >= len(prose_lines):
        errors.append(f"Las tablas parecen reemplazar la explicación: {path}")
    if any(all(f"## {heading}" in text for heading in headings) for headings in FIXED_OUTLINES):
        errors.append(f"Se detectó un esquema fijo en lugar de una explicación narrativa: {path}")

    task_positions = [
        position
        for heading in (SPANISH_TASK_HEADING, LEGACY_TASK_HEADING)
        if (position := text.find(heading)) >= 0
    ]
    if not task_positions:
        errors.append(f"Falta una actividad para el estudiante: {path}")
    if "## Fuentes y límites" not in text and "来源" not in text:
        errors.append(f"Faltan referencias a las fuentes o sus límites: {path}")

    if require_v4_protocol:
        navigation = metadata.get("navigation")
        if not isinstance(navigation, dict):
            errors.append(f"Faltan los metadatos navigation del material v4: {path}")
        for layer in REQUIRED_TEACHING_LAYERS:
            if not isinstance(metadata.get(layer), dict):
                errors.append(f"Faltan los metadatos {layer} del material v4: {path}")
        for label, legacy_label in NAVIGATION_LABELS:
            label_positions = [
                position
                for candidate in (label, legacy_label)
                if (position := text.find(candidate)) >= 0
            ]
            if not label_positions:
                errors.append(f"Falta el rótulo de navegación «{label}» en el material v4: {path}")
            elif task_positions and min(label_positions) > min(task_positions):
                errors.append(f"El rótulo «{label}» aparece después de la actividad: {path}")


def validate_assessments(
    plan: dict,
    plan_path: Path,
    plan_version: int,
    errors: list[str],
) -> None:
    assessment_config = plan.get("assessment")
    if not isinstance(assessment_config, dict):
        if plan_version >= 3:
            errors.append("Falta la configuración de evaluación en el plan de lección v3")
        return

    assessment_path = resolve(plan_path.parent, assessment_config.get("path"))
    if not assessment_path or not assessment_path.is_file():
        errors.append("Falta el archivo de evaluación")
        return

    assessment_data = load_yaml(assessment_path, errors) or {}
    assessment_version = assessment_data.get("version", 1)
    assessments = assessment_data.get("assessments")
    if not isinstance(assessments, list) or not assessments:
        errors.append("El archivo de evaluación debe contener una lista assessments con al menos un elemento")
        return

    assessment_ids = [item.get("assessment_id") for item in assessments]
    if any(not assessment_id for assessment_id in assessment_ids):
        errors.append("Falta assessment_id en la evaluación")
    if len(assessment_ids) != len(set(assessment_ids)):
        errors.append("Hay valores assessment_id duplicados")

    delivered_ids = set(assessment_config.get("delivered_assessment_ids") or [])
    pending_ids = set(assessment_config.get("pending_assessment_ids") or [])
    referenced_ids = delivered_ids | pending_ids
    missing_ids = referenced_ids - set(assessment_ids)
    for assessment_id in sorted(missing_ids):
        errors.append(f"El plan de lección referencia una evaluación que falta: {assessment_id}")

    for item in assessments:
        assessment_id = item.get("assessment_id", "<missing>")
        for field in ("correct_answer", "rationale"):
            if not item.get(field):
                errors.append(f"{assessment_id}: falta {field}")
        if not isinstance(item.get("acceptable_variants"), list):
            errors.append(f"{assessment_id}: acceptable_variants debe ser una lista")
        grading_rule = item.get("grading_rule")
        if not isinstance(grading_rule, dict):
            errors.append(f"{assessment_id}: grading_rule debe contener pares de clave y valor")
        else:
            for rule in REQUIRED_GRADING_RULES:
                if not isinstance(grading_rule.get(rule), list) or not grading_rule.get(rule):
                    errors.append(f"{assessment_id}: grading_rule.{rule} debe tener contenido")

        if isinstance(assessment_version, int) and assessment_version >= 4:
            if not item.get("target_node_id"):
                errors.append(f"{assessment_id}: falta target_node_id")
            preflight = item.get("preflight")
            if not isinstance(preflight, dict):
                errors.append(f"{assessment_id}: falta preflight")
            else:
                for field in REQUIRED_PREFLIGHT:
                    if preflight.get(field) is not True:
                        errors.append(f"{assessment_id}: preflight.{field} debe ser true")
            if item.get("question_type") in {"multiple_choice", "single_choice"}:
                options = item.get("options")
                if not isinstance(options, list) or len(options) < 2:
                    errors.append(f"{assessment_id}: una pregunta cerrada requiere dos opciones como mínimo")
            invalidation = item.get("invalidation")
            if not isinstance(invalidation, dict):
                errors.append(f"{assessment_id}: falta el registro de invalidación")
            elif invalidation.get("invalidated"):
                if not invalidation.get("reason_type") or not invalidation.get("reason"):
                    errors.append(f"{assessment_id}: la evaluación invalidada requiere un motivo")
                if not invalidation.get("prior_grading_withdrawn"):
                    errors.append(f"{assessment_id}: la invalidación debe retirar la calificación")
                if not invalidation.get("mastery_evidence_removed"):
                    errors.append(f"{assessment_id}: la invalidación debe retirar la evidencia de dominio")

        if assessment_id in delivered_ids:
            if not item.get("frozen_before_delivery") or not item.get("frozen_at"):
                errors.append(f"{assessment_id}: la evaluación se presentó antes de fijar sus criterios")
            status = str(item.get("status", ""))
            if not status.startswith("delivered"):
                errors.append(
                    f"{assessment_id}: la evaluación presentada tiene un estado incompatible {status!r}"
                )


def validate_course(course_dir: Path, strict: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_FILES:
        if not (course_dir / relative).is_file():
            errors.append(f"Falta un archivo obligatorio: {relative}")

    if errors:
        return errors, warnings

    outline = load_yaml(course_dir / "00-course-outline.yaml", errors) or {}
    learner_state = load_yaml(course_dir / "learner-state.yaml", errors) or {}
    source_manifest = load_yaml(course_dir / "00-source-manifest.yaml", errors) or {}
    review_queue = load_yaml(course_dir / "review-queue.yaml", errors) or {}

    source_version = source_manifest.get("version", 1)
    if isinstance(source_version, int) and source_version >= 3:
        research = source_manifest.get("research")
        if not isinstance(research, dict):
            errors.append("Falta la política de investigación en el registro de fuentes v3")
        elif research.get("source_mode") not in SOURCE_MODES:
            errors.append(
                f"El registro de fuentes v3 tiene un source_mode no válido {research.get('source_mode')!r}"
            )
        if not isinstance(source_manifest.get("claim_source_matrix"), list):
            errors.append("Falta claim_source_matrix en el registro de fuentes v3")
        if not isinstance(source_manifest.get("review_log"), list):
            errors.append("Falta review_log en el registro de fuentes v3")

    lessons = outline.get("lessons") or []
    if not lessons:
        errors.append("El plan general carece de lecciones")
        return errors, warnings

    lesson_ids = [lesson.get("lesson_id") for lesson in lessons]
    if len(lesson_ids) != len(set(lesson_ids)):
        errors.append("Hay valores lesson_id duplicados")

    active_lessons = [lesson for lesson in lessons if lesson.get("route_status") == "active"]
    if len(active_lessons) != 1:
        errors.append(f"Se esperaba una única lección activa. Se encontraron {len(active_lessons)}")

    for lesson in lessons:
        lesson_id = lesson.get("lesson_id", "<missing>")
        route_status = lesson.get("route_status")
        material_status = lesson.get("material_status")
        delivery_status = lesson.get("delivery_status")
        mastery_status = lesson.get("mastery_status")

        if route_status not in ROUTE_STATUSES:
            errors.append(f"{lesson_id}: route_status no válido {route_status!r}")
        if material_status not in MATERIAL_STATUSES:
            errors.append(f"{lesson_id}: material_status no válido {material_status!r}")
        if delivery_status not in DELIVERY_STATUSES:
            errors.append(f"{lesson_id}: delivery_status no válido {delivery_status!r}")
        if mastery_status not in MASTERY_STATUSES:
            errors.append(f"{lesson_id}: mastery_status no válido {mastery_status!r}")

        if route_status == "provisional" and material_status not in {
            "not_generated",
            "legacy_prebuilt",
        }:
            errors.append(
                f"{lesson_id}: la lección futura provisional ya tiene material ({material_status})"
            )
        if (
            route_status == "provisional"
            and lesson.get("assessment_ids")
            and material_status != "legacy_prebuilt"
        ):
            errors.append(
                f"{lesson_id}: la lección futura provisional ya tiene evaluaciones"
            )

        for prerequisite in lesson.get("prerequisites") or []:
            if prerequisite not in lesson_ids:
                errors.append(f"{lesson_id}: requisito previo desconocido {prerequisite}")

    if active_lessons:
        active = active_lessons[0]
        plan_path = resolve(course_dir, active.get("lesson_plan_path"))
        if not plan_path or not plan_path.is_file():
            errors.append("Falta el plan de la lección activa")
        else:
            plan = load_yaml(plan_path, errors) or {}
            plan_version = plan.get("version", 1)
            if isinstance(plan_version, int) and plan_version >= 3:
                source_policy = plan.get("source_policy")
                if not isinstance(source_policy, dict):
                    errors.append("Falta source_policy en el plan de lección v3")
                elif source_policy.get("mode") not in SOURCE_MODES:
                    errors.append(
                        f"El plan de lección v3 tiene un modo de fuentes no válido {source_policy.get('mode')!r}"
                    )
                cost_policy = plan.get("cost_policy")
                if not isinstance(cost_policy, dict):
                    errors.append("Falta cost_policy en el plan de lección v3")
                else:
                    if cost_policy.get("max_research_workers", 1) > 1:
                        warnings.append(
                            "La política de costos utiliza más de un agente de investigación. Comprueba que repartir el trabajo reduzca el costo total."
                        )
                    if cost_policy.get("parallel_research"):
                        warnings.append(
                            "La investigación en paralelo está activada. Registra por qué se pueden consultar las fuentes por separado."
                        )
                validate_assessments(plan, plan_path, plan_version, errors)
                if isinstance(plan_version, int) and plan_version >= 4:
                    teaching_layers = plan.get("teaching_layers")
                    if not isinstance(teaching_layers, dict):
                        errors.append("Falta teaching_layers en el plan de lección v4")
                    else:
                        for layer in REQUIRED_TEACHING_LAYERS:
                            if not isinstance(teaching_layers.get(layer), dict):
                                errors.append(f"Falta teaching_layers en el plan de lección v4.{layer}")
                    completion_gate = plan.get("lesson_completion_gate")
                    if not isinstance(completion_gate, dict):
                        errors.append("Falta lesson_completion_gate en el plan de lección v4")
                    elif completion_gate.get("next_lesson_generation_allowed"):
                        for field in (
                            "immediate_review_completed",
                            "retrieval_before_summary",
                            "transfer_task_completed",
                            "core_nodes_ready",
                        ):
                            if completion_gate.get(field) is not True:
                                errors.append(
                                    "El plan v4 permite la siguiente lección sin cumplir " + field
                                )
            parts = plan.get("parts") or []
            # Completed parts are historical evidence, not simultaneously active output.
            # Keep validating their material below, but exclude them from the
            # current-part-only concurrency check so a course can advance normally.
            current_ready_parts = [
                part
                for part in parts
                if part.get("status") in READY_PART_STATUSES
                and part.get("status") != "completed"
            ]
            if not parts:
                errors.append("El plan de la lección activa carece de segmentos")
            if len(current_ready_parts) > 1:
                errors.append(
                    "Se esperaba un único segmento generado o listo que aún no estuviera completado. "
                    f"Se encontraron {len(current_ready_parts)}."
                )
            for part in parts:
                material_path = part.get("material_path")
                if part.get("status") in READY_PART_STATUSES:
                    if isinstance(plan_version, int) and plan_version >= 3:
                        status = part.get("status")
                        review = part.get("review") or {}
                        required_checks: list[str] = []
                        if status in {
                            "source_checked",
                            "fact_checked",
                            "pedagogy_checked",
                            "frozen",
                        }:
                            required_checks.append("source_check")
                        if status in {"fact_checked", "pedagogy_checked", "frozen"}:
                            required_checks.append("fact_check")
                        if status in {"pedagogy_checked", "frozen"}:
                            required_checks.append("pedagogy_check")
                        if status == "verified":
                            errors.append(
                                f"{part.get('part_id')}: el plan v3 requiere estados de revisión detallados en vez de verified"
                            )
                        for check in required_checks:
                            if review.get(check) not in PASSED_REVIEW:
                                errors.append(
                                    f"{part.get('part_id')}: {status} requiere {check}=passed"
                                )
                    if isinstance(plan_version, int) and plan_version >= 4:
                        navigation = part.get("navigation")
                        if not isinstance(navigation, dict):
                            errors.append(f"{part.get('part_id')}: falta navigation")
                        else:
                            for field in (
                                "position",
                                "lesson_question",
                                "previous_part_resolved",
                                "why_this_part_now",
                                "source_focus",
                                "success_criterion",
                            ):
                                if not navigation.get(field):
                                    errors.append(
                                        f"{part.get('part_id')}: navigation.{field} está vacío"
                                    )
                        for layer in REQUIRED_TEACHING_LAYERS:
                            if not isinstance(part.get(layer), dict):
                                errors.append(f"{part.get('part_id')}: falta {layer}")
                    resolved = resolve(plan_path.parent, material_path)
                    if not resolved or not resolved.is_file():
                        errors.append(f"Falta el material del segmento marcado como listo: {part.get('part_id')}")
                    else:
                        validate_longform(
                            resolved,
                            errors,
                            warnings,
                            require_v4_protocol=isinstance(plan_version, int)
                            and plan_version >= 4,
                        )
                elif material_path:
                    warnings.append(
                        f"Un segmento aún sin generar ya tiene material_path: {part.get('part_id')}"
                    )

            user_notes = plan_path.parent / "02-user-notes.md"
            tutor_summary = plan_path.parent / "03-tutor-summary.md"
            if not user_notes.is_file():
                errors.append("Falta 02-user-notes.md en la lección activa")
            if not tutor_summary.is_file():
                errors.append("Falta 03-tutor-summary.md en la lección activa")
            if user_notes.resolve() == tutor_summary.resolve():
                errors.append("Las notas del estudiante y el resumen del tutor requieren archivos separados")

    if isinstance(source_version, int) and source_version >= 3:
        if not any((course_dir / name).is_file() for name in COURSE_HOME_NAMES):
            errors.append(f"Al curso v3 le falta {COURSE_HOME_NAMES[0]}")

    content_progress = learner_state.get("content_progress")
    if not isinstance(content_progress, dict):
        errors.append("Falta el campo independiente content_progress en learner-state.yaml")
    if not learner_state.get("nodes"):
        errors.append("Faltan los nodos de dominio en learner-state.yaml")

    learner_version = learner_state.get("version", 1)
    if isinstance(learner_version, int) and learner_version >= 3:
        for node in learner_state.get("nodes") or []:
            node_id = node.get("id", "<missing>")
            for field in (
                "historical_highest_status",
                "current_status",
                "current_evidence",
                "active_misconceptions",
                "promotion_blockers",
                "advance_allowed",
            ):
                if field not in node:
                    errors.append(f"{node_id}: falta {field}")
            historical = node.get("historical_highest_status")
            current = node.get("current_status")
            if historical not in MASTERY_STATUSES:
                errors.append(f"{node_id}: historical_highest_status no válido {historical!r}")
            if current not in MASTERY_STATUSES:
                errors.append(f"{node_id}: current_status no válido {current!r}")
            if historical in MASTERY_RANK and current in MASTERY_RANK:
                if MASTERY_RANK[historical] < MASTERY_RANK[current]:
                    errors.append(f"{node_id}: el máximo histórico está por debajo del nivel actual")
            if node.get("advance_allowed") and current in {"unknown", "exposed", "guided"}:
                errors.append(f"{node_id}: se permitió avanzar antes de demostrar dominio independiente")

        evidence_log = learner_state.get("evidence_log")
        if not isinstance(evidence_log, list):
            errors.append("Falta evidence_log en el estado del estudiante v3")
        else:
            for entry in evidence_log:
                promotion = entry.get("promotion_evidence")
                if not isinstance(promotion, dict):
                    errors.append("Falta promotion_evidence en una entrada del registro de evidencia")
                    continue
                required = (
                    "grading_result",
                    "criteria_met",
                    "criteria_unmet",
                    "active_misconceptions",
                    "historical_highest_status",
                    "current_status",
                    "advance_allowed",
                    "promotion_blockers",
                )
                for field in required:
                    if field not in promotion:
                        errors.append(f"Falta {field} en promotion_evidence")
                hint_level = entry.get("hint_level")
                promoted_to = (entry.get("mastery_change") or {}).get("to")
                if hint_level in {1, 2, 3, 4, "L1", "L2", "L3", "L4"} and promoted_to in {
                    "independent",
                    "transferable",
                    "durable",
                }:
                    errors.append("Una respuesta con pistas solo permite alcanzar el nivel guided")
                if hint_level in {5, "L5"} and promoted_to in {
                    "guided",
                    "independent",
                    "transferable",
                    "durable",
                }:
                    errors.append("Una tarea con demostración L5 solo permite alcanzar el nivel exposed")

        if review_queue.get("version", 1) >= 2:
            immediate_reviews = review_queue.get("immediate_reviews")
            if not isinstance(immediate_reviews, list) or not immediate_reviews:
                errors.append("Falta immediate_reviews en la lista de repasos v2")
            else:
                for review in immediate_reviews:
                    if review.get("review_type") != "immediate":
                        errors.append("El repaso inmediato tiene un review_type incorrecto")
                    if review.get("retrieval_before_summary") is not True:
                        errors.append("El repaso inmediato debe empezar con un intento de recuerdo")
                    if review.get("next_action") not in {"reinforce", "continue", "pause"}:
                        errors.append("El repaso inmediato tiene un next_action no válido")

        active_plan_gate = None
        if active_lessons:
            active_plan_path = resolve(course_dir, active_lessons[0].get("lesson_plan_path"))
            if active_plan_path and active_plan_path.is_file():
                active_plan = load_yaml(active_plan_path, errors) or {}
                active_plan_gate = active_plan.get("lesson_completion_gate")
        if isinstance(active_plan_gate, dict) and active_plan_gate.get(
            "next_lesson_generation_allowed"
        ):
            core_nodes = [
                node
                for node in learner_state.get("nodes") or []
                if node.get("importance", "core") == "core"
            ]
            if any(node.get("advance_allowed") is not True for node in core_nodes):
                errors.append("Se autorizó la siguiente lección con un nodo fundamental bloqueado")
            completed_immediate = [
                review
                for review in review_queue.get("immediate_reviews") or []
                if review.get("review_type") == "immediate"
                and review.get("result") not in {None, "", "not_attempted"}
                and review.get("next_action") == "continue"
                and review.get("completed_at")
            ]
            if not completed_immediate:
                errors.append("Se autorizó la siguiente lección sin evidencia de repaso inmediato completo")

    if strict and warnings:
        errors.extend(f"Modo estricto: {warning}" for warning in warnings)

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course_dir", type=Path, metavar="DIRECTORIO", help="Carpeta del curso guardado")
    parser.add_argument("--strict", action="store_true", help="Trata los avisos como errores")
    args = parser.parse_args()

    course_dir = args.course_dir.expanduser().resolve()
    errors, warnings = validate_course(course_dir, args.strict)

    for warning in warnings:
        print(f"AVISO: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"Validación fallida. Errores: {len(errors)}. Avisos: {len(warnings)}.")
        return 1

    print(f"Curso válido. Avisos: {len(warnings)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
