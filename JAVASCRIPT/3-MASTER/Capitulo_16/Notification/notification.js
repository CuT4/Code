"use strict";

if(!Notification in window){
    console.log("Las notificaciones NO están disponibles en tu navegador");
}else{
    console.log("Las notificaciones SÍ están disponibles en tu navegador");
}

Notification.requestPermission(()=>{
    if(Notification.permission=="granted") console.log("Tienes permisos de notificaciones");
    else console.log("No tienes permiso de notificaciones");
});

new Notification("Así se hacen las notificaciones");