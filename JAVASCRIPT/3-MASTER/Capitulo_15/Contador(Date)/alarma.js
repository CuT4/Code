"use strict";
const addZero= n =>{
    if (n.toString().length<2) return "0".concat(n);
    return n; 
}

const actualizarHora=()=>{
    const time=new Date();
    let hora=addZero(time.getHours());
    let minutos=addZero(time.getMinutes());
    let segundos=addZero(time.getSeconds());
    let milisegundos=addZero(time.getMilliseconds());
    //asignamos los valores de los <div> a los valores que devuelve Date():
    document.querySelector(".hora").textContent=hora;
    document.querySelector(".min").textContent=minutos;
    document.querySelector(".seg").textContent=segundos;
    document.querySelector(".mili").textContent=milisegundos;
}
actualizarHora();
setInterval(actualizarHora, 1);
