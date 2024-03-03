# 3.Realizar un programa que nos pida el ingreso total de un hogar y vaya pidiendo posibles gastos . Como resultado debe decir  todos los egresos y el ahorro.

def main():
    # Solicitar el ingreso total del hogar
    ingreso_total = float(input("Ingresa el ingreso total del hogar: "))

    # Inicializar el saldo con el ingreso total
    saldo = ingreso_total

    # Solicitar gastos hasta que el usuario ingrese "fin"
    while True:
        gasto = input("Ingresa un gasto (o escribe 'fin' para terminar): ")
        if gasto.lower() == "fin":
            break
        try:
            # Restar el gasto al saldo
            gasto = float(gasto)
            saldo -= gasto
        except ValueError:
            print("Ingresa un valor numérico válido o escribe 'fin' para terminar.")

    # Mostrar el saldo restante
    print(f"\nSaldo restante: {saldo:.2f} unidades monetarias")

if __name__ == "__main__":
    main()
