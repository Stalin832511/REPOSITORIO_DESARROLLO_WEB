const imageUrlInput = document.getElementById("imageUrl");
const addBtn = document.getElementById("addBtn");
const deleteBtn = document.getElementById("deleteBtn");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// AGREGAR IMAGEN
addBtn.addEventListener("click", () => {
    const url = imageUrlInput.value.trim();

    if (url === "") {
        alert("Por favor ingresa una URL válida.");
        return;
    }

    const img = document.createElement("img");
    img.src = url;

    img.addEventListener("click", () => selectImage(img));

    gallery.appendChild(img);
    imageUrlInput.value = "";
});

// SELECCIONAR IMAGEN
function selectImage(img) {
    const images = document.querySelectorAll(".gallery img");

    images.forEach(image => image.classList.remove("selected"));

    img.classList.add("selected");
    selectedImage = img;
}

// ELIMINAR IMAGEN
deleteBtn.addEventListener("click", () => {
    if (selectedImage) {
        selectedImage.remove();
        selectedImage = null;
    } else {
        alert("Selecciona una imagen para eliminar.");
    }
});

// ATAJOS DE TECLADO
document.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        addBtn.click();
    }

    if (e.key === "Delete") {
        deleteBtn.click();
    }
});
