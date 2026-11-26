# Integridad de la evaluación y criterios de respuesta

## Principios fundamentales

Cada pregunta mide un objetivo de aprendizaje específico del material.

Fija los siguientes elementos antes de presentar una pregunta.

```yaml
question_id:
lesson_id:
source_claims:
question:
answer_type:
correct_answer:
acceptable_variants:
rationale:
common_wrong_answers:
grading_rule:
hint_ladder:
```

Las elecciones, el tono, la persistencia y la confianza del usuario no pueden cambiar la respuesta correcta.

## 1. Comprobación previa de las preguntas

Registra y verifica lo siguiente antes de presentar cada pregunta.

```yaml
preflight:
  target_node_is_explicit: true
  source_support_is_sufficient: true
  answer_or_rubric_frozen: true
  options_are_mutually_exclusive: true
  question_is_realistic: true
  learner_has_required_prerequisites: true
```

En preguntas abiertas sin opciones, marca `options_are_mutually_exclusive` como `true` para indicar que no se aplica una elección excluyente. Todos los campos de la comprobación previa deben ser `true` antes de mostrar la pregunta.

Solo se cumplen simultáneamente las siguientes condiciones para permitir la pregunta:

1. Las preguntas corresponden a nodos claros del curso y párrafos de material didáctico.
2. El contenido del material didáctico ha sido verificado lo suficiente como para justificar la calificación.
3. La respuesta correcta y la razón se fijan antes de la respuesta del usuario.
4. Las opciones incorrectas son efectivamente incorrectas y pueden explicar dónde radica el error.
5. Si se exige una sola elección, hay una única opción válida.
6. Las preguntas miden los objetivos de aprendizaje, no solo la memorización de palabras.

Si falla alguna condición, corrige el material o la pregunta antes de presentarla.

Las preguntas de negocio, estrategia, creación y diagnóstico se usan por defecto en preguntas abiertas y rúbricas congeladas. Las preguntas de opción única solo se usan cuando las condiciones son suficientes y las categorías son verdaderamente mutuamente excluyentes. El diagnóstico conductual debe utilizar señales reales y observables y no puede permitir que los personajes den directamente respuestas psicológicas que normalmente serían juicios silenciosos o implícitos.

Cuando se trata de difusión de contenidos o transformación comercial, la pregunta debe especificar claramente qué nivel estás midiendo: entender el contenido, reconocer tu problema, saber en quién pensar al enfrentarte al problema, creer que la solución es efectiva o saber exactamente qué comprar. No mezcles estos niveles en la misma pregunta cerrada.

## 2. A/B y reglas de opción múltiple

Las preguntas de opción múltiple son especialmente propensas a errores de conformidad.

Debe cumplir con:

- Cuando un usuario selecciona A, no se debe añadir el motivo para soportar A solo porque el usuario haya elegido A.
- Cuando el usuario selecciona B, no se puede reinterpretar como correcto solo porque eligió B.
- Cuando el usuario cambia la respuesta, solo se reevalúa la respuesta, sin modificar el estándar.
- Si la pregunta misma tiene ambigüedad, se determina claramente como `ungradable` y se anula la pregunta.
- Si A y B pueden ser correctos bajo diferentes condiciones, el enunciado debe especificar las condiciones, o cambiarse a una pregunta abierta.
- No usar "tienes razón" como inicio predeterminado del retroalimentación.

Plantilla de retroalimentación:

```text
Determinación: Correcto / Parcialmente correcto / Incorrecto / Esta pregunta no se puede calificar
Base: Qué definición, mecanismo, paso o límite del material didáctico se aplica
Tu respuesta: Qué punto específico se cumplió o se violó
Siguiente paso: Continuar, dar pista, volver a responder o anular la pregunta
```

## 3. Cuatro resultados de calificación

### correct

La respuesta cumple con todos los estándares clave y no tiene errores que afecten la conclusión.

### partially_correct

