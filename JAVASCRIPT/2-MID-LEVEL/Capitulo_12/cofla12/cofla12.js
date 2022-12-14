const materiasHTML=document.querySelector(".materias");

const materias=[
    {
        nombre:"Física",
        nota:7
    },{
        nombre:"Cálculo",
        nota:8
    },{
        nombre:"Bases de Datos",
        nota:9
    },{
        nombre:"Matemáticas",
        nota:7
    },{
        nombre:"Programación",
        nota:7
    }
]

const obtenerMateria=(id)=>{
    return new Promise((resolve, reject)=>{
        materia=materias[id];
        if(materia==undefined)reject("La materia no existe");
        else setTimeout(resolve(materia), Math.ramndom()*400)
    })
}
const devolverMaterias=async()=>{
    let materia=[];
    for(let i=0; i<materias.length;i++){
        materia[i]=await obtenerMateria(i);
        let newHTMLCode=`
        <div class="materia">
            <div class="nombre">${materia[i].nombre}</div>
            <div class="nota">${materia[i].nota}</div>
        </div>`;
        materiasHTML.innerHTML+=newHTMLCode;
    }
}
devolverMaterias();
