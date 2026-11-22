from datetime import date

from base_datos import crear_tablas, guardar_libro, cargar_libros, cargar_estudiantes, guardar_estudiante, guardar_prestamo, guardar_devolucion, cargar_prestamos

from biblioteca import Biblioteca
from libros import Libro
from estudiantes import Estudiante
from prestamos import Prestamos

crear_tablas()
b = Biblioteca() #pruebita para ver si me devuelve la cantidad de este libro

for fila in cargar_libros():
    libro = Libro(fila[0], fila[1])
    libro.disponible = bool(fila[2])
    b.agregar_libro(libro)

for fila in cargar_estudiantes():
    b.agregar_estudiante(Estudiante(fila[1], fila[0]))

for fila in cargar_prestamos():
    titulo_p, dni_p, f_prestamo, f_devolucion = fila
    libro_p = None
    for l in b.libros:
            libro_p = l
            break
    estudiante_p = None
    for e in b.estudiantes:
        if e.dni == dni_p:
            estudiante_p = e
            break
    if libro_p and estudiante_p:
        p = Prestamos(libro_p, estudiante_p, f_prestamo)
        p.fecha_devolucion = f_devolucion
        b.prestamos.append(p)

while True:
    print("\n1. Agregar libro")
    print("2. Ver libros")
    print("3. Agregar estudiante")
    print("4. Ver estudiantes")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Ver préstamos")
    print("8. Ver historial")
    print("9. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        libro = Libro(titulo, autor)
        b.agregar_libro(libro)
        guardar_libro(libro)
        print("Libro agregado.")
    elif opcion == "2":
        for libro in b.libros:
            print(libro.titulo, "-", libro.autor)
    elif opcion == "3":
        nombre = input("Nombre del estudiante: ")
        dni = input("DNI: ")
        estudiante = Estudiante(nombre, dni)
        resultado = b.agregar_estudiante(estudiante)
        if resultado == False:
            print("Ya existe un estudiante con ese DNI")
        else:
            guardar_estudiante(estudiante)
            print("Estudiante agregado")
    elif opcion == "4":
        for estudiante in b.estudiantes:
            print(estudiante.nombre, "-", estudiante.dni)
    elif opcion == "5":
        titulo = input("Título del libro: ")
        dni = input("DNI del estudiante: ")
        resultado = b.prestar(titulo, dni)
        if resultado == True:
            guardar_prestamo(titulo, dni, date.today())
            print("Préstamo realizado.")
        elif resultado == "estudiante_no_registrado":
            print("El estudiante no está registrado.")
        elif resultado == "libro_no_disponible":
            print("El libro no está disponible.")
    elif opcion == "6":
        titulo = input("Título del libro: ")
        dni = input("DNI del estudiante: ")
        if b.devolver(titulo, dni):
            guardar_devolucion(titulo, dni, date.today())
            print("Libro devuelto.")
        else:
            print("No se encontró ese préstamo.")
    elif opcion == "7":
        for prestamo in b.prestamos:
            if prestamo.fecha_devolucion is None:
                print(prestamo.libro.titulo, "-", prestamo.estudiante.nombre, "-", prestamo.fecha_prestamo)
    elif opcion == "8":
        for prestamo in b.prestamos:
            if prestamo.fecha_devolucion is None:
                devolucion = "pendiente"
            else:
                devolucion = prestamo.fecha_devolucion
            print(prestamo.libro.titulo, "-", prestamo.estudiante.nombre, "-", prestamo.fecha_prestamo, "-", devolucion)
    elif opcion == "9":
        break