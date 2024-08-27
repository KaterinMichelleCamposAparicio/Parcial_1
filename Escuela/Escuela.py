"""Un colegio privado desea registrar la asistencia de sus estudiantes a las
clases cada docente tiene su listado de los estudiantes en los cuáles se
les ha solicitado colocar a la par de cada estudiante si ha asistido, si
cuenta con permiso o tiene inasistencia con la fecha respectiva.
Actualmente esto se maneja por unas hojas de papel impreso y se
entregan al director al final del día; la escuela necesita agilizar este
proceso."""


# Clase para representar un Estudiante
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del estudiante
        self.asistencias = []  # Lista de asistencias del estudiante

    def __str__(self):
        return self.nombre


# Clase para representar la Asistencia de un Estudiante
class Asistencia:
    def __init__(self, fecha, estado, razon=None):
        self.fecha = fecha  # Fecha de la asistencia
        self.estado = estado  # Estado (Asistió, Permiso, Inasistencia)
        self.razon = razon  # Razón del permiso (si aplica)

    def __str__(self):
        return f"Fecha: {self.fecha}, Estado: {self.estado}" + (f", Razón: {self.razon}" if self.razon else "")


# Clase para representar un Docente
class Docente:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del docente
        self.estudiantes = []  # Lista de estudiantes del docente

    # Método para agregar un estudiante a la lista del docente
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    # Método para mostrar la lista de estudiantes
    def mostrar_estudiantes(self):
        print("Lista de estudiantes:")
        for i, estudiante in enumerate(self.estudiantes, start=1):
            print(f"{i}. {estudiante.nombre}")

    # Método para registrar la asistencia de los estudiantes
    def registrar_asistencia(self):
        fecha = input("Ingrese la fecha de hoy (YYYY-MM-DD): ")
        self.mostrar_estudiantes()  # Mostrar lista de estudiantes al registrar asistencia
        print("Ingrese la asistencia para los estudiantes:")
        for estudiante in self.estudiantes:
            estado = input(f"¿{estudiante.nombre} asistió hoy? (Asistió/Permiso/Inasistencia): ")
            razon = None
            if estado.lower() == "permiso":
                razon = input(f"Ingrese la razón del permiso para {estudiante.nombre}: ")
            asistencia = Asistencia(fecha, estado, razon)
            estudiante.asistencias.append(asistencia)

    # Método para mostrar el registro de asistencia de los estudiantes
    def mostrar_asistencias(self):
        for estudiante in self.estudiantes:
            print(f"\nAsistencias de {estudiante.nombre}:")
            for asistencia in estudiante.asistencias:
                print(asistencia)


# Clase para representar el Director
class Director:
    def revisar_asistencias(self, docentes):
        for docente in docentes:
            print(f"\nRegistro de asistencias para el docente {docente.nombre}:")
            docente.mostrar_asistencias()


# Ejemplo de uso

# Crear una lista de 10 estudiantes
nombres_estudiantes = [
    "Juan Pérez", "Ana Gómez", "Luis Rodríguez", "Marta Fernández", "Carlos Sánchez",
    "Laura Martínez", "Pedro López", "Elena García", "Jorge Hernández", "Sofia Morales"
]

# Crear docente
docente = Docente("Prof. Martínez")

# Agregar los estudiantes al docente
for nombre in nombres_estudiantes:
    estudiante = Estudiante(nombre)
    docente.agregar_estudiante(estudiante)

# Registrar asistencias para el día de hoy
docente.registrar_asistencia()

# Crear director y revisar asistencias
director = Director()
director.revisar_asistencias([docente])

