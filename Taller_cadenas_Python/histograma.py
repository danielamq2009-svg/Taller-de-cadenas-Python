texto = input("Texto: ")

texto = texto.lower()

frecuencias = {}

for letra in texto:
    if letra != " ":
        if letra in frecuencias:
            frecuencias[letra] += 1
        else:
            frecuencias[letra] = 1

total = 0
mayor = 0
mas_frecuente = "ninguna"

for letra in frecuencias:
    frecuencia = frecuencias[letra]

    print(letra + ": " + str(frecuencia) + " " + "*" * frecuencia)

    total += frecuencia

    if frecuencia > mayor:
        mayor = frecuencia
        mas_frecuente = letra

print("Total:", total, end="; ")
print("Distintas:", len(frecuencias), end="; ")
print("Más frecuente:", mas_frecuente)