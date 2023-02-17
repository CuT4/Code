if(navigator && navigator.serviceWorker){
    navigator.serviceWorker.register("chat_sw.js")
};

const sw=navigator.serviceWorker;
const enviar=document.querySelector(".enviar");
const texto=document.querySelector(".msg-sender");

enviar.addEventListener("click", ()=>{
    sw.ready.then(res=>{
        res.active.postMessage(texto.value)
        console.log(texto.value)
    })
})
