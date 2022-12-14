//IT DOESN'T WORK PROPERLY
//https://www.youtube.com/watch?v=z95mZVUcJ-E 
//6:45:43
let materias={
    fisica:["Ramirez","pedro", "pepito", "cofla", "maria"],
    programacion:["Dalto","pedro", "juan", "pepito"],
    logica:["Rodriguez","pedro", "juan", "pepito", "cofla", "maria"],
    quimica:["Jesús","pedro", "juan", "pepito", "cofla", "maria"]
}
const inscribir=(alumno, materia)=>{
    personas=materias[materia];
    alumnos=personas;
    if(personass.lenght>=21){
        document.write(`Lo sentimos <b>${alumno}</b>, las clases de <b>${materia}</b> están llenas.`)
    }else{
        personas.push(alumno);
        if(materia=="fisica"){
            materias={
                fisica: personas,
                programacion: materias['programacion'],
                logica: materias['logica'],
                quimica: materias['quimica']
            }
        }
        else if(materia="programacion"){
            materias={
                fisica: materias['fisica'],
                programacion: personas,
                logica: materias['logica'],
                quimica: materias['quimica'] 
            }
        }else if(materia="logica"){
            materias={
                fisica: materias['fisica'],
                programacion: materias['programacion'],
                logica: personas,
                quimica: materias['quimica'] 
            }
        }else if(materia="quimica"){
            materias={
                fisica: materias['fisica'],
                programacion: materias['programacion'],
                logica: materias['logica'],
                quimica: personas 
            }
        }
        document.write(`Felicidades ${alumno}, has entrado en ${materia}.<br><br>`)
    }
}
document.write(materias["fisica"]+"<br><br>");
inscribir("pedrito", "programacion");
document.write(materias["fisica"]+"<br><br>");