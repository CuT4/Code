"use strict";

const publicaciones=document.querySelector(".publicaciones");
let contador=0;

const createPublicationCode=(name, content)=>{
    const container=document.createElement("div");
    const comentarios=document.createElement("div");
    const nombre=document.createElement("h3");
    const contenido=document.createElement("p");
    const btnComentraio=document.createElement("input");
    const btnEnviar=document.createElement("input");

    btnComentraio.type="text";
    btnEnviar.type="submit";

    container.classList.add("publicacion");
    comentarios.classList.add("comentarios");
    btnEnviar.classList.add("enviar");
    btnComentraio.classList.add("comentario");

    btnComentraio.setAttribute("placeholder", "Escribe un comentario");

    nombre.textContent=name;
    contenido.textContent=content;
    comentarios.appendChild(btnComentraio);
    comentarios.appendChild(btnEnviar);
    container.appendChild(nombre);
    container.appendChild(contenido);
    container.appendChild(comentarios);

    return container
}

const cargarMasPublis=(entry)=>{
    if(entry[0].isIntersecting){
        cargarPublicaciones(4)
    }
}

const observer=new IntersectionObserver(cargarMasPublis);

const cargarPublicaciones=async(num)=>{
    const request=await fetch("lzload.txt");
    const content=await request.json();
    const arr=content.content;
     
    const documentFragment=document.createDocumentFragment();

    console.log(arr);

    for (let i = 0; i < num; i++) {
        if(arr[contador]!=undefined){
            const newPublicacion=createPublicationCode(arr[contador].nombre, arr[contador].contenido);
            documentFragment.appendChild(newPublicacion);
            contador++;
        }
        if(i==num-1){
            observer.observe(newPublicacion);
        }else{
            let noMore=document.createElement("h3");
            noMore.textContent="No hay más publicaciones";
            documentFragment.appendChild(noMore);
            publicaciones.appendChild(documentFragment);
            break;
        }
    }
}

cargarPublicaciones(3)