
# /////////////////////// Menu /////////////////////////////
print("====================================================")
print("Bienvenidos al menu de la mejor inmobiliaria de Chile")
print("=====================================================")
print("A continuación se mostraran las alternativas de navegación: ")
print("1. Registrar oficina")
print("2. Registrar inmueble")
print("3. Registrar visita")
print("4. Registrar contrato")
print("5. Solicitar reporte")
print("=====================================================")
opcion = int(input("Seleccione la alternativa que desea: "))
print("************************************************")

# //////////////////////// Registro Oficina /////////////////////////////////////
if opcion == 1:
    #Informacion de la oficina
    print("Registro de información de la oficina")
    print("")
    oficina = input("Introduzca el nombre de oficina: ")
    gerente_oficina = input("Introduzca el nombre del gerente de oficina: ")
    agente_venta =input("Introduzca el nombre del agente de venta: ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Oficina registrada")
    print("Oficina: ", oficina)
    print("Gerente de oficina: ", gerente_oficina)
    print("Agente de venta: ", agente_venta)

# ////////////////////// Registro Inmueble /////////////////////////
elif opcion == 2:
    
    #Información específica del inmueble
    print("Registro de información del inmueble")
    print("")
    print("Indica la opción del tipo de inmueble a registrar: ")
    print("")
    print("0: Vivienda")
    print("1: Local comercial")
    print("2: Bodega")
    print("")
    tipo_inmueble = int(input("El tipo de inmueble es: "))
    
    #Información general del inmueble
    print("")
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
        numero_puertas =  int(input("Indica el número de puertas de acceso: "))
        ventanas = input("Indica la presencia de ventanas (Si/No): ")
        estructura = input("Indica si el inmueble esta 'acondicionado' o es 'planta libre': ")

    #Información del propietario que ofrecerá el inmueble
    print("************************************************")
    print("Registro de información del propietario ")
    print("")
    nombre_propietario = input("Introduzca el nombre completo: ")
    rut_propietario = input("Introduzca el RUT: ")
    telefono_propietario1 = input("Introduzca el número de contacto: ")
    telefono_propietario2 = input("Opcionalmente un 2° número de contacto, sino, no escriba nada: ")
    plazo_contrato = input("Introduzca el plazo del contrato, indicando las unidades de tiempo (meses): ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Inmueble registrado")
    if tipo_inmueble == 0:
        registro_inmueble = "Vivienda"
    elif tipo_inmueble == 1:
        registro_inmueble = "Local comercial"
    else: 
        registro_inmueble = "Bodega"

    print("Tipo de inmueble: ", registro_inmueble)
    print("Calle: ", calle)
    print("Numero: ", numero)
    print("Comuna: ", comuna)
    print("Superficie m2: ", superficie_m2)
    print("Valor de tasación: ", valor_tasacion)
    
    if tipo_inmueble == 0:
        print("Estado de la vivienda: ", estado_vivienda)
        print("Tipo de vivienda: ", tipo_vivienda)
        print("Numero de habitaciones: ",n_habitaciones)
        print("Numero de baños: ",n_baños)
        print("Numero de cocinas: ",n_cocinas)
        print("Tiene red de gas: ",red_gas)
        print("Tiene puerta blindada: ",puerta_blindada)
        print("El tipo de piso es: ",tipo_piso)
    else: 
        print("Numero de puertas de acceso: ", numero_puertas)
        print("Tiene ventanas: ", ventanas)
        print("Condición: ", estructura)
        print("")
    
    print("")  
    print("Propietario registrado")
    print("Nombre del propietario: ", nombre_propietario)
    print("Rut del propietario: ", rut_propietario)
    print("Telefonos: ", telefono_propietario1, " - ", telefono_propietario2)
    print("Plazo del contrato: ", plazo_contrato)
        
   
# ////////////////////////// Registro Visita //////////////////////////////

elif opcion == 3:

    print("Registro de información de visita")
    print("")

    cliente = input("Ingrese nombre del cliente: ")
    propiedad = input("Ingrese propiedad a visitar: ")
    fecha = input("Ingrese fecha de visita: ")
    comentario = input("Ingrese comentario del cliente: ")
    
    print("===============================================")
    print("Datos registrados: ")
    print()

    print("Visita registrada")
    print("Cliente: ", cliente)
    print("Propiedad: ", propiedad)
    print("Fecha: ", fecha)
    print("Comentario: ", comentario)
    
