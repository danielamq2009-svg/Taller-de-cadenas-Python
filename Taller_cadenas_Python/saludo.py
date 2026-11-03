nombre = input("Ingrese su nombre: ")
if len(nombre) <= 40 and nombre == nombre.strip() and nombre != "":
    print(f"Hola , {nombre}!")
else: 
    print("Formato incorrecto")