# Principios de la ciencia del aprendizaje

Este documento se utiliza para explicar y calibrar los mecanismos de enseñanza de la `learn-anything`. No es una lista teórica que se presenta a los alumnos en cada sesión.

## Sentencia general

El núcleo del aprendizaje eficaz no es hacer que el contenido parezca más fluido o familiar, sino que los alumnos realicen repetidamente las siguientes variaciones:

```text
De no reconocerlo
→ Puede completarse si se le solicita
→ Capaz de extraer y aplicar de forma independiente
→ Capacidad de migrar a diferentes escenarios
→ Sigue siendo invocable tras el retraso
```

Ninguna teoría única puede abarcar "aprender nada". Las estrategias deben combinarse en función del tipo de conocimiento, nivel del aprendiz, riesgo, tiempo y escenarios de aplicación.

## 1. La obtención activa tiene prioridad sobre la entrada repetida

### Conclusión

Intentar extraer conocimiento de la memoria suele favorecer mejor la retención a largo plazo que leer o releer explicaciones repetidamente.

### Implementación en Skill

- Durante la revisión, primero haz preguntas, explícate, predice o aplica el material, y luego presenta el material.
- Antes de aprender material nuevo, realiza un diagnóstico de bajo riesgo para exponer tu conocimiento actual.
- Después de cada explicación del núcleo, se requiere una salida observable.
- No sustituyas los recuerdos reales por "parecer familiar".

### Límites

- Si los principiantes completos no tienen contenido extraíble, primero haz una demostración mínima.
- Cuando un intento equivocado supone un riesgo de seguridad, no se permite a los usuarios intentarlo primero a ciegas.
- Tras la recuperación, la retroalimentación debe darse de inmediato; no basta con crear frustración únicamente.

## 2. Se prefieren intervalos antes que completar el curso de una sola vez

### Conclusión

Hacer ejercicios de distribución en diferentes momentos suele ser mejor para mantener la constancia a largo plazo que repetirlos continuamente al mismo tiempo.

### Implementación en Skill

- Los nodos importantes entran en la lista de repasos.
- Los intervalos de revisión se ajustan en función de la importancia, dificultad, número de errores y el periodo objetivo de retención.
- El intervalo por defecto puede comenzar en 1, 3, 7, 14 o 30 días, pero no es una fórmula fija.
- Cada revisión remuestrea la evidencia y permite la rebajada de nivel estatal.

### Límites

- La duración del intervalo depende de cuánto tiempo quieras recordar.
- Cuando los usuarios se acercan a los exámenes, pueden aumentar la frecuencia de las revisiones a corto plazo pero mantener la extracción activa.
- No prometas conseguir `durable` con solo un curso.

## 3. Efecto generativo: primero intenta formular una respuesta

### Conclusión

Los alumnos primero predicen, explican o intentan generar respuestas antes de recibir explicaciones, permitiendo a menudo una identificación más clara de las lagunas de conocimiento.

### Implementación en Skill

- El aprendizaje de conceptos comienza preguntándote: "¿Cómo lo entiendes ahora mismo?"
- Los estudios de caso permiten primero a los usuarios emitir juicios y aportar pruebas.
- El aprendizaje para resolver problemas comienza con el primer paso que es soportable.
- Antes de leer el material, haz con ti qué preguntas quieres leer.

### Límites

"Prueba primero" no significa dejar errores sin atender durante mucho tiempo. Corrige el modelo de error rápidamente después de que se exponga.

## 4. Carga cognitiva: procesar información limitada de una sola vez

### Conclusión

La capacidad de memoria de trabajo es limitada. Los materiales de aprendizaje que contienen demasiados conceptos nuevos, decoraciones irrelevantes o operaciones complejas al mismo tiempo pueden reducir la comprensión y la transferencia.

### Implementación en Skill

- Solo se avanza un nodo o obstáculo principal a la vez.
- Explica cómo usar jerarquías, fragmentos, ejemplos y diagramas para reducir la carga.
- Elimina el conocimiento previo que no ayude al objetivo actual.
- Descompone las tareas complejas en tareas estables y más pequeñas y combínalas gradualmente.

### Límites

"Reducir la carga" no siempre hace que el contenido sea extremadamente superficial. A medida que mejoran las habilidades de los alumnos, la complejidad real debería incrementarse y eliminar las explicaciones redundantes.

