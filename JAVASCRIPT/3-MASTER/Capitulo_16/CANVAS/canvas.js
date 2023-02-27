const canvas=document.getElementById("canvas");
//hay que crear un CONTEXTO
const ctx=canvas.getContext("2d");
//Los elementos serán añadidos al contexto, no al canvas directamente

ctx.lineWidth="4" //Grosor de la línea
ctx.strokeStyle="#48e";
ctx.fillStyle="#26f";

ctx.strokeRect(30, 50, 400, 200); //.strokeRect(left, right, x, y)

ctx.fillRect(10,20, 400, 200); //Genera ese rectángulo negro, pero lo he desplazado para dar ese efecto

/*
Los siguientes puntos serán recorridos en orden lineal por la linea que se dibujará posteriormente,
el resultado final en este caso será un triángulo.
*/
ctx.lineTo(100, 300);//Define un punto  .lineTo(x,y)
ctx.lineTo(150, 325);   
ctx.lineTo(100, 350);   
ctx.lineTo(100, 298);

ctx.stroke();//Traza una línea entre los dos puntos anteriores
ctx.closePath(); //Levanta el lápiz, por así decirlo

ctx.beginPath()//Baja el lápiz, por así decirlo
ctx.arc(290, 370, 90, 45, 90); //Creates a circle, checkout the parameters
ctx.stroke()

