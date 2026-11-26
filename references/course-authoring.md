# Plan de estudio y redacción de la lección actual

## Juicio fundamental

El aprendizaje sistemático establece primero una ruta completa y luego produce materiales didácticos para cada lección.

El mapa del curso resuelve «dónde acabas aprendiendo y por qué sigues este orden»; el paquete actual de cursos resuelve «qué se está aprendiendo exactamente ahora, cuál es la base y cómo demostrar el dominio». No generes ambas cosas a la vez.

```text
Objetivos de aprendizaje
→ Los mapas de los recorridos pueden ajustarse
→ Plan de lección actual
→ Pasaje de estudio actual y fuentes
→ Explicación, ejercicios y retroalimentación
→ Siguiente párrafo de aprendizaje
→ Las preguntas quedan congeladas antes de que se muestre la revisión
→ Ajustar los cursos futuros
→ Próxima lección
```

## 1. Primero, crea un mapa de ruta ajustable

Al aprender sistemáticamente, entrar en un campo, prepararse para exámenes o desarrollar habilidades, primero prepara una ruta de 3–12 lecciones. Los conceptos pequeños solo pueden ser de 1 a 3 lecciones.

Cada lección solo necesita estar claramente indicada:

```yaml
lesson_id:
title:
why_now:
learning_objective:
prerequisites:
mastery_evidence:
route_status:
material_status:
delivery_status:
mastery_status:
```

Ordena el plan por la secuencia más corta de requisitos que permita alcanzar la meta. Registra las próximas lecciones como provisionales y prepara sus textos y preguntas cuando corresponda.

Muestre a los usuarios el título del curso, los problemas resueltos en cada lección, la lección actual y la competencia final. Aclare que los cursos futuros se ajustarán en función del rendimiento de la lección y de la retroalimentación de los usuarios.

## 2. Crear un paquete de cursos separado solo para la lección actual

El paquete actual de cursos incluye:

```text
../../evaluaciones/01-{lesson-slug}.yaml
00-lesson-plan.yaml
parts/
  01-{part-slug}.md
  02-{part-slug}.md
02-user-notes.md
03-tutor-summary.md
```

Cada lección resuelve solo un problema principal claro, normalmente dividido en 3–4 segmentos de aprendizaje. Primero, el plan del segmento de aprendizaje queda congelado y solo se genera el segmento actual; Después de que el alumno complete la interacción o retroalimentación, se genera el siguiente segmento. De este modo, la lección actual puede ajustarse según el estado real de comprensión.

## 3. Convierte el material didáctico en un pasaje largo para la clase docente

### La sección de aprendizaje posiciona primero al aprendiz

Para cada segmento de aprendizaje, el contenido visible para el usuario se navega primero dentro de seis líneas o menos, y luego pasa al texto principal:

```text
Posición actual: L01-P02 / segundo segmento de la lección actual
Pregunta central de la lección:
Qué resolvió el segmento anterior:
Por qué sigue este segmento:
Qué explica la fuente en este segmento:
Qué podrás hacer al terminar:
```

La navegación es un proceso de reposicionamiento en una conversación larga, no una repetición de todo el mapa del curso. No solo informes "qué párrafo", ni empieces directamente desde una única pregunta local. Si no se ha completado el primer segmento de aprendizaje, indica "Este es el punto de partida de esta lección" y por qué es el punto de partida.

El texto principal del material didáctico debe ser un texto didáctico extenso que pueda leerse de forma independiente, no un esquema ampliado de "definiciones + tablas + tres resúmenes", ni debe rellenarse mecánicamente con columnas fijas.

Cada segmento de aprendizaje se desarrolla de forma natural a lo largo de un hilo conductor lógico:

1. Comenzar con un problema real, una contradicción o un caso, permitiendo que los aprendices primero obtengan una intuición.
2. Explicar gradualmente los mecanismos detrás del fenómeno, aclarar el “por qué” y luego proporcionar los términos y definiciones.
3. Continuar desarrollando con el mismo caso a lo largo de todo el recorrido, agregando un contraejemplo o un caso límite si es necesario.
4. Hacer pausas en los puntos clave de inflexión, pidiendo a los aprendices que predigan, expliquen, juzguen o actúen.
5. Corregir según las respuestas y luego conectar el concepto actual con la siguiente fase de aprendizaje.
6. Al final del texto, conservar los puntos de anclaje de la fuente y los límites de aplicabilidad.

### Separar la fuente, la síntesis del tutor y la aplicación del usuario.

El plan actual de la lección y los metadatos de la fase de aprendizaje deben conservar tres niveles:

