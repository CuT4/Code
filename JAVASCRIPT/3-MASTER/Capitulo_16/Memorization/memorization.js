"use strict";

let arr=[];
const funcionLentaDeCojones=(num)=>{
    
    for(let i=0; i<num**num; i++){
        arr.push(i)
    }
    return arr;
}

let cache=[]
const memorizer=(func)=>{
    return e=>{
        const index = e.toString();
        if(cache[index]==undefined){
            cache[index]=func(e);
        }
        return cache[index];
    }
}

const memo=memorizer(funcionLentaDeCojones)

const date1= new Date();
console.log(memo(8))//No pasar de ocho (demasiados cálculos)
console.log(new Date()- date1)
//Cuenta el tiempo que tarda en ejecutarse (milisegundos)

const date2=new Date();
console.log(memo(8));
console.log(new Date()-date2)