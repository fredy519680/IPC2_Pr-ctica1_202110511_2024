class producto:
    def __init__(self, codigo, nombre, descripcion, precio) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"Código: {self.codigo}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nPrecio del producto: {self.precio}"