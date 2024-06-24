class Estadios():
    def __init__(self, equipo_local, equipo_visitante, fecha, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.estadio = estadio

    def mostrar_estadio(self):
        return self.nombre, self.ubicación, self.estadio
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Ubicación: {self.ubicación}, Estadio: {self.estadio}")