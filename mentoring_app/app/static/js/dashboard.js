document.getElementById('filterButton').addEventListener('click', function() {
    var areaSelect = document.getElementById('areaSelect');
    var selectedArea = areaSelect.options[areaSelect.selectedIndex].value;
    var url = `/filtrar_mentores/${selectedArea}`;
    this.setAttribute('href', url);
});