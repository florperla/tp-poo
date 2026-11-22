# Sistema de Biblioteca

Sistema de consola en Python para gestionar una biblioteca que presta libros a estudiantes. Trabajo práctico final.

## Funcionalidades

- Agregar y listar libros
- Agregar y listar estudiantes (sin DNI repetido)
- Prestar libros (con fecha de préstamo)
- Devolver libros (con fecha de devolución)
- Ver préstamos activos
- Ver historial completo de préstamos
- Búsqueda de títulos sin distinguir mayúsculas/minúsculas
- Persistencia de datos con SQLite

## Estructura del proyecto

```
├── main.py          # Menú de consola
├── biblioteca.py    # Clase Biblioteca (lógica de préstamos)
├── libro.py         # Clase Libro
├── estudiante.py    # Clase Estudiante
├── prestamos.py     # Clase Prestamos
├── base_datos.py    # Funciones de acceso a SQLite
└── biblioteca.db    # Base de datos (se crea automáticamente)
```

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas (`sqlite3` viene incluido con Python)

## Cómo ejecutarlo

```bash
python3 main.py
```

La base de datos `biblioteca.db` se crea sola la primera vez.

## Modelo de datos

- **libros**: id, titulo, autor, disponible
- **estudiantes**: dni, nombre
- **prestamos**: id, libro_id, estudiante_dni, fecha_prestamo, fecha_devolucion

## Autora

Maria Florencia Perla - Programación orientada a objetos - 1er año - 2026
