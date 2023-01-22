"use strict";
const geolocation=navigator.geolocation;

const posicion=(pos)=>{
    console.log(pos);
}
const err=(err)=>{
    console.log(err);
}
const options={
    enableHighAccurrancy: true
}
geolocation.getCurrentPosition(posicion, err, options);