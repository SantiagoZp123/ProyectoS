class Estadios():
    def __init__(self, name, city, capacity, estadio_id):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.estadio_id = estadio_id

    def mostrar_estadio(self):
        return self.name, self.city, self.capacity, self.estadio_id
    
    def __str__(self):
        return (f" Nombre: {self.name}, Ciudad: {self.city}, Capacidad: {self.capacity}")
    
    def show_nombre_est(self):
        return (f"Nombre: {self.name}, Ciudad: {self.city}, Capacidad: {self.capacity}, ID: {self.estadio_id}")