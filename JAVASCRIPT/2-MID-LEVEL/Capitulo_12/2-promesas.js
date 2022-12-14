// const objeto={
//     propiedad_1:"valor-1",
//     propiedad_2:"valor-2",
//     propiedad_3:"valor-3"
// };
const obtenerInformacion=(text)=>{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>resolve(text), Math.random()*200);
    });
};

const mostrarData=async()=>{
    data1=await obtenerInformacion("1: hola");
    data2=await obtenerInformacion("2: buenas");
    data3=await obtenerInformacion("3: tardes");
    console.log(data1);
    console.log(data2);
    console.log(data3);


};

// obtenerInformacion().then(resultado=>console.log(resultado));
// const mostrarResultado=async()=>{
//     resultado=await obtenerInformacion();
//     console.log(resultado);
// };

// mostrarResultado();