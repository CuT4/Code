"use strict"
const circulo=document.querySelector(".circulo");
const cuadrado=document.querySelector(".cuadrado");

circulo.addEventListener("dragstart", (e)=>{
    //Al iniciar el arrastre, declaramos una clave "clase" asociada a la clase del objeto en cuestión.
    e.dataTransfer.setData("clase", e.target.className)
});
/*
circulo.addEventListener("drag", ()=>{
    console.log(2)
});
circulo.addEventListener("dragend", ()=>{
    console.log(3)
});
*/
cuadrado.addEventListener("dragenter", ()=>{
    console.log(1);//Cuando el círculo entre en el rectángulo
});
cuadrado.addEventListener("dragover", (e)=>{
    //NOTA: e.preventDefault() permite soltar objetos dentro de él, lo cuál por defecto está desactivado.
    e.preventDefault();//Cuándo el círculo esté en el rectángulo
    console.log(2);
});
cuadrado.addEventListener("drop", (e)=>{
    //Cuándo se suelte un objeto dentro, imprime la clase del objeto soltado.
    console.log(e.dataTransfer.getData("clase"));
});
cuadrado.addEventListener("dragleave", ()=>{
    console.log(4);//Cuándo el circulo no está en el rectángulo.
});