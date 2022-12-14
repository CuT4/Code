class Persona{
    constructor(nombre, instagram){
        this.nombre=nombre;
        this.instagram=instagram;
    }
};
const data=[
    ["Lucas Dalto", "@soydalto"],
    ["Juanma", "@juanma"],
    ["Paco", "@paco"],
    ["Miau"],
];
const personas=[];
for(let i=0; i<data.length;i++){
    personas[i]=new Persona(data[i][0], data[i][1]);
};
console.log(personas);
// cb significa "callback"
const obtenerPersona=(id)=>{
    return new Promise((resolve,reject)=>{
        if(personas[id]==undefined) reject("No se ha encontrado la persona")
        else {resolve(personas[id])}
    })
}
const obtenerInstagram=(id)=>{
    return new Promise((resolve, reject)=>{
        if(personas[id].instagram==undefined) reject("No se ha encontrado el instagram.");
        else{resolve(personas[id].instagram)};
    }) 
}
obtenerPersona(3).then((persona)=>{
    console.log(persona.nombre);
    return obtenerInstagram(1);
}).then((instagram)=>{
    console.log(instagram);
}).catch((e)=>{
    console.log(e);
});