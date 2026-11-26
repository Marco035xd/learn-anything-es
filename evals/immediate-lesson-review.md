# Evaluación 14 · Recuerdo y transferencia al terminar la lección

## Objetivo de la evaluación

Verificar que al terminar una lección se complete primero la revisión inmediata, en lugar de usar el tutor para resumir y generar familiaridad o pasar directamente a la siguiente lección.

## Escenario

Todos los segmentos de aprendizaje de L01 ya han sido entregados. El aprendiz dice “continuar con la siguiente lección”. El nodo central actual tiene solo un desempeño correcto con indicación.

## Comportamiento requerido

1. No generar el material de L02.
2. Indicar con una frase que ahora se inicia la revisión inmediata de L01.
3. Cerrar el material y dejar que el aprendiz recuerde de forma activa las relaciones centrales de la lección.
4. Luego dar un nuevo escenario con cambios superficiales para completar la transferencia.
5. Registrar `review_type: immediate`, `retrieval_before_summary: true`, resultados, errores recurrentes y próximos pasos.
6. En caso de fracaso, volver al primer punto débil; solo permitir L02 después de tener éxito y que el nodo central alcance el criterio de avance.
7. No marcar un éxito inmediato como `durable`, programar aparte la revisión diferida.

## Fallos graves

- Primero mostrar el resumen del tutor, respuestas antiguas o expresiones correctas.
- Solo hacer un resumen, sin extracción activa ni transferencia.
- Si la revisión falla, aun así generar L02.
- Otorgar durable en el momento.

## Criterio de aprobación

Registro completo de la revisión inmediata, el derecho a generar la siguiente lección es consistente con el criterio de avance.
