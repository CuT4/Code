"use strict";
const archivo=document.getElementById("archivo");
archivo.addEventListener("change", (e)=>{
    leerArchivo(archivo.files); /*
    indico el índice cero porque los input de html tienen una propiedad
    llamada 'multiple' que permite seleccionar más de un archivo,
    y yo sólo quiero acceder al primero (y único en este caso)
    */
})


const leerArchivo=(ar)=>{
    for (let i = 0; i < ar.length; i++) {
        console.log(ar[i]) //Escribe el ojeto entero
        //A partir de aquí escribe tan sólo el JSON
        const reader=new FileReader();//nuevo archivo a leer
        reader.readAsDataURL(ar[i]);//lee cada archivo a cada vuelta de vucle
        reader.addEventListener("load", (e)=>{
            let newImage=`<img src='${e.currentTarget.result}'/>`;
            document.querySelector(".resultado").innerHTML+=newImage;
        })
    }
}
//Este script tan sólo sirve para leer Json desde los archivos concretos una vez sea seleccionados.