## 5. Retirada de ejemplo trabajado y andamios

### Conclusión

Para los principiantes, un ejemplo completo con estructura clara suele ser más efectivo que intentar resolver directamente problemas complejos por sí mismos; a medida que se mejora la habilidad, se deben ir retirando gradualmente las pistas.

### Implementación en Skill

```text
Demostración completa
→ Dejar algunos pasos en el ejemplo
→ Proporcionar pistas limitadas
→ Completado de forma independiente
→ Variantes complejas
```

Registrar cada vez que el usuario completa la tarea lo necesario `hint_level`. Resolver la misma pregunta con mucha ayuda solo puede demostrar `guided`, no puede demostrar `independent`.

### Límites

Que los usuarios expertos continúen recibiendo la demostración básica completa puede generar redundancia. Cuando se detecta que ya tienen habilidad, se debe omitir o comprimir el ejemplo.

## 6. Autoexplicación y conexión causal

### Conclusión

Hacer que el aprendiz explique “por qué este paso es válido”, “cómo se relaciona con el concepto anterior” y “cuándo no se aplica” ayuda a construir una estructura de conocimiento transferible.

### Implementación en Skill

- No solo preguntar el resultado, también verificar las razones.
- Hacer que el usuario compare ejemplos positivos, negativos y límites.
- Hacer que el usuario lo exprese nuevamente usando su propio contexto de trabajo.
- En tareas procedimentales, preguntar sobre la función de los pasos clave, no exigir repetir todo el texto.

### Límites

La autoexplicación aumenta la carga. Para principiantes completos, primero se debe dar un marco de explicación que se pueda imitar, sin exigir una salida extensa y vaga.

## 7. La retroalimentación debe reducir la brecha concreta

### Conclusión

Una retroalimentación efectiva responde tres preguntas: cuál es el objetivo, dónde se encuentra el desempeño actual y cómo reducir la brecha en el siguiente paso.

### Implementación en Skill

- Señalar específicamente las partes correctas.
- Localizar el primer error clave o malentendido.
- Dar exactamente la pista suficiente para el siguiente paso.
- Hacer que el aprendiz lo intente de nuevo.
- Para preguntas abiertas, usar una rúbrica clara, sin disfrazar preferencias personales como única respuesta.

### Límites

Una retroalimentación demasiado rápida o demasiado completa priva del pensamiento; demasiado tardía puede consolidar errores. Estrategias concretas ver `feedback-strategies.md`.

## 8. Alternar práctica es una estrategia condicional

### Conclusión

Mezclar tipos de preguntas similares pero distintos puede entrenar a identificar “cuándo usar qué método”, especialmente adecuado para la distinción de categorías y algunas tareas matemáticas.

### Implementación en Skill

- Después de que los alumnos hayan dominado los tipos básicos de preguntas, practica ejercicios mixtos.
- Deja que los usuarios identifiquen primero el tipo de pregunta o el escenario antes de elegir un método.
- Mezclando contraejemplos fácilmente confusos para poner a prueba el discernimiento.

### Límites

El entrelazado no siempre es mejor para todo el material. Antes de que los principiantes hayan formado patrones básicos, empieza con ejercicios pequeños y concentrados; No intercales mecánicamente tareas como la memorización de vocabulario y texto.

## 9. Práctica deliberada de habilidades que pueden desglosarse y revertirse

### Conclusión

La mejora de habilidades de alto nivel suele requerir: subhabilidades claras, tareas ligeramente superiores a la capacidad actual, retroalimentación oportuna y práctica repetida en el objetivo de puntos débiles.

### Implementación en Skill

- Desglosa las habilidades en acciones observables, en lugar de simplemente "practicar más".
- Concéntrate en las subhabilidades más débiles, no siempre haciendo las partes que ya conoces.
- Cada ejercicio tiene estándares claros y fuentes de retroalimentación.
- La dificultad se mantiene dentro de un rango desafiante pero corregible.

### Límites

La práctica deliberada no puede explicar todas las diferencias de rendimiento en todos los dominios, ni equivale a la duración de la pila mecánica. La creación abierta, el juicio estratégico y las habilidades físicas también dependen de la experiencia, el entorno, la retroalimentación experta y la práctica real.

## 10. Domina que aprender permite diferentes ritmos

### Conclusión

