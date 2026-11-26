# Selección de modelos y control de costos sin perder calidad

## Juicio fundamental

El objetivo de optimización no es "usar modelos baratos para cada paso", sino reducir el coste total necesario para completar una sesión de aprendizaje eficaz sin rebajar la calificación de materiales didácticos, respuestas o juicios docentes.

Anota tres cosas por separado:

- Token total: La suma del tutor principal, los agentes hijos, los reintentos y las lecturas repetidas.
- Coste: costes reales incurridos por diferentes modelos, niveles de inferencia y llamadas a herramientas.
- Coste de calidad: consumo adicional causado por errores en los materiales didácticos, retrabajo, investigaciones duplicadas y correcciones de usuarios.

Los modelos más baratos pueden reducir los costes por sesión, pero los subagentes añaden contexto y llamadas independientes. Solo cuando se reduce el coste total tras la revisión y el reintento se ahorra realmente.

## 1. Orden de ejecución predeterminado

```text
Scripts o herramientas deterministas
→ Tareas cortas para el tutor principal actual
→ Agente de datos único de bajo coste
→ Revisión del tutor jefe y decisión final
→ Aumentar los umbrales de inferencia solo durante conflictos, alto riesgo o fracaso
```

No dividas tareas solo porque "se usan demasiados agentes". Delega solo si se cumplen todas las siguientes condiciones:

1. Los límites de las subtareas son claros, así que no necesitas entender la relación de aprendizaje completa.
2. La salida puede comprimirse en intermedios cortos y estructurados.
3. El tutor principal puede aceptar rápidamente usando fuentes o reglas.
4. El fracaso no enseña directamente al usuario equivocado.
5. Los ahorros esperados superan los costes de añadir nuevo contexto, agregación y repetir.

Por defecto, se utiliza como máximo un Agente de información, ejecutándose en orden, sin buscar en paralelo el mismo problema. Solo se considera la paralelización si la fuente puede particionarse de manera independiente y el curso actual realmente lo requiere.

## 2. Enrutamiento de nivel cuatro

### L0: No usar modelo

Usar scripts, parser o herramientas existentes para completar:

- Análisis de formatos de archivo, hashes, eliminación de duplicados y fragmentación.
- Validación de sintaxis y esquema YAML/JSON.
- Formateo de referencias, verificación de rutas y revisión de enumeración de estados.
- Cálculo de fechas de repaso, creación de archivos y actualización determinista de estados.

No hacer que el modelo repita trabajos que pueden codificarse de manera estable.

### L1: Agente de información de bajo costo

Puede usarse para:

- Recolectar fuentes candidatas según el problema de aprendizaje actual.
- Extraer títulos, autores, instituciones, fechas, versiones y capítulos relacionados.
- Extraer afirmaciones claras y evidencia breve de los rangos especificados.
- Eliminar fuentes duplicadas y generar una lista de fuentes candidatas.
- Marcar fuentes de baja calidad que claramente carecen de autor, fecha o fuente original.

Prohibido:

- Afirmar que las fuentes candidatas son lo suficientemente autorizadas.
- Resolver conflictos entre fuentes confiables.
- Sintetizar de manera independiente para formar el material final.
- Congelar la respuesta estándar, rubrica de evaluación o conclusión de dominio.
- Emitir juicios finales sobre contenido de alto riesgo como médico, legal o financiero.

En el entorno Codex se da prioridad al rol de proyecto `learning_researcher`. Si este rol no está disponible, el modelo no está disponible o la delegación falla, el tutor principal realiza una búsqueda de alcance limitado en el hilo actual; no se debe interrumpir el curso ni requerir que el usuario busque información en lugar del Agente.

### L2: Archivo habitual del tutor principal

Responsable de:

- Confirmar los objetivos de dominio y la ruta del curso.
- Seleccionar las fuentes y conclusiones que ingresarán al material didáctico.
- Redactar segmentos de aprendizaje extensos al estilo del profesor actual.
- Diseñar casos, ejercicios, retroalimentación y ajustes de curso.
- Completa el ámbito general de fuentes, datos y puertas de calidad docente.

Normalmente se usan modelos equilibrados y razonamiento `medium` o `high`. No dejes cada paso mecánico al tutor principal solo porque el hilo actual esté configurado al nivel más alto.

### L3: Revisión y corrección forzadas

Aumentar a `high / xhigh` o intensidad equivalente solo bajo las siguientes condiciones:

