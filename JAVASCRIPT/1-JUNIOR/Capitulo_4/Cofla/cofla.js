const obtenerInformacion=(materia)=>{
    const materias={
        fisica:["Ramirez","pedro", "pepito", "cofla", "maria"],
        programacion:["Dalto","pedro", "juan", "pepito"],
        logica:["Rodriguez","pedro", "juan", "pepito", "cofla", "maria"],
        quimica:["Jesús","pedro", "juan", "pepito", "cofla", "maria"]
    }
    if (materias[materia]!=undefined){
        return [materias[materia], materia, materias];
    }else{
        return materias;
    }
}
const mostarInformacion=(materia)=>{
    let info=obtenerInformacion(materia);
    if(info!=false){
        let profesor=info[0][0];
        let alumnos=info[0];
        alumnos.shift();
        document.write(`El profesor de <b>${info[1]}</b> es: <b style="color:green">${profesor}</b><br>
        Los alumnos son: <b style="color:red">${alumnos}</b><br><br>`);
    }
}
const cantidadDeClases=(alumno)=>{
    let info=obtenerInformacion();
    let clasesPresentes=[];
    let cantidadTotal=0;
    for (i in info){
        if (info[i].includes(alumno)){
            cantidadTotal++;
            clasesPresentes.push(" "+i);
        }  
    }
    return `${alumno} está en ${cantidadTotal} clases<br>Está cursando: ${clasesPresentes}<br><br>`;
}



mostarInformacion("fisica");
mostarInformacion("programacion");
mostarInformacion("logica");
mostarInformacion("quimica");

document.write(cantidadDeClases("cofla"));
document.write(cantidadDeClases("maria"));
document.write(cantidadDeClases("pedro"));