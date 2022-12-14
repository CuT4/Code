// function prueba(callback){
//     callback("Roberto");
// }
// function decirNombre(nombre){
//     console.log(nombre);
// }

// prueba(decirNombre);

class Persona{
    constructor(nombre, instagram){
        this.nombre=nombre;
        this.instagram=instagram;
    }
    // Se crea la clase persona
};
const data=[
    ["Lucas Dalto", "@soydalto"],
    ["Juanma", "@juanma"],
    ["Paco", "@paco"],
    ["Miau"],
    //Esto son los datos con los que vamos a trabajar
];
const personas=[];
//El array personas se crea
for(let i=0; i<data.length;i++){
    personas[i]=new Persona(data[i][0], data[i][1]);
    //Se crean objetos de la clase "Persona" a partir de los datos que tenemos
};
console.log(personas);//Se imprime en consola la lista de usuarios
const obtenerPersona=(id, cb)=>{
    // cb significa "callback"
    //"id" es el número que hace referencia a la posición de cada elemento del array
    if(personas[id]==undefined){
        cb("No se ha encontrado el id de la persona");
    }else{
        cb(null,personas[id], id);
        //ESTO NO SÉ CÓMO FUNCIONA  
    }
}
const obtenerInstagram=(id, cb)=>{
    if(personas[id].instagram==undefined){
        cb("No se ha encontrado el instagram de la persona");
    }else{
        cb(null,personas[id].instagram);
        //Funciona igual que la función anterior, y sigo sin saber como funciona:"cb(null,personas[id].instagram);"
    } 
}
obtenerPersona(3,(err, persona, id)=>{
    //Está usando la función obtenerPersona, con "id=3" y "cb" como una función interna en la propia llamada
    //El parámetro "cb" (callback) es una función interna que se ejecuta a continuación:
    if(err){
        //Si sucede un error, lo escribirá de forma más "amigable" que si no hubieramos hecho esto
        console.log(err);
    }else{
        console.log(persona.nombre);
        //Imprime el nombre del objeto de la clase "persona", que en este caso funciona como una "i" iterando el array "personas"
        obtenerInstagram(id,(err, instagram)=>{
            if(err){
                //Si sucede un error, lo escribirá de forma más "amigable" que si no hubieramos hecho esto
                console.log(err);
            }else{
                //Imprime el instagram de la persona
                console.log(instagram);
            }
        });
    }
});
