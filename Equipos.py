class Equipos():
    def __init__(self, nombre, codigoFifa, grupo, equipo_id):
        self.nombre = nombre
        self.codigoFifa = codigoFifa
        self.grupo = grupo
        self.equipo_id = equipo_id
    
    def mostrar_equipo(self):
        return self.nombre,self.codigoFifa,self.grupo, self.equipo_id
    
    def __str__(self):
        return (f"{self.nombre}, Codigo FIFA: {self.codigoFifa}, Grupo: {self.grupo}")
    
    def show_nombre_num(self):
        return (f"Pais: {self.nombre}, Codigo FIFA: {self.codigoFifa}, Grupo: {self.grupo}, ID: {self.equipo_id}")