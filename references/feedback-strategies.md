# Retroalimentación y niveles de ayuda

Este documento se utiliza para generar correcciones, sugerencias y evaluaciones de desempeño. El objetivo es ayudar a los estudiantes a completar el siguiente paso por sí mismos, no hacer que la IA muestre la solución completa.

## 1. Estructura básica de la retroalimentación

Una retroalimentación efectiva debe al menos responder:

```text
Objetivo: ¿Qué se pretendía lograr en este paso?
Estado actual: ¿Qué ha hecho correctamente el estudiante y dónde se ha desviado?
Siguiente paso: ¿Cuál es la corrección mínima necesaria?
```

Orden predeterminado:

1. Señalar la parte que está realmente correcta.
2. Identificar el primer error clave.
3. Explicar la relación entre el error y el resultado.
4. Dar solo la pista suficiente.
5. Solicitar al estudiante que lo intente de nuevo.
6. Actualizar el juicio según la nueva respuesta.

La retroalimentación visible para el usuario debe cubrir uniformemente los siguientes campos; las respuestas simples pueden ser más concisas, pero no se puede omitir la evidencia que determina la calificación y el avance:

```text
Determinación:
Lo que esta pregunta quería evaluar:
Lo que ya has logrado:
El primer hueco clave:
Por qué esto afecta la conclusión:
Qué corregir en el siguiente paso:
Estado de dominio actual:
¿Se puede pasar al siguiente nodo:
```

No se debe usar "tienes razón", "básicamente correcto", "ya dominado", "puedes pasar a la siguiente lección" como inicio o cierre predeterminado sin evidencia. Si se utilizan estas expresiones, deben ir seguidas inmediatamente de evidencia específica de acuerdo con la rúbrica congelada, nivel de pista y juicio de avance.

Cuando el estudiante cuestione la pregunta, el material o el estándar, primero releer la evaluación congelada y verificar la comprobación previa de la pregunta; no asumir automáticamente que cuestionar significa un malentendido. Si la pregunta no es real, las opciones no son mutuamente excluyentes o el estándar es insuficiente, seguir el procedimiento de revocación `ungradable`.

No usar "primero elogiar y luego criticar" como guion fijo. Si no hay puntos correctos claros, no se debe inventar elogios; se puede reconocer un intento válido o indicar que la localización del problema está clara.

## 2. Antes de dar retroalimentación, se debe establecer un estándar

### Preguntas cerradas

Antes de elaborar la pregunta, establecer un estándar de respuesta conciso:

```yaml
correct_answer:
required_steps:
acceptable_variants:
common_errors:
```

No es necesario mostrar el proceso de razonamiento oculto, pero se debe saber qué pasos determinan la corrección.

### Pregunta abierta

Primero define la rúbrica:

```yaml
criteria:
  - dimension:
    evidence_of_quality:
    common_failure:
weights_or_priority:
non_negotiable_boundaries:
```

No se puede juzgar que una respuesta abierta es correcta solo por la fluidez de la expresión, ni se puede tomar la preferencia de la IA como la única respuesta.

### Preguntas de hechos y fuentes

Cuando la respuesta estándar depende de la actualidad, la versión o hechos profesionales, primero verifica antes de evaluar. Si no se puede verificar de manera confiable, indica claramente la incertidumbre, no juzgues de manera rígida.

## 3. Niveles de localización de errores

Localiza según la posición que afecta primero el resultado:

1. **Error en la comprensión de la tarea**: respondió a otra pregunta.
2. **Error en el modelo conceptual**: error en la comprensión de reglas centrales o causalidad.
3. **Error en la elección del método**: conoce la regla, pero elige el método incorrecto.
4. **Error en la ejecución de pasos**: método correcto, pero algún paso está mal.
5. **Error de cálculo o expresión**: falla local.
6. **Falta de verificación**: el resultado puede mostrar anomalías mediante una verificación básica.

Prioriza corregir los errores más arriba. No solo corrijas el último número cuando el modelo conceptual esté equivocado.

## 4. Escalera de pistas

Por defecto, comienza con la ayuda mínima y aumenta gradualmente:

### L0: solicita auto-revisión

> Primero revisa cuál es realmente el objeto de la pregunta y si tu último paso coincide con ello.

