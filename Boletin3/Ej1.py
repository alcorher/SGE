class Persona():
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años"
    
    def informacion(self):
        return f"{self.nombre} mide {self.altura} metros"
    

persona1 = Persona("Ana", 28, 1.65)
print(persona1.saludar())
print(persona1.informacion())