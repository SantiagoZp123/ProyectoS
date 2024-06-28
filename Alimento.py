class Alimento():
    def __init__(self,nombre,cantidad,precio, stock, aditional):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.stock = stock
        self.aditional = aditional

    def mostrar_alimento(self):
        return (f"Alimento: \nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Aditional:{self.aditional}")
    
    def mostrar_producto(self):
        return (f"Alimento: \nNombre: {self.nombre} \nClasificacion: {self.cantidad} \nPrecio:{self.precio} \n Stocl:{self.stock} \n Aditional:{self.aditional}")