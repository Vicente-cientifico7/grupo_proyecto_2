#Informacion de la oficina
print("Información de la oficina del caso: ")
oficina = input("Introduzca el nombre de oficina: ")
gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
agente_venta =input("Introduzca el nombre del agente de venta: ")

#Información específica del inmueble
print("Indica la opción del tipo de vivienda: ")
print("0: Vivienda")
print("1: Local comercial")
print("2: Bodega")
tipo_inmueble = int(input())

#Información general del inmueble
print("Información general del inmueble: ")
calle = input("Introduzca la calle del inmueble: ")
numero = int(input("Introduzca el número del inmueble: "))
comuna = input("Introduzca la comuna del inmueble:")

superficie_m2 = int(input("Introduzca la superficie del inmueble (m^2): "))
valor_tasacion = float(input("Introduzca el valor de tasación del inmueble(UF): "))

if tipo_inmueble == 0:
    estado_vivienda = input("Indica si la vivienda es 'nueva' o 'usada': ")
    tipo_vivienda = input("Indica si la vivienda es 'casa' o 'departamento': ")
    n_habitaciones = int(input("Indica el número de habitaciones: "))
    n_baños = int(input("Indica el número de baños: "))
    n_cocinas = int(input("Indica el número de cocinas: "))
    red_gas = input("Indique si la propiedad cuenta con red de gas (Si/No): ")
    puerta_blindada = input("Indique si la propiedad cuenta con puerta blindada (Si/No): ")
    tipo_piso = input("Indique el tipo de piso de la propiedad: ")
else:
    número_puertas =  int(input("Indica el número de puertas de acceso: "))
    ventanas = input("Indica la presencia de ventanas (Si/No): ")
    estructura = input("Indica si el inmueble esta 'acondicionado' o es 'planta libre': ")

#Información del propietario que ofrecerá el inmueble
print("Información del antiguo propietario: ")
nombre_propietario = input("Introduzca el nombre completo: ")
rut_propietario = input("Introduzca el RUT: ")
telefono_propietario1 = input("Introduzca el número de contacto: ")
telefono_propietario2 = input("Opcionalmente un 2° número de contacto, sino, no escriba nada: ")
plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses): ")
