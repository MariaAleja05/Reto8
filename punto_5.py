# -*- coding: utf-8 -*-
"""Punto_5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyLPKr76XsXXICfinr2kBoVhA43Up0iB

# **Quinto Punto**

**Enunciado:** Calcular el valor de 2 elevado a la potencia n usando ciclos for.
"""

n = int(input("Ingrese el número de la potencia: "))
potencia = 2

for i in range(n-1):
  potencia *= 2

print("El resultado es: " + str(potencia))