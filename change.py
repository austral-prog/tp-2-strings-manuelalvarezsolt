def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input())
    dinero = int(input())
    vuelto = dinero - gasto
    vuelto_entero = vuelto // 1
    print(f"pesos : \n{vuelto_entero}")
    vuelto_centavos1 = (vuelto - vuelto_entero) * 100
    vuelto_centavos = vuelto_centavos1 // 1
    print(f"centavos: \n{vuelto_centavos}")
