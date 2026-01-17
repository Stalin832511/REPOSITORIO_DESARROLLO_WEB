const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmar = document.getElementById("confirmar");
const edad = document.getElementById("edad");
const btnEnviar = document.getElementById("btnEnviar");

function validarNombre() {
    if (nombre.value.length >= 3) {
        setValido(nombre, "errorNombre", "");
        return true;
    } else {
        setInvalido(nombre, "errorNombre", "El nombre debe tener al menos 3 caracteres");
        return false;
    }
}

function validarCorreo() {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (regex.test(correo.value)) {
        setValido(correo, "errorCorreo", "");
        return true;
    } else {
        setInvalido(correo, "errorCorreo", "Correo electrónico no válido");
        return false;
    }
}

function validarPassword() {
    const regex = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;
    if (password.value.length >= 8 && regex.test(password.value)) {
        setValido(password, "errorPassword", "");
        return true;
    } else {
        setInvalido(password, "errorPassword", "Debe tener 8 caracteres, un número y un carácter especial");
        return false;
    }
}

function validarConfirmacion() {
    if (confirmar.value === password.value && confirmar.value !== "") {
        setValido(confirmar, "errorConfirmar", "");
        return true;
    } else {
        setInvalido(confirmar, "errorConfirmar", "Las contraseñas no coinciden");
        return false;
    }
}

function validarEdad() {
    if (edad.value >= 18) {
        setValido(edad, "errorEdad", "");
        return true;
    } else {
        setInvalido(edad, "errorEdad", "Debe ser mayor o igual a 18 años");
        return false;
    }
}

function setValido(campo, errorId, mensaje) {
    campo.classList.add("valido");
    campo.classList.remove("invalido");
    document.getElementById(errorId).textContent = mensaje;
}

function setInvalido(campo, errorId, mensaje) {
    campo.classList.add("invalido");
    campo.classList.remove("valido");
    document.getElementById(errorId).textContent = mensaje;
}

function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        btnEnviar.disabled = false;
    } else {
        btnEnviar.disabled = true;
    }
}

nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmar.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault();
    alert("Formulario validado correctamente. Datos enviados con éxito.");
});
