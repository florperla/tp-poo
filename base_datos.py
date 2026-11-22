import sqlite3

from datetime import date

def conectar():
    return sqlite3.connect("biblioteca.db")

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            disponible INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            dni TEXT PRIMARY KEY,
            nombre TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            libro_id INTEGER,
            estudiante_dni TEXT,
            fecha_prestamo TEXT,
            fecha_devolucion TEXT
        )
    """)

    conexion.commit()
    conexion.close()

def guardar_libro(libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libros (titulo, autor, disponible) VALUES (?, ?, ?)",
        (libro.titulo, libro.autor, 1)
    )
    conexion.commit()
    conexion.close()

def cargar_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT titulo, autor, disponible FROM libros")
    filas = cursor.fetchall()
    conexion.close()
    return filas

def guardar_estudiante(estudiante):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO estudiantes (dni, nombre) VALUES (?, ?)",
        (estudiante.dni, estudiante.nombre)
    )
    conexion.commit()
    conexion.close()

def cargar_estudiantes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT dni, nombre FROM estudiantes")
    filas = cursor.fetchall()
    conexion.close()
    return filas

def guardar_prestamo(titulo, dni, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT id FROM libros WHERE LOWER(titulo) = LOWER(?) AND disponible = 1 LIMIT 1",
        (titulo,)
    )
    fila = cursor.fetchone()
    libro_id = fila[0]
    cursor.execute(
        "INSERT INTO prestamos (libro_id, estudiante_dni, fecha_prestamo) VALUES (?, ?, ?)",
        (libro_id, dni, str(fecha))
    )
    cursor.execute("UPDATE libros SET disponible = 0 WHERE id = ?", (libro_id,))
    conexion.commit()
    conexion.close()

def guardar_devolucion(titulo, dni, fecha):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT prestamos.id, prestamos.libro_id
        FROM prestamos
        JOIN libros ON libros.id = prestamos.libro_id
        WHERE LOWER(libros.titulo) = LOWER(?) AND prestamos.estudiante_dni = ?
        AND prestamos.fecha_devolucion IS NULL
        LIMIT 1
    """, (titulo, dni))
    fila = cursor.fetchone()
    if fila:
        cursor.execute("UPDATE prestamos SET fecha_devolucion = ? WHERE id = ?", (str(fecha), fila[0]))
        cursor.execute("UPDATE libros SET disponible = 1 WHERE id = ?", (fila[1],))
    conexion.commit()
    conexion.close()


def cargar_prestamos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.titulo, prestamos.estudiante_dni, prestamos.fecha_prestamo, prestamos.fecha_devolucion
        FROM prestamos
        JOIN libros ON libros.id = prestamos.libro_id
    """)
    filas = cursor.fetchall()
    conexion.close()
    return filas