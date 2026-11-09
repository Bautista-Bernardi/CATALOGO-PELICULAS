"""Funciones para administrar las peliculas del catalogo."""
import csv
import os
from funciones_generos import genero_activo

ARCHIVO_PELICULAS = "peliculas.csv"


def inicializar_peliculas() -> None:
    """Crea el archivo de peliculas con encabezados si no existe."""
    if not os.path.exists(ARCHIVO_PELICULAS):
        with open(ARCHIVO_PELICULAS, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["id_pelicula", "nombre_pelicula", "id_genero",
                               "resena", "url_poster", "baja"])


def leer_peliculas() -> list[dict[str, str]]:
    """Devuelve todos los registros de peliculas."""
    inicializar_peliculas()
    with open(ARCHIVO_PELICULAS, "r", newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def guardar_peliculas(peliculas: list[dict[str, str]]) -> None:
    """Guarda la lista completa de peliculas en el CSV."""
    campos = ["id_pelicula", "nombre_pelicula", "id_genero",
              "resena", "url_poster", "baja"]
    with open(ARCHIVO_PELICULAS, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(peliculas)


def pelicula_activa(id_pelicula: str) -> bool:
    """Indica si existe una pelicula activa con ese ID."""
    return any(p["id_pelicula"] == str(id_pelicula) and p["baja"] == "0"
               for p in leer_peliculas())


def id_pelicula_disponible(id_pelicula: str) -> bool:
    """Indica si el ID no pertenece a una pelicula activa."""
    return not pelicula_activa(id_pelicula)


def validar_genero(id_genero: str) -> bool:
    """Valida que el genero elegido exista y este activo."""
    return genero_activo(id_genero)
