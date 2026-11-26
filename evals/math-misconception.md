# Evaluación 02 · Errores conceptuales en matemáticas y pistas graduales

## Objetivo de la evaluación

Verifica si Skill puede establecer de antemano estándares de respuesta correctos, identificar con precisión los malentendidos matemáticos y pedir a los alumnos que los corrijan por sí mismos en lugar de revelar las respuestas directamente.

## Escenario

Los alumnos conocen la probabilidad de cara para un lanzamiento de moneda, pero añaden erróneamente dos eventos no mutuamente excluyentes directamente.

## Solicitud inicial

> Estoy aprendiendo probabilidad. La pregunta es: Cuando lanzas una moneda justa dos veces seguidas, ¿cuál es la probabilidad de sacar al menos una cara? Calculé 1/2 + 1/2 = 1. Por favor, ayúdame a encontrar el error, no me des una respuesta directa todavía.

## Respuesta estándar

```yaml
correct_answer: 3/4
valid_methods:
  - Enumera HH, HT, TH, TT, y hay 3 condiciones que satisfacen la condición
  - Complemento de uso: 1 - P (ambas colas) = 1 - 1/4
core_misconception: Suma directamente los dos eventos superpuestos del "primer frente" y el "segundo cabeza" para calcular repetidamente HH
acceptable_variants:
  - 0.75
  - 75%
```

## Espera retroalimentación en la primera ronda

Debe:

1. En concreto, la probabilidad de que los usuarios conozcan cada positivo es 1/2.
2. Señala que el punto clave de interrupción es que dos eventos ocurrirán simultáneamente y no pueden sumarse.
3. No dando inmediatamente 3/4.
4. Utiliza los indicativos L1-L2, como pedir a los usuarios que enumeren cuatro posibles resultados o preguntar "¿Cuántas veces se ha calculado HH?"
5. Exigir a los usuarios que recalculen.
6. La situación actual sigue siendo `guided`.

No se permite:

- Decir "el razonamiento es completamente correcto, solo un error de cálculo".
- Presenta directamente la solución completa cuando el usuario solicita por primera vez encontrar un error.
- Simplemente di: «No, piénsalo otra vez».
- Juzga las respuestas que son correctas en la respuesta final pero que siguen siendo incorrectas basándose en la respuesta.

## Segunda ronda de aportaciones

> Los cuatro resultados son HH, HT, TH, TT. Al menos una cara tiene HH, HT, TH, así que es 3/4.

## Retroalimentación esperada

Debe:

1. Los resultados del juicio y la base son todos correctos.
2. Aclarar que anteriormente `1/2 + 1/2` calculado repetidamente HH.
3. Esto indica que esta vez el proceso se completó bajo indicación, con un estado máximo de `guided`.
4. Da una variante que no dependa de la memoria del enum original, por ejemplo, "Tirar el dado dos veces, al menos un 6".
5. Permitir que los usuarios elijan enumeración o complemento, pero no escribas primero la fórmula.

## Normas sobre cuestiones migratorias

```yaml
question: Tirar dos dados justos de seis caras con al menos una posibilidad de sacar un 6
correct_answer: 11/36
preferred_method: 1 - (5/6)^2
common_error: 1/6 + 1/6 = 1/3, repetición doble 6s
```

## Si la transferencia de usuarios falla

Debe:

- No actualice a `independent` o `transferable`.
- Volver a la estructura central de "solapamiento de eventos" o complemento.
- Sustituir por una tarea de identificación más pequeña en lugar de continuar con un nuevo capítulo.
- El registro del malentendido sigue activo.

## Puntos clave de la clasificación

- Exactitud de las respuestas estándar.
- La primera desubicación crítica.
- Escaleras rápidas.
- El estado y la intensidad de la indicación son consistentes.
- transferencia de variantes.

## Fallos graves

- Juez 1 como correcto.
- La respuesta estándar no es 3/4.
- Da respuestas completas sin intentarlo.
- Tras el indicador, la finalización se marca como `independent`.
- El fallo de transferencia sigue reclamando el control.

## Criterio de aprobación

Puntuación ≥ 80 según las dimensiones aplicables de `tutor-quality-rubric.md`, sin Fallo Crítico.
