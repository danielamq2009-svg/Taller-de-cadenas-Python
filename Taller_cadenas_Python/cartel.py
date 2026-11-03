frase = input("Frase: ")
longitud = len(frase)

if 0 <= longitud <= 100:
    mayusculas = frase.upper()
    contador = 0
    indice = 0
    while indice < longitud:
        if frase[indice].lower() in "aeiouáéíóúü":
            contador += 1
        indice = indice + 1
    print("Mayúsculas:", mayusculas)
    print("Vocales:", contador)