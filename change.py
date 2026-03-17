def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)
    print("Dinero recibido")
    dinero = int(input())
    print(dinero)
    vuelto = dinero - gasto
    vuelto_entero = vuelto // 1
    print("\nVuelto\n")
    print(f"Pesos:\n{int(vuelto_entero)}")
    vuelto_centavos = (vuelto - vuelto_entero) * 100
    print(f"Centavos:\n{int(vuelto_centavos)}")
