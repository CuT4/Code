//Función que devuelve un string en formato UTC con la fecha de tantos días en el futuro como le indiquemos
//Será usada luego para determinar cuántos días permanecerá una cookie
const FechaUTC=(dias)=>{
    let fecha=new Date();
    fecha.setTime(fecha.getTime() + dias*1000*60*60*24);//Lo que está a la derecha de la suma está en milisegundos
    return fecha.toUTCString(); //Returns a date converted to a string using Universal Coordinated Time (UTC)
}
//Función que crea las cookies y su fecha de expiración
const crearCookies=(name, dias)=>{
    let expires=FechaUTC(dias);
    document.cookie=`${name};expires=${expires}`;
}

const obtenerCookies=(cookieName)=>{
    let cookies=document.cookie;
    cookies=cookies.split(";");
    for(let i=0; i<cookies.length; i++){
        let cookie=cookies[i].trim();
        if(cookie.startsWith(cookieName)){
            return cookie.split("=")[1];
        }
    }
    return "No hay ninguna cookie que se corresponda con ese nombre";
}

crearCookies("Nombre=M.Dolores", 5)