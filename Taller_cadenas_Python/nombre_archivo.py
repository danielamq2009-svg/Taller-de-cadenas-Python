base = input("Base: ")
if 1 <= len(base) <= 30 and base.replace("_", "").isalnum() and base.isascii():
    longitud = len(base)
    nombre_extension = base + ".txt"
    print(f"Longitud de la base: {longitud}; Nombre completo: {nombre_extension}")
