frase = input("Frase: ")

normalizado = frase.replace(" ", "").lower()

longitud = len(normalizado)
indice = 0
palindromo = True

if longitud == 0:
    print("Sin letras")
    print("Palíndromo: False")
else:
    while indice < longitud // 2:
        if normalizado[indice] != normalizado[longitud - 1 - indice]:
            palindromo = False

        indice += 1

    print("Normalizado:", normalizado)
    print("Palíndromo:", palindromo)