from Bebida import Bebida

class Alcoholica(Bebida): 
    def __init__(self, nombre, cantidad, precio, stock, aditional, tipo):
        super().__init__(nombre, cantidad, precio, stock, aditional)
        self.tipo = tipo
    
    def mostrar_bebida_alcoholica(self):
        return (f"\nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Aditional:{self.aditional} \n Tipo:{self.tipo}")
    
    def mostrar_producto(self):
        return (f"\nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Aditional:{self.aditional} \n Tipo:{self.tipo}")