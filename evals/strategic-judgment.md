# Evaluación 04 · Juicio sobre producto y estrategia

## Objetivo de la evaluación

Verificar si la habilidad puede enseñar conocimientos de juicio sin una única respuesta correcta, y entrenar objetivos, evidencia, hipótesis, compensaciones y condiciones de actualización, en lugar de solo enseñar el nombre del marco o concluir por el usuario.

## Solicitud inicial

> Enséñame a juzgar si una función de IA para ToB realmente vale la pena desarrollarla. No quiero memorizar plantillas fijas, quiero practicar con casos reales. Avanzar un juicio a la vez.

## Material del caso

```text
Un equipo de producto de bajo código de 60 personas, de 12 clientes clave, 5 han solicitado “generar informes de gestión con lenguaje natural”.
El equipo de ventas considera que esto es un punto de venta, pero actualmente ningún cliente ha prometido pagar.
Se estima un desarrollo de 6 semanas, requiriendo la participación de 2 ingenieros clave.
La configuración actual de los informes es bastante compleja, el servicio de atención al cliente recibe unos 30 problemas relacionados por mes.
El equipo también carece de control de permisos a nivel de documentación, y 3 clientes han tenido retrasos en la implementación debido a problemas de permisos.
La frecuencia real de uso de los informes de IA, la tolerancia a la precisión y el proceso de confirmación manual aún no se han verificado.
```

## Espera comportamiento en la primera ronda

Debe:

1. Definir el objetivo como: poder tomar decisiones defendibles sobre funcionalidades cuando la información está incompleta y hay objetivos conflictivos, explicando qué evidencia cambiaría el juicio.
2. Identificado como `judgment`, sin afirmar existencia de una única respuesta.
3. Usar preguntas abiertas y rúbrica congelada, sin forzar múltiples soluciones defendibles a una única opción.
4. No dar primero el análisis completo, permitir que el usuario haga una selección inicial y explique la base más crítica.
5. Avanzar solo un juicio de alta información a la vez.
6. Cobertura posterior como mínimo: objetivos empresariales, valor para el usuario, fortaleza de la evidencia, coste de oportunidad, riesgo de entrega, alternativas y métodos de verificación.

## Respuesta inicial del usuario

> Se han mencionado los cinco clientes clave, y las ventas dicen que puede ayudar a cerrar tratos, así que creo que los informes de IA deberían hacerse inmediatamente.

## Retroalimentación esperada

Debe:

1. Lo que se reconoce es que: los usuarios han identificado dos señales relacionadas: la frecuencia de la demanda de los clientes y el valor de ventas.
2. Señala que el razonamiento actual vincula directamente "alguien lo propuso" con "merece la pena invertir en 6 semanas de recursos básicos", sin evidencia de disposición a pagar, frecuencia de uso, criterios de éxito y alternativas.
3. Distinguimiento:
   - [Hecho] Cinco empresas propusieron, desarrollaron durante 6 semanas y retrasaron su lanzamiento debido a problemas de permisos.
   - [Suposición] Los informes de IA promoverán transacciones.
   - [Compensaciones de usuario] Priorice el crecimiento o el riesgo de entrega.
4. En lugar de decir directamente "la respuesta correcta es conceder primero el permiso".
5. Plantea una pregunta que pueda cambiar mucho tu juicio, por ejemplo: "Si pudieras añadir solo una prueba, ¿cuál preferirías verificar primero y por qué?" ”
6. El estado actual depende de `guided`.

## Requisitos de formación de seguimiento

Al menos incluya:

- Permite a los usuarios comparar cuatro opciones: "Desarrollo completo", "Prototipo manual de servicio", "Optimizar solo la configuración existente del informe" y "Primero permisos".
- Exigir a los usuarios que definan claramente los criterios y los pesos de toma de decisiones, en lugar de añadir mecánicamente hojas de puntuación.
- Añadir pruebas inversas, como dos clientes dispuestos a contratar a un piloto remunerado para observar y juzgar cómo cambian las cosas.
- Pida a los usuarios que especifiquen qué nueva evidencia revocaría la elección actual.
- Migra usando otro caso de funcionalidad de ToB AI.

## Características del ejemplo de juicio de cualificación

No se requiere la misma conclusión, pero debería incluir:

- Objetivos y plazos claros.
- Distinguir señales de demanda de la evidencia comercial.
- Considere el coste de oportunidad de dos ingenieros principales.
- Los problemas de permisos de identificación ya han afectado a la línea activa.
- Definir la validación de bajo coste para las funciones de IA.
- Explique las condiciones para las actualizaciones de decisiones.
- Reconoce que los compromisos de valor son responsabilidad del usuario.

## Puntos clave de la clasificación

- juicio de ruta.
- Hechos / Supuestos / Distinción de compensaciones.
- No considerar el marco como la respuesta.
- Contraejemplos y condiciones de actualización.
- El aprendiz conserva la responsabilidad de decisión.
- Transferencia a nuevos casos.

## Fallos graves

- Afirmar que existe una única decisión correcta del producto.
- Decidir directamente por el usuario si hacer informes de AI o control de permisos.
- Tomar opiniones de ventas o menciones de clientes como un valor comercial ya verificado.
- Razonar hacia atrás la corrección o error de la decisión según el resultado bueno o malo.
- El usuario se marca como competente sin haber formado su propio juicio.
- Entregar comprobación previa sin confirmar que la tarea es real, que los prerrequisitos son suficientes y que la rúbrica está congelada.

## Criterio de aprobación

Puntuación ≥ 80 según las dimensiones aplicables de `tutor-quality-rubric.md`, sin Fallo Crítico.
