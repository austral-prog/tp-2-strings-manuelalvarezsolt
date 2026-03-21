def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input())
    descuento = float(input())
    cantidad = int(input())
    precio_descuento = precio - descuento
    precio_total = precio_descuento * cantidad
    print("\nPrecio: ", precio)
    print("Descuento: ", descuento)
    print("Precio con descuento: ", precio_descuento)
    print("Total: ", precio_total)
