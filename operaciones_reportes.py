# Parte: Operaciones y reportes (calculadora de comisiones)

COMISION_VENTA = 2       # 2% del precio de venta
COMISION_ARRIENDO = 50   # 50% del primer mes de arriendo

total_ventas = 0
total_arriendos = 0
cantidad_operaciones = 0

continuar = "si"

while continuar == "si":
    agente = input("Nombre del agente: ")
    tipo_operacion = input("Tipo de operación (venta o arriendo): ")
    valor = float(input("Valor en pesos: "))

    while valor <= 0:
        valor = float(input("El valor debe ser mayor a 0: "))

    if tipo_operacion == "venta":
        comision = valor * COMISION_VENTA / 100
        total_ventas = total_ventas + comision
    else:
        comision = valor * COMISION_ARRIENDO / 100
        total_arriendos = total_arriendos + comision

    cantidad_operaciones = cantidad_operaciones + 1
    print("La comisión de", agente, "es: $", comision)

    continuar = input("¿Desea registrar otra operación? (si o no): ")

print("===== REPORTE =====")
print("Cantidad de operaciones:", cantidad_operaciones)
print("Comisiones por ventas: $", total_ventas)
print("Comisiones por arriendos: $", total_arriendos)
print("Total de comisiones: $", total_ventas + total_arriendos)
