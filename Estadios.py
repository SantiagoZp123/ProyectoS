class Estadios():
    def __init__(self, nombre, ubicación, estadio):
        self.nombre = nombre
        self.ubicación = ubicación
        self.estadio = estadio

    def mostrar_estadio(self):
        return self.nombre, self.ubicación
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Ubicación: {self.ubicación}")