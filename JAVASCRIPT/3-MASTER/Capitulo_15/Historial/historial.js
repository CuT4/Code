"use strict";
console.log(window.history)

let recargar=document.querySelector(".recargar");
let adelante=document.querySelector(".adelante");
let atras=document.querySelector(".atras");

recargar.addEventListener("click", ()=>{
    location.reload()
    console.log(history.go())
})
adelante.addEventListener("click", ()=>{
    history.go()
    console.log(history.forward())
})
recargar.addEventListener("click", ()=>{
    history.back()
    console.log(history.back())
})





