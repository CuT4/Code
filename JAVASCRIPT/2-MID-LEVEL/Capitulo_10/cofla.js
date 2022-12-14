const sendButton=document.getElementById("snd-nota");
sendButton.addEventListener("click", ()=>{
    let resultado, mensaje;
    try{
        prevRes=parseInt(document.getElementById("nota").value);
        if(isNaN(prevRes)){
            throw "Sos gracioso";
        }
        resulatdo=verificarAprobacion(8,5,mensaje[1]);
        mensaje=definirMensaje(resultado[1]);
    }catch(e){
        resultado="SOS GRACIOSO";
        mensaje="NO HACKEES";
    }
    abrirModal(resultado[0], mensaje);
});
const definirMensaje=(pr)=>{
    let resultado;
    switch(pr){
        case 1:"No puedes ser tan hdp"
        break;
        case 2:"Eres malisimo"
        break;
        case 3:"No sabes nada"
        break;
        case 4:"Muy mal"
        break;
        case 5:"Mal"
        break;
        case 6:"Regular"
        break;
        case 7:"Bien pero puede mejorar"
        break;
        case 8:"Muy bien"
        break;
        case 9:"Excelente"
        break;
        case 10:"Insuperable, literalmente"
        break;
        default: resultado=null;s
    }
    return resultado;
}
const verificarAprobacion=(nota1, nota2, prevRes)=>{
    promedio=(nota1+nota2+prevRes)/3
    if (promedio>=7){
        return "<span class='green'>APROBADO<span/>";
    }
    return "<span class='red'>DESAPROBADO<span/>";

}
const abrirModal=(res, msg)=>{
    document.querySelector(".resultado").innerHTML=res;
    document.querySelector(".mensaje").innerHTML="Tu prueba: "+msg;
    let modal=document.querySelector(".modal-background");
    modal.style.display="flex";
    modal.style.animation="aparecer 1s forwards";

}