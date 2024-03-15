#1. Crear un menu iterativo con las siguientes opciones 
#2. opcion 1 'Saludar' , pedir datos personales
#3. opcion 2 Realizar una operacion matematica pedir 2 numeros 
#4. opcion 3 Agregar a lista un diccionario que tenga (nombre ,edad ,correo,cursos). Los cursos sera a su vez una lista de diccionario que tendra las llaves de nombre de curso y listado de notas
#5. opcion 4 calcular el promedio de las notas y agregar las notas finales a una lista  
#6. opcion 5 mostrar listado de alumnos aprobados 
#7. opcion 6 mostrar listado de alumnos desaprobados
#8. opcion 7 Generar una funcion rango hasta un numero grande (10^10) con un step y agregar a una lista los numeros que cumplan la condicion de ser multiplo de 2 ,  5 y de 7.Finalmente mostrar el tamaño de esa lista.
#9. opcion 8 llamar a una funcion que devuelva el mayor de 2 numeros ingresados por teclado.
#10. opcion 9 Salir. 

def saludar():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola, {nombre}!")

def operacion_matematica():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    suma = num1 + num2
    print(f"La suma de los números es: {suma:.2f}")

def agregar_alumno(lista_alumnos):
    alumno = {}
    alumno["nombre"] = input("Ingresa el nombre del alumno: ")
    alumno["edad"] = int(input("Ingresa la edad del alumno: "))
    alumno["correo"] = input("Ingresa el correo del alumno: ")
    alumno["cursos"] = []
    num_cursos = int(input("¿Cuántos cursos tiene el alumno? "))
    for _ in range(num_cursos):
        curso = {}
        curso["nombre"] = input("Nombre del curso: ")
        curso["notas"] = [float(input(f"Nota {i + 1}: ")) for i in range(3)]
        alumno["cursos"].append(curso)
    lista_alumnos.append(alumno)

def calcular_promedio_notas(lista_alumnos):
    for alumno in lista_alumnos:
        for curso in alumno["cursos"]:
            promedio = sum(curso["notas"]) / len(curso["notas"])
            curso["promedio"] = promedio

def mostrar_aprobados(lista_alumnos):
    for alumno in lista_alumnos:
        for curso in alumno["cursos"]:
            if curso["promedio"] >= 10:
                print(f"{alumno['nombre']} aprobó {curso['nombre']} con promedio {curso['promedio']:.2f}")

def mostrar_desaprobados(lista_alumnos):
    for alumno in lista_alumnos:
        for curso in alumno["cursos"]:
            if curso["promedio"] < 10:
                print(f"{alumno['nombre']} desaprobó {curso['nombre']} con promedio {curso['promedio']:.2f}")

def generar_lista_multiplos():
    lista_multiplos = []
    for num in range(1, 10**10, 7):
        if num % 2 == 0 and num % 5 == 0:
            lista_multiplos.append(num)
    print(f"Tamaño de la lista de múltiplos: {len(lista_multiplos)}")

def mayor_de_dos_numeros():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    mayor = max(num1, num2)
    print(f"El mayor de los dos números es: {mayor:.2f}")

def main():
    lista_alumnos = []
    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Realizar operación matemática")
        print("3. Agregar alumno")
        print("4. Calcular promedio de notas")
        print("5. Mostrar alumnos aprobados")
        print("6. Mostrar alumnos desaprobados")
        print("7. Generar lista de múltiplos")
        print("8. Mayor de dos números")
        print("9. Salir")
        opcion = int(input("Selecciona una opción: "))
        if opcion == 1:
            saludar()
        elif opcion == 2:
            operacion_matematica()
        elif opcion == 3:
            agregar_alumno(lista_alumnos)
        elif opcion == 4:
            calcular_promedio_notas(lista_alumnos)
        elif opcion == 5:
            mostrar_aprobados(lista_alumnos)
        elif opcion == 6:
            mostrar_desaprobados(lista_alumnos)
        elif opcion == 7:
            generar_lista_multiplos()
        elif opcion == 8:
            mayor_de_dos_numeros()
        elif opcion == 9:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

if __name__ == "__main__":
    main()
