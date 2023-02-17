self.addEventListener("install", ()=>{
    console.log("Instalando service worker")
});
self.addEventListener("activate", ()=>{
    console.log("El service worker está activo")
});
self.addEventListener("message", (e)=>{
    console.log(`Se ha recibido el siguiente mensaje proveniente del script principal: ${e.data}`)
    e.source.postMessage("Mensaje recibido");
});