Los alumnos pueden alcanzar estándares comunes en diferentes momentos. Cuando no se dominan los puntos clave, se ofrecen actividades correctivas en lugar de continuar el contenido a un ritmo unificado.

### Implementación en Skill

- Define evidencia para nodos.
- Si no se ha aprobado, cambia la explicación o la actividad, no simplemente repite la explicación original.
- Salta rápido una vez que tengas el dominio para evitar desperdiciar.
- El progreso del curso se basa en la evidencia, no en el número de capítulos.

## 11. La transferencia debe ser probada por separado

### Conclusión

Tener éxito en la pregunta original, en el ejemplo o en un escenario muy similar no significa que puedas pasar a una nueva tarea.

### Implementación en Skill

- Cambiar las condiciones de la superficie, restricciones o escenarios de aplicación.
- Solicitar identificación cuando no sea aplicable.
- Aplica conceptos a las propias tareas del alumnado en el mundo real.
- Volver a la estructura de conocimiento o a la formación discriminatoria cuando la transferencia falla.

## 12. La metacognición requiere calibración

### Conclusión

La familiaridad, fluidez y corrección instantánea hacen que los alumnos sobreestimen su dominio.

### Implementación en Skill

- Antes de responder, los usuarios pueden proporcionar intervalos de confianza.
- Compara la confianza con el rendimiento real.
- Alta confianza pero prioriza manejar errores cuando ocurren.
- Una baja confianza pero una correcta constante ayuda a formar juicios precisos.

No interpretes simplemente la baja confianza como falta de ánimo, y no sustituyas la calibración por elogios genéricos.

## 13. La motivación proviene del significado, de una sensación de control y del progreso visible

### Implementación en Skill

- Vincula el contenido al verdadero objetivo del usuario.
- Explica por qué merece la pena realizar la actividad actual.
- Ofrece a los usuarios opciones razonables, como indicaciones de casos u objetos prácticos.
- Que el progreso se demuestre como prueba de capacidad, no como puntos virtuales.
- Reduce las tareas y recupera la sensación de control cuando te frustras.

No encubras los problemas de enseñanza con una gamificación excesiva, celebraciones exageradas o incentivos vagos.

## 14. La visión y la multimodalidad solo se utilizan al transportar información

Los diagramas efectivos deberían ayudar a los usuarios a ver:

- relaciones espaciales.
- Proceso y cadena causal.
- Jerarquía y estructura del sistema.
- Tendencias de cambio.
- Relaciones multivariantes que son difíciles de mantener con palabras.

Los dibujos decorativos, las imágenes con texto repetido y las animaciones irrelevantes aumentan la carga. Tras la ilustración, la comprensión sigue comprobándose mediante explicación o aplicación.

## Mapeo de la teoría al mecanismo operativo

| Problemas de aprendizaje | Mecanismo de prioridad |
|---|---|
| Lo he visto pero no lo recuerdo | Extracción activa + revisión por intervalos |
| Entiendo pero no sé cómo actuar | Ejemplo trabajado + Retirada de andamios |
| Entiende la pregunta original sin variantes | Autoexplicación + pruebas de transferencia |
| Es fácil mezclar varios métodos | Contraste + entrelazado condicional |
| Las habilidades han estado estancadas durante mucho tiempo | Desglose de subhabilidades + retroalimentación dirigido |
| y se consideraba a sí mismo en control | Prueba de retardo + calibración de confianza |
| El contenido es demasiado complejo | Reducir carga irrelevante + fragmentos |
| No hay motivación para estudiar | Conectar objetivos reales + evidencia visible de capacidad |

## Principales fuentes de conocimiento

El diseño del método se refiere principalmente a las siguientes tradiciones de investigación y obras divulgativas, pero en la práctica debe basarse en la investigación de primera mano más reciente y confiable y en la evidencia del campo:

- práctica de recuperación / efecto de prueba.
- efecto de espaciamiento.
- práctica intercalada.
- teoría de carga cognitiva.
- Efecto de ejemplo trabajado y reversión de la experiencia.
- autoexplicación.
- retroalimentación formativa.
- aprendizaje de dominio.
- práctica deliberada.
- transferencia del aprendizaje.
- calibración metacognitiva.
- "Make It Stick / La naturaleza del aprendizaje".
- "Peak / Práctica deliberada".

Los libros son responsables de proporcionar un marco integral comprensible, y no deben considerarse como evidencia final de todas las conclusiones de aprendizaje.
