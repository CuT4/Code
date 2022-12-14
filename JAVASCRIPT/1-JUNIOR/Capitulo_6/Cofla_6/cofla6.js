const contenedor=document.querySelector(".flex-container");
function crearLlave(nombre, modelo, precio){
    img="<img class='llave-img'src='llave.png'>";
    nombre=`<h2>${nombre}</h2>`;
    modelo=`<h3>${modelo}</h3>`;
    precio=`<p><b>${precio}</b></p>`;
    return[img,nombre, modelo, precio];
}

let documentFragment=document.createDocumentFragment();

const changeHidden=(number)=>{
    document.querySelector(".key-data").value=number;
}

for(i=1;i<=20;i++){
    let modeloRamdon=Math.round(Math.random()*10000);
    let precioRandom=Math.round(Math.random()*10+30);
    let llave=crearLlave(`llave ${i}`,` modelo ${modeloRamdon}`, `${precioRandom}€`);
    let div=document.createElement("DIV");
    div.classList.add(`item-${i}`,`flex-item`);
    div.addEventListener("click",()=>{changeHidden(modeloRamdon)});
    div.tabIndex=i;//ESTO ME HA SERVIDO PARA PULSAR Y QUE SE MANTENGE, CONSULTAR CSS
    div.innerHTML=llave[0]+llave[1]+llave[2]+llave[3];
    documentFragment.appendChild(div);
}
contenedor.appendChild(documentFragment);