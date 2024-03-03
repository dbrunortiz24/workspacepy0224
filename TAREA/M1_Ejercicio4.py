# 4.Realizar un programa que filtre si eres apto para registrar un negocio ,condiciones: mayor de edad , tener ruc y tener un nombre comercial ,los inputs son si y /o no . la salida debe ser si esta apto o no para abrir un comercio.

def verificar_apto_para_negocio():
    # Solicitar respuestas del usuario
    mayor_edad = input("¿Eres mayor de edad? (si/no): ").lower()
    tiene_ruc = input("¿Tienes RUC? (si/no): ").lower()
    tiene_nombre_comercial = input("¿Tienes un nombre comercial? (si/no): ").lower()

    # Verificar las condiciones
    if mayor_edad == "si" and tiene_ruc == "si" and tiene_nombre_comercial == "si":
        print("¡Estás apto para abrir un comercio!")
    else:
        print("No cumples con todas las condiciones para abrir un negocio.")

if __name__ == "__main__":
    verificar_apto_para_negocio()
