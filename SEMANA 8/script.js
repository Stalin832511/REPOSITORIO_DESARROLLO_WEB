// ===== BOTÓN ALERTA =====
function mostrarAlerta() {
    alert("¡Hola! Esta es una alerta personalizada.");
}


// ===== VALIDACIÓN FORMULARIO =====
document.getElementById("formulario").addEventListener("submit", function(e){

    e.preventDefault();

    let nombre = document.getElementById("nombre").value.trim();
    let correo = document.getElementById("correo").value.trim();
    let mensaje = document.getElementById("mensaje").value.trim();

    let valido = true;

    // Limpiar errores
    document.getElementById("errorNombre").textContent = "";
    document.getElementById("errorCorreo").textContent = "";
    document.getElementById("errorMensaje").textContent = "";

    // Validar nombre
    if(nombre === ""){
        document.getElementById("errorNombre").textContent = "Nombre obligatorio";
        valido = false;
    }

    // Validar correo
    if(correo === ""){
        document.getElementById("errorCorreo").textContent = "Correo obligatorio";
        valido = false;
    }

    // Validar mensaje
    if(mensaje === ""){
        document.getElementById("errorMensaje").textContent = "Mensaje obligatorio";
        valido = false;
    }

    if(valido){
        alert("Formulario enviado correctamente");
        document.getElementById("formulario").reset();
    }

});