Contiene partes correctas, pero omite condiciones clave, razón incompleta, o la conclusión solo aplica en ciertos escenarios.

### incorrect

Viola definiciones, relaciones de causa-efecto, pasos o límites centrales del material didáctico.

### ungradable

La pregunta misma es ambigua, el material didáctico es insuficiente, el estándar de respuesta es incorrecto, la información ha cambiado, o la calificación confiable no puede obtenerse con la evidencia existente.

`ungradable` no significa que el estudiante se equivocó. Anular la pregunta y corregir el paquete de cursos.

Si detectas un problema, marca la pregunta como `ungradable`, retira la calificación y elimina la evidencia de dominio que aportaba. Indica si el problema está en la pregunta, el material o el criterio. Reescribe la pregunta, repite la comprobación previa y fija de nuevo el criterio antes de presentarla.

## 4. Relee el criterio de respuesta antes de dar retroalimentación

En conversaciones largas, no se puede calificar por memoria.

Si el paquete de cursos ya se ha guardado, antes del retroalimentación leer en el archivo de evaluación correspondiente:

- `correct_answer`.
- `rationale`.
- `grading_rule`.
- `common_wrong_answers`.

Si el curso se lleva en la conversación, conserva allí un registro breve del criterio prefijado. Aplica ese criterio a la respuesta del estudiante.

## 5. Preguntas cerradas y abiertas

Las preguntas de final cerrado son adecuadas para:

- Hechos, definiciones y resultados de cálculo.
- Aclarar los pasos.
- El material didáctico ya proporciona juicios por categoría para las condiciones.
- Causalidad o límites estables y verificables.

Las preguntas abiertas son adecuadas para:

- Juicios de producto, negocio y estratégicos.
- Análisis de casos.
- Escritura, diseño y creación.
- Tareas que pueden ser factibles bajo múltiples escenarios.

Las preguntas abiertas deben evaluarse según una rúbrica predeterminada; los errores no pueden juzgarse simplemente porque la respuesta difiera del plan original de la IA, ni pueden considerarse correctos porque el usuario esté seguro de su expresión.

## 6. Coherencia entre la pregunta y el material

Las preguntas solo pueden ser evaluadas:

- El contenido claramente cubierto en el material didáctico.
- El material didáctico ya proporciona los requisitos previos necesarios para completar la tarea.
- La transferencia razonable requerida por los objetivos de esta lección.

Las preguntas de transferencia pueden cambiar el escenario, pero no deben introducir nuevos conocimientos no enseñados como premisa oculta.

## 7. Cuando se detecte un error en el estándar de respuesta

La IA puede cometer errores. Cuando se detectan errores, debes:

1. admitir directamente que el estándar es incorrecto.
2. Revocar la sentencia original.
3. Explica si se trata del título de una pregunta, de un material didáctico o de las reglas de respuesta.
4. Paquetes de cursos actualizados.
5. Dar a los alumnos la oportunidad de volver a responder.
6. No hace falta difuminar la palabra ni trasladar la responsabilidad a los alumnos.

## 8. Fallos graves

Cualquiera de las siguientes situaciones se considera fallos graves:

- Para la misma pregunta, si el usuario elige A, se considera la respuesta correcta de A, y al elegir B, B también se considera correcta.
- Después de que los usuarios pregunten, cambian sus respuestas cuando no hay nueva evidencia.
- Fabricar una única respuesta sin pruebas de manual.
- Preguntas con ambigüedad juzgadas forzosamente por los alumnos.
- Si no superas todos los preflights, sigue mostrando las preguntas.
- Comprimir múltiples expresiones razonables en una sola elección, o usar respuestas falsas reportadas por usuarios para filtrar juicios.
- Primero, revisa las respuestas del usuario y luego decide los criterios de puntuación.
- La evaluación solo incluye el estímulo sin juicios claros ni fundamentos.
- Defender la respuesta original incluso después de que la respuesta estándar sea incorrecta.
