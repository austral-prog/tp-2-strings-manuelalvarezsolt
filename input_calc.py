def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    pass
    base = int(input())
    altura = int(input())
    area = base * altura
    perimetro1 = base + altura
    perimetro = 2 * perimetro1
    print(f"base: {base}")
    print(f"altura: {altura}")
    print(f"area: {area}")
    print(f"perimetro: {perimetro}")
