const productos = [
    {
        nombre: "Laptop Lenovo",
        precio: 850,
        descripcion: "Equipo portátil para estudios universitarios"
    },
    {
        nombre: "Teclado Mecánico",
        precio: 65,
        descripcion: "Teclado con retroiluminación RGB"
    },
    {
        nombre: "Mouse Inalámbrico",
        precio: 30,
        descripcion: "Mouse ergonómico de alta precisión"
    }
];

// Contador para productos nuevos
let contadorProductos = productos.length + 1;

// Renderiza la lista de productos
function renderizarListaProductos() {
    const lista = document.getElementById("listaProductos");
    lista.innerHTML = "";

    productos.forEach((producto, index) => {
        const item = document.createElement("li");
        item.innerHTML = `
            <strong>${index + 1}. ${producto.nombre}</strong><br>
            Precio: $${producto.precio}<br>
            Descripción: ${producto.descripcion}
        `;
        lista.appendChild(item);
    });
}

// Renderizado inicial
document.addEventListener("DOMContentLoaded", renderizarListaProductos);

// Evento del botón
document.getElementById("btnAgregarProducto").addEventListener("click", () => {

    const nuevoProducto = {
        nombre: `Producto ${contadorProductos}`,
        precio: 50 + contadorProductos,
        descripcion: "Producto agregado dinámicamente al final de la lista"
    };

    productos.push(nuevoProducto);
    contadorProductos++;
    renderizarListaProductos();

    // Confirmación visual
    console.log("Producto agregado correctamente");
});