```yaml
source_layer:
  author_claims: []
  source_location: ""
tutor_synthesis:
  claims: []
  confidence: ""
application_layer:
  user_context: ""
  working_hypothesis: ""
  evidence_needed: []
```

El texto principal debe primero explicar fielmente en lenguaje sencillo el material o fuente original, luego señalar claramente el juicio sintético del tutor, y finalmente conectar con el escenario del usuario. Incluso si no hay un curso `agent_researched` del autor original, se deben distinguir las conclusiones apoyadas directamente por la fuente de la síntesis del tutor. Las decisiones en el escenario del usuario que aún no se hayan verificado deben denominarse hipótesis y explicar qué evidencia se necesita; no se debe reescribir como conclusión del material.

`source_layer` es una declaración de evidencia, no una etiqueta de formato. Solo las fuentes realmente consultadas por el tutor pueden escribirse en `author_claims`, y `source_location` debe poder localizar la afirmación actual. Si el texto original no está disponible, no se debe crear un falso material del libro: degradar explícitamente a explicación temática o detenerse en la puerta de la fuente, y no usar “el libro dice” o “el autor da un ejemplo” para cubrir la ausencia.

Usa el caso conductor para aclarar el objetivo actual. Apóyate en conceptos ya enseñados, mantén el foco en la pregunta de la lección y atribuye a la fuente solo las afirmaciones que esta sostiene.

El título solo sirve para la narrativa. Se permiten de 2 a 5 secciones naturales, no se exige un título unificado. Las tablas y listas pueden usarse para resumir, pero deben colocarse después de la explicación y no reemplazarla.

Elimina las repeticiones y el relleno. Como orientación, un segmento en español puede tener entre 700 y 1400 palabras. Ajusta la longitud a la complejidad del tema. El estudiante debe poder entender el texto y completar la actividad fuera de la conversación.

### Criterios de calidad de la explicación

Comprueba estos criterios antes de mostrar el segmento.

- ¿Hay un problema concreto o un caso conductor que conecte las ideas?
- ¿Se explica el mecanismo, la relación causal o el proceso de decisión?
- ¿Los términos abstractos se explican en situaciones conocidas por el estudiante?
- ¿Hay al menos un razonamiento completo, una demostración, un contraejemplo o un caso límite?
- ¿Hay una actividad breve que requiere una respuesta del estudiante?
- ¿Queda claro en qué condiciones se aplica lo aprendido?
- Si hay fuentes rastreables y las citas no dificultan la lectura.
- Si se eliminan tablas y resúmenes, el texto permanece como un material de enseñanza completo.

Si alguna de estas claves es negativa, reescribir antes de pasar a la enseñanza.

El contenido de definición primero establece la intuición antes de nombrar; el contenido procedimental muestra ejemplos completos y disminuye gradualmente las pistas; el contenido de juicio utiliza casos reales para mostrar objetivos, evidencias, supuestos y decisiones; el contenido creativo enseña mediante comparación de obras y procesos concretos de modificación.

## 4. controlar la granularidad del segmento de aprendizaje

Una lección normalmente incluye:

1. Establecer intuición y conciencia de problemas.
2. Explicar el mecanismo central y hacer un pequeño ejercicio.
3. Profundizar con casos, contraejemplos o demostraciones completas.
4. Aplicación independiente, evaluación y transferencia.

Solo generar y presentar un segmento de aprendizaje a la vez. Después de que el usuario haga una pregunta, responder y volver a la posición original. Si el usuario encuentra dificultad, primero reducir la abstracción, cambiar el caso de referencia o reducir la tarea, sin introducir nuevos conceptos. Si el usuario considera que la dirección es incorrecta, los segmentos no generados pueden modificarse directamente.

## 5. fuentes del material y fiabilidad de los hechos

La lección actual debe establecer una lista de fuentes:

```yaml
source_id:
source_type: official_doc | textbook | paper | trusted_reference | user_material | verified_synthesis
claim_scope:
location:
verified_at:
confidence:
known_limits:
```

Primero, pulsa `safety-and-sources.md` para seleccionar `agent_researched / source_bounded / source_augmented`. Usa `agent_researched` cuando el usuario no haya proporcionado materiales, recopila de forma independiente los materiales del segmento de aprendizaje actual, sin requerir que el usuario suba primero el material didáctico.

Prioridad de fuente:

1. Documentos oficiales, normas, investigaciones originales, materiales didácticos autorizados.
2. Instituciones fiables y materiales de segunda mano de alta calidad.
3. Compilación exhaustiva consistente en múltiples fuentes.
4. Los blogs regulares, los debates comunitarios y los resúmenes de búsqueda solo complementan los estudios de caso.