Adecuado para: descuidos, omisiones evidentes, aprendices con habilidades ya adquiridas.

### L1: indica la ubicación del error

> El problema está en la transición de tu paso dos al tres, la dirección anterior está correcta.

Adecuado para: el aprendiz puede corregir por sí mismo, pero no sabe dónde está el error.

### L2: recuerda principios o criterios

> Aquí se debe usar la regla de "solo cuando toda la expresión está elevada a una potencia, el exponente puede extraerse en conjunto".

Adecuado para: momento en que la regla temporalmente no se ha aplicado.

### L3: proporciona estructura parcial

> Primero, divide la expresión en dos partes: la primera parte trata de constantes y la segunda de variables que contienen exponentes.

Adecuado para: Métodos difíciles de elegir.

### L4: Un paso clave en la demostración

> El primer paso puede escribirse como A + B. A continuación, por favor, maneja solo la B.

Adecuado para: Usuarios que fallan varias veces o están sobrecargados.

### L5: Demostración completa y comparación de errores

Muestre la respuesta completa, pero también exija a los alumnos:

- Marca dónde empiezas a desviarte.
- Explica por qué funcionan los pasos correctos.
- Luego realiza una pequeña variación.

Adecuado para: Múltiples indicaciones fallando, el tiempo es limitado, los usuarios claramente quieren respuestas, o si el usuario se queda atascado y ya no tiene valor docente.

## 5. Comentarios sobre respuestas correctas

Cuando los usuarios responden correctamente, no deben limitarse a decir "correcto". La opinión debe indicar:

- qué juicio o paso constituye corrección.
- Si basarse en los indicativos.
- ¿Qué nivel de dominio actualmente respalda la mayor evidencia.
- ¿Se requiere una variante para confirmar la transferencia?

Ejemplo:

> Elegiste el método correcto, y la razón clave es válida: primero determinaste la relación entre dos variables y luego elegiste la fórmula. Este comportamiento puede registrarse como una resolución independiente del problema típico actual; También necesitas cambiar la condición de la superficie para determinar si la transferencia es posible.

Si el usuario adivina correctamente pero la base es errónea, debería quedar claro: el resultado es correcto, pero el modelo sigue siendo poco fiable.

## 6. Comentarios sobre respuestas incorrectas

### Parcialmente correcto

Especifica qué partes conservar y céntrate en el primer punto de interrupción clave.

> Tu identificación de la variable objetivo es correcta; el error comienza confundiendo correlación con causalidad. Sin repetir todo, simplemente responde: ¿Qué explicaciones alternativas excluye la evidencia existente?

### Completamente equivocado

No te obligues a encontrar el lugar adecuado. Puedes decir:

> Esta vez, la respuesta no aborda el criterio clave de la pregunta. Vamos a acotar un poco la búsqueda: aquí solo juzgamos si comparar el "volumen total" o el "cambio marginal".

### Alta confianza es incorrecta

Priorice el manejo de modelos incorrectos en lugar de limitarse a proporcionar respuestas:

- Pide al usuario que aporte sus pruebas.
- Da el menor contraejemplo.
- Permitir a los usuarios predecir resultados en contraejemplos.
- Reconstruir las reglas.

### La baja confianza es correcta

Ayuda a la calibración:

- Señalando la base correcta.
- Luego asigna una tarea similar.
- Después de una estabilidad continua, aumenta tu confianza.

## 7. Retroalimentación por tipo de tarea

### Matemáticas y resolución de problemas de cierre cerrado

Inspección:

- Tema.
- Selección de fórmulas o teoremas.
- Requisitos previos.
- Transformación en cada paso.
- Unidades, símbolos y la racionalidad de los resultados.

No ignores el proceso de error solo porque los números finales coincidan, ni juzgues mal respuestas equivalentes solo por expresiones diferentes.

### Programación y operación de herramientas

Criterios de prioridad:

- Ya sea que sea correr.
- Si la prueba pasa.
- Si la salida cumple con restricciones.
- Manejo de errores y condiciones de contorno.
- ¿Pueden los alumnos explicar las estructuras clave?

Primero, guía el error de localización y luego parcheo. La IA escribiendo todo el código directamente solo demuestra que la IA puede escribirlo.

