let frutas=["pera", "manzana", "plátano"];

document.write(frutas);


let pc={
    procesador:"Intel core i7 11700K",
    ram:"16GB",
    espacio:"1TB",
}


let procesador=pc["procesador"];
let ram=pc["ram"];
let espacio=pc["espacio"];

frase=`<br><br>El procesador de mi PC es: ${procesador}<br> la ram son: ${ram}<br> y el espacio es de ${espacio}`;

document.write(frase)
