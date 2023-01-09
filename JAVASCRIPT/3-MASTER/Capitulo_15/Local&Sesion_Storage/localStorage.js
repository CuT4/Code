console.log(localStorage)

englishButton=document.querySelector(".en");
spanishButton=document.querySelector(".es");
removeButton=document.querySelector(".remove");


const revisarIdioma=()=>{
    //Verifica si ya tiene la clave "idioma en localStorage"
    localStorage.getItem("idioma")!==undefined? console.log(`When the client sing in, the language was set to: ${localStorage.getItem("idioma")}`)
        : console.log("The language hasn't been choosen yet");
    
}
//Cambia el idioma con los botones del documento
englishButton.addEventListener("click", ()=>{
    localStorage.setItem("idioma", "en");
});
spanishButton.addEventListener("click", ()=>{
    localStorage.setItem("idioma", "es");
});
removeButton.addEventListener("click", ()=>{
    localStorage.removeItem("idioma");
});
//Los addEventListener se ejecutan al pulsar uno de los botones
//setInterval() ejecuta la función que revisa el idioma cada segundo.
setInterval(revisarIdioma, 1000);