- Fuentes fiables con conflictos sustantivos.
- Las conclusiones clave se basan en una causalidad compleja, matemáticas, código o síntesis cruzada.
- El material didáctico se utiliza en campos profesionales de alto riesgo.
- Existe duda sobre si la respuesta es única.
- Los usuarios cuestionan materiales didácticos o califican juicios y aportan nuevas pruebas.
- Los materiales de candidato de bajo coste no superaron la prueba principal del tutor.

Elevar el nivel no puede sustituir la verificación. Cuando no hay pruebas, se deben contraer conclusiones, poner las etiquetas en incertidumbre o suspender el uso en lugar de añadir razonamientos y adivinar la respuesta.

## 3. Contrato de entrega de agentes de datos de bajo coste

Proporcione solo el contexto mínimo requerido para el segmento de aprendizaje actual al delegar:

```yaml
learning_question: Cuestiones que deben aclararse en el segmento actual de aprendizaje
learner_context: Conserva solo el contexto que afecta a la selección del material
claim_types: definition | mechanism | current_fact | dispute | example
preferred_sources: official_doc | standard | primary_research | textbook
date_or_version_scope: ""
exclusions: Ámbito de curso futuro que no requiere investigación
output_limit: Número máximo de fuentes candidatas y longitud resumida
```

Solicitud de devolución:

```yaml
candidates:
  - title:
    author_or_org:
    source_type:
    location:
    publication_or_version_date:
    relevant_scope:
    candidate_claims: []
    evidence_locator:
    limitations: []
unresolved_questions: []
```

Solo se devuelve la lista de candidatos, no el material didáctico completo. El tutor principal debe reabrir la fuente adoptada y confirmar las afirmaciones clave antes de escribir `00-source-manifest.yaml`.

## 4. Cuándo escalar o detenerse

En cualquier caso, detenga el camino de bajo coste y vuelva al tutor principal:

- Incapaz de encontrar fuentes primarias o suficientemente autorizadas.
- Fechas de fuente, versiones, temas de investigación o definiciones inconsistentes.
- Las conclusiones candidatas no pueden situarse dentro del ámbito del texto original.
- La causalidad debe derivarse de las relaciones relevantes.
- La conclusión se utilizará como única respuesta a la pregunta cerrada.
- Acciones que involucran a personas de alto riesgo.
- Sigue fallando la inspección de fuente tras una reestructuración consecutiva.

No pruebes repetidamente modelos baratos y ten suerte. Actualizar tras un fallo suele ser más rentable que varios intentos de baja calidad.

## 5. Estrategia de costes

Por defecto, se utiliza `balanced`, por lo que los usuarios no necesitan rellenar cuestionarios modales. La confirmación solo se realiza cuando el presupuesto cambia sustancialmente el alcance del curso.

```yaml
cost_policy:
  mode: budget | balanced | quality
  max_research_workers: 1
  parallel_research: false
  final_approval: main_tutor
  record_usage: true
```

- `budget`: Cursos más cortos y fuentes más limitadas, pero sin bajar los estándares de los hechos clave y las respuestas.
- `balanced`: Los materiales de bajo riesgo se organizan y se rebajan de categoría, siendo el tutor principal responsable de la enseñanza y la corrección de textos.
- `quality`: Los cursos controvertidos, de alto riesgo o de alto valor requieren verificación independiente y aceptan costes más altos.

Cuando el presupuesto sea insuficiente, priorice reducir el alcance de los cursos, reducir ampliaciones innecesarias y posponer futuras lecciones, y no entregue materiales didácticos baratos no verificados a los usuarios.

## 6. Si se utiliza enrutamiento jerárquico

Primero, compáralo con el mismo conjunto de tareas congeladas:

```text
R: El tutor principal completa todos los pasos
B: herramienta L0 + agente de perfil L1 único + adjudicación principal del tutor
```

Récord:

- Tokens de entrada, salida e inferencia.
- Llamadas de herramientas y retrasos.
- Ya sea que las comprobaciones de fuentes, verificaciones de hechos y comprobaciones de calidad docente se pasen de una sola vez.
- Número de retrabajos.
- Rúbrica del material didáctico, consistencia de las preguntas y volumen de revisiones por parte del usuario.

B solo se establece como predeterminado si mantiene la calidad entre casos de uso congelados y reservados, no presenta nuevos fallos críticos e incluye un coste total más bajo tras el retrabajo. De lo contrario, se conserva una única ruta del Agente.