Cuando los materiales didácticos sean sintetizados por IA, indique "compilación basada en fuentes". Primero deben verificarse hechos recientes, versiones de software, conceptos en disputa o cuestiones profesionales. El contenido que no puede ser verificado se marca como incierto y no se utiliza como única respuesta a preguntas cerradas.

El segmento de aprendizaje actual no puede accederse directamente desde `draft` a la instrucción. Comprobar en el siguiente orden:

```text
draft
→ source_checked: Las fuentes reales utilizadas son auténticas y aplicables, y se pueden señalar conclusiones clave
→ fact_checked: El material didáctico no distorsiona las fuentes, y los números, condiciones, versiones y disputas se gestionan correctamente
→ pedagogy_checked: El material didáctico explica claramente a los alumnos objetivo, y los casos, simulaciones, límites y ejercicios son efectivos
→ congelado: La enseñanza o la revisión han comenzado
```

Las verificaciones de fuentes y de hechos se centran en "si hay un error de enseñanza"; La comprobación de calidad docente se centra en "si existe una iglesia genuina". Estas tres no pueden combinarse en una sola frase "comprobada". Si algún punto clave falla, debe revisarse; Si no se pueden resolver problemas de evidencia, acota la conclusión sin añadir texto que la encubra.

No analice todas las fuentes durante la fase de creación del curso. Lee las páginas, capítulos o periodos de tiempo necesarios en torno a los objetivos actuales de la lección.

## 6. Capturas de pantalla y materiales visuales

Úsalo solo cuando el coste de comprensión pueda reducirse significativamente:

- Interfaz de software y ruta de operación específica.
- Espacio, estructura, proceso o relaciones causales.
- Gráficos, cambios de fórmula o comparaciones de categorías.
- Los alumnos deben identificar páginas, diseños o obras reales.

Cada imagen explica "dónde mirar, qué ilustra y cómo se relaciona con los objetivos de la lección." Si no hay capturas de pantalla fiables disponibles, utiliza diagramas de texto o estructurales sin fabricar interfaces.

## 7. Las rutas futuras pueden cambiarse, pero los estándares históricos no deben desviarse

Dependiendo del rendimiento, puedes:

- Reducir o aumentar la dificultad de las tareas posteriores.
- Se añadieron clases complementarias.
- saltar las clases respaldadas por la evidencia existente.
- Estuches de reemplazo.
- Ajusta el orden futuro o recorta los cursos.

Solo `provisional` lecciones se modifican y se registran las versiones de ruta. Los materiales didácticos y los estándares de respuesta que hayan comenzado deben ser rastreables.

Cuando se detectan errores de contenido histórico:

1. Señalar errores específicos.
2. Marcar versiones antiguas de los materiales didácticos como inválidas.
3. Revocar preguntas y puntuaciones afectadas.
4. Crear una versión revisada.
5. No culpes a los alumnos por los errores de los materiales didácticos.

## 8. En la entrada del curso solo se muestra la información necesaria

Visualización de la entrada al curso por defecto:

- Habilidad suprema.
- Versión actual de la ruta.
- Lección actual.
- progreso en el contenido y progreso en dominio.
- Acciones disponibles por el usuario.
- Siguiente paso.

Los cursos futuros solo muestran títulos, objetivos y el estatus de "tentativo", y no muestran enlaces a materiales que aún no se hayan generado.

## 9. Tras completar la lección actual, decide la siguiente lección

Tras terminar el último segmento de aprendizaje de la lección actual, realizar una repaso inmediato: resumir la lección en una sola frase, cerrar el material didáctico tras la lección y animar a los alumnos a recordar activamente; luego asignar una tarea de transferencia basada en cambios superficiales o de escena; corregir malentendidos recurrentes y actualizar la evidencia. Solo cuando el nodo central alcanza la Puerta puede generarse el principio de Material de la siguiente lección.

En el repaso inmediato, pide al estudiante que recuerde y aplique lo aprendido antes de mostrar respuestas, resúmenes o formulaciones previas. Acredita `durable` solo mediante un repaso programado tras un intervalo real.

Finalizar la comprobación actual de la clase:

```text
¿El objetivo sigue siendo válido?
¿La lección actual es demasiado difícil, demasiado simple o va en una dirección equivocada?
¿Qué actuaciones son evidencia independiente y cuáles dependen de indicaciones?
¿Qué error afectará la próxima lección?
¿La próxima lección debería seguir la ruta original, reforzar prerrequisitos, cambiar ejemplos, saltarse contenido o cambiar de dirección?
```

Primero actualiza la ruta y el estado, luego genera la próxima lección. No crees material futuro antes de que el usuario complete la lección actual.
