from Alimento import Alimento

class Package(Alimento): 
    def __init__(self, nombre, cantidad, precio, stock, aditional, tipo):
        super().__init__(nombre, cantidad, precio, stock, aditional)
        self.tipo = tipo

    def mostrar_empaque(self):
        return (f"\nNombre: {self.nombre} \nCantidad: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Tipo:{self.tipo}")
    
    def mostrar_producto(self):
        return (f"\nNombre: {self.nombre} \nCantidad: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Tipo:{self.tipo}")