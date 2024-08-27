"""Una empresa cuenta con dos tipos de empleados: aquellos con plaza
fija y aquellos que trabajan por horas. Se han registrado los datos de
ambos tipos y, al generar la planilla de pago, se realizan dos cálculos
diferentes. A los empleados de plaza fija se les paga el salario base más
comisiones, mientras que a los empleados por horas se les paga en
función de la cantidad de horas trabajadas."""


# Clase para representar a un Empleado en la empresa
class Empleado:
    def __init__(self, nombre, edad, anios_trabajados):
        self.nombre = nombre  # Nombre del empleado
        self.edad = edad  # Edad del empleado
        self.anios_trabajados = anios_trabajados  # Años que ha trabajado en la empresa
        self.bono = self.calcular_bono()  # Bono adicional por antigüedad

    # Método para calcular el bono por años trabajados
    def calcular_bono(self):
        if self.anios_trabajados > 5:
            return 500  # Bono de $500 si ha trabajado más de 5 años
        return 0  # Sin bono si ha trabajado 5 años o menos

    # Método para calcular el pago total del empleado (debe ser implementado en subclases)
    def calcular_pago(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    # Método para generar y mostrar el recibo de pago del empleado
    def generar_recibo(self):
        print(f"\nRecibo de pago para {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Años trabajados: {self.anios_trabajados}")
        print(f"Bono por antigüedad: ${self.bono}")
        print(f"Total a pagar: ${self.calcular_pago()}\n")


# Clase para representar a un Empleado con Plaza Fija
class EmpleadoPlazaFija(Empleado):
    def __init__(self, nombre, edad, anios_trabajados, salario_base, comisiones):
        super().__init__(nombre, edad, anios_trabajados)
        self.salario_base = salario_base  # Salario base del empleado
        self.comisiones = comisiones  # Comisiones adicionales

    # Método para calcular el pago total del empleado con plaza fija
    def calcular_pago(self):
        return self.salario_base + self.comisiones + self.bono  # Salario base + comisiones + bono


# Clase para representar a un Empleado que trabaja por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, edad, anios_trabajados, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, edad, anios_trabajados)
        self.horas_trabajadas = horas_trabajadas  # Número de horas trabajadas
        self.tarifa_por_hora = tarifa_por_hora  # Tarifa por hora

    # Método para calcular el pago total del empleado por horas
    def calcular_pago(self):
        return self.horas_trabajadas * self.tarifa_por_hora + self.bono  # Pago por horas trabajadas + bono


# Función para ingresar los datos de un empleado con plaza fija
def registrar_empleado_fijo():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    anios_trabajados = int(input("Ingrese los años trabajados: "))
    salario_base = float(input("Ingrese el salario base: "))
    comisiones = float(input("Ingrese las comisiones: "))
    empleado = EmpleadoPlazaFija(nombre, edad, anios_trabajados, salario_base, comisiones)
    return empleado


# Función para ingresar los datos de un empleado que trabaja por horas
def registrar_empleado_por_horas():
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado: "))
    anios_trabajados = int(input("Ingrese los años trabajados: "))
    horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
    tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
    empleado = EmpleadoPorHoras(nombre, edad, anios_trabajados, horas_trabajadas, tarifa_por_hora)
    return empleado


# Registro de empleados
print("Registro de empleados con plaza fija")
empleado_fijo = registrar_empleado_fijo()
print("Registro de empleados por horas")
empleado_por_horas = registrar_empleado_por_horas()

# Generación de recibos de pago
empleado_fijo.generar_recibo()
empleado_por_horas.generar_recibo()
