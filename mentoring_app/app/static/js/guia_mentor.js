function copiarTexto(id) {
  var inputElement = document.getElementById(id);
  inputElement.select();
  document.execCommand('copy');

  var botonCopiar = document.getElementById('button-copiar-' + id);
  botonCopiar.innerText = 'Copiado';

  setTimeout(function() {
    botonCopiar.innerText = 'Copiar';
  }, 1500);
}