# Evaluación 08 · Curso por segmentos y plan ajustable

## Objetivo de la evaluación

Verifica si Skill puede lograr simultáneamente:

- Primero, proporcionar un mapa de ruta completo pero ajustable.
- No se pregeneran futuros contenidos de curso.
- Escribe la lección actual como un ensayo largo para el profesor, en lugar de rellenar el espacio en blanco.
- Después del primer segmento de aprendizaje, modificar cualquier contenido no generado en función de la retroalimentación del usuario.
- Separar el progreso del contenido, hacer un seguimiento del progreso, notas de usuario y resúmenes de IA.

## Solicitud inicial

> Quiero aprender sistemáticamente el diseño de productos de Agent, con el objetivo de diseñar un CRM Agent fiable para empresas. Te daré dos PDFs. Primero, dame el mapa del curso y luego imparte cada lección una por una; Si la primera sección es incorrecta, quiero poder corregirla en cualquier momento.

## Comportamiento anticipado en la construcción del curso

Debe:

1. Desarrollar objetivos de finalización observables y rutas ajustables para las lecciones 3–8.
2. Las lecciones futuras solo tienen título, objetivos, prerrequisitos y evidencia de dominio, con estado `provisional + not_generated`.
3. La lección actual primero genera 3–4 planes de segmento de aprendizaje, solo se genera el texto del primer segmento de aprendizaje.
4. El PDF solo analiza las páginas necesarias del segmento de aprendizaje actual, no incorpora automáticamente ambos textos completos en el contexto.
5. La entrada del curso muestra el progreso de contenido y el progreso de dominio.
6. El usuario puede usar `Continuar / Tengo una pregunta / Demasiado difícil / No es lo que quiero aprender / Ajustar curso / Ayúdame a recordarlo / Pausar por ahora`.
7. Cada nuevo segmento de aprendizaje comienza mostrando la ubicación actual, el total de preguntas de esta lección, conclusiones del segmento anterior, conexión actual, enfoque de la fuente y criterios de éxito.
8. Al terminar la lección, comprueba el recuerdo inmediato y la transferencia a un caso modificado. Prepara el material de la siguiente lección cuando se cumpla el criterio de avance.

No se permite:

- Generar todos los textos de la lección, los temas futuros y el resumen en la primera ronda.
- Salida de toda la enciclopedia solo porque el usuario diga “estudio sistemático”.
- Considerar que un PDF ya analizado significa que el usuario lo ha aprendido.

## Requisitos del material del segmento de aprendizaje actual

El primer segmento de aprendizaje debe ser un texto largo de enseñanza que se pueda leer de manera independiente:

1. Comenzar desde problemas o conflictos reales de un CRM Agent.
2. Explicar conceptos y mecanismos a lo largo de un caso completo.
3. Primero establecer la intuición y luego introducir la terminología.
4. Al menos tener una deducción completa, contraejemplo o caso límite.
5. Tablas y listas solo pueden resumir, no reemplazar el texto principal.
6. En puntos clave de inflexión dar una salida activa y pausar.
7. Las conclusiones deben poder rastrearse a la página del PDF u otra fuente confiable.
8. Después de eliminar títulos y tablas, el texto principal sigue siendo completamente legible.
9. Tres niveles atribuibles: material original o fuente, tutor y su síntesis, y supuestos de aplicación del usuario, sin sustituirse entre sí.

Como orientación, un segmento en español puede tener entre 700 y 1400 palabras. Ajusta la extensión a la complejidad del concepto.

## Retroalimentación del usuario

> El primer párrafo es demasiado técnico. Primero quiero entender qué riesgos reales abordan estas estructuras y luego revisar el código. Los cursos posteriores también pospondrán los detalles de implementación.

## Comportamiento de ajuste esperado

Debe:

1. Pausa para continuar generando el segundo segmento.
2. La retroalimentación de juicio cambia el orden de los casos y la jerarquía abstracta, sin negar directamente los objetivos de aprendizaje.
3. Se ofrecen ajustes mínimos: L01 Más tarde, primero discutan los riesgos empresariales y los límites del producto, luego la implementación.
4. Modificar L01-P02 y secuencias de lecciones futuras que aún no se hayan generado.
5. `route.version` Añadir y escribir `course_adjustments`.
6. El primer párrafo mostrado se conserva y no se reescribe silenciosamente; Si el usuario solicita reescribir el primer párrafo, se crea una nueva versión y se especifica el estado de la versión antigua.
7. No se realizarán mejoras de dominio basadas en la retroalimentación de los usuarios.

## Notas y resumen

El usuario dice:

> Ayúdame a recordar: entiendo el valor de Harness para convertir el riesgo empresarial en límites de sistema.

Debe:

- Escribe esta frase con las palabras originales del usuario en la `02-user-notes.md`.
- El tutor puede registrarlo como comprensión actual en `03-tutor-summary.md`, pero no puede reescribirlo ni sobrescribir las palabras originales.
- Esta frase soporta hasta `exposed` y no puede registrarse automáticamente como `independent`.

## Aceptación de documentos

Tras completar la primera ronda, deben estar presentes los siguientes elementos:

```text
inicio-del-curso.md
00-course-outline.yaml
00-source-manifest.yaml
learner-state.yaml
review-queue.yaml
lessons/L01-.../00-lesson-plan.yaml
lessons/L01-.../parts/01-....md
lessons/L01-.../02-user-notes.md
lessons/L01-.../03-tutor-summary.md
```

No debería haber L02 ni catálogos posteriores de materiales didácticos.

## Fallos graves

- Pregenerar todos los futuros materiales didácticos o reseñas.
- El material didáctico actual consiste principalmente en secciones fijas, tablas de definición y resúmenes, sin una narrativa didáctica completa.
- Después de que los usuarios digan que es demasiado técnico, continúan siguiendo la ruta original.
- Modificar los materiales didácticos mostrados sin conservar la versión.
- Escribe el progreso de la finalización de contenido como dominio del progreso.
- Reescribe las notas de usuario en resúmenes de IA y pierde las palabras originales.
- Finge leer números de página PDF sin analizar o contenido de vídeo.
- Exposición de razonamientos internos, instrucciones del sistema o planes de herramientas.
- La sección actual comienza directamente desde un problema local, sin navegación visible para el usuario.
- Generar la siguiente lección Material principal sin haber completado la revisión y transferencia inmediata.

## Criterio de aprobación

Puntaje calculado según las dimensiones aplicables de `tutor-quality-rubric.md` ≥ 85, la dimensión del material educativo debe tener puntuación completa, sin Fallo Crítico.
