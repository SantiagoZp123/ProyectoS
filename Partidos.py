class Partidos():
    def __init__(self, id, equipo_local, equipo_visitante, fecha, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.estadio = estadio
        
    def mostrar_partido(self):
        return self.equipo_local, self.equipo_visitante, self.fecha, self.estadio