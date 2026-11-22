from datetime import date

from prestamos import Prestamos

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.estudiantes = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_estudiante(self, estudiante):
        for e in self.estudiantes:
            if e.dni == estudiante.dni:
                return False
        self.estudiantes.append(estudiante)
        return True

    def prestar(self, titulo_libro, dni):
        # buscar el libro
        # ponemos una variable vacía como si fuera una caja vacía que luego llenaremos
        libro_encontrado = None
        # el for no chequea que la caja esté o no vacía
        for libro in self.libros:
            if libro.titulo.lower() == titulo_libro.lower() and libro.disponible:
                libro_encontrado = libro
                break

        if libro_encontrado is None:
            return "libro_no_disponible"

        # buscar el estudiante
        estudiante_encontrado = None
        for estudiante in self.estudiantes:
            if estudiante.dni == dni:
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado is None:
            return "estudiante_no_registrado"

        # Si el libro no está disponible se devuelve un False
        libro_encontrado.disponible = False

        # Si el libro está disponible se crea un objeto préstamo
        # con ese libro, ese estudiante y la fecha de hoy. 
        # El .self lo agrega a la lista de prestamos de la biblioteca
        self.prestamos.append(Prestamos(libro_encontrado, estudiante_encontrado, date.today()))
        return True

    def devolver(self, titulo_libro, dni):
        for prestamo in self.prestamos:
            # Si se quiere hacer una devolucion pasamos un titulo 
            # y un dni para que el sistema compare con la funcion 
            # prestamos y si estaba prestado, se hace la devolucion
            if (prestamo.libro.titulo.lower() == titulo_libro.lower() 
                    and prestamo.estudiante.dni == dni
                    and prestamo.fecha_devolucion is None):
                # y cambia nuevamente el estado del libro a disponible
                prestamo.libro.disponible = True
                prestamo.fecha_devolucion = date.today()
                return True
        return False