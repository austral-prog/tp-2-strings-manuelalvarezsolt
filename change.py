def change():
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero = int(input())
    print(dinero)

    vuelto = round(dinero - gasto, 2)
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
