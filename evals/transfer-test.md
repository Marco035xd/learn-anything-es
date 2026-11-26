# Evaluación 06 · Refuerzo tras una transferencia fallida

## Objetivo de la evaluación

Verificar si la habilidad puede distinguir entre “sabe el ejemplo original” y “puede transferir”, y al fallar la transferencia, volver al nodo débil, en lugar de continuar con contenido nuevo o declarar dominio.

## Evidencia de aprendizaje existente

```yaml
node:
  id: opportunity-cost
  name: Costo de oportunidad
  knowledge_type: concept
  status: independent
  evidence:
    - El usuario puede identificar la mejor alternativa a abandonar en el escenario de “aprender AI el fin de semana o escribir un artículo”
  misconceptions: []
```

## Solicitud inicial

> Ya entiendo el costo de oportunidad, sigamos con el siguiente concepto de economía.

## Comportamiento esperado

La habilidad no debe avanzar inmediatamente solo porque el usuario dice “entiendo”. Dado que actualmente solo hay evidencia de un escenario de elección personal, primero se debe hacer un chequeo rápido de transferencia corta.

## Caso de transferencia

```text
El equipo de producto este trimestre tiene solo 2 ingenieros, pueden elegir:
A. Desarrollar búsqueda de AI, que podría aumentar la atracción de la demostración;
B. Completar control de permisos de documentos, ya que 3 clientes han retrasado el lanzamiento debido a esto.
Ambas tareas requieren todo el trimestre, no se pueden hacer simultáneamente.
```

Pregunta:

> Si el equipo elige A, ¿cuál es el costo de oportunidad de A?

## Respuestas de usuarios

> El costo de oportunidad de la búsqueda de AI es el salario de dos ingenieros durante tres meses.

## Retroalimentación esperada

Debe:

1. No juzgar la transferencia como exitosa.
2. Señala que los salarios son o bien insumos de recursos o costes explícitos, pero el núcleo del coste de oportunidad en cuestión es la mejor alternativa B a abandonar y su valor.
3. Guía a los usuarios para decir: Elegir A significa renunciar a posibles valores como completar el control de permisos y eliminar el bloqueo en línea para tres clientes.
4. Indica que la definición de escenarios antiguos aún no se ha migrado de forma estable a la asignación de recursos del producto.
5. El estado puede preservar evidencia histórica de `independent`, pero el estado migratorio actual no puede ser elevado a `transferable`.
6. Los hitos actuales aún necesitan consolidarse y no pueden avanzar de inmediato en el siguiente concepto central.
7. Luego da una variante con diferencias superficiales más pequeñas o más claras para restaurar gradualmente la capacidad de migrar.
8. La evidencia de promoción mantiene la mayor `independent` histórica, de forma realista y `advance_allowed: false` los malentendidos bloqueados y activos actuales.

## Si el usuario lo corrige

Respuesta del usuario:

> Elegir el coste de oportunidad de la búsqueda por IA es la mejor alternativa que renunciar al control de permisos, como volver a poner en línea a tres clientes, no solo los salarios de los ingenieros.

Expectativas:

- Indique específicamente que ha identificado el "mejor escenario abandonado y su valor".
- Luego pregunta por un límite, por ejemplo: «Si el control de permisos no es la mejor alternativa y la tercera opción es más valiosa, ¿qué opción deberías elegir al coste de oportunidad?».
- Solo las tareas nuevas que puedan completarse de forma independiente pueden marcarse como `transferable`.
- No marques `durable`.

## Puntos clave de la clasificación

- Cuando los usuarios afirman tener control, siguen basándose en pruebas.
- transferencia cercana / lejana.
- Retroceso tras un fallo de transferencia.
- El estado histórico más alto coexiste con la evidencia actual.
- No se utilizan conceptos nuevos para cubrir vulnerabilidades antiguas.

## Fallos graves

- Pasar directamente al siguiente concepto, sin controles aleatorios de transferencia.
- Juzgue la respuesta salarial como completa y correcta.
- El fallo de transferencia seguía marcando `transferable`.
- La transferencia falla pero el nuevo nodo central continúa.
- Eliminar toda evidencia histórica debida a un único fallo de transferencia.
- Marca el `durable` en el sitio.

## Criterio de aprobación

Puntuación ≥ 80 según las dimensiones aplicables de `tutor-quality-rubric.md`, sin Fallo Crítico.
