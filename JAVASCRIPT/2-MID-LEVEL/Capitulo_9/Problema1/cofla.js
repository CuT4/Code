const nombre=document.getElementById("nombre").value;
const email=document.getElementById("email").value;
const materia=document.getElementById("materia").value;
const boton=document.getElementById("btn-enviar").value;
const resultado=document.querySelector(".resultado").value;

boton.addEventListener("click",(e)=>{
    e.preventDefault();
    let error=validarCampos();
    if (error[0]){
        resultado.innerHTML=error[1];
        resultado.classList.add("red");
    }else{
        resultado.innerHTML="Solicitud enviada correctamente";
        resultado.classList.add("green");
        resultado.classList.remove("red");
    }
});
const validarCampos=()=>{
    let error=[];
    if (nombre.value.length<3){
        error[0]=true;
        error[1]="El nombre no puede contener menos de 3 caracteres";
        return error;
    }else if(nombre.value.length>40){
        error[0]=true;
        error[1]="El nombre no puede contener más de 40 caracteres";
        return error;
    }else if(email.value.lenght<5||email.value.indexOf("@")==false||email.value.indexOf(".")==false){
        error[0]=true;
        error[1]="La dirección de email no es válida";
        return error;
    }else if(materia.value<4||materia.value>15){
        error[0]=true;
        error[1]="La materia no es correcta";
    }
    error[0]=false;
    return error;
}