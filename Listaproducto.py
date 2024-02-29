from Producto import producto

class listaproducto:
    def __init__(self):
        self.lista_objetos = []

    def agregar_objeto(self, objeto):
        self.lista_objetos.append(objeto)

    def mostrar_objetos(self):
        if not self.lista_objetos:
            print("La lista está vacía.")
        else:
            print("=== Lista de Productos ===")
            for i, objeto in enumerate(self.lista_objetos, 1):
                print(f"Objeto {i}:")
                print(objeto)
                print()
    
    def buscar_por_codigo(self, texto):
        for objeto in self.lista_objetos:
            if objeto.codigo == texto:
                return objeto
        return None
    
    def buscarprecio_por_objeto(self, obje):
        for objeto in self.lista_objetos:
            if objeto == obje:
                return objeto.precio
        return None
