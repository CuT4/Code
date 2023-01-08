let fruta=["pera", "manzana", "melón", "naranja"];
let carne=["vaca", "caerdo", "pollo", "pavo"];

/*
fruta.push(carne);
-> En este ejemplo el resultado es: 
["pera", "manzana", "melón", "naranja",["vaca", "caerdo", "pollo", "pavo"]];
-> Pero no queremos un array dentro de un arrray. Queremos:
["pera", "manzana", "melón", "naranja", "vaca", "caerdo", "pollo", "pavo"];
->Por lo que usamos:
*/ 
fruta.push(...carne)
console.log(fruta);