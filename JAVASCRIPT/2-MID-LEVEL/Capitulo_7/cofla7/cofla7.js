let alto=window.screen.availHeight;
let ancho=window.screen.availWidth;
comprar=confirm(`El alto es de ${alto}, el ancho es de ${ancho}`);

if(comprar){
    alert("Compra realizada correctamente");
}else{
    alert("Compra cancelada");
}


let href=window.location.href;
let hostname=window.location.hostname;
let pathname=window.location.pathname;
let protocol=window.location.protocol;

let html=`Protocolo:<b>${protocol}</b><br>`;
html+=`Host:<b>${hostname}</b><br>`;
html+=`URL:<b>${href}</b><br>`;
html+=`Pathname:<b>${pathname}</b><br>`;

document.write(html);


