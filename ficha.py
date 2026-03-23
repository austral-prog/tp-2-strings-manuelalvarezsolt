def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass
    nombre = input()
    mail = input()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())
    print('''========================
    FICHA DEL ALUMNO
========================''')
    print(f"Nombre: {nombre.title().strip()}")
    print(f"Email: {mail.lower()}")
    print(f"Caracteres en nombre: {len(nombre)}")
    espacio = nombre.find(" ")
    print(f"Iniciales: {nombre[0].upper()}{nombre[espacio + 1].upper()}")
    print(f"Usuario: {nombre[espacio + 1 : ].lower()}.{nombre[0 : espacio].lower()}")
    print(f"Email valido: {'@' in mail}")
    arroba = mail.find("@")
    print(f"Dominio: {mail[arroba + 1 :]}")
    nombre2 = nombre.replace(" ", "_")
    print(f"Nombre para archivo {nombre2.title().strip()}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Codigo secreto: {nombre[::-1].upper()}")
    sumanotas = nota1 + nota2 + nota3
    promedio = sumanotas / 3
    promedioent = sumanotas // 3
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {sumanotas}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {int(promedioent)}")
    print("=" * 24)
