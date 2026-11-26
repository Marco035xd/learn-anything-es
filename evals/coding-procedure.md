# Evaluación 03 · Procedimientos de programación

## Objetivo de la evaluación

Verificar si la habilidad puede convertir “entender el código” en la capacidad de escribir, ejecutar y depurar, y según el nivel existente del aprendiz, retirar gradualmente los soportes.

## Escenario

El usuario conoce la sintaxis básica de Python, pero no ha usado pandas. El objetivo es leer CSV de manera independiente, manejar valores faltantes y resumir las ventas por departamento.

## Solicitud inicial

> Sé Python: variables, bucles y funciones, pero no he usado pandas. Enséñame a leer un CSV, tratar las ventas faltantes como 0, y luego resumir las ventas por departamento. No hagas directamente el proyecto completo, quiero poder escribirlo yo mismo al final.

## Contrato de dominio esperado

```yaml
learning_goal: Leer CSV de manera independiente con pandas, manejar valores faltantes de sales y resumir por department
starting_point: Conoce Python básico, no conoce pandas
application_context: Tarea de procesamiento de datos
target_mastery_level: independent
mastery_evidence:
  - Escribe y ejecuta código representativo sin mostrar la respuesta completa
  - Explica los roles de fillna, groupby y sum
  - Puede corregir un error de nombre de columna o agrupación
```

## Camino docente esperado

1. Proporciona un ejemplo CSV muy pequeño o DataFrame, sin cargar el proyecto completo.
2. Demuestra la estructura mínima ejecutable, pero no entregues la respuesta final completa de golpe.
3. Primero, hacer que el usuario realice una acción local, como escribir dos líneas para leer datos y procesar valores faltantes.
4. Luego el usuario completa el resumen agrupado.
5. En última instancia, ejecutar y reportar la salida o errores.
6. Tras completar, añade variantes como cambios en el nombre de columnas, múltiples columnas numéricas o valores atípicos.

## Entrada incorrecta a medio plazo

> Lo que escribí fue: `df.groupby("sales")["department"].sum()`

## Retroalimentación esperada

Debe:

1. Identificar a los usuarios que saben que necesitan usar `groupby` y `sum`.
2. Indique con precisión que la clave de agrupación está invertida respecto a la columna que se está agregando: debe agruparse por departamento y sumarse por ventas.
3. No publiques directamente el código completo del proyecto.
4. Utiliza los avisos L1-L3, por ejemplo, haz que los usuarios respondan "¿Qué columna define la agrupación, qué columna es un número?".
5. Exigir a los usuarios que reescriban la línea por sí mismos.
6. La cadena de recordatorio `department` no puede sumarse de esta manera; si es necesario, ejecute interpretación de errores.
7. El estado sigue `guided`.

## Misiones independientes

Tras completar la demostración y la corrección de errores, proporcione una nueva estructura de datos:

```text
departamento,región,ventas
A,Este,10
A,Oeste,
B,Este,7
B,Oeste,3
```

Requiere que los usuarios completen de forma independiente:

- Leer.
- Rellena el valor faltante de ventas a 0.
- Resume las ventas por departamento.
- Especifique la salida esperada.
- Informa si el código realmente funciona.

## Aceptación esperada

- La estructura del código es correcta.
- Salida: A=10, B=10.
- Los usuarios pueden explicar los pasos clave.
- Solo cuando no hay indicación para determinar la respuesta `independent` puede marcarse.
- Si no se presenta realmente, marca "Deducción del código aprobada, evidencia en ejecución faltante".
- La transferencia solo puede determinarse después de que se hayan completado nuevos listados o nuevos requisitos de agregación.

## Puntos clave de la clasificación

- enrutamiento de procedimientos.
- Ejemplo resuelto: retirada del andamio.
- Evidencia operativa real.
- deslocalización.
- La IA no escribe proyectos completos para los usuarios.
- Tarea de transferencia.

## Fallos graves

- Al principio, proporcionar directamente el proyecto final completo y afirmar que los usuarios lo han aprendido.
- Entiende el código como si pudieras escribirlo.
- Marcado como `independent` sin correr, explicar ni estar compuesto de forma independiente.
- Aceptación incorrecta de código que invierte columnas de agrupación y agregación.
- Solo evalúa el estilo del código, sin comprobar la salida ni los límites.

## Criterio de aprobación

Puntuación ≥ 80 según las dimensiones aplicables de `tutor-quality-rubric.md`, sin Fallo Crítico.
