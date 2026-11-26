# Rúbrica de dominio

## Principios fundamentales

El dominio está determinado únicamente por evidencia observable. Las clases magistrales, los usuarios la entienden, se expresan con fluidez o responden correctamente a una pregunta de opción única no pueden por sí solos demostrar el dominio.

Cada decisión debe registrarse:

```yaml
node:
task:
result:
hint_level:
evidence:
misconceptions:
old_status:
new_status:
rationale:
```

Antes de cada cambio de estado, también se debe formar evidencia de promoción:

```yaml
node: ""
task: ""
grading_result: correct | partially_correct | incorrect | ungradable
hint_level: L0 | L1 | L2 | L3 | L4 | L5 | null
criteria_met: []
criteria_unmet: []
active_misconceptions: []
historical_highest_status: unknown
current_status: unknown
advance_allowed: false
promotion_blockers: []
```

Sin este formulario de evidencia, el estatus no puede ser mejorado; `ungradable` No se presenta evidencia positiva ni negativa.

## 1. Seis niveles de dominio

### 0. `unknown` · Sin evidencia

**Definición**: No hay evidencia fiable, o la evidencia existente se contradice entre sí.

Situaciones comunes:

- Aún no diagnosticado.
- Solo conocer el nivel autoproclamado del usuario.
- Las respuestas de los usuarios son insuficientes para juzgar.
- Los cambios en el conocimiento ascendente hacen que la evidencia antigua pierda sus premisas.

No puede escribirse como "No". `unknown` indica no reconocido.

### 1. `exposed` · Exposición

**Definición**: Los alumnos han visto, escuchado o pueden reconocer contenido pero aún no pueden recuperar o completar tareas de forma fiable.

Evidencia aceptable:

- Reconoce términos en las opciones.
- Sigue la explicación y cuéntalo de nuevo.
- Mira el ejemplo y señala las partes clave.

Situaciones en las que las mejoras son insuficientes:

- Simplemente di "Lo entiendo".
- Repite directamente frases que aún sean visibles en pantalla.
- La IA ya ha escrito la respuesta completa.

### 2. `guided` · Desempeño con ayuda

**Definición**: Capaz de completar con pistas, andamiajes, ejemplos o asistencia para corregir errores.

Evidencia aceptable:

- L1—L4 Completado tras la indicación.
- Pasos para completar las piezas que faltan.
- Modificar tareas similares según la demostración.
- Emita juicios razonables dentro de un marco claro.

Registrar la intensidad del prompt. Una alta finalización de prompt no puede empaquetarse como dominio independiente.

### 3. `independent` · Desempeño independiente

**Definición**: No hay indicaciones clave para completar una tarea representativa, y el proceso o la base son fiables.

Evidencia mínima:

- Las tareas cubren los requisitos básicos del nodo actual.
- La respuesta o producto no se copia directamente del ejemplo actualmente visible.
- No utilices pistas que determinen la respuesta.
- Los resultados son correctos o cumplen los criterios básicos de RUBRIC.
- No hay trampas clave ocultas.

Evidencia con mayor confianza:

- Dos éxitos independientes en diferentes formas superficiales.
- Capaz de explicar los pasos clave o la base del juicio.
- Capaz de realizar autocomprobaciones básicas o detectar errores.

Un único éxito independiente puede registrarse temporalmente como `independent`, pero debe indicarse la solidez de la evidencia; no se puede inferir estabilidad a largo plazo.

### 4. `transferable` · Transferencia

**Definición**: Capaz de identificar las condiciones aplicables, seleccionar métodos y completar tareas incluso en situaciones nuevas y cambiantes.

Debe incluirse al menos una variación:

- Cambios de escena.
- Cambios en la forma superficial.
- Aumentar la información sobre interferencias.
- Limitaciones o cambios en los objetivos.
- Es necesario combinar varios nodos.
- Solicite una explicación de cuándo no es aplicable.

Evidencia aceptable:

- Aplicación correcta en casos nuevos.
- Capaz de distinguir ejemplos de frontera de contraejemplos.
- Aplicar conocimientos a las propias tareas del mundo real.
- Explicar por qué los métodos antiguos necesitan ajustarse bajo nuevas condiciones.

Solo hacer variaciones de alto grado de similitud del tema original no es suficiente para demostrar una transferencia fuerte.

### 5. `durable` · Retención después de un intervalo

**Definición**: Después de un intervalo de tiempo coincidente con el objetivo, todavía se puede recordar o aplicar sin revisar previamente la respuesta.

