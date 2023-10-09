document.getElementById('filterButton').addEventListener('click', function() {
    var areaSelect = document.getElementById('areaSelect');
    var selectedArea = areaSelect.options[areaSelect.selectedIndex].value;
    var url = `/filtrar_mentores/${selectedArea}`;
    this.setAttribute('href', url);
});


(() => {
    'use strict'
    const tooltipTriggerList = Array.from(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(tooltipTriggerEl => {
    new bootstrap.Tooltip(tooltipTriggerEl)
    })
})()

//Calendario
document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {

        });
        calendar.render();
    });