# ///////////////////////////// Registro Contrato //////////////////////
elif opcion == 4:
    
    print("Registro de información del contrato")
    print("")


    nombre = input("Nombre del propietario: ")
    rut = input("RUT del propietario: ")
    telefono = input("Telefono del propietario: ")
    print("")

# Registro del contrato

    inmueble = input("Codigo del inmueble: ")
    tasacion = float(input("Valor de tasacion sin puntos: "))

    if tasacion <= 0:
        print("El valor debe ser mayor que cero.")
    
    else:
        monto = tasacion * 0.5 / 100
        
        print("===============================================")
        print("Datos registrados: ")
        print()
        
        print("\nContrato de exclusividad")
        print("Propietario:", nombre)
        print("Rut: ", rut)
        print("telefono: ", telefono)
        print("Codigo del inmueble:", inmueble)
        print("Monto del 0,5%:", monto)

# ///////////////////////// Solicitar reporte ////////////////////

elif opcion == 5:

    comision_gerente = 0.1
    comision_agente = 0.3
    comision_venta = 0.3

    total_ventas_casas = 300000000
    total_arriendos_casa = 100000000
    total_casa = total_ventas_casas + total_arriendos_casa
    
    total_ventas_depto = 200000000
    total_arriendos_depto = 60000000
    total_depto = total_ventas_depto + total_arriendos_depto
    
    total_ventas_bodega = 500000000
    total_arriendos_bodega = 0
    total_bodega = total_ventas_bodega + total_arriendos_bodega
    
    total_ventas_local = 0
    total_arriendos_local = 600000000
    total_local = total_ventas_local + total_arriendos_local
    
    print("Solicitud de reportabilidad")
    print("")

    print("Seleccione el reporte que desea visualizar: ")
    print("")
    
    print("1. Total de ingresos: ")
    print("2. Total de ingresos por ventas: ")
    print("3. Total de ingresos por arriendo: ")
    print("")
    opcion_reporte = int(input("Alternativa seleccionada: "))
    print("")
    
    if opcion_reporte == 1:
        ingreso = total_casa + total_depto + total_bodega + total_local
    
    elif opcion_reporte == 2:
        print("Seleccione el reporte a visualizar: ")
        print("")
        print("1. Total ventas globales")
        print("2. Total ventas casas")
        print("3. Total ventas departamentos")
        print("4. Total ventas bodegas")
        print("5. Total ventas locales comerciales")
        alternativa_reporte = int(input("Alternativa seleccionada: "))
        
        if alternativa_reporte == 1:
            ingreso = total_ventas_casas + total_ventas_depto + total_ventas_bodega + total_ventas_local
        elif alternativa_reporte == 2:
            ingreso = total_ventas_casas
        elif alternativa_reporte == 3:
            ingreso = total_ventas_depto
        elif alternativa_reporte == 4:
            ingreso = total_ventas_bodega
        elif alternativa_reporte == 5:
            ingreso = total_ventas_local
    
    elif opcion_reporte == 3:
        print("Seleccione el reporte a visualizar: ")
        print("")
        print("1. Total arriendo globales")
        print("2. Total arriendo casas")
        print("3. Total arriendo departamentos")
        print("4. Total arriendo bodegas")
        print("5. Total arriendo locales comerciales")
        alternativa_reporte = int(input("Alternativa seleccionada: "))
        
        if alternativa_reporte == 1:
            ingreso = total_arriendos_casa + total_arriendos_depto + total_arriendos_bodega + total_arriendos_local
        elif alternativa_reporte == 2:
            ingreso = total_arriendos_casa
        elif alternativa_reporte == 3:
            ingreso = total_arriendos_depto
        elif alternativa_reporte == 4:
            ingreso = total_arriendos_bodega
        elif alternativa_reporte == 5:
            ingreso = total_arriendos_local
    
    else:
        print("La opción que ha ingresado no es valida")
            
    
    ingreso_gerente = 0.1 * ingreso
    ingreso_agente = 0.3 * ingreso
    ingreso_comision = 0.3 * ingreso
    
    print("Los ingresos son: ")
    print("Ingresos totales: ", ingreso)
    print("Ingresos por comision de gerente: ", ingreso_gerente)
    print("Ïngreso por comision de agente: ", ingreso_agente)
    print("Ingreso por comision: ", ingreso_comision)