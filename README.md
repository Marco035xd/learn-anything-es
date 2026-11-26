# Learn Anything · por Nar

Learn Anything es una habilidad de tutoría adaptativa para Codex, Claude Code, Cursor y otros agentes compatibles. Convierte una meta de aprendizaje en un curso ajustable basado en fuentes. Combina práctica, retroalimentación, transferencia a otros contextos y repasos espaciados para comprobar si puedes usar lo aprendido por tu cuenta.

Esta es la edición en español de Learn Anything, creado por Nar / 那不然. Puedes usar, modificar y redistribuir el proyecto con la licencia MIT. Al redistribuirlo total o sustancialmente, conserva el aviso de derechos de autor y el texto de la licencia. [Repositorio original](https://github.com/Nar101/learn-anything)

## Elige cómo quieres aprender

Después de instalar la habilidad, describe tu objetivo con tus propias palabras.

### Ya tienes material de estudio

Sube un PDF, un artículo, apuntes de clase, una transcripción o tus propias notas. También puedes compartir un enlace accesible. El tutor se ciñe al material, explica lo que dice y lo conecta con tu caso de uso.

```text
Usa learn-anything para estudiar de forma sistemática el PDF que subí.
Quiero poder aplicar sus métodos por mi cuenta en casos reales.
Muéstrame primero la estructura del material y el plan de estudio.
Luego enséñame un solo segmento de la lección a la vez.
```

Si el material es largo, el tutor lee las secciones necesarias para la lección actual.

### Partes de un objetivo

Cuéntale al tutor qué quieres aprender y dónde lo aplicarás. El tutor busca fuentes fiables para la lección actual y propone un plan de estudio.

```text
Usa learn-anything para enseñarme OAuth 2.0 desde cero.
Quiero poder revisar por mi cuenta un diseño de inicio de sesión con un tercero.
Busca fuentes fiables para la lección actual.
```

### Ya estudiaste el tema y quieres ponerte a prueba

```text
Usa learn-anything para comprobar si entiendo el costo de oportunidad.
Dame un caso realista y espera mi respuesta antes de explicarme la solución.
Decide a partir de mi respuesta si necesito repasar.
```

### Quieres retomar un curso

Si ya guardaste el estado del curso, puedes decir:

```text
Retoma mi curso anterior.
Primero revisa si tengo repasos pendientes.
Luego sigue desde donde me quedé o desde el primer concepto que aún no domino.
```

## Instalación rápida

```bash
npx skills add Marco035xd/learn-anything-es
```

Por ejemplo, puedes pedirle a tu agente:

```text
Subí material de estudio. Usa learn-anything para ayudarme a dominarlo.
Propón un plan de estudio ajustable y enséñame un segmento a la vez.
```

## Cómo funciona

- Si aportas materiales, el tutor distingue lo que sostiene la fuente, su propia síntesis y las hipótesis sobre cómo aplicarlo a tu caso.
- Si partes de un objetivo, el tutor investiga lo necesario para el segmento actual.
- El tutor fija la respuesta esperada o la rúbrica antes de que respondas.
- Cada actividad aporta evidencia de lo que puedes hacer con pistas, de forma independiente, en otro contexto o después de un tiempo.
- Si persiste un error conceptual fundamental, el siguiente paso es reforzarlo.

```text
Objetivo → criterios de dominio → plan de estudio ajustable
→ preparación de la lección actual → explicación basada en fuentes
→ aplicación a tu contexto → evaluación con criterios prefijados
→ retroalimentación y reintento → recuerdo inmediato y transferencia
→ repaso diferido
```

El protocolo completo está en [SKILL.md](./SKILL.md).

## Instalación manual

Clona el repositorio completo en un directorio de habilidades al que tu agente tenga acceso. También puedes copiarlo a la carpeta `.agents/skills/learn-anything/` de tu proyecto. La habilidad necesita sus plantillas, rúbricas y validador además de `SKILL.md`.

La habilidad sigue la estructura de Agent Skills. Si el entorno carece de permisos de escritura, el protocolo funciona durante la conversación actual. Retomar un curso en otra sesión requiere acceso a los archivos donde se guardó el estado.

## Validación

Comprueba la estructura de la habilidad con el validador de `skill-creator`:

```bash
python3 /ruta/a/skill-creator/scripts/quick_validate.py .
```

Instala PyYAML y ejecuta las pruebas de regresión del validador:

```bash
python3 -m pip install PyYAML
python3 -B scripts/test_validate_course.py
```

Valida un curso guardado:

```bash
python3 -B scripts/validate_course.py /ruta/al/curso
```

## Alcance de la tutoría

- Las preguntas puntuales reciben una respuesta directa.
- El tutor prepara las lecciones a medida que avanza el curso.
- El dominio se acredita con tareas observables.
- La práctica en ámbitos de alto riesgo requiere la supervisión adecuada para trasladarla a la realidad.
- El tutor atribuye afirmaciones a sus autores cuando ha podido consultar la fuente.

## Autoría y licencia

Nar / 那不然 creó Learn Anything para explorar cómo la IA puede participar en el aprendizaje, el razonamiento y el trabajo. [Autor](https://github.com/Nar101) · [Proyecto original](https://github.com/Nar101/learn-anything) · [Licencia MIT](./LICENSE)
