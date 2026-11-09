"""Funciones para administrar los generos del catalogo."""
import csv
import os

ARCHIVO_GENEROS = "generos.csv"


def inicializar_generos() -> None:
    """Crea el archivo de generos con encabezados si no existe."""
    if not os.path.exists(ARCHIVO_GENEROS):
        with open(ARCHIVO_GENEROS, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["id_genero", "nombre", "baja"])


def leer_generos() -> list[dict[str, str]]:
    """Devuelve todos los registros de generos."""
    inicializar_generos()
    with open(ARCHIVO_GENEROS, "r", newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def guardar_generos(generos: list[dict[str, str]]) -> None:
    """Guarda la lista completa de generos en el CSV."""
    with open(ARCHIVO_GENEROS, "w", newline="", encoding="utf-8") as archivo:
        campos = ["id_genero", "nombre", "baja"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(generos)


def genero_activo(id_genero: str) -> bool:
    """Indica si existe un genero activo con el ID recibido."""
    return any(g["id_genero"] == str(id_genero) and g["baja"] == "0"
               for g in leer_generos())


def id_genero_disponible(id_genero: str) -> bool:
    """Permite reutilizar un ID si no tiene registros activos."""
    return not genero_activo(id_genero)
