
class compra:
    def __init__(self, cliente):
        self.cliente = cliente
        self.id = 0
        self.Total = 0
        self.impuestos = 0
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def agregar_datos(self,id, total, impuestos):
        self.id = id
        self.Total = total
        self.impuestos = impuestos

    def mostrar_orden(self):
        print("=== Reporte de compra ===")
        print("Cliente:")
        print("")
        print(self.cliente)
        print("")
        print("Productos:")
        if not self.lista_productos:
            print("La orden no tiene productos.")
        else:
            for i, producto in enumerate(self.lista_productos, 1):
                print(f"Producto {i}:")
                print(producto)
                print()
        print("")
        print("")
        print("Total: Q",self.Total)
        print("Impuestos: Q",self.impuestos)
        print("id de la compra:",self.id)

