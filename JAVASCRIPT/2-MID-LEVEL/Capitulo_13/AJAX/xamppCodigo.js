let peticion

if(window.XMLHttpRequest){
    peticion=new XMLHttpRequest();
}else{
    peticion=new ActiveXObject("Microsoft.XMLHTTP");
}

peticion.addEventListener("readystatechange",()=>{
    let respuesta;
    if(peticion.status==200||peticion.status==201) respuesta=peticion.response;
    else respuesta="Lo sentimos, no se ha podido encontrar resultado para su búsqueda"
})
console.log(JSON.parse(respuesta));

peticion.open("POST", "https://reqres.in/api/users");

peticion.setRequestHeader("Content-type", "application/json;charset=UTF8");

peticion.send(JSON.stringify({
    "nombre":"morfeo",
    "trabajo":"líder"
}
));

