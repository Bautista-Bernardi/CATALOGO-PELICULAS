"""Programa 3: consulta de generos activos."""
from funciones_generos import leer_generos


def consultar() -> None:
    """Lista los generos que no tienen baja."""
    print("\n--- GENEROS ACTIVOS ---")
    for genero in leer_generos():
        if genero["baja"] == "0":
            print(genero["id_genero"], "-", genero["nombre"])


if __name__ == "__main__":
    consultar()
