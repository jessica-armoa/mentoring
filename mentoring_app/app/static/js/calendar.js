function validateTime() {
    const inputElement = document.getElementById("hour_start");
    const selectedTime = inputElement.value;
    const parts = selectedTime.split(":");
    const minutes = parseInt(parts[1]);
  
    if (minutes !== 0 && minutes !== 30) {
      alert("Por favor, seleccione una hora en punto o en punto y media.");
      inputElement.value = ""; // Limpia el valor si no cumple con los requisitos
    }
  }
  