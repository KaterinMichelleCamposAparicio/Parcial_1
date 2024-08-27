"""Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos."""


# Clase para representar una Habitación en el hotel
class Habitacion:
    def __init__(self, tipo, precio):
        self.tipo = tipo  # Tipo de habitación (Económica, Estándar, Suite)
        self.precio = precio  # Precio por noche de la habitación

    def __str__(self):
        return f"Habitación: {self.tipo}, Precio por noche: ${self.precio}"


# Clase para representar un Cliente
class Cliente:
    def __init__(self, nombre, dni, correo, telefono):
        self.nombre = nombre  # Nombre del cliente
        self.dni = dni  # DNI del cliente
        self.correo = correo  # Correo electrónico del cliente
        self.telefono = telefono  # Número de teléfono del cliente
        self.habitacion = None  # Habitación seleccionada por el cliente
        self.noches = 0  # Número de noches que el cliente se hospedará
        self.servicios_extras = []  # Lista de servicios extra que el cliente solicita

    # Método para seleccionar una habitación y la cantidad de noches
    def seleccionar_habitacion(self, habitacion, noches):
        self.habitacion = habitacion
        self.noches = noches

    # Método para agregar un servicio extra a la cuenta del cliente
    def agregar_servicio_extra(self, servicio):
        self.servicios_extras.append(servicio)

    # Método para calcular el total a pagar por el cliente
    def calcular_total(self):
        total = self.habitacion.precio * self.noches  # Costo de la habitación
        for servicio in self.servicios_extras:
            total += servicio.precio  # Suma de costos adicionales por servicios extra
        return total

    # Método para generar y mostrar la factura del cliente
    def generar_factura(self):
        print(f"\nFactura para {self.nombre} (DNI: {self.dni})")
        print(f"Correo electrónico: {self.correo}")
        print(f"Teléfono: {self.telefono}")
        print(f"{self.habitacion}")
        print(f"Noches: {self.noches}")
        for servicio in self.servicios_extras:
            print(f"Servicio extra: {servicio.descripcion} - ${servicio.precio}")
        print(f"Total a pagar: ${self.calcular_total()}\n")


# Clase para representar un Servicio Extra que el cliente puede solicitar
class ServicioExtra:
    def __init__(self, descripcion, precio):
        self.descripcion = descripcion  # Descripción del servicio (ej. Uso de piscina)
        self.precio = precio  # Precio del servicio


# Función para que el cliente seleccione una habitación
def seleccionar_habitacion(habitaciones):
    print("Seleccione la habitación:")
    for i, habitacion in enumerate(habitaciones):
        print(f"{i + 1}. {habitacion}")  # Muestra las habitaciones disponibles
    opcion = int(input("Ingrese el número de la habitación deseada: ")) - 1
    noches = int(input("Ingrese el número de noches de estancia: "))
    return habitaciones[opcion], noches


# Función para que el cliente seleccione servicios extras
def seleccionar_servicios_extras(servicios_extras):
    seleccionados = []
    while True:
        print("\nSeleccione un servicio extra (o 0 para finalizar):")
        for i, servicio in enumerate(servicios_extras):
            print(f"{i + 1}. {servicio.descripcion} - ${servicio.precio}")  # Muestra los servicios extra disponibles
        opcion = int(input("Ingrese el número del servicio extra: ")) - 1
        if opcion == -1:
            break  # Sale del ciclo si el cliente no desea más servicios extra
        seleccionados.append(servicios_extras[opcion])
    return seleccionados



# Lista de habitaciones disponibles en el hotel
habitaciones = [
    Habitacion("Económica", 50),
    Habitacion("Estándar", 80),
    Habitacion("Suite", 120)
]

# Lista de servicios extra disponibles en el hotel
servicios_extras = [
    ServicioExtra("Uso de piscina", 20),
    ServicioExtra("Cancha de golf", 30)
]

# Ingreso de datos del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")
dni_cliente = input("Ingrese el DNI del cliente: ")
correo_cliente = input("Ingrese el correo electrónico del cliente: ")
telefono_cliente = input("Ingrese el número de teléfono del cliente: ")

# Creación de un objeto Cliente con los datos ingresados
cliente = Cliente(nombre_cliente, dni_cliente, correo_cliente, telefono_cliente)

# Selección de habitación y noches de estancia
habitacion, noches = seleccionar_habitacion(habitaciones)
cliente.seleccionar_habitacion(habitacion, noches)

# Selección de servicios extras por parte del cliente
extras = seleccionar_servicios_extras(servicios_extras)
for servicio in extras:
    cliente.agregar_servicio_extra(servicio)

# Generación de la factura del cliente
cliente.generar_factura()

