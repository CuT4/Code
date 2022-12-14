const getName=async()=>{

    //Esto fue hecho con LiveServer de VS-Code para que me dejara usar el protocolo HTTP
    let peticion= await fetch("http://127.0.0.1:5500/JAVASCRIPT/2-MID-LEVEL/Capitulo_13/F%26A%2CA%26A/informacion.txt");
    let resultado=await peticion.json();
    let div=document.createElement("DIV");
    div.classList.add("nombre");
    div.innerHTML=resultado.nombre;
    document.body.appendChild(div)
}
const getAge=async()=>{

    //Esto fue hecho con LiveServer de VS-Code para que me dejara usar el protocolo HTTP
    let peticion= await fetch("http://127.0.0.1:5500/JAVASCRIPT/2-MID-LEVEL/Capitulo_13/F%26A%2CA%26A/informacion.txt");
    let resultado=await peticion.json();
    let div=document.createElement("DIV");
    div.classList.add("edad");
    div.innerHTML=resultado.edad;
    document.body.appendChild(div)
}

document.getElementById('getName').addEventListener("click", getName);
document.getElementById('getAge').addEventListener("click", getAge);