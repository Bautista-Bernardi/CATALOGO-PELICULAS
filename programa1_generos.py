"""Programa 1: altas, bajas y modificaciones de generos."""
from funciones_generos import (leer_generos, guardar_generos,
                               id_genero_disponible)


def alta() -> None:
    """Agrega un genero nuevo."""
    id_genero = input("ID del genero: ").strip()
    if not id_genero.isdigit() or not id_genero_disponible(id_genero):
        print("ID no valido o ya utilizado por un genero activo.")
        return
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return
    generos = leer_generos()
    generos.append({"id_genero": id_genero, "nombre": nombre, "baja": "0"})
    guardar_generos(generos)
    print("Genero agregado.")


def baja() -> None:
    """Da de baja logicamente un genero."""
    id_genero = input("ID del genero a dar de baja: ").strip()
    generos = leer_generos()
    encontrado = False
    for genero in generos:
        if genero["id_genero"] == id_genero and genero["baja"] == "0":
            genero["baja"] = "1"
            encontrado = True
    guardar_generos(generos)
    print("Genero dado de baja." if encontrado else "No se encontro el genero.")


def modificar() -> None:
    """Modifica un genero conservando el registro anterior."""
    id_genero = input("ID del genero a modificar: ").strip()
    generos = leer_generos()
    for genero in generos:
        if genero["id_genero"] == id_genero and genero["baja"] == "0":
            nombre = input("Nuevo nombre: ").strip()
            if nombre:
                genero["baja"] = "1"
                generos.append({"id_genero": id_genero, "nombre": nombre, "baja": "0"})
                guardar_generos(generos)
                print("Genero modificado.")
                return
    print("No se encontro el genero activo.")


def listar() -> None:
    """Muestra los generos activos."""
    for genero in leer_generos():
        if genero["baja"] == "0":
            print(genero["id_genero"], "-", genero["nombre"])


def menu() -> None:
    """Muestra el menu principal de generos."""
    while True:
        print("\n--- ABM DE GENEROS ---")
        print("1. Alta  2. Baja  3. Modificar  4. Listar  0. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            alta()
        elif opcion == "2":
            baja()
        elif opcion == "3":
            modificar()
        elif opcion == "4":
            listar()
        elif opcion == "0":
            break
        else:
            print("Opcion incorrecta.")


if __name__ == "__main__":
    menu()
