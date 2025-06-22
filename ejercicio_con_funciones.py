'''La drogueria solo maneja 3 productos en el sistema.  
Cada uno tiene su propio nombre, precio e ingreso acumulado.
El usuario padrá: 
Vender cualquier de los 3 productos 
Consultar ingresos totales 
Salir del sistema  '''
# creamos las variables para cada producto
p1 = "acetaminofen"
precio1 = 2000
ingreso1 = 0 

p2 = "ibiuprofeno"
precio2 = 35000
ingreso2 = 0

p3 = "advil"
precio3 = 6700
ingreso3 = 0

# creamos una funcion que nos muestre un menu
def mostrarMenu():
    print("\n menu drogueria")
    print("1. ver productos dosponibles")
    print("2. vender producto")
    print("3. mostrar ingresos totales")
    print("4. salir")
 
 # creamos una funcion para mostrar los productos disponibles y su valor 
def verProductos():
    print(" \n prodcutos disponibles")
    print(f"1. {p1} --> ${precio1}")
    print(f"2. {p2} --> ${precio2}")
    print(f"3. {p3} --> ${precio3}")

def venderProducto():
    global ingreso1, ingreso2, ingreso3 # usamos el elemento global para llamar las variables universales y poder usarlas
    verProductos()
    opcion = int(input("selecione el numero del producto a vender: "))
    
    if opcion == 1:
        cantidad = int(input(f"cuantos {p1} desea vender: "))
        total = cantidad * precio1
        ingreso1 += total
        print(f"venta realizada por ${total}")    
    elif opcion == 2: 
        cantidad = int(input(f"cuantos {p2} desea vender: "))    
        total = cantidad * precio2
        ingreso2 += total
        print(f"venta realizada por ${p2}")    
    elif opcion == 3:
        cantidad = int(input(f"cuanos {p3} desea vender: "))
        total = cantidad * precio3
        ingreso3 += total
        print(f"venta realizada por ${total}")
    else:
        print("opcion no valida")
        
def mostrarIngreso():
    total_ingreso = ingreso1 + ingreso2 + ingreso3 
    print(f"se vendio en total del {p1} la suma de: ${ingreso1}")
    print(f"se vendio en total del {p2} la suma de: ${ingreso2}")
    print(f"se vendio en total del {p3} la suma de: ${ingreso3}")
    print(f"total gereal: ${total_ingreso}")
# agregar una variable que muestre los prodcutos de manera individual|

while True:
    mostrarMenu()
    opcion = int(input("slecione una opcion: "))        
    
    if opcion == 1:
        verProductos()
    elif opcion == 2: 
        venderProducto()    
    elif opcion == 3:
        mostrarIngreso()
    elif opcion == 4:
        print("hemos salido del menu")
        break         
    else:
        print("opcion no valida")    