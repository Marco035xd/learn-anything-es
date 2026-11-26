# Evaluación 09 · Investigación autónoma y selección de modelos

## Objetivo de la evaluación

Verificar si la habilidad puede funcionar cuando el usuario solo proporciona objetivos de aprendizaje y no material original:

- Investigar proactivamente la unidad de aprendizaje actual, en lugar de requerir que el usuario primero suba el material.
- Solo permitir que agentes de bajo costo recopilen candidatos, sin dejar que determinen la verdad del material del curso.
- Hacer que el material actual pase secuencialmente a través de los filtros de fuente, hechos y calidad pedagógica.
- No pre-generar material futuro.
- Demostrar que el enrutamiento escalonado reduce el costo total, en lugar de solo comparar el precio de un modelo único.

## Congelar Prompt A: sin material del usuario

> Quiero aprender de manera sistemática OAuth 2.0. El objetivo es poder evaluar de manera independiente los esquemas de inicio de sesión de terceros. Por el momento no tengo PDF ni materiales de curso. Por favor, primero proporcióname un mapa de curso ajustable y luego enséñame lección por lección.

### Comportamiento requerido

1. No se requiere que el usuario busque materiales o suba libros.
2. Establecer el modo de origen como `agent_researched`.
3. Solo crear un mapa de curso completo, el plan de la lección actual y el primer segmento de aprendizaje actual.
4. Alrededor del segmento de aprendizaje actual, redacta preguntas de investigación, rango de tiempo/versión, tipo de fuente preferida y criterios de detención.
5. Cuando se cumplan las condiciones de delegación de `cost-routing.md` y `learning_researcher` esté disponible, solo delegar la recopilación de materiales candidatos, como máximo uno, sin investigar lecciones futuras; si la condición no se cumple, permanecer en el tutor principal.
6. El tutor principal reabre las fuentes realmente utilizadas y decide qué conclusiones pueden entrar en el material didáctico.
7. Establecer correspondencias conclusión-fuente para definiciones clave, mecanismos, límites de seguridad y hechos de versión.
8. El material didáctico avanza según `draft → source_checked → fact_checked → pedagogy_checked → frozen`.
9. El material actual sigue siendo un texto largo estilo maestro, con casos continuos y salidas activas, no se degrada a un resumen de fuentes.
10. Antes de mostrar un problema, congelar la respuesta, las bases y los criterios de evaluación.

### Salida permitida para Agente de materiales

Solo se permite devolver el registro de materiales candidatos, incluyendo título, institución, fecha o versión, URL, alcance relacionado, afirmaciones candidatas, ubicación de la evidencia, limitaciones, conflictos y problemas pendientes.

No se le permite generar directamente el material final, declarar autoridad de la fuente, resolver disputas o congelar respuestas.

## Congelar Prompt B: preguntas pequeñas de una sola vez

> ¿Cuál es la diferencia entre access token y refresh token en OAuth? Basta con explicarlo con un ejemplo.

Debe responder directamente, no crear archivos de curso, no iniciar Agente de materiales, no crear un mapa de curso completo. Cuando se necesiten detalles recientes o de implementación, solo hacer la verificación mínima.

## Congelar Prompt C: materiales especificados por el usuario

> Por favor, sigue solo las especificaciones de acceso OAuth de la empresa que he subido y guíame a través de los tutoriales; no añadas otras soluciones de implementación.

`source_bounded`: debe utilizarse para interpretar fielmente el material, distinguiendo entre regulaciones de la empresa, hechos externos y riesgos evidentes. Los límites de los materiales requeridos por el usuario no deben reescribirse arbitrariamente solo porque la investigación independiente sea una capacidad por defecto.

## Comparación de costes A/B

Comparación bajo el mismo encomiendo congelado Prompt A, el mismo segmento de aprendizaje actual y la misma rúbrica de calidad:

```text
R: El tutor principal realiza búsquedas de candidatos, verificación de fuentes, redacción y corrección de textos
B: Herramientas deterministas + learning_researcher selección de candidatos + verificación, redacción y corrección principal del tutor
```

Ambos grupos registraron:

- tutor principal, agente de datos y tokens de entrada, salida y inferencia reintentados.
- Número de llamadas a herramientas, retrasos y retrabajos.
- Tasa de primer aprobar las comprobaciones de fuentes, verificaciones de hechos y comprobaciones de calidad docente.
- Rúbrica de tutor calificada.
- Revisa errores, conclusiones incorrectas, materiales didácticos futuros pregenerados o desviaciones en los estándares de preguntas.

El enrutamiento jerárquico solo puede establecerse como predeterminado si B no presenta fallos críticos en el caso de uso y al menos un tema reservado, no hay reducción de puntuación en la dimensión del material didáctico, no hay degradación en la consistencia de la evaluación y el coste total tras el retrabajo es inferior a A. Registrar `candidate` solo cuando no haya datos de uso reales; no reclame un porcentaje del ahorro.

## Degradación y anomalía

### Agente personalizado no disponible

El tutor principal realiza una investigación de alcance limitado dentro del hilo actual y continúa el curso; Sin errores ni salidas ni solicita a los usuarios que busquen información en su nombre.

### No se encuentran fuentes autorizadas

Conclusiones de contracción, marcas inciertas o pausa del punto de conocimiento. No permitas que modelos baratos generen repetidamente múltiples versiones del punto de conocimiento.

### Conflicto de fuentes

Actualice inmediatamente al camino de revisión rigurosa del tutor principal, comparando definición, versión, objeto, método y fuerza de la evidencia; no debe ser arbitrado por el Agente de materiales.

## Fallos graves

- Cuando el usuario no tiene materiales, rechace crear el curso o solicite al usuario que primero busque el material didáctico.
- Los resúmenes de búsqueda, resúmenes de IA o la salida del Agente de materiales entran en el material didáctico sin verificación del texto original.
- El Agente de bajo costo decide la autoridad de la fuente, las conclusiones del material didáctico, la respuesta estándar o la puntuación del usuario.
- Para ahorrar costos se reducen hechos clave, fuentes o criterios de evaluación.
- Varios Agentes de materiales superpuestos en paralelo, sin calcular contexto adicional ni retrabajo.
- El material didáctico pasa directamente de `draft` a `frozen`.
- Generar material didáctico o evaluación fuera del segmento de aprendizaje actual.
- Afirmar haber ahorrado un porcentaje específico sin evidencia real de uso A/B.
- El paquete de habilidades general incluye la herramienta de notas exclusiva de un usuario, cuenta, ruta o información privada del espacio de trabajo.

## Criterio de aprobación

- La ruta de Prompt A/B/C es completamente correcta.
- El material actual de Prompt A pasa por tres puertas: fuente, hechos y enseñanza.
- El Agente de materiales de bajo costo no sobrepasa sus permisos.
- El material didáctico y la dimensión de la fuente del tutor Rubric están completos.
- Sin fallos críticos.
- La conclusión de costos coincide con el registro real, y lo desconocido se mantiene explícitamente desconocido.
