class cliente:
    def __init__(self, nombre, correo, NIT) -> None:
        self.nombre = nombre
        self.correo = correo
        self.NIT = NIT
        

    def __str__(self):
        return f"Nombre Cliente: {self.nombre}\nCorreo: {self.correo}\nNit cliente: {self.NIT}"
    