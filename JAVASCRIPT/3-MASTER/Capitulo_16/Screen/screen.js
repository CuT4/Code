ancho=screen.width;//Ancho
altura=screen.height;//Altura

anchoDisponible=screen.availWidth
alturaDisponible=screen.availHeight

resolucion=screen.pixelDepth //Resolucion de color de la pantalla
profundidad=screen.colorDepth //Profundidad de bits de la paleta de colores

console.log(`Width: ${ancho}`);
console.log(`Height: ${altura}`);

console.log(`availWidth: ${anchoDisponible}`);
console.log(`availHeight: ${alturaDisponible}`);

console.log(`pixelDepth: ${resolucion}`);
console.log(`colorDepth: ${profundidad}`);

