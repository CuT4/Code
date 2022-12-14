// DECLARACIÓN DE CLASES, VARIABLES Y FUNCIONES GLOBALES------------------------------
class CLIENTE{
    constructor(nombre, direccion, precioHora, horas, maquinas_usadas){
        this.nombre=nombre;//String
        this.direccion=direccion;//String
        this.precioHora=precioHora;//Float
        this.horas=horas;//Float
        this.maquinas_usadas=maquinas_usadas;//Array
        //Añadimos el total y la información:
        this.total=(this.precioHora)*(this.horas);
        this.info={
            //this.info va a ser un diccionario con toda la información
            nombre:[`${this.nombre}`],
            direccion:[`${this.direccion}`],
            precioHora:[`${this.precioHora}`],
            horas:[`${this.horas}`],
            maquinas_usadas:[`${this.maquinas_usadas}`],
            total:[`${this.total}`]
        }
    }
    //Mostramos la información con una función:
    informar(){
        return `${(this.info["nombre"])}<br>
        ${(this.info["direccion"])}<br>
        ${(this.info["precioHora"])}<br>
        ${(this.info["horas"])}<br>
        ${(this.info["maquinas_usadas"])}<br>
        ${(this.info["total"])}<br>`
    };  
};
// AGREGADO DE CLIENTES ---------------------------------------------------------------------------------
const mella=new CLIENTE("Manuel Mella", "somewhere", 12, 4, ["desbrozadora", " cortacésped"]);
const miau=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const pedro=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const paco=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const juan=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const malbono=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const spaghethi=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
const carbonara=new CLIENTE("Miau Miau", "somewhere", 15, 8, ["furgoneta", " cortacésped"]);
clientes=[mella, miau, pedro, paco, juan, malbono, spaghethi, carbonara];

for(cliente of clientes){
    granTabla=document.querySelector(".granTabla");
    granTabla.innerHTML+=`<tr contentEditable="true" class="contenidoTabla_${cliente.nombre}">
    <td class="nombre_${cliente.nombre}">${cliente.nombre}</td>
    <td class="direccion_${cliente.nombre}">${cliente.direccion}</td>
    <td class="precioHora_${cliente.nombre}">${cliente.precioHora}€/h</td>
    <td class="horas_${cliente.nombre}">${cliente.horas}</td>
    <td class="maquinas_usadas_${cliente.nombre}">${cliente.maquinas_usadas}</td>
    <td class="total_${cliente.nombre}">${cliente.total}€</td></tr>`;
}
// BOTONES ----------------------------------------------------------------------------
const addButton=document.querySelector(".addButton");
addButton.addEventListener("click",()=>{
granTabla.innerHTML+=`<tr contenteditable="true"><td></td><td></td><td></td><td></td><td></td><td></td></tr>`;
});
