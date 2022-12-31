//Este archivo se llama 'operadorTernario'porque es el único operador en JS que implica tres factores.
num=parseFloat(prompt("Número: "));
const comprobar=(n)=>{
    if(n>0){
        return true;
    }
    if(n<0){
        return false;
    }
}

if(num!=0){
    document.write(comprobar(num) ? "positivo":"negativo");
    //el operador ternario devuelve el segundo término si el primero es 'true'
    //el operador ternario devuelve el tercer término si el primero es 'false'
}else{
    document.write("Cero no es positivo ni negativo")
}


    