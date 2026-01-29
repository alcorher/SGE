class Vehiculo():
    cantidad_total = 0
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        Vehiculo.cantidad_total += 1


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Honda", "Civic", 2019)
print(f"Cantidad total de vehículos: {Vehiculo.cantidad_total}")
vehiculo3 = Vehiculo("Ford", "Focus", 2018)
print(f"Cantidad total de vehículos: {Vehiculo.cantidad_total}")