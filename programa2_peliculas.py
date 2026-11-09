"""Programa 2: altas, bajas y modificaciones de peliculas."""
from funciones_peliculas import (leer_peliculas, guardar_peliculas,
                                 id_pelicula_disponible, validar_genero)


def alta() -> None:
    """Agrega una pelicula validando su genero."""
    id_pelicula = input("ID de pelicula: ").strip()
    if not id_pelicula.isdigit() or not id_pelicula_disponible(id_pelicula):
        print("ID no valido o ya utilizado.")
        return
    nombre = input("Nombre de pelicula: ").strip()
    id_genero = input("ID de genero: ").strip()
    if not validar_genero(id_genero):
        print("El genero no existe o esta dado de baja.")
        return
    resena = input("Resena: ").strip()
    poster = input("URL del poster (puede quedar vacia): ").strip()
    peliculas = leer_peliculas()
    peliculas.append({"id_pelicula": id_pelicula, "nombre_pelicula": nombre,
                      "id_genero": id_genero, "resena": resena,
                      "url_poster": poster, "baja": "0"})
    guardar_peliculas(peliculas)
    print("Pelicula agregada.")


def baja() -> None:
    """Da de baja logicamente una pelicula."""
    id_pelicula = input("ID de pelicula a dar de baja: ").strip()
    peliculas = leer_peliculas()
    for pelicula in peliculas:
        if pelicula["id_pelicula"] == id_pelicula and pelicula["baja"] == "0":
            pelicula["baja"] = "1"
            guardar_peliculas(peliculas)
            print("Pelicula dada de baja.")
            return
    print("No se encontro la pelicula activa.")


def modificar() -> None:
    """Modifica una pelicula guardando el registro anterior como baja."""
    id_pelicula = input("ID de pelicula a modificar: ").strip()
    peliculas = leer_peliculas()
    for pelicula in peliculas:
        if pelicula["id_pelicula"] == id_pelicula and pelicula["baja"] == "0":
            nombre = input("Nuevo nombre: ").strip()
            id_genero = input("Nuevo ID de genero: ").strip()
            if not validar_genero(id_genero):
                print("El genero no existe o esta dado de baja.")
                return
            resena = input("Nueva resena: ").strip()
            poster = input("Nueva URL del poster: ").strip()
            pelicula["baja"] = "1"
            peliculas.append({"id_pelicula": id_pelicula,
                              "nombre_pelicula": nombre,
                              "id_genero": id_genero, "resena": resena,
                              "url_poster": poster, "baja": "0"})
            guardar_peliculas(peliculas)
            print("Pelicula modificada.")
            return
    print("No se encontro la pelicula activa.")


def menu() -> None:
    """Muestra el menu de administracion de peliculas."""
    while True:
        print("\n--- ABM DE PELICULAS ---")
        print("1. Alta  2. Baja  3. Modificar  0. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "0":
            break
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