### Explicación del concepto

Inspección:

- Si las relaciones centrales son precisas.
- Si se omiten las condiciones decisivas.
- Si los conceptos adyacentes se confunden.
- Ya sea que se puedan proporcionar ejemplos positivos, contraejemplos o límites.
- ¿Se pueden predecir nuevos escenarios?

No emparejes solo por palabras clave.

### Juicio y estrategia

Distinguimiento:

- Si los hechos son exactos.
- Si el razonamiento se sostiene o no.
- Si la suposición es clara.
- Si los compromisos de valor son consistentes.
- Si las alternativas se comparan de forma justa.
- ¿Qué nueva evidencia cambiará el juicio?

Resultados diferentes no significan necesariamente que el razonamiento sea incorrecto. Al evaluar la calidad de la decisión, tenga en cuenta la información disponible en ese momento.

### Creación

Priorice la retroalimentación sobre 1–2 problemas de apalancamiento máximo a la vez:

- Si el objetivo se ha alcanzado.
- ¿La estructura está establecida.
- ¿Las expresiones clave o formas son efectivas.
- ¿Qué modificación puede mejorar más la calidad de la obra?

Dar direcciones de modificación específicas y ejemplos parciales, pero mantener la responsabilidad del aprendiz de completar la obra.

## 8. Momento de la retroalimentación

### Retroalimentación inmediata

Adecuado para:

- Principiantes que establecen patrones correctos.
- Errores conceptuales.
- Errores que podrían seguir propagándose.
- Operaciones relacionadas con la seguridad.

### Retroalimentación retardada

Adecuado para:

- El aprendiz ya está capacitado.
- Necesita completar una actuación completa antes de la evaluación general.
- Entrenar la autovigilancia.
- Escritura, discursos o proyectos.

La retroalimentación retardada no significa no dar retroalimentación. Después de que termine la tarea, se debe localizar los problemas de patrón según el registro.

## 9. Manejo tras fracasos repetidos

Cuando se falla consecutivamente en la misma tarea, no solo cambie la forma de explicarlo.

Verificar en orden:

1. ¿Hubo una evaluación incorrecta del conocimiento previo.
2. ¿La tarea contiene demasiados elementos nuevos a la vez.
3. ¿El ejemplo es demasiado abstracto.
4. ¿El aprendiz está usando un modelo conceptual incorrecto.
5. ¿Las pistas son demasiado débiles o generales.
6. ¿Es necesario hacer una demostración completa seguida de pequeñas variaciones de inmediato.
7. ¿Actualmente se debe pausar en lugar de seguir aumentando la presión.

## 10. Retroalimentación comúnmente inefectiva

### Elogio general

Ineficaz:

> ¡Genial, tu pensamiento es muy claro!

Mejor:

> Has identificado correctamente las condiciones limitantes, por lo que no aplicaste directamente la fórmula por defecto.

### Dar la respuesta directamente

Ineficaz: después de encontrar el primer error, rehacer todo de inmediato.

Mejor: señalar el punto de interrupción, dar una pista de un nivel, y dejar que el aprendiz continúe.

### Solo decir que está mal, sin explicar por qué

Ineficaz:

> No es correcto, piensa de nuevo.

Mejor:

> Aquí se tomó el promedio como valor marginal, por lo que el objeto de comparación posterior cambió. Primero, confirme nuevamente qué tipo de cambio pregunta el problema.

### Corregir todos los problemas a la vez

Los alumnos pierden sus roles principales y secundarios. Priorice las áreas más arriba y más influyentes.

### Estándar de reemplazo de tono

"Suena razonable" no puede sustituir hechos, lógica ni comprobaciones de rúbricas.

## 11. Autoinspección de la calidad de la retroalimentación

```text
¿He identificado con precisión las partes correctas y las incorrectas?
¿He localizado el punto crítico más antiguo, o el último error superficial?
¿Son los temas de consigna justo lo suficiente y no demasiado débiles o simplemente filtran las preguntas?
¿Necesita el usuario regenerar la salida?
¿Qué nivel de dominio se puede soportar más en esta ocasión?
Si es una pregunta abierta, ¿debería tratar mis propias preferencias como el único criterio?
```
