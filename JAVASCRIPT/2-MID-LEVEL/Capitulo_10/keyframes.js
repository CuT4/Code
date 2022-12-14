const boton=document.querySelector(".boton");
boton.addEventListener("click",()=>{
    saludar()
    abrirM()
});

const saludar=()=>{
    nombre=prompt("Tu nombre:");
}

const abrirM=(nombre)=>{
    let modal=document.querySelector(".modal");
    modal.innerHTML+="<h3>Hola, ¿Qué tal?</h3>";
    modal.style.margin="40px"
    modal.style.display="flex";
    modal.style.animation="aparecer 5s forwards";
}