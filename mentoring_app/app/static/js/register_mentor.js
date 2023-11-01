document.addEventListener('DOMContentLoaded', function() {
    let pasoActual = 1;

    function mostrarPaso(paso) {
        document.querySelectorAll('.paso').forEach(p => p.style.display = 'none');
        document.querySelector(`.paso${paso}`).style.display = 'block';
    }

    function validarPaso1() {
        const inputs = document.querySelectorAll('.paso1 input[required]');
        let paso1Valido = true;
        inputs.forEach(input => {
            if (!input.checkValidity()) {
                paso1Valido = false;
                input.classList.add('is-invalid');
            } else {
                input.classList.remove('is-invalid');
            }
        });

        return paso1Valido;
    }

    function continuarPaso1() {
        if (validarPaso1()) {
            pasoActual = 2;
            mostrarPaso(pasoActual);
        }
    }

    function volverAtras() {
        if (pasoActual === 2) {
            pasoActual = 1;
            mostrarPaso(pasoActual);
        }
    }

    document.getElementById('continuar1').addEventListener('click', function(event) {
        event.preventDefault();
        continuarPaso1();
    });

    document.querySelector('.btn-secondary').addEventListener('click', function(event) {
        event.preventDefault();
        volverAtras();
    });

    document.querySelector('.btn-volver').addEventListener('click', function(event) {
        event.preventDefault();
        volverAtras();
    });
});
