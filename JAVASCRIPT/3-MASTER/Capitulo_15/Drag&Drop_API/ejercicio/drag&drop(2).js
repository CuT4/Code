"use strict"
const zona=document.querySelector(".zona");
zona.addEventListener("dragover", (e)=>{
    e.preventDefault();
})
zona.addEventListener("drop", (e)=>{
    let n=e.dataTransfer.getData("textura");
    zona.style.background=`url("textura${n}.png")`;
})
const transferirTextura=(n,e)=>{
    e.dataTransfer.setData("textura", n);
}
const verificar=()=>{
    textura_1=document.querySelector(".textura_1")
    textura_1.document.addEventListener("dragstart", ()=>{
        console.log("Arrastra");
    })
    textura_1.document.addEventListener("drag", ()=>{
        console.log("Está siendo arrastrado");
    })
    textura_1.document.addEventListener("dragend", ()=>{
        console.log("Se ha soltado");
    })
    //--------------------------------------------------------
    textura_2=document.querySelector(".textura_2")
    textura_2.document.addEventListener("dragstart", ()=>{
        console.log("Arrastra");
    })
    textura_2.document.addEventListener("drag", ()=>{
        console.log("Está siendo arrastrado");
    })
    textura_2.document.addEventListener("dragend", ()=>{
        console.log("Se ha soltado");
    })
    //--------------------------------------------------------
    textura_3=document.querySelector(".textura_3")
    textura_3.document.addEventListener("dragstart", ()=>{
        console.log("Arrastra");
    })
    textura_3.document.addEventListener("drag", ()=>{
        console.log("Está siendo arrastrado");
    })
    textura_3.document.addEventListener("dragend", ()=>{
        console.log("Se ha soltado");
    })
}

for(let i=1; i<document.querySelector(".texturas").children.length + 1; i++){
   document.querySelector(`.textura_${i}`).addEventListener("dragstart", (e)=>transferirTextura(i,e));
}


