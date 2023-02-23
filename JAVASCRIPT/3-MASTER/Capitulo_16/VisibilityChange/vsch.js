document.addEventListener("visibilitychange", (e)=>{
    if(e.target.visibilityState=="hidden") console.log("Te has ido de la pestaña")
})