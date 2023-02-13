"use strict";
//Se usa el constructor Worker
const worker=new Worker("worker.js")//El parámetro es el archivo que se va a ejecutar ensegundo plano
document.querySelector(".boton").addEventListener("click", ()=>enviar_mensaje_al_worker())

//Hay que mandar la orden al worker porque no tiene como objeto global a window
const enviar_mensaje_al_worker=()=>{
    worker.postMessage("esto el la data del evento messaje en el web-worker");
    worker.terminate()
}


console.log(worker);