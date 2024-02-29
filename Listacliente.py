from Cliente import cliente

class listacliente:
    def __init__(self):
        self.lista_objetos = []

    def agregar_objeto(self, objeto):
        self.lista_objetos.append(objeto)

    def mostrar_objetos(self):
        if not self.lista_objetos:
            print("La lista está vacía.")
        else:
            print("=== Lista de Clientes ===")
            for i, objeto in enumerate(self.lista_objetos, 1):
                print(f"Objeto {i}:")
                print(objeto)
                print()

    def buscar_por_nit(self, texto):
        for objeto in self.lista_objetos:
            if objeto.NIT == texto:
                return objeto
        return None