//NOTA: EL PARÁMETRO REST DEBE SER SIEMRPE EL ÚLTIMO
//puede recibir cualquier nombre (...args), (...nums)...
const sumar=(frase,...args)=>{//con el parámetro args se pueden pasar infinitos parámetros
    let result=0;
    for (let i = 0; i < args.length; i++) {//el parámetro args devuelve un array, y aquí lo recorremos:
        result += args[i];
    }
    console.log(`${frase} ${result}`)
};
sumar("A ver si funciona: ", 11, -12, 67, 234, -567)