//Registra, crea un SW dentro de Aplication/Service Worker
if(navigator.serviceWorker){
    navigator.serviceWorker.register("sw.js")
}

const sw=navigator.serviceWorker;
sw.ready.then(res=>{
    res.active.postMessage("El mensaje");
});

navigator.serviceWorker.addEventListener("message", (e)=>{
    console.log(`Mensaje recibido del service worker: ${e.data}`)
})



