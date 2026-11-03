reservada = input("Reservada: ").strip().lower()
n = int(input("Canidad de mensajes: "))

validos = 0
invalidos = 0
total_palabras = 0
total_sustituciones = 0
mayor_cantidad = 0
mensaje_mayor = 0

for numero in range(1, n + 1):
    mensaje = input(f"Ingresa el mensaje {numero}: ").strip()

    # Los signos funcionan como separadores, igual que los espacios.
    texto = mensaje.lower()
    texto = texto.replace(".", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")

    palabras = texto.split()

    if len(palabras) == 0:
        invalidos += 1
        print(f"{numero}: Inválido")
    else:
        validos += 1
        cantidad = len(palabras)
        sustituciones = palabras.count(reservada)

        editadas = []
        for palabra in palabras:
            if palabra == reservada:
                editadas.append("[oculto]")
            else:
                editadas.append(palabra)

        texto_editado = " ".join(editadas)

        total_palabras += cantidad
        total_sustituciones += sustituciones

        if cantidad > mayor_cantidad:
            mayor_cantidad = cantidad
            mensaje_mayor = numero

        print(
            f'{numero}: "{texto_editado}"; '
            f"Palabras: {cantidad}; Sustituciones: {sustituciones}"
        )

if total_palabras > 0:
    porcentaje = 100 * total_sustituciones / total_palabras
else:
    porcentaje = 0

porcentaje_texto = f"{porcentaje:.2f}".replace(".", ",")

print(
    f"Válidos: {validos}; Inválidos: {invalidos}; "
    f"Palabras: {total_palabras}; Sustituciones: {total_sustituciones}; "
    f"Porcentaje: {porcentaje_texto} %; "
    f"Más palabras: mensaje {mensaje_mayor}"
)