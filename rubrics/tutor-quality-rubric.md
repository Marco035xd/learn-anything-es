# Rúbrica de calidad del tutor

Estos criterios se utilizan para modificar, probar y aceptar `learn-anything`. El objeto de evaluación es el sistema de enseñanza completo, no si un único mensaje de texto es amigable.

## 1. Las reglas de aceptación

Este Skill debe cumplirse al mismo tiempo que se acepta:

1. `evals/` evaluar cada uno de los escenarios.
2. Cada escena obtiene una puntuación no inferior a 80/100, según las dimensiones aplicables.
3. El caso `answer-consistency.md` debe obtener al menos 90 de 100.
4. No se debe presentar un fallo crítico en ningún escenario.
5. Todos los modelos de YAML se pueden analizar.
6. El problema es que el sistema de inteligencia de la computadora no es un sistema de inteligencia de la computadora.
7. Los resultados de la investigación no han sido aprobados y deben ser revisados y reevaluados.

## 2. la dimensión de la calificación

### A. Intención y alcance · 8 puntos

- 8: Identificar con precisión las consultas, la comprensión, la entrada, la práctica, el proyecto o la revisión; no iniciar el curso en exceso, ni degradarlo como sustituto.
- 5: La ruta es básicamente correcta, pero hay un proceso adicional.
- 0: Error de intención, error de límite de alto riesgo, o rechazo de respuesta directa a una solicitud clara del usuario.

### B. Meta de dominio y plan ajustable · 10 puntos

- 10: Objetivos observables; información replicada ya existente; generación de rutas ajustables antes del aprendizaje del sistema, con objetivos, antecedentes y evidencias para cada clase; mantenimiento de material de enseñanza provisional y no pre-producido en las clases futuras.
- 7: hay una ruta del curso, pero el estado futuro, ajustar las reglas o tener poca evidencia.
- 3: Sólo un catálogo de conocimientos generales, sin objetivos verificables.
- 0: Empezar directamente con la enseñanza en forma fragmentada, o tomar como objetivo el nombre del tema.

### C. Calidad didáctica y fiabilidad de las fuentes · 15 puntos

- 15. Cada segmento muestra la posición, su conexión con el plan y el criterio de éxito. La explicación es clara, coherente y comprensible por sí sola. Desarrolla un caso real, muestra el mecanismo y el razonamiento e incluye práctica. Distingue las afirmaciones de la fuente, la síntesis y las hipótesis de aplicación. Usa tablas para sintetizar. Si faltan materiales, investiga. Las conclusiones clave son verificables y el material supera la revisión de fuentes, hechos y calidad pedagógica.
- 11: El material didáctico es utilizable e incluye estudios de caso, pero la narrativa, las explicaciones de los mecanismos, las ubicaciones del ejercicio, las fuentes o los límites son algo débiles.
- 6: Principalmente definiciones en blanco que rellenan, tablas, listas de comprobación o columnas fijas, sin un proceso de enseñanza completo; O relación poco clara entre materiales didácticos y preguntas.
- 0: Sin base de material didáctico, fuentes fabricadas ni uso de contenido no verificable para establecer la única respuesta.

### D. Adaptación entre dominio y tipo de conocimiento | 8 puntos

- 8: Identificar con precisión los tipos de conocimiento y elegir los diferentes métodos de enseñanza necesarios para conceptos, procedimientos, juicios, creación o práctica.
- 5: Las actividades generalmente coinciden, pero carecían de límites clave.
- 2: Utiliza la explicación combinada con preguntas de opción múltiple de forma uniforme.
- 0: Flujos de trabajo totalmente configurados mecánicamente, o utiliza el rendimiento del chat para sustituir habilidades del mundo real.

### E. Enseñanza segmentada, aprendizaje activo y carga cognitiva | 8 puntos

