# Calculadora Termodinámica: Ley de Hess y Kirchhoff

Este proyecto es una herramienta de línea de comandos desarrollada en Python para resolver ejercicios de termodinámica, específicamente enfocados en el cálculo de la entalpía de reacción, el calor transferido (Q), el trabajo (W) y el cambio de energía interna (Delta U).

Fue creado como parte de la asignatura de **Fundamentos de Conversión Energética** para automatizar los cálculos de la Ley de Hess y la Ley de Kirchhoff.

## 🚀 Características

*   **Ley de Hess:** Calcula la entalpía de reacción estándar (298.15K) a partir de las entalpías de formación de múltiples reactivos y productos.
*   **Ley de Kirchhoff (Polinómica):** Calcula la entalpía de reacción a una temperatura diferente (T_2) integrando las capacidades caloríficas (C_p) expresadas como polinomios (a + bT + cT^-2).
*   **Primera Ley de la Termodinámica:** Calcula automáticamente el Calor (Q), el Trabajo (W) y la Energía Interna (Delta U) para sistemas cerrados a presión constante.
*   **Manejo de estados:** Identifica si las sustancias son gases o líquidos/sólidos para calcular correctamente el cambio de moles de gas (Delta n) y el trabajo de expansión/compresión.
*   **Convención de signos IUPAC:** Utiliza la convención donde el trabajo realizado *por* el sistema es positivo (W = P\Delta V).

💻 ¿Cómo usarlo?

**************************************************************************
** puedes copiar el código y correrlo en https://pythoncompiler.io/ ******
**************************************************************************

El programa te guiará paso a paso. Te pedirá:

- La cantidad de reactivos y productos.

- Los datos de cada sustancia (coeficiente estequiométrico, entalpía de formación estándar y si es gas).

- Los coeficientes (a,b,ca,b,c) de la capacidad calorífica.

- La temperatura final (si aplica usar Kirchhoff).

EJEMPLO : A continuación se muestra cómo se vería la consola al resolver el ejercicio de combustión del propano a 25∘C:

=========================================
   CALCULADORA TERMODINÁMICA (Hess y Kirchhoff)
=========================================

¿Cuántos REACTIVOS hay en la reacción? 2
Datos del REACTIVO 1:
Nombre: Propano
Coeficiente estequiométrico: 1
Entalpía de formación estándar (kJ/mol): -103.8
¿Es un GAS? (s/n): s
...

========================================
               RESULTADOS FINALES
========================================
Temperatura de cálculo: 298.15 K
Variación de moles de gas (Delta n): -3.0
Calor (Q): -2219.90 kJ/mol
Trabajo (W): -7.4365 kJ/mol
Energía Interna (Delta U): -2212.46 kJ/mol
========================================


👨‍🎓 Autor
Mariana Atenais Campos García

Maestría y Doctorado en Ciencia y Tecnología para la Transición Energética

Instituto Politécnico Nacional

Asignatura: Fundamentos de Conversión Energética
Dra. Violeta Yasmin Mena Cervante
