from http.cookiejar import uppercase_escaped_char


def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass
    nombre = input("cual es tu nombre")
    print(f"{nombre.lower()}")
    print(f"{nombre.upper()}")
    print(f"{nombre.title()}")
    print(f"\t{nombre}")
