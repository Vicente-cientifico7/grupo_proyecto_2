# Registro del propietario

def registrar_propietario():
    nombre = input("Nombre del propietario: ")
    rut = input("RUT del propietario: ")
    telefono = input("Telefono del propietario: ")

    propietario = {
        "nombre": nombre,
        "rut": rut,
        "telefono": telefono
    }

    return propietario


# Registro del contrato

def registrar_contrato(propietario):
    inmueble = input("Codigo del inmueble: ")
    tasacion = float(input("Valor de tasacion sin puntos: "))

    if tasacion <= 0:
        print("El valor debe ser mayor que cero.")
        return None

    monto = tasacion * 0.5 / 100

    contrato = {
        "rut_propietario": propietario["rut"],
        "inmueble": inmueble,
        "tasacion": tasacion,
        "monto": monto
    }

    print("\nContrato de exclusividad")
    print("Propietario:", propietario["nombre"])
    print("Inmueble:", inmueble)
    print("Tasacion:", tasacion)
    print("Monto del 0,5%:", monto)

    return contrato


# Ejecutar el archivo directamente

if __name__ == "__main__":
    propietario = registrar_propietario()
    contrato = registrar_contrato(propietario)
