# Funcionamiento de los cursos adaptativos

Este protocolo define cómo guardar, impartir, ajustar y retomar cursos de larga duración. Un conjunto pequeño de archivos de estado permite continuar lección por lección.

## 1. Modelo de estado mínimo

El curso se organiza en cinco componentes.

```text
Acuerdo de aprendizaje   Objetivo, contexto de aplicación y evidencia final
Plan de estudio          Ruta ajustable y registro de versiones
Lección actual           Plan, material del segmento y evaluación con criterios prefijados
Estado del estudiante    Evidencia de dominio, errores y posición actual
Lista de repasos         Recuerdo programado y tareas de transferencia
```

`inicio-del-curso.md` muestra el estado al estudiante. Los archivos YAML guardan el estado estructurado y permiten regenerar la página.

## 2. Principios de generación lección por lección

### Qué preparar al crear el curso

- Acuerdo sobre los criterios de dominio.
- Una ruta ajustable de entre 3 y 12 lecciones.
- Objetivo de cada lección, prerrequisitos, evidencia de dominio y orden provisional.
- Un plan de 3 a 4 segmentos para la primera lección.
- El material desarrollado y el registro de fuentes del primer segmento.

### Qué se prepara más adelante

- Texto principal de la segunda lección y siguientes.
- Texto de segmentos de aprendizaje aún no iniciados de la lección actual.
- Ejemplos, imágenes, evaluaciones y resúmenes de lecciones futuras.
- Análisis completo de fuentes desconocidas.
- Lecciones de recuperación basadas en el rendimiento de aprendizaje supuesto.

Las próximas lecciones tienen `route_status: provisional` y `material_status: not_generated`. Crea el directorio de una lección cuando se vuelva activa y guarda el material de cada segmento cuando llegue su turno.

## 3. Enumeración de estados

### Estado de la ruta `route_status`

- `active`: lección que se está preparando o enseñando actualmente.
- `provisional`: marcador de posición de ruta futura, puede ajustarse libremente.
- `completed`: enseñanza completada, versiones históricas conservadas.
- `skipped`: Omite basándote en pruebas existentes y registra la razón.

Una lección como máximo `active` a la vez.

### Estado del material `material_status`

- `not_generated`. La lección figura en el plan.
- `draft`. El material de la lección actual se generó y está pendiente de verificación o revisión.
- `source_checked`. El tutor principal verificó las fuentes usadas y las afirmaciones clave pueden rastrearse hasta ellas.
- `fact_checked`. Se revisaron la transcripción de las fuentes, la síntesis, las cifras, las condiciones y los desacuerdos.
- `pedagogy_checked`. El material cumple los criterios de explicación desarrollada, caso conductor, límites de aplicación y práctica activa.
- `verified`. Estado anterior conservado por compatibilidad. Para material nuevo se usan los tres estados de revisión detallada.
- `frozen`. Comenzó la enseñanza o el material ya se usó para evaluar.
- `invalidated`. Se detectó un problema en la fuente o en el criterio y se retiró el material.
- `legacy_prebuilt`. Material futuro generado con una versión anterior. Se consulta cuando la lección se vuelve activa y entonces se revisa antes de confirmarla.

### Estado de la enseñanza `delivery_status`

- `not_started`.
- `in_progress`.
- `completed`.

### Nivel de dominio `mastery_status`

Usa solo `unknown / exposed / guided / independent / transferable / durable`. Define leer `../rubrics/mastery-rubric.md`.

## 4. Versiones y congelación

Fijar una versión deja un registro verificable del material y de los criterios aplicados. El plan de las próximas lecciones sigue siendo ajustable.

### Línea base de la ruta

Después de confirmar el objetivo, escriba:

```yaml
route:
  version: 1
  status: provisional
  confirmed_scope:
    - learning_goal
    - application_context
    - final_mastery_evidence
    - active_lesson
  future_lessons_are_provisional: true
```

Cuando los usuarios modifican objetivos, indicaciones, dificultad u orden, solo se modifica la lección futura y el `route.version` se incrementa en uno.

### Cómo fijar el material de la lección y del segmento actual

La lección actual avanza en orden:

```text
borrador del plan
→ parte 1 fuente verificada
→ parte 1 hechos verificados
→ parte 1 pedagogía verificada
→ parte 1 entrega y práctica
→ adaptar partes no generadas
→ próxima parte
→ evaluación congelada inmediatamente antes de la entrega
```

Antes de entregar cada segmento de aprendizaje, la navegación visible para el usuario debe prepararse y entregarse en orden:

```text
Las posiciones conectan de delante a atrás
→ material didáctico simplificado de fuentes actuales
→ Síntesis del tutor y límites aplicables
→ Suposiciones de aplicación en escenarios de usuario
→ Actividad del estudiante revisada y con criterios prefijados
```

