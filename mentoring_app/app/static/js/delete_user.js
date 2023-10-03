mostrarModalBtn.addEventListener('click', function () {
    // Muestra el modal
    var myModal = new bootstrap.Modal(document.getElementById('del_user_modal'));
    myModal.show();
});

var cancelBtn = document.querySelector('#del_user_modal .modal-footer .btn-secondary');

cancelBtn.addEventListener('click', function () {
    // Oculta el modal
    var myModal = new bootstrap.Modal(document.getElementById('del_user_modal'));
    myModal.hide();
});
