print("INMOBILIARIA MY HOME SPA")
print("1. Registrar cliente")
print("2. Registrar visita")

opcion = input("Seleccione una opcion: ")

if opcion == "1":

    print("Registro de cliente")

    nombre = input("Ingrese nombre: ")
    rut = input("Ingrese RUT: ")
    telefono = input("Ingrese telefono: ")

    print("Cliente registrado")
    print("Nombre:", nombre)
    print("RUT:", rut)
    print("Telefono:", telefono)

else:

    print("Registro de visita")

    cliente = input("Ingrese nombre del cliente: ")
    propiedad = input("Ingrese propiedad a visitar: ")
    fecha = input("Ingrese fecha de visita: ")

    print("Visita registrada")
    print("Cliente:", cliente)
    print("Propiedad:", propiedad)
    print("Fecha:", fecha)