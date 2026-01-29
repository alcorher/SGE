class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar(self, cantidad):
        self.cantidad += cantidad
        print(f"Se han agregado {cantidad} unidades de {self.nombre}. Nueva cantidad: {self.cantidad}")

    def quitar(self, cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficientes unidades de {self.nombre} para quitar.")
        else:
            self.cantidad -= cantidad
            print(f"Se han quitado {cantidad} unidades de {self.nombre}. Nueva cantidad: {self.cantidad}")

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"
    
    
producto1 = Producto("Manzanas", 0.5, 100)
print(producto1)
producto1.agregar(50)
print(producto1)
producto1.quitar(30)
print(producto1)