Debe cumplir con:

- Existe un retraso real.
- La revisión inicia con extracción, sin repasar primero.
- La tarea alcanza el estándar requerido de independencia o transferencia.
- El modelo de errores no se repite de manera evidente.

`durable` no puede otorgarse en la primera sesión de aprendizaje.

## 2. Intensidad de la pista y límite de estado

| Nivel de pista | Explicación | Límite usual de evidencia de un solo intento |
|---|---|---|
| L0 | Solo se requiere autoevaluación | independent, se debe confirmar que la pista no revela puntos clave |
| L1 | Señalar la ubicación del error | guided |
| L2 | Recordar las reglas o criterios | guided |
| L3 | Proporcionar estructura parcial | guided |
| L4 | Demostrar pasos clave | guided |
| L5 | Respuesta completa | exposed; posteriormente se puede recolectar evidencia nuevamente con nueva variación |

Si la pista no afecta el núcleo de la respuesta, se puede explicar la razón y considerar una excepción, pero debe hacerse de manera conservadora.

Restricción adicional: después de L1—L4, la puntuación máxima usual es `guided`; después de la demostración completa L5, la puntuación máxima del tema original es `exposed`. Repetir el mismo tema original mientras la respuesta o la estructura clave aún son visibles no constituye evidencia independiente. La última vez que se responde correctamente no puede cubrir la dependencia de pistas previas del mismo nodo; se debe recolectar nueva evidencia con tareas representativas de respuestas no reveladas. Conclusión correcta pero fundamento decisivo incorrecto, se clasifica como `partially_correct`, no se puede actualizar el estado.

## 3. Evidencia de diferentes tipos de conocimiento

### Hechos (`Fact`)

- `independent`: extracción precisa sin pistas.
- `transferable`: reconocer, explicar o usar en contexto.
- `durable`: todavía puede extraerse después de un retraso.

### Conceptos (`Concept`)

- `independent`: explicar con palabras propias la relación central correctamente.
- `transferable`: Predecir nuevos casos, identificar límites y contraejemplos.
- `durable`: Puede explicar y aplicar incluso después de un retraso.

### Procedimientos (`Procedure`)

- `independent`: Completar tareas representativas sin pistas clave.
- `transferable`: Manejar nuevas variantes, anomalías o tareas de depuración.
- `durable`: Puede ejecutar de manera independiente incluso después de un retraso.

### Discriminación entre casos (`Discrimination`)

- `independent`: Clasificar correctamente y explicar pistas decisivas en casos mixtos.
- `transferable`: Manejar casos límite y nuevas formas de interferencia.
- `durable`: La capacidad de discernimiento se mantiene estable incluso después de un retraso.

### Juicio (`Judgment`)

- `independent`: Clarificar objetivos, restricciones, hechos, hipótesis y fundamentos, formando juicios defendibles.
- `transferable`: Reequilibrar en nuevos casos, explicando las condiciones de actualización.
- `durable`: Puede invocar el marco de juicio incluso después de un retraso, no solo recordar conclusiones.

### Creación (`Creative`)

- `independent`: Producir de manera independiente trabajos que cumplan con los estándares centrales.
- `transferable`: Mantener calidad relevante bajo nuevos temas o restricciones.
- `durable`: Puede invocar habilidades clave y autocorregirse incluso después de un retraso.

### Habilidades físicas o sociales (`Physical or Social`)

La evidencia dentro del chat solo puede apoyar la comprensión del conocimiento o la simulación de desempeño. Lo anterior bajo `independent` generalmente requiere desempeño real, grabaciones, evaluación humana o observación profesional.

## 4. situaciones que no se pueden considerar como evidencia de dominio

- El usuario dice “entendido”.
- El usuario repite la oración original escrita por la IA.
- La respuesta correcta aún se muestra en la pantalla.
- Acertar por azar en preguntas de opción múltiple sin poder explicar.
- La respuesta final es correcta pero el fundamento clave es incorrecto.
- La IA completó el razonamiento principal, código o trabajo.
- La tarea es demasiado simple y no cubre los requisitos centrales.
- El usuario memorizó la respuesta en la misma pregunta original.
- No hay retraso pero se marca como `durable`.
- La habilidad real solo tiene éxito en juegos de rol.

## 5. errores y cambios de estado

### Mejorar

Solo se mejora cuando aparece nueva evidencia superior al estado actual.

### Mantener

El rendimiento es coherente con el estado actual, pero la solidez de la evidencia puede aumentarse.

### Rebajado de categoría o marcado para consolidación

Cuando se producen las siguientes situaciones:

- Fallo de retirada retardada.
- Los malentendidos fundamentales se repiten.
- Las tareas antes independientes volvían a requerir indicaciones elevadas.
- Una tarea de transferencia revela que la comprensión se basa en características superficiales.

Notas recomendadas:

```yaml
status: guided
previous_highest_status: independent
downgrade_reason: delayed_retrieval_failure
```

No borres la evidencia histórica más elevada, pero el estado actual debe reflejar la realidad.

### No se puede determinar

Usa `unknown` o mantenlo tal cual cuando las tareas o la información sean insuficientes, sin forzar la calificación.

## 6. Calibración de confianza

Permite a los usuarios dar entre un 0 y un 100 % de confianza antes de tareas importantes.

| Rendimiento | Confianza | Procesamiento |
|---|---:|---|
| Correcto | Alto | Proceder con normalidad y realizar controles aleatorios de reubicación |
| Correcto | Bajo | Luego asigna tareas similares para ayudar a construir una confianza precisa |
| Error | Bajo | Corrige los errores normalmente para evitar más vergüenza |
| Error | Alto | Priorizar la exposición y corrección de modelos erróneos |

La confianza no consiste en dominar el nivel, sino que afecta a las estrategias de retroalimentación.

## 7. Criterio de avance por concepto

Responde antes de pasar al siguiente nodo:

1. ¿Qué nivel se requiere actualmente el objetivo?
2. ¿Ya hay pruebas correspondientes?
3. ¿Es el representante de la tarea?
4. ¿Cuántos niveles de indicaciones se usaron al completarlo?
5. ¿Existen conceptos erróneos fundamentales que aún no se hayan corregido?
6. Si avanzamos, ¿las partes inestables interrumpirán el aprendizaje futuro?

Los requisitos fundamentales suelen exigir como mínimo `independent`. Si la única evidencia independiente procede de un solo contexto y otros conceptos dependen de él, incluye una comprobación breve de transferencia antes de avanzar. Si falla, conserva la evidencia independiente histórica y refuerza el concepto. En proyectos de bajo riesgo se permite practicar en `guided` y se programan tareas de refuerzo.

El estado del nodo registra simultáneamente `historical_highest_status` y `current_status`. En caso de falla en la transferencia, recurrencia de errores o dependencia de indicaciones avanzadas nuevamente, no se eliminan las pruebas históricas, pero se debe reducir o bloquear el estado actual de manera veraz, y se debe indicar la razón en `promotion_blockers`. Solo `advance_allowed: true` puede acceder a nuevos contenidos centrales que dependan de este nodo.

## 8. Estándares de finalización de un objetivo de aprendizaje completo

Un curso o un objetivo de aprendizaje solo puede considerarse "completado actualmente" si cumple simultáneamente con las siguientes condiciones:

- Todos los nodos centrales alcanzan el estado objetivo.
- Se ha completado al menos una tarea independiente representativa.
- Se ha completado al menos una tarea de transferencia.
- Las ideas erróneas activas en el núcleo han sido eliminadas o marcadas claramente.
- Si el objetivo incluye memoria a largo plazo, se ha completado la revisión retardada.
- Si el objetivo incluye habilidades prácticas, existen evidencias de producción real o rendimiento externo.

Si aún no se ha realizado la revisión retardada, solo se puede decir "la comprensión inmediata ha sido verificada, la retención a largo plazo aún debe confirmarse".

## 9. Ejemplos de determinación

### Ejemplo 1: Resolver un problema siguiendo la fórmula

Estado: `guided`.

Razón: La elección de la fórmula y los pasos clave dependen de indicaciones visibles.

### Ejemplo 2: El usuario resuelve de manera independiente un problema nuevo, pero no puede explicar por qué

Estado: Se puede registrar provisionalmente `independent` con baja confianza, luego verificar mediante variaciones o según el problema.

### Ejemplo 3: El usuario aplica un marco en un nuevo caso comercial, pero omite conflictos de objetivos

Estado: Mantener `guided` o el estado original, no se considera transferencia exitosa. Los comentarios deben localizar las dimensiones faltantes en el marco de juicio.

### Ejemplo 4: Una semana después, primero recuerda, aún puede explicar y aplicar

Estado: Según la dificultad de la tarea, se puede actualizar a `durable`, registrando si se cumplen los requisitos de transferencia.
