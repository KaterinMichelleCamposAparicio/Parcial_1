"""
1. Una tienda local vende diversos productos, cada vez que un cliente
hace una compra niña mary se encarga de anotarlo en una libreta. A su
vez, con una calculadora le da el total a cada cliente y les da su
respectivo vuelto en caso de necesitarlo.

Niña mary también se encarga de atender a los proveedores que
le dan cierta cantidad de producto y un precio sugerido de venta,
propón una solución dentro de tu programa para ayudarle.

"""
#para almacenar  elementos
#Clase para productos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#Clase para clientes
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.compras = []

    def agregar_compra(self, producto):
        self.compras.append(producto)

    def calcular_total(self):
        return sum(producto.precio for producto in self.compras)

    def calcular_vuelto(self, pago):
        total = self.calcular_total()
        return pago - total if pago >= total else 0
    
#Clase para los proveedores
class Proveedor:
    def __init__(self, nombre, producto, precio_sugerido):
        self.nombre = nombre
        self.producto = producto
        self.precio_sugerido = precio_sugerido

def ingresar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    return Producto(nombre, precio)

def ingresar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cliente = Cliente(nombre)
    while True:
        producto = ingresar_producto()
        cliente.agregar_compra(producto)
        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break
    return cliente

def ingresar_proveedor():
    nombre = input("Ingrese el nombre del proveedor: ")
    producto = input("Ingrese el nombre del producto que ofrece: ")
    precio_sugerido = float(input("Ingrese el precio sugerido de venta: "))
    return Proveedor(nombre, producto, precio_sugerido)

def menu_principal():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrar Cliente")
        print("2. Registrar Proveedor")
        print("3. Salir")
        opcion = input("Ingrese su opción (1/2/3): ")

# verificar si el pago del cliente es suficiente para cubrir el total de la compra
        if opcion == '1':
            cliente = ingresar_cliente()
            pago = float(input(f"¿Cuánto pagó {cliente.nombre}? "))
            total = cliente.calcular_total()
            vuelto = cliente.calcular_vuelto(pago)

            print(f"Total a pagar: {total:.2f}, Vuelto: {vuelto:.2f}")
        elif opcion == '2':
            proveedor = ingresar_proveedor()
            print(f"Proveedor registrado: {proveedor.nombre}, Producto: {proveedor.producto}, Precio Sugerido: {proveedor.precio_sugerido:.2f}")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu_principal()