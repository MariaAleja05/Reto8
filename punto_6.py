# -*- coding: utf-8 -*-
"""Punto_6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

##**Punto 6**

**Enunciado:** Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.
"""

n = int(input("Ingrese un número natural: "))
x = float(input("Ingrese un número real: "))
operacion = 1

for i in range(n-1):
  operacion *= x

print("El resultado es: " + str(operacion))