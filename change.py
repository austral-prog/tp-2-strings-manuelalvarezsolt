def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    print("Ingresar gasto:")
    gasto = float(input())
    print("Dinero recibido")
    dinero = int(input())
    vuelto = dinero - gasto
    vuelto_entero = vuelto // 1
    print("Vuelto")
    print(f"Pesos:\n{int(vuelto_entero)}")
    vuelto_centavos1 = (vuelto - vuelto_entero) * 100
    vuelto_centavos = vuelto_centavos1 // 1
    print(f"Centavos:\n{int(vuelto_centavos)}")
