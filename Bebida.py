class Bebida():
    def __init__(self,nombre,cantidad,precio,stock, aditional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.aditional = aditional

    def mostrar_bebida(self):
        return (f"\nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stock:{self.stock} \n Aditional:{self.aditional}")
    def mostrar_producto(self):
        return (f"\nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stock:{self.stock} \n Aditional:{self.aditional}")