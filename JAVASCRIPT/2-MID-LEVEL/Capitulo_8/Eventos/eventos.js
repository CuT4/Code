const boton=document.querySelector(".button");
boton.addEventListener("click",(e)=>{
    alert("He clickeado un boton");
})
const azul=document.querySelector(".contenedor-1");
azul.addEventListener("contexmenu",(e)=>{
    alert("Esto es azul");
})
const rosa=document.querySelector(".contenedor-2");
rosa.addEventListener("contexmenu",(e)=>{
    alert("Esto es rosa");
})

const input=document.querySelector(".input-prueba");
const keylogger=document.querySelector(".keylogger");
input.addEventListener("keyup",(e)=>{
    let tecla=e.key;
    keylogger.innerHTML=`Tecla presionada: <b>${tecla}</b>`;
})