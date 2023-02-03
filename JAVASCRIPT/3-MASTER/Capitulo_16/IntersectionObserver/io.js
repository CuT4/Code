"use strict"; // Declara el modo estricto para asegurar la escritura de código seguro

const cajas = document.querySelectorAll(".caja"); // Selecciona todos los elementos con la clase "caja" y los almacena en "cajas"

// Función que verifica la visibilidad de los elementos
const verifyVisibility = (entries) => {
  // Recorre cada entrada
  for (let entry of entries) {
    // Si el elemento actual está intersectando (es decir, visible)
    if (entry.isIntersecting) {
      console.log(entry.target.textContent, " es visible ahora"); // Muestra un mensaje en consola indicando que el elemento es visible
    } else {
      console.log(entry.target.textContent, " no es visible ahora"); // Muestra un mensaje en consola indicando que el elemento no es visible
    }
  }
};

// Crea una instancia del Intersection Observer
const observer = new IntersectionObserver(verifyVisibility);

// Recorre cada elemento en "cajas" y los observa para detectar cambios de visibilidad
for (let caja of cajas) {
  observer.observe(caja);
}