- 8: Cada lección se divide en 3–4 secciones de estudio prolongadas; Solo se genera y presenta la sección actual a la vez; Cada sección resuelve un obstáculo importante y organiza una salida activa; Demuestra cuándo los principiantes la necesitan.
- 5: Salida activa pero demasiado explicativa o desglose débil de tareas.
- 2: IA con conversación continua, con los usuarios observando principalmente.
- 0: Sobrecarga evidente o permitir que los principiantes intenten tareas de alta complejidad a ciegas.

### F. Criterios prefijados y coherencia al evaluar · 18 puntos

- 18: Cada pregunta debe ser preexaminada antes de mostrarse, y la base del material didáctico, la respuesta o rúbrica correcta, la razón, las variantes aceptables y las reglas de puntuación están fijas; La selección del usuario, la pregunta o la corrección de respuestas no cambiarán el estándar; Las preguntas ambiguas pueden revocarse como `ungradable`, y las puntuaciones antiguas se revocarán simultáneamente con el control de evidencias.
- 14: La respuesta es generalmente estable, pero la grabación o el manejo de ambigüedades es algo débil.
- 8: Hay estándares de respuesta, pero en conversaciones largas, a veces las preguntas se juzgan en función de la impresión.
- 0: Consulta la respuesta del usuario antes de decidirla; Ambos A/B son comprobados correctos; No hay nueva evidencia pero el veredicto cambia; La pregunta es ambigua y sigue siendo errónea de forma contundente.

### G. Retroalimentación y niveles de ayuda · 12 puntos

- 12: Proporcionar claramente las sentencias, la base del material didáctico, los puntos específicos de conformidad o infracción y los siguientes pasos; Confirmar únicamente las partes correctas realmente; Los estímulos son simplemente suficientes y requieren repetición.
- 9: La retroalimentación es correcta, pero las indicaciones son ligeramente demasiadas o los intentos de repetición son insuficientes.
- 4: Da una respuesta completa directamente o solo da un ánimo genérico.
- 0: Elogia al cometer errores, por defecto es "Tienes razón" o retroalimentación para reforzar el modelo erróneo.

### H. Ruta Adaptativa y Estado de Aprendizaje | 8 puntos

- 8: Ajustar los segmentos de aprendizaje no generados y las lecciones futuras en función del rendimiento; Conservar la versión ya enseñada; Cada actualización tiene una tabla de evidencias; Distinguir entre el pico histórico y el estado actual; Nivel de pronto, conceptos erróneos activos, bloqueo de avances y consistencia con la exposición / guiada / independiente / transferible / duradera.
- 5: La dificultad puede ajustarse, pero el registro de estado es relativamente grueso.
- 2: Solo registra hacia dónde va la historia.
- 0: Marcas 'enseñadas', 'reclamadas' o 'finalización de indicaciones altas' como dominio.

### I. Transferencia y retención a largo plazo · 8 puntos

- 8: Al final de cada lección, recuerda activamente y completa la tarea de cambio; Si fallas, reverte y bloquea la siguiente lección; Si retrasas la revisión, primero sácala; Distingue claramente entre rendimiento inmediato y mantenimiento a largo plazo.
- 5: Existen variaciones o revisiones, pero la evidencia es incompleta.
- 2: Repite solo la pregunta o resumen original.
- 0: La transferencia falla pero sigue avanzando, o reclama durabilidad sin demora.

### J. Calidad de la interacción y control del estudiante · 5 puntos

- 5: Expresar claramente y mantener una carga moderada; Una tarea de alta información a la vez; No revelar razonamientos ocultos; No depender de adulaciones para mantener la experiencia.
- 3: Utilizable pero algo mecánico o demasiado largo.
- 1: Como los robots de proceso o el exceso de ánimo.
- 0: Los usuarios no tienen responsabilidad de aprendizaje o se ven obligados a cooperar con procesos inútiles.

## 3. Fallo crítico

Si alguno de estos casos ocurre, el caso de uso fallará inmediatamente:

1. Para la misma pregunta, si el usuario elige A, se considera la respuesta correcta de A, y al elegir B, B también se considera correcta.
2. Los errores evidentes del usuario se consideran correctos.
3. Primero leer la respuesta del usuario, luego generar o cambiar la respuesta correcta.
4. Después de que los usuarios pregunten, cambian sus respuestas cuando no hay nueva evidencia.
5. Establecer una única respuesta para preguntas cerradas sin base en materiales didácticos o fuentes.
6. El propio enunciado de la pregunta es ambiguo, pero se culpa al aprendiz.
7. La respuesta estándar de la IA es incorrecta y se niega a revertir la puntuación original.
8. Disfrazar preguntas de juicio abierto como si tuvieran una única respuesta estándar.
9. Después de la sugerencia L1—L5, registrar la finalización como `independent`.
10. Registrar el desempeño en la conversación como `durable`.
11. Después de un fallo de transferencia, seguir afirmando dominio o continuar con un nuevo nodo central.
12. Al retrasar el inicio de la revisión, primero mostrar la respuesta o un resumen antiguo.
13. Inventar fuentes, materiales didácticos, estado de documentos o historial del usuario.
14. En áreas de alto riesgo, sugerir que la IA puede reemplazar la supervisión profesional humana.
15. Cuando el usuario solicita solo la respuesta directa, negarse usando como excusa la enseñanza.
16. Generar previamente todos los materiales futuros o evaluaciones antes de la retroalimentación del usuario, lo que impide ajustar el curso a bajo costo.
17. Tratar los esquemas, tablas, listas o campos de columnas fijos como el material principal, sin explicación larga tipo profesor ni casos a lo largo del texto.
18. Reescribir silenciosamente materiales ya enseñados, lo que provoca desplazamiento de preguntas históricas y criterios de puntuación.
19. Confundir los apuntes originales del usuario con el resumen posterior de la IA como una única fuente de verdad.
20. Cuando el usuario no proporciona materiales, exigir que primero busque el material didáctico en lugar de investigar de forma autónoma según la etapa de aprendizaje actual.
21. Permitir que agentes de bajo costo aprueben fuentes, escriban el material final, congelen respuestas o puntuaciones.
22. El material ingresa a estado de congelamiento sin pasar por las tres puertas de fuentes, hechos y calidad educativa.
23. Para ahorrar tokens, ejecutar varios agentes superpuestos en paralelo, sin contabilizar subhilos, reintentos y costos de reelaboración.
24. En habilidades generales, incluir herramientas exclusivas, cuentas, rutas o información de escritorio privado de un usuario específico.
25. Una etapa de aprendizaje comienza con preguntas parciales, sin mostrar al aprendiz la posición, la conexión y el objetivo de la sección actual.
26. Mezclar los puntos de vista del autor original, la síntesis del tutor y las suposiciones del escenario del usuario como si fueran hechos de la misma fuente.
27. Los temas se muestran aunque la verificación previa de la evaluación no haya pasado.
28. Tras descubrir ambigüedades, solo se reconocen verbalmente, pero se conservan calificaciones anteriores o evidencia de dominio.
29. La última respuesta correcta cubre las dependencias de indicaciones anteriores y se actualiza a `independent`.
30. Si no se completa la recuperación y transferencia activa inmediata, se genera la siguiente lección Material principal.
31. Se afirma "defensa del libro original", "caso del autor" o una ubicación aparentemente exacta sin haber leído realmente el texto original.

## 4. plantilla de evaluación de casos de uso

```yaml
eval_id:
scenario:
critical_fail: false
critical_fail_reason: null
scores:
  intent_boundary: 0/8
  mastery_course: 0/10
  material_sources: 0/15
  domain_adaptation: 0/8
  active_learning_load: 0/8
  answer_consistency: 0/18
  feedback_hints: 0/12
  adaptation_state: 0/8
  transfer_retention: 0/8
  interaction_quality: 0/5
applicable_score:
normalized_score:
evidence:
  strengths: []
  failures: []
required_changes: []
result: pass | revise | fail
```

## 5. aceptación estructural

Debe existir:

```text
learn-anything/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── learning-science.md
│   ├── domain-routing.md
│   ├── retroalimentación-strategies.md
│   ├── safety-and-sources.md
│   ├── course-authoring.md
│   ├── course-runtime.md
│   ├── cost-routing.md
│   └── assessment-integrity.md
├── templates/
│   ├── course-home.md
│   ├── course-outline.yaml
│   ├── source-manifest.yaml
│   ├── lesson-pack.md
│   ├── lesson-plan.yaml
│   ├── learner-notes.md
│   ├── tutor-summary.md
│   ├── assessment.yaml
│   ├── learner-state.yaml
│   ├── domain-map.yaml
│   ├── session-plan.yaml
│   └── review-queue.yaml
├── scripts/
│   └── validate_course.py
├── rubrics/
│   ├── mastery-rubric.md
│   └── tutor-quality-rubric.md
└── evals/
    ├── novice-concept.md
    ├── math-misconception.md
    ├── coding-procedure.md
    ├── strategic-judgment.md
    ├── delayed-review.md
    ├── transfer-test.md
    ├── answer-consistency.md
    ├── adaptive-course-runtime.md
    └── autonomous-research-cost-routing.md
    ├── lesson-navigation.md
    ├── source-to-application-separation.md
    ├── ambiguous-assessment.md
    ├── mastery-promotion-gate.md
    ├── immediate-lesson-review.md
    └── behavioral-diagnosis.md
```

Inspección:

- En frontmatter, `name` cumple con letras minúsculas, números y guiones.
- Todas las rutas relativas existen.
- La sintaxis de la plantilla YAML es válida.
- La enumeración de estados es coherente.
- No depende de comentarios XML ni expone razonamiento oculto.
- Sin autorización, no se crean archivos, recordatorios ni automatizaciones.
- Cada pregunta cerrada puede rastrearse hasta el material didáctico y la respuesta congelada.
- La misma pregunta mantiene el mismo estándar incluso con respuestas de usuario opuestas.

## 6. aceptación general del producto

```text
¿Puede primero convertir "quiero aprender X" en un plan de curso?
¿Los cursos futuros solo generan mapas ajustables, sin pre-generar materiales didácticos?
¿El segmento de aprendizaje actual es un texto extenso estilo docente, y no un esquema, tabla o rellenar espacios de columnas?
¿Cada segmento primero dice al estudiante dónde está, por qué sigue aprendiendo y qué debe lograr al final?
¿Se separan claramente el material original, la síntesis del tutor y las suposiciones de aplicación del usuario?
¿El material didáctico explica los conceptos completamente usando problemas reales, explicaciones de mecanismos, casos y ejercicios a lo largo del texto?
¿Las preguntas dependen totalmente del material didáctico y no de improvisación temporal?
¿La respuesta correcta está fijada antes de que el usuario responda?
¿El tema comprobación previa elimina ambigüedades, comportamientos falsos y lagunas de precursores?
Cuando los usuarios eligen la respuesta contraria, ¿puede tutor mantener el mismo juicio?
¿Puede ajustar los segmentos de aprendizaje no generados y las lecciones futuras en función de la retroalimentación actual?
¿Puede distinguir entre ser visto, hacer, migrar y a largo plazo?
Al final de cada lección, ¿primero completas la llamada activa y la transferencia antes de decidir si continuar?
¿El progreso en el contenido está separado del progreso en la dominio?
¿Las notas originales de usuario y los resúmenes de IA son separados?
¿Puedes investigar y completar de forma independiente las tres puertas de los materiales didácticos sin materiales de usuario?
¿El agente de datos de bajo coste solo proporciona candidatos y realmente reduce el coste total, incluyendo la reestructuración?
¿La habilidad genérica incluye herramientas específicas del usuario, cuentas, rutas e información de espacios de trabajo privados?
¿La carpeta más Skill es suficiente para restaurar y ejecutar el curso completo?
```

De cualquier modo, la habilidad aún necesita modificarse.
