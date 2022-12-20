class Objeto{
    saludar(){
        console.log("hola")
    }
    despedirse(){
        console.log("hasta luego")
    }
}
let variable=["un string", 234, null, "patito"];//Todo en JS es interpretado como objeto, con prototipos predeterminados excepto las funciones.
let funcion=function(){}; //Las funciones crean nuevos prototipos propios.
let objeto= new Objeto();

console.log(variable);
console.log(variable.__proto__);

console.log(objeto);
console.log(objeto.__proto__);
console.log(objeto.__proto__.__proto__);


