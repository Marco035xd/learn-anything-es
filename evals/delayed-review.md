# Evaluación 05 · Repaso diferido entre sesiones

## Objetivo de la evaluación

Verifica si la habilidad puede leer los estados de aprendizaje existentes para recuperar y comenzar a revisar proactivamente, actualizando el estado en función de la latencia en lugar de reenseñar o fingir recordar progresos inexistentes.

## Estado actual

```yaml
mastery_contract:
  learning_goal: Distinguir entre relevancia y causalidad, y ser capaz de examinar las afirmaciones causales cotidianas
  target_mastery_level: durable
nodes:
  - id: correlation-causation
    name: Correlación y causalidad
    knowledge_type: concept
    status: independent
    evidence:
      - Hace tres días, una explicación independiente de las causas comunes podía generar correlación
    misconceptions:
      - description: Siempre que A preceda a B y esté relacionado, se puede demostrar que A causa B
        status: corrected_but_fragile
    last_practiced: 2026-07-09
    next_review: 2026-07-12
review:
  due_now:
    - correlation-causation
```

## Solicitud inicial

> Continuando con el estudio previo sobre relevancia y causalidad.

## Espera comportamiento en la primera ronda

Debe:

1. Reutiliza objetivos y hitos existentes, sin preguntarte "¿Qué quieres aprender?"
2. No muestres primero el resumen o definición anterior.
3. Da directamente un breve recuerdo o un caso nuevo, como "Las ventas de helados y los números de ahogamiento aumentan simultáneamente—¿puede lo primero causar lo segundo, y por qué?"
4. Primero, dejar que los usuarios den una calificación de confianza.
5. Aclara que esta es una fecha límite para la revisión, no un nuevo capítulo.

## Respuestas de usuarios

> Ambos están relacionados, y dado que las ventas de helados subieron primero, debería indicar que el helado está causando más ahogamientos. Estoy 80% seguro.

## Retroalimentación esperada y actualizaciones de estado

Debe:

1. Identificar los conceptos erróneos fundamentales como recurrentes no debe considerarse correcto solo porque la expresión sea completa.
2. Señalando que el orden cronológico y la correlación siguen siendo insuficientes para descartar causas comunes.
3. Usar "altas temperaturas que afectan simultáneamente a las ventas de helados y a los nadadores" como contraejemplo o pista mínima.
4. Exigir a los usuarios que reinterpreten en lugar de recontar inmediatamente todo el capítulo.
5. Degradar el estatus de `independent` a `guided` o marcarlo como para consolidación.
6. Preservar la evidencia histórica más elevada y registrar el fracaso de este retraso.
7. Señala que la idea errónea es activa.
8. Programa una revisión más detallada, por ejemplo, un día después.
9. No se concede `durable`.

## Si el usuario corrige correctamente

Expectativas:

- Esto indica que esta actualización se corrigió tras un aviso, por lo que aún no puede revertirse a `independent`.
- Aquí hay una pequeña caja con una forma de superficie diferente.
- Después de que un nuevo caso se mantenga independiente con éxito, `independent` puede restablecerse, pero la retención a largo plazo sigue requiriendo la siguiente confirmación retrasada.

## Ejemplo de actualizaciones de estado

```yaml
status: guided
previous_highest_status: independent
downgrade_reason: delayed_retrieval_failure
misconception:
  description: El momento y la correlación son suficientes para demostrar la causalidad
  status: active
next_review: 1_day_later
durable_mastery_verified: false
```

## Cuando no hay ningún archivo de estado

Skill debe especificar que la recuperación solo es posible actualmente basándose en conversaciones visibles y no puede fingir que se ha leído el estado del historial. La reubicación puede realizarse con una tarea de retirada.

## Puntos clave de la clasificación

- Multiplexación entre estados de sesión.
- La revisión comienza con la extracción.
- Manejo de errores con alta confianza.
- Ajuste de estado.
- Revisar la programación.
- Disciplina duradera en la evidencia.

## Fallos graves

- Al inicio de la revisión, se muestran primero las respuestas antiguas.
- Volver a preguntar sobre los objetivos de aprendizaje existentes.
- Juzgar las respuestas incorrectas como correctas.
- Corrige inmediatamente la marca `durable` después de la indicación.
- Eliminar evidencias antiguas sin conservar historial.
- Fingir leer un estado inexistente.

## Criterio de aprobación

Puntuación ≥ 80 según las dimensiones aplicables de `tutor-quality-rubric.md`, sin Fallo Crítico.
