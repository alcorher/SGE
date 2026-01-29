class Estudiante():
    def __init__(self, nombre,calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)
    
estudiante1 = Estudiante("Ana", [8, 9, 7, 10, 6])
print(f"El promedio de {estudiante1.nombre} es: {estudiante1.promedio()}")
