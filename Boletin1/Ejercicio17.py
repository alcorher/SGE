diccionario = {
    'nombre': 'Juan José',
    'edad': 30,
    'ciudad': 'Madrid',
}

print("Diccionario:", diccionario)
print("Nombre:", diccionario['nombre'])
print("Edad:", diccionario['edad'])
print("Ciudad:", diccionario['ciudad'])

diccionario.update({'nickname': 'JJ'})
del(diccionario['ciudad'])
print("Diccionario actualizado:", diccionario)
