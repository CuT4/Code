/*
30' cosas de casa
100' trabajos
10' descanso
100' estudiar
240' trabajar
*/
let trabajo="240 minutos de trabajo";
let estudio="100 minutos de estudio";
let tp="100 minutos de hacer trabajos practicos";
let homework="30 minutos de las cosas de la casa";
let descanso="10 minutos de descanso";

console.log("TAREAS");
for(var i=0;i<14;i++){
    if(i==0){
        console.group("semana 1");
    }
console.groupCollapsed("dia "+(i+1));
console.log(trabajo);
console.log(descanso);
console.log(estudio);
console.log(tp);
console.log(homework);
console.groupEnd();
if(i==7){
    console.groupCollapsed("semana 2");
}
}
console.groupEnd();
console.groupEnd();
// console.group("dia 1");
// console.log(trabajo);
// console.log(descanso);
// console.log(estudio);
// console.log(tp);
// console.log(homework);
// console.groupEnd();


