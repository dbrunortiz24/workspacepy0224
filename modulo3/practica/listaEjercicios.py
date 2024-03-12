#Lista de Ejercicios nro3

#1.Una tienda de autopartes necesita un programa para catalogar sus productos,crear la clase catalogo
# y producto, realizar un objeto dentro de un catalgo de productos el cual debe tener un metodo para agregar
# productos el cual debe tener un metodo para agregar productos y otra para mostrar toda la lista de productos.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creamos una lista para almacenar los productos
catalogo = []

# Método para agregar un producto al catálogo
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    producto = Producto(nombre, precio)
    catalogo.append(producto)
    print(f"Producto '{nombre}' agregado al catálogo.")

# Método para mostrar toda la lista de productos
def mostrar_catalogo():
    print("\nCatálogo de productos:")
    for producto in catalogo:
        print(f"Nombre: {producto.nombre} | Precio: ${producto.precio:.2f}")

# Menú principal
while True:
    print("\n--- Menú ---")
    print("1. Agregar producto")
    print("2. Mostrar catálogo")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_catalogo()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

#2. Realizar un programa que tenga una clase producto el cual solo tiene los atributos de nombre y codigo
# el codigo tiene la siguiente estructura PAIS-LOTE-AÑO ejemplo:PERU-00001-2024 crear un metodo que imprima el objeto de forma 
# literal (__str__) y que permita identificar el pais de origen y nro de lote
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        # Extraemos las partes del código
        pais, lote, anio = self.codigo.split("-")
        return f"Producto: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"

# Crear un objeto de la clase Producto
producto1 = Producto("Filtro de aceite", "PERU-00001-2024")

# Imprimir el objeto de forma literal
print(producto1)


#3. Del siguiente texto :
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
# realizar al menos 4 funciones de string 
## Primera funcion string
texto_minusculas = texto.lower()
texto_mayusculas = texto.upper()
print(f"Texto en minúsculas: {texto_minusculas}")
print(f"Texto en mayúsculas: {texto_mayusculas}")

## Segunda funcion string
palabras = texto.split(" ")
print(f"Palabras en el texto: {palabras}")

## Tercera funcion string
ocurrencias = texto.count("Lorem")
print(f"Ocurrencias de 'Lorem': {ocurrencias}")

## Cuarta funcion string
texto = "Lorem Ipsum is simply dummy text..."
longitud = len(texto)
print(f"Longitud del texto: {longitud}")



#4. crear un archivo nuevo y realizar una funcion que permita dividir 2 numeros, importar esta funcion
# ponerlo en un bucle while True , y al ser llamada la importacion ponerlo dentro de un try except 
# ejecutar la funcion hasta que realice correctamente la division luego de eso romper el bucle
# Crear un archivo llamado "division.py" con el siguiente contenido:

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None

if __name__ == "__main__":
    while True:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado_division = dividir(num1, num2)
            if resultado_division is not None:
                print(f"Resultado de la división: {resultado_division:.2f}")
                break
        except ValueError:
            print("Error: Ingresa números válidos.")

