from Compra import compra

class listaCompras:
    def __init__(self):
        self.compras = []

    def agregar_compra(self, compra):
        self.compras.append(compra)

    def mostrar_compras(self):
        for i, compra in enumerate(self.compras, start=1):
            print(f"Compra {i}:")
            compra.mostrar_orden()
            print()

    def buscar_por_id1(self, texto):
        for objeto in self.compras:
            if objeto.id == texto:
                return objeto
        return None
    
    def buscar_por_id(self, compra_id):
        for compra in self.compras:
            if compra.id == compra_id:
                return compra
        return None
    
    def mostrar_por_indice(self, indice):
        if 0 <= indice < len(self.compras):
            return (self.compras[indice].mostrar_orden())
        else:
            return None