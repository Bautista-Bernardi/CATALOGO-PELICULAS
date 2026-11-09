const archivoPeliculas = "peliculas.csv";
const archivoGeneros = "generos.csv";

let peliculas = [];
let generos = [];

async function cargarCSV(archivo) {
    const respuesta = await fetch(archivo);
    if (!respuesta.ok) {
        throw new Error("No se pudo cargar " + archivo);
    }
    return await respuesta.text();
}

function convertirCSV(texto) {
    const lineas = texto.trim().split(/\r?\n/);
    const encabezados = lineas[0].split(",");
    return lineas.slice(1).map(linea => {
        const valores = linea.split(",");
        const objeto = {};
        encabezados.forEach((encabezado, indice) => {
            objeto[encabezado] = valores[indice] || "";
        });
        return objeto;
    });
}

async function iniciarCatalogo() {
    try {
        const textoPeliculas = await cargarCSV(archivoPeliculas);
        const textoGeneros = await cargarCSV(archivoGeneros);

        peliculas = convertirCSV(textoPeliculas).filter(p => p.baja === "0");
        generos = convertirCSV(textoGeneros).filter(g => g.baja === "0");

        cargarGeneros();
        mostrarPeliculas(peliculas);
    } catch (error) {
        document.getElementById("catalogo").innerHTML =
            "<p>No se pudieron cargar los archivos CSV. Abrí la página con Live Server.</p>";
        console.error(error);
    }
}

function cargarGeneros() {
    const select = document.getElementById("filtroGenero");
    generos.forEach(genero => {
        const opcion = document.createElement("option");
        opcion.value = genero.id_genero;
        opcion.textContent = genero.nombre;
        select.appendChild(opcion);
    });
}

function mostrarPeliculas(lista) {
    const catalogo = document.getElementById("catalogo");
    catalogo.innerHTML = "";

    document.getElementById("cantidad").textContent =
        "Peliculas encontradas: " + lista.length;

    lista.forEach(pelicula => {
        const genero = generos.find(g => g.id_genero === pelicula.id_genero);
        const tarjeta = document.createElement("article");
        tarjeta.className = "tarjeta";

        const imagen = document.createElement("img");
        imagen.src = pelicula.url_poster;
        imagen.alt = "Poster de " + pelicula.nombre_pelicula;
        imagen.onerror = function () {
            imagen.onerror = null;
            imagen.src = "https://placehold.co/300x450/222222/ffffff?text=" +
                encodeURIComponent(pelicula.nombre_pelicula);
        };

        const contenido = document.createElement("div");
        contenido.className = "contenido";

        const titulo = document.createElement("h2");
        titulo.textContent = pelicula.nombre_pelicula;

        const nombreGenero = document.createElement("p");
        nombreGenero.className = "genero";
        nombreGenero.textContent = genero ? genero.nombre : "Sin genero";

        const resena = document.createElement("p");
        resena.textContent = pelicula.resena;

        contenido.append(titulo, nombreGenero, resena);
        tarjeta.append(imagen, contenido);
        catalogo.appendChild(tarjeta);
    });
}

function aplicarFiltros() {
    const texto = document.getElementById("buscador").value.toLowerCase().trim();
    const idGenero = document.getElementById("filtroGenero").value;

    if (texto.length > 0 && texto.length < 3) {
        mostrarPeliculas([]);
        document.getElementById("cantidad").textContent =
            "Escribi al menos 3 caracteres para buscar.";
        return;
    }

    const resultado = peliculas.filter(pelicula => {
        const coincideNombre = pelicula.nombre_pelicula.toLowerCase().includes(texto);
        const coincideGenero = idGenero === "" || pelicula.id_genero === idGenero;
        return coincideNombre && coincideGenero;
    });

    mostrarPeliculas(resultado);
}

document.getElementById("buscador").addEventListener("input", aplicarFiltros);
document.getElementById("filtroGenero").addEventListener("change", aplicarFiltros);

iniciarCatalogo();
