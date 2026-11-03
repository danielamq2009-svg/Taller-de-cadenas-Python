texto = input("Texto: ")
longitud = len(texto)

if 0 <= longitud <= 80:
    invertido = ""
    indice = longitud - 1

    while indice >= 0:
        invertido = invertido + texto[indice]
        indice = indice - 1

    print(invertido)