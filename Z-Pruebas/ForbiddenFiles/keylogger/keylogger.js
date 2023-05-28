const input=document.querySelector(".input-prueba");
const keylogger=document.querySelector(".keylogger");
input.addEventListener("keyup",(e)=>{
    let tecla=e.key;
    keylogger.innerHTML=`Tecla presionada: <b>${tecla}</b>`;
})