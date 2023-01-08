const validarEdad=(msg)=>{ //validarEdad() recibe como parámetro "msg"
    let edad;// Se declara la variable edad
    try{//prueba esto
        if(msg) edad=prompt(msg);//Si la función recibe un mensaje, ese será el prompt
        else edad=prompt("Introduce tu edad");//En caso de no recibir un mensaje la función utilizará este
        edad=parseInt(edad);//La edad pasa de string a nº entero
        if(isNaN(edad)) throw "Introduce un número válido para la edad";//Si edad "is not a number" tira ese mensaje
        if(edad>18) console.log("Eres mayor de edad");//Si la edad es mayor que 18, imprime lo siguiente
        else console.log("Eres menor de edad");//Si la edad es menor que 18, imprime lo siguiente
    }catch(e){//Si llegara a haber un error, antes de tirarlo por consola, lo intentaría de nuevo
        validarEdad(e);
    }
}
validarEdad("Patito de goma");//En este caso "Patito de goma" es el prompt, pero como hemos visto, puede omitirse este parámetro