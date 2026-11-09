"""Programa 4: busqueda de peliculas por genero o nombre."""
from funciones_peliculas import leer_peliculas
from funciones_generos import leer_generos


def consultar_por_genero() -> None:
    """Muestra peliculas activas de un genero."""
    id_genero = input("ID de genero: ").strip()
    generos = {g["id_genero"]: g["nombre"] for g in leer_generos()
               if g["baja"] == "0"}
    if id_genero not in generos:
        print("Genero inexistente.")
        return
    for pelicula in leer_peliculas():
        if pelicula["baja"] == "0" and pelicula["id_genero"] == id_genero:
            print(pelicula["id_pelicula"], "-", pelicula["nombre_pelicula"])


def consultar_por_nombre() -> None:
    """Busca peliculas activas por una parte del nombre."""
    nombre = input("Nombre o parte del nombre: ").strip().lower()
    for pelicula in leer_peliculas():
        if pelicula["baja"] == "0" and nombre in pelicula["nombre_pelicula"].lower():
            print(pelicula["id_pelicula"], "-", pelicula["nombre_pelicula"])


def menu() -> None:
    """Muestra el menu de consultas."""
    while True:
        print("\n--- CONSULTA DE PELICULAS ---")
        print("1. Buscar por genero  2. Buscar por nombre  0. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            consultar_por_genero()
        elif opcion == "2":
            consultar_por_nombre()
        elif opcion == "0":
            break
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