Los metadatos del plan de estudio y del material docente desde v4 deben incluir `source_layer / tutor_synthesis / application_layer`. Los paquetes antiguos que carezcan de estos campos se leen como legacy, sin reescribir la historia; los nuevos segmentos de aprendizaje que aún no han comenzado se completan según v4.

Cada segmento de aprendizaje mantiene su propio `material_version` después de iniciar la enseñanza. Los segmentos que aún no se han generado pueden modificar el plan directamente según los comentarios; los segmentos ya enseñados necesitan crear una nueva versión si se requiere corrección, indicando las preguntas afectadas y anulando la puntuación antigua.

### Cómo fijar los criterios de evaluación

Antes de mostrar la pregunta, se fijan `correct_answer` o rúbrica, motivo, variantes aceptables, errores comunes y escalera de pistas. Tras la respuesta del usuario solo se permite: puntuar según el estándar; o en caso de problemas con la pregunta/fuente, marcar `ungradable` y anular.

## 5. Eventos de control por el usuario

Normalizar el siguiente lenguaje natural a eventos:

```yaml
continue: Continuar, siguiente segmento
question: Tengo una pregunta, ¿qué significa esto?
too_hard: Demasiado difícil, explícalo más simple, no puedo seguir el ritmo
change_direction: No es lo que quiero aprender, cambiar de dirección, ajustar el curso
pause: Parar un momento, continuar la próxima vez
note: Esta es mi comprensión, ayúdame a guardarla
```

### `continue`

Pasa al siguiente segmento cuando se cumpla el criterio de avance. Al terminar la lección, completa primero el recuerdo inmediato, la transferencia a otro contexto, la revisión de errores y la actualización del estado. Si un concepto fundamental requiere refuerzo, `Continúa` lleva a ese refuerzo.

### `question`

Responder preguntas dentro del alcance actual y registrar la posición de retorno. Cuando las preguntas revelen lagunas previas, insertar el mínimo complemento, sin expandirse automáticamente a una nueva rama de curso.

### `too_hard`

Intentar en orden: reducir el nivel de abstracción, acortar la tarea, usar ejemplos familiares al usuario, dar un ejemplo completo, complementar lo previo. Registrar el nivel de pista. Completar una pista alta no se considera dominio independiente.

### `change_direction`

Pausa la lección actual y primero resume si la desviación es un objetivo, dificultad, caso, ritmo o ruta. Proporciona un plan de ajuste mínimo y modifica solo `provisional` curso. Si los objetivos actuales de la lección también necesitan cambiar, crea una nueva versión y explica cómo se manejará la versión original.

### `pause`

Guarda la lección actual, el segmento de aprendizaje actual, las preguntas pendientes y los siguientes pasos. No fuerces resúmenes ni juicios solo para crear una sensación de 'finalización del curso'.

### `note`

Añade el discurso original del usuario al `02-user-notes.md`. Cuando sea necesario organizar, guarda el discurso original y la organización de IA en una sección separada.

## 6. Registros de ajuste de curso

Escribe cada cambio de ruta:

```yaml
course_adjustments:
  - adjustment_id: CA-001
    changed_at: ""
    trigger: user_feedback | performance_evidence | source_change | constraint_change
    evidence: ""
    route_version_from: 1
    route_version_to: 2
    affected_lessons: [L02, L03]
    before: ""
    after: ""
    reason: ""
    user_confirmed: false
```

No modifique ni cree versiones únicamente por redacción. Registre únicamente cambios en objetivos, orden, dificultad, adquisición de evidencia o cambios en las adiciones o eliminaciones de clases.

## 7. Registro del avance y del dominio

La entrada al curso al menos muestra:

| Número de lección | Estado de la ruta | Progreso del contenido | Mantente en el camino | Siguiente paso |
|---|---|---|---|---|
| L01 | Actualmente | Párrafo 2/4 | guided | Completa la variante sin aviso |
| L02 | Tentativo | No generado | unknown | Confirma tras L01 pruebas |

El progreso del contenido responde "¿Dónde cubre el curso?"; El progreso de dominio responde a "Qué pueden hacer los usuarios." Está prohibido el porcentaje de derivación del contenido completado.

## 8. Acceso a fuentes y análisis bajo demanda

Los materiales de usuario no son un requisito previo para la construcción del curso. Cuando los materiales de usuario no estén disponibles, utiliza `agent_researched`, fija únicamente los ámbitos de investigación en torno al segmento de aprendizaje actual, recopila materiales autorizados, establece conclusiones clave — correspondencia de fuentes y luego procede a la redacción de materiales didácticos. Lee `safety-and-sources.md` de puerta detallada.

### PDF y archivos locales

Registrar `original_location`, hashes de archivos o identificadores estables, números de página reales en uso, estado de análisis analizado y limitaciones. Primero localiza el rango necesario para la lección actual y luego lee la página correspondiente. `sources/originals/` solo se coloca cuando el usuario está autorizado y la copia es valiosa.

### Página web

Registrar URL, fecha de acceso, título, autor o institución y alcance de uso. Vuelve a consultar fuentes oficiales para hechos recientes. No copies contenido completo protegido por derechos de autor solo para guardar la lección.

### Video o audio

Prioriza el uso de subtítulos del editor, subtítulos de la plataforma o transcripciones confiables. Registra `time_range`. Si no hay transcripción o no es accesible, marca como `unavailable` e informa al usuario que se requieren subtítulos, transcripción o archivo local.

### Notas externas o sistema de cursos

Cuando el usuario lo solicite explícitamente y el entorno de ejecución actual tenga las herramientas de lectura correspondientes, se pueden integrar los cursos, notas, páginas PDF o transcripciones de video como `user_material`. Conserva la identificación estable del objeto o enlace original; no consideres automáticamente los resúmenes antiguos de tutor como evidencia de hecho o conocimiento. La forma específica de conexión del producto pertenece a la capa de adaptación de despliegue y no se registra en el protocolo general de aprendizaje.

## 9. Control de costos de Tokens

Optimiza el costo total según `cost-routing.md` bajo restricciones de calidad. Primero utiliza herramientas deterministas, luego considera el Agent de bajo costo; por defecto, máximo uno, solo procesa los materiales candidatos y metadatos, el tutor principal conserva la aprobación de la fuente, síntesis del material didáctico, verificación de hechos y derechos de evaluación.

Cargar en cada ronda solo:

1. La ubicación actual de la entrada del curso.
2. El nodo actual y la revisión pendiente en el estado del estudiante.
3. El plan de curso actual y el segmento de aprendizaje actual.
4. La evaluación correspondiente al momento de calificar.
5. Fragmentos de fuente necesarios para la pregunta actual.

Prohibido: cargar todo el material futuro, reescribir el resumen completo del curso en cada ronda, analizar repetidamente el mismo archivo grande, generar materiales extensos antes de que el usuario confirme el objetivo.

También está prohibido: usar múltiples Agents de investigación superpuestos para ahorrar Tokens; tomar directamente el resumen del modelo de bajo costo como fuente; reintentar repetidamente después de fallos del modelo económico sin actualizar; solo contabilizar el hilo principal e ignorar el costo de sub-Agents y retrabajos.

## 10. Compatibilidad con paquetes de cursos antiguos

La versión antigua puede usar:

```text
lessons/01-title.md
lessons/L01-title/assessment.yaml
```

Al retomar un curso existente, busca `inicio-del-curso.md` o el nombre usado anteriormente, `课程入口.md` o `00-课程入口.md`. Aplica también estas reglas de compatibilidad.

1. Conserva los archivos anteriores en sus rutas.
2. Completa el plan con los estados de ruta, material, enseñanza y dominio.
3. Sigue utilizando las rutas existentes para la lección actual.
4. Marca como `legacy_prebuilt` los materiales anteriores de lecciones futuras y ábrelos cuando su lección se vuelva activa.
5. Para lecciones nuevas, usa un directorio por lección y guarda cada evaluación en la carpeta del curso, por ejemplo `assessments/01-title.yaml`.
6. La evidencia del estudiante determina el dominio. Un archivo existente acredita únicamente que hay material guardado.

## 11. Actualización conjunta al cerrar una lección

Finalice, pausa o ajusta la lección actual pulsando una acción atómica para actualizar:

1. Segmentos actuales de aprendizaje y progreso en el contenido.
2. Evidencia, indicaciones, malentendidos y estado de dominio en el estado del aprendiz.
3. Notas de usuario y resúmenes de tutores.
4. lista de repasos.
5. Proyección de acceso al curso.
6. Si se necesitan ajustes, actualice las versiones de rutas y los registros de cambios.

La lista de repasos debe registrar el repaso inmediato con `review_type: immediate`, `retrieval_before_summary: true`, la tarea de transferencia, el resultado, los errores que reaparecieron y `next_action`. Si queda pendiente el repaso inmediato o falla la transferencia central, la siguiente lección sigue como `provisional + not_generated`.

Antes de cambiar el dominio, guarda el concepto, la tarea, la calificación, el nivel de pista, los criterios cumplidos y pendientes, los errores activos, el máximo histórico, el nivel actual y si se permite avanzar. Un acierto aislado es insuficiente si el estudiante sigue dependiendo de ayuda en ese concepto. Si falla la transferencia, conserva el máximo histórico y registra el nivel actual y el motivo del bloqueo.

Si algún archivo crítico no se escribe, no afirme que el estado se ha guardado. Especifique el alcance del fallo y preserve la siguiente acción de recuperación.
