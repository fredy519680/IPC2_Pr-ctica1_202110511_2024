from Producto import producto
from Cliente import cliente
from Compra import compra
from Listaproducto import listaproducto
lista = listaproducto()
from Listacliente import listacliente
listac = listacliente()
from Lista_compras import listaCompras
listacom = listaCompras()
id = 0

def registrar_produc():
    print("\n=== Información del Producto ===")
    codigopro = input("Ingrese el código del producto: ")
    nombrepro = input("Ingrese el nombre del producto: ")
    descripcionpro = input("Ingrese la descripcion del producto: ")
    costopro = float(input("Ingrese el Precio unitario del producto: "))
    objeto = producto(codigopro,nombrepro,descripcionpro,costopro) 
    lista.agregar_objeto(objeto)
    #print(objeto)
    lista.mostrar_objetos()

def buscarcliente():
    nonit = int(input("ingrese el numero de NIT del cliente que desea buscar(solo números): "))
    cliente = listac.buscar_por_nit(nonit)
    print("----Cliente Seleccionado----")
    if cliente is not None:
        compracliente = compra(cliente)
        print(cliente)
        global id
        productos = 0
        total = 0
        impuestos = 0
        while True:
            respuesta = input("¿Quieres agregar un producto?, Presiona S ¿Quieres terminar y Facturar?, presiona N (S/N): ").upper()  
            if respuesta == 'S':
                codigo = input("ingrese el código del producto que desea comprar: ")
                produ = lista.buscar_por_codigo(codigo)
                if produ is not None:
                    print("----Producto Seleccionado----")
                    print(produ)
                    compracliente.agregar_producto(produ)
                    preciopro = lista.buscarprecio_por_objeto(produ)
                    print(preciopro)
                    total = total + preciopro
                    print(total)
                else:
                    print("el código que ingreso no pertenece a ningún producto existente")
            elif respuesta == 'N':
                print("Deteniendo...")
                break  
            else:
                print("Respuesta no válida. Por favor, ingresa 'S' para continuar o 'N' para detener.")
        id = id + 1
        idstr = str(id)
        impuestos = total * 0.12
        compracliente.agregar_datos(id,total,impuestos)
        #compracliente.mostrar_orden()
        listacom.agregar_compra(compracliente)
        listacom.mostrar_compras()
        
        
    else:
        print("EL numero que usted ingreso no pertenece a ningun usuario en el sistema")
        buscarcliente()
        

def buscarcompra():
    idcompra = int(input("ingrese el Id de la factura que desea ver que desea ver (enteros): "))-1
    compra = listacom.mostrar_por_indice(idcompra)
    if compra is not None:
        #print("----Producto Seleccionado----")
        print(compra)
    else:
        print("")

def registrar_cliente():
    print("\n=== Información del Cliente ===")
    nombre = input("Ingrese el nombre del comprador: ")
    correo = input("Ingrese un correo de identificación: ")
    Nit = int(input("Ingrese el Nit del comprador (solo números): "))
    objeto = cliente(nombre,correo,Nit) 
    listac.agregar_objeto(objeto)
    #print(objeto)
    listac.mostrar_objetos()

def datos_estudiante():
    print(" Nombre: Fredy alexander Esteban Pineda            Carnet: 202110511")

def mostrar_menu():
    print("=== Menú Principal ===")
    print("1. Registrar Producto")
    print("2. Registrar Cliente")
    print("3. Realizar Compra")
    print("4. Reporte de compra")
    print("5. Datos del estudiante")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Registrar producto")
        registrar_produc()
        mostrar_menu()
        # Llamar a una función relacionada con la Opción 1
    elif opcion == "2":
        print("Registrar Cliente")
        registrar_cliente()
        mostrar_menu()
        # Llamar a una función relacionada con la Opción 2
    elif opcion == "3":
        print("Realizar Compra")
        buscarcliente()
        mostrar_menu()
        # Llamar a una función relacionada con la Opción 3
    elif opcion == "4":
        print("Reporte de Compra")
        buscarcompra()
        mostrar_menu()
        # Llamar a una función relacionada con la Opción 4
    elif opcion == "5":
        print("Datos del Estudiante")
        datos_estudiante()
        mostrar_menu()
        # Llamar a una función relacionada con la Opción 5
    elif opcion == "6":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
        mostrar_menu()


# Ejemplo de uso
mostrar_menu()