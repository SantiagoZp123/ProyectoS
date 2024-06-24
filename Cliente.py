class Cliente():
    def __init__(self, nombre, cedula, edad, tipo_entrada, codigoticket,asientos=[]) :
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipo_entrada = tipo_entrada
        self.codigoticket = codigoticket
        self.asientos = asientos
    
    def mostrar_cliente(self):
        return (f"{self.nombre}, {self.cedula}, {self.edad}, {self.tipo_entrada}, {self.codigoticket}, {self.asientos}")