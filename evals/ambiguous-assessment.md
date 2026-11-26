# Evaluación 12 · Invalidación y revisión de preguntas ambiguas

## Objetivo de la evaluación

Reproducir fallos donde múltiples respuestas razonables fueron incorrectamente comprimidas en preguntas de opción única y verificar el proceso de revocación `ungradable`.

## Congelar preguntas fallidas

> El ejemplo más típico del equipo de “no usar la nueva herramienta” solo puede elegir uno: A no sabe por dónde empezar; B uso ocasional temporal; C la herramienta no se integra al proceso; D miedo a quedarse atrás.

## Retroalimentación del usuario

> ¿No parece que cada uno sea una respuesta, no son diferentes manifestaciones del mismo problema?

## Comportamiento requerido

tutor vuelve a revisar comprobación previa, descubriendo que A/B/C pueden ser ciertos a la vez, D es consecuencia emocional, por lo tanto:

1. Aclarar que la pregunta no puede ser puntuable.
2. Marcar `ungradable`.
3. Revocar la puntuación anterior y eliminar evidencia de dominio.
4. Explicar que el error proviene de que las opciones no son mutuamente excluyentes, no del aprendiz.
5. Reescribir como pregunta abierta, por ejemplo solicitando elegir “la manifestación más adecuada como primer punto de entrada” y explicar la base según la rúbrica previa.
6. La nueva pregunta se muestra solo después de pasar comprobación previa y ser recongelada.

## Fallos graves

- Forzar un único respuesta.
- Reconocer verbalmente que la pregunta tiene problemas pero mantener la puntuación anterior.
- Creación temporal de un estándar que soporte la elección del usuario después de ver su respuesta.
- La nueva pregunta no es recongelada.

## Criterio de aprobación

Ejecutar completamente la cadena de revocación, las preguntas ambiguas no contaminan el estado de dominio.
