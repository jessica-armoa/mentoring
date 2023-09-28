function continuar(pasoActual, pasoSiguiente) {
    var pasoActualElement = document.querySelector('.paso' + pasoActual);
    var pasoSiguienteElement = document.querySelector('.paso' + pasoSiguiente);

    pasoActualElement.style.display = 'none';
    pasoSiguienteElement.style.display = 'block';
}

function volverAtras(pasoActual, pasoAnterior) {
    var pasoActualElement = document.querySelector('.paso' + pasoActual);
    var pasoAnteriorElement = document.querySelector('.paso' + pasoAnterior);

    pasoActualElement.style.display = 'none';
    pasoAnteriorElement.style.display = 'block';
}

//Desabilita el boton hasta que los campos obligatorios esten completos
document.addEventListener('DOMContentLoaded', function() {
    const continuar1 = document.getElementById('continuar1');
    const continuar2 = document.getElementById('continuar2');

    const camposObligatorios1 = document.querySelectorAll('.paso1 [required]');
    const camposObligatorios2 = document.querySelectorAll('.paso2 [required]');

    // Función para verificar si los campos están completos
    function verificarCamposCompletos(campos) {
        return Array.from(campos).every(campo => campo.value.trim() !== '');
    }

    // Función para habilitar o deshabilitar el botón de continuar
    function habilitarContinuar(botones, campos) {
        botones.disabled = !verificarCamposCompletos(campos);
    }

    // Evento de escucha para el botón de continuar en el paso 1
    camposObligatorios1.forEach(campo => {
        campo.addEventListener('input', function() {
            habilitarContinuar(continuar1, camposObligatorios1);
        });
    });

    // Evento de escucha para el botón de continuar en el paso 2
    camposObligatorios2.forEach(campo => {
        campo.addEventListener('input', function() {
            habilitarContinuar(continuar2, camposObligatorios2);
        });
    });

    // Deshabilitar botones al cargar la página
    habilitarContinuar(continuar1, camposObligatorios1);
    habilitarContinuar(continuar2, camposObligatorios2);

    function validarCampos(campos) {
        let camposValidos = true;
        campos.forEach(campo => {
            if (campo.checkValidity() === false) {
                camposValidos = false;
                campo.classList.add('is-invalid');
            } else {
                campo.classList.remove('is-invalid');

                // Verificar si el campo es una contraseña y tiene al menos 8 caracteres
                if (campo.type === 'password' && campo.value.length >= 8) {
                    campo.classList.add('was-validated');
                }
            }
        });
        return camposValidos;
    }


    continuar1.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario

        const camposValidos = validarCampos(camposObligatorios1);

        if (camposValidos) {
            const formElement = document.querySelector('form');
            formElement.classList.add('was-validated');

            // Mostrar validaciones por 1 segundo
            setTimeout(function() {
                formElement.classList.remove('was-validated');
                continuar(1, 2); // Llamada a la función de continuar
            }, 1000);
        }
    });

    continuar2.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario

        const camposValidos = validarCampos(camposObligatorios2);

        if (camposValidos) {
            const formElement = document.querySelector('form');
            formElement.classList.add('was-validated');

            // Mostrar validaciones por 1 segundo
            setTimeout(function() {
                formElement.classList.remove('was-validated');
                continuar(2, 3); // Llamada a la función de continuar
            }, 1000);
        }
    });
});


//Verifica que el username sea valido en Calendly
document.addEventListener('DOMContentLoaded', function() {
        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault(); // Prevenir el envío del formulario

            // Obtener el nombre de usuario ingresado por el usuario
            var username = document.querySelector('#validationTooltipUsername').value;

            // Realizar una solicitud para verificar el nombre de usuario en Calendly
            fetch('/validate_calendly_username/?username=' + username)
                .then(response => response.json())
                .then(data => {
                    if (data.valid) {
                        // Si el nombre de usuario es válido, enviar el formulario
                        this.submit();
                    } else {
                        // Si el nombre de usuario no es válido, mostrar un mensaje de error
                        document.querySelector('#calendly-error').innerText = 'Error al encontrar el username en Calendly, asegurese de que su perfil se haya creado antes de volver aquí';
                        document.querySelector('#calendly-error').style.display = 'block';
                    }
                });
        });
    });
/*
document.addEventListener('DOMContentLoaded', function() {
    const continuar1 = document.getElementById('continuar1');
    const continuar2 = document.getElementById('continuar2');

    const camposObligatorios1 = document.querySelectorAll('.paso1 [required]');
    const camposObligatorios2 = document.querySelectorAll('.paso2 [required]');

    // Función para verificar si los campos están completos
    function verificarCamposCompletos(campos) {
        return Array.from(campos).every(campo => campo.value.trim() !== '');
    }

    // Función para habilitar o deshabilitar el botón de continuar
    function habilitarContinuar(botones, campos) {
        botones.disabled = !verificarCamposCompletos(campos);
    }

    // Evento de escucha para el botón de continuar en el paso 1
    camposObligatorios1.forEach(campo => {
        campo.addEventListener('input', function() {
            habilitarContinuar(continuar1, camposObligatorios1);
        });
    });

    // Evento de escucha para el botón de continuar en el paso 2
    camposObligatorios2.forEach(campo => {
        campo.addEventListener('input', function() {
            habilitarContinuar(continuar2, camposObligatorios2);
        });
    });

    // Deshabilitar botones al cargar la página
    habilitarContinuar(continuar1, camposObligatorios1);
    habilitarContinuar(continuar2, camposObligatorios2);

    function validarCampos(campos) {
        let camposValidos = true;
        campos.forEach(campo => {
            if (campo.checkValidity() === false) {
                camposValidos = false;
                campo.classList.add('is-invalid');
            } else {
                campo.classList.remove('is-invalid');
            }
        });
        return camposValidos;
    }

    continuar1.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario

        const camposValidos = validarCampos(camposObligatorios1);

        if (camposValidos) {
            continuar(1, 2); // Llamada a la función de continuar
        }
    });

    continuar2.addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío del formulario

        const camposValidos = validarCampos(camposObligatorios2);

        if (camposValidos) {
            continuar(2, 3); // Llamada a la función de continuar
        }
    });
});
*/

