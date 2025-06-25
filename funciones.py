'''ENUNCIADO FINAL – SISTEMA DE VENTAS DE PROGRAMAS EDUCATIVOS EN DEV SENIOR
(SIN COLECCIONES)
La reconocida startup educativa Dev Senior Code, que forma desarrolladores de software
con validez internacional, necesita un sistema básico para registrar las ventas de sus 3
programas más demandados:
• Java de Cero a Senior
• Python con IA Aplicada
• Mobile Senior con IA
Cada programa tiene un valor oficial de $18.000.000, pero gracias a las Becas Manos al
Futuro, el estudiante accede con un 90% de descuento, pagando únicamente $1.800.000
por todo el programa.
El sistema debe permitir a los asesores académicos:
1. Mostrar los programas disponibles, con su precio con descuento.
2. Registrar la venta de cualquiera de los tres programas, indicando la cantidad de
estudiantes matriculados.
3. Consultar los ingresos acumulados por cada programa.
4. Mostrar el total general de ingresos del día.
5. Salir del sistema.
Requisitos técnicos:
• Cada funcionalidad debe estar implementada en una función.
• Solo deben utilizarse variables simples (por ejemplo: programa1, precio1,
ventas1…), no se permite el uso de listas, diccionarios ni ninguna estructura de
colección.
• El sistema debe utilizar un menú principal controlado con un ciclo while, que se
repite hasta que el usuario decida salir.
• Deben usarse condicionales para validar la opción ingresada y prevenir errores.''' 

programa_1 = "Java de Cero a Senior"
estudiantes_matriculados_programa_1 = 0 
ventas_programa_1 = 0


programa_2 = "Python con IA Aplicada"
estudiantes_matriculados_programa_2 = 0 
ventas_programa_2 = 0


programa_3 = "Mobile Senior con IA"
estudiantes_matriculados_programa_3 = 0 
ventas_programa_3 = 0


precio_de_los_programas = float(18000000)
descuento = precio_de_los_programas * 0.90
total_a_pagar = precio_de_los_programas - descuento



def mostrar_menu():
    print("\n Menu de ventas")
    print("1. Programas disponibles")
    print("2. Realizar venta")
    print("3. Ingresos por programa")
    print("4. Total recaudado en el día")
    print("5. Salir")
    
def programas_disponibles():   
    print("\n programas disponibles") 
    print(f"1. el programa {programa_1} tiene un valor de ${precio_de_los_programas} cuenta con un  descuento de ${descuento} total a pagar es de ${total_a_pagar} ")    
    print(f"2. el programa {programa_2} tiene un valor de ${precio_de_los_programas} cuenta con un  descuento de ${descuento} total a pagar es de ${total_a_pagar} ")    
    print(f"3. el programa {programa_3} tiene un valor de ${precio_de_los_programas} cuenta con un  descuento de ${descuento} total a pagar es de ${total_a_pagar} ")    
    
def realizar_venta():
    global ventas_programa_1, ventas_programa_2, ventas_programa_3, estudiantes_matriculados_programa_1, estudiantes_matriculados_programa_2, estudiantes_matriculados_programa_3
    programas_disponibles()
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:    
        estudiantes_a_matricular = int(input(f"ingrese la cantidad de alumnos que desean acceder al programa {programa_1}: "))
        estudiantes_matriculados_programa_1 += estudiantes_a_matricular
        ventas_programa_1 += (estudiantes_a_matricular * precio_de_los_programas)
        print(f"se vendio el programa{programa_1} a {estudiantes_a_matricular} estudiantes") 
    elif opcion == 2: 
        estudiantes_a_matricular = int(input(f"ingrese la cantidad de alumnos que desean acceder al programa {programa_2}: "))
        estudiantes_matriculados_programa_2 += estudiantes_a_matricular
        ventas_programa_2 += (estudiantes_a_matricular * precio_de_los_programas)
        print(f"se vendio el programa{programa_2} a {estudiantes_a_matricular} estudiantes") 
    elif opcion == 3:
        estudiantes_a_matricular = int(input(f"ingrese la cantidad de alumnos que desean acceder al programa {programa_3}: "))
        estudiantes_matriculados_programa_3 += estudiantes_a_matricular
        ventas_programa_3 += (estudiantes_a_matricular * precio_de_los_programas)
        print(f"se vendio el programa{programa_3} a {estudiantes_a_matricular} estudiantes") 
    else:
        print("aun no se a realizado ninguna venta")    
        
        
def ver_ingreso_por_programa():
    print("\n igresos por programa")
    print("1. ver los ingresos del programa de Java De Cero a Senior")        
    print("2. ver los ingresos del programa de Python con IA Aplicada")        
    print("3. ver los ingresos del programa de Mobile Senior con IA")        
    opcion = int(input("ingrese el numero del programa que desea ver: "))
    if opcion == 1:
        print(f"los ingresos totales del programa de Java De Cero a Senior son ${ventas_programa_1}")
    elif opcion == 2: 
        print(f"los ingresos totales del programa de Python Con IA son ${ventas_programa_2}")   
    elif opcion == 3:
        print(f"los ingresos totales del programa de Mobile Senior con IA son ${ventas_programa_3}  ")
    
def ingresos_totales_del_dia():
    ventas_totales = ventas_programa_1 + ventas_programa_2 + ventas_programa_3
    print(f"los ingresos totales son ${ventas_totales} ") 
            
        
        
while True:
    mostrar_menu()
    opcion = int(input("ingrese una opcion: "))    
    if opcion == 1:
        programas_disponibles()
    elif opcion == 2: 
        realizar_venta()
    elif opcion == 3:
        ver_ingreso_por_programa()    
    elif opcion == 4:
        ingresos_totales_del_dia()    
    elif opcion == 5:
        print("saliendo del sistema")
        break
    else:
        print("opcion invalida")            
        