tiendaProductos = [
    {"nombre": "Manzana", "precio": 0.5, "cantidad": 100},
    {"nombre": "Agua", "precio": 1.0, "cantidad": 50},
    {"nombre": "Pan", "precio": 1.5, "cantidad": 30},
    {"nombre": "Leche", "precio": 0.8, "cantidad": 20},
    {"nombre": "Huevos", "precio": 2.0, "cantidad": 10}
]

carrito=[]


def agregar_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    tiendaProductos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto {nombre} agregado.")


def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in tiendaProductos:
        if producto["nombre"].lower() == nombre.lower():
            nuevo_precio = float(input("Introduce el nuevo precio: "))
            nueva_cantidad = int(input("Introduce la nueva cantidad: "))
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            print(f"Producto {nombre} actualizado.")
            return
    print(f"Producto {nombre} no encontrado.")


def mostrar_disponibles():
    print("Productos disponibles:")
    for producto in tiendaProductos:
        if producto["cantidad"] > 0:
            print(f"{producto['nombre']}: Precio: {producto['precio']}€, Cantidad: {producto['cantidad']}")


def agregar_al_carrito():
    nombre = input("Introduce el nombre del producto a agregar al carrito: ")
    for producto in tiendaProductos:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input("Introduce la cantidad a agregar al carrito: "))
            if cantidad <= producto["cantidad"]:
                carrito.append({"nombre": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad})
                producto["cantidad"] -= cantidad
                print(f"{cantidad} unidades de {nombre} agregadas al carrito.")
            else:
                print(f"No hay suficiente stock de {nombre}.")
            return
    print(f"Producto {nombre} no encontrado.")

def retirar_del_carrito():
    nombre = input("Introduce el nombre del producto a retirar del carrito: ")
    for item in carrito:
        if item["nombre"].lower() == nombre.lower():
            cantidad = int(input("Introduce la cantidad a retirar del carrito: "))
            if cantidad <= item["cantidad"]:
                item["cantidad"] -= cantidad
                for producto in tiendaProductos:
                    if producto["nombre"].lower() == nombre.lower():
                        producto["cantidad"] += cantidad
                        break
                if item["cantidad"] == 0:
                    carrito.remove(item)
                print(f"{cantidad} unidades de {nombre} retiradas del carrito.")
            else:
                print(f"No hay suficientes unidades de {nombre} en el carrito.")
            return
    print(f"Producto {nombre} no encontrado en el carrito.")


def mostrar_carrito():
    if not carrito:
        print("El carrito está vacío.")
        return
    print("Productos en el carrito:")
    total = 0
    for item in carrito:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']}: Precio: {item['precio']}€, Cantidad: {item['cantidad']}, Subtotal: {subtotal}€")
    print(f"Total a pagar: {total}€")

def total_carrito():
    total = 0
    for item in carrito:
        total += item["precio"] * item["cantidad"]
    print(f"Total del carrito: {total}€")


def comprar():
    if not carrito:
        print("El carrito está vacío. No hay nada que comprar.")
        return
    total_carrito()
    print("Compra realizada. Gracias por su compra.")
    carrito.clear()


def menuAdmin():
    contraseña = "admin123"
    intento = input("Introduce la contraseña de administrador: ")
    if intento != contraseña:
        print("Contraseña incorrecta.")
        return
    else:
        while True:
            print("\nMenú de administración:")
            print("1. Agregar producto")
            print("2. Actualizar producto")
            print("3. Mostrar productos disponibles")
            print("4. Volver al menú principal")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                actualizar_producto()
            elif opcion == "3":
                mostrar_disponibles()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

def menu():
    while True:
        print("\nMenú de la tienda:")
        print("1. Menú de administración")
        print("2. Mostrar productos disponibles")
        print("3. Agregar producto al carrito")
        print("4. Retirar producto del carrito")
        print("5. Mostrar carrito")
        print("6. Total del carrito")
        print("7. Comprar")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                menuAdmin()
            case "2":
                mostrar_disponibles()
            case "3":
                agregar_al_carrito()
            case "4":
                retirar_del_carrito()
            case "5":
                mostrar_carrito()
            case "6":
                total_carrito()
            case "7":
                comprar()
            case "8":
                print("Saliendo de la tienda. ¡Hasta luego!")
                break

if __name__ == "__main__":
    menu()


    