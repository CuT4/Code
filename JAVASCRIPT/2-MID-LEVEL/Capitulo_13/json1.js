const JSON_deserializado={
    "variable1":"valor1",
    "variable2":"valor2"
};

const JSON_serializado=JSON.stringify(JSON_deserializado);
console.log(JSON_deserializado);

//.stringify() sirve para transformar objetos JSON a cadenas de texto JSON, es decir, JSON serializado.
//.parse() es el opuesto de .stringify(), transorma JSON serializado en objetos JSON para poder trabajar con ellos.

/*NOTA: Al enviar y recibir informacion entre servidores esta debe de estar en JSON serializado para 
evitar incompatibilidades entre servidores, por lo que para trabajar con la información recibida es necerio
deserializarla. En el caso de tener que enviar de vuelta la información, se hará en JSON serializado. */

