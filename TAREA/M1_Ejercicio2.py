# Realizar un programa que calcule el area y el perimetro de un poligono a tu eleccion( triangulo , cuadrado , circulo)

import math

# Solicitar la longitud del lado del cuadrado al usuario
lado = float(input("Ingresa la longitud del lado del cuadrado: "))

# Calcular el área y el perímetro
area = lado ** 2
perimetro = 4 * lado

# Mostrar los resultados
print(f"Área del cuadrado: {area:.2f} unidades cuadradas")
print(f"Perímetro del cuadrado: {perimetro:.2f} unidades")
