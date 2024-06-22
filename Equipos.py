class Equipos():
    def __init__(self, nombre, codigoFifa, grupo):
        self.nombre = nombre
        self.codigoFifa = codigoFifa
        self.grupo = grupo
    
    def mostrar_equipo(self):
        return self.nombre,self.codigoFifa,self.grupo
    
    def __str__(self):
        return (f"Nombre: {self.nombre}, Codigo FIFA: {self.codigoFifa}, Grupo: {self.grupo}")
    
    def show_nombre_num(self):
        return (f"Nombre: {self.nombre}, Codigo FIFA: {self.codigoFifa}")