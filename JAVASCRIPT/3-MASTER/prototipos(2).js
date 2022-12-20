//26:59 JS master
class Objeto{
    saludar(){
        console.log("Hola");
    };
    despedirse(){
        console.log("Hasta luego");
    }
};

const objeto= new Objeto();

//Diferencia enrte sobreescribir proto y sobreescribir método

objeto.saludar=()=>{
    console.log("Saludar. Modificado afuera");
};

objeto.__proto__.saludar=()=>{
    console.log("Saludar. Modificado adentro");
};

let array_1=[];

array_1.__proto__ = objeto; //Este array hereda el prototipo    COMPLETO del objeto 'objeto' (absolutamente todo)

let array_2=[];

array_2.__proto__ = objeto.__proto__; //Este array hereda el prototipo PROTO del objeto 'objeto' (donde están los métodos)

objeto.saludar()
objeto.__proto__.saludar()
array_2.despedirse()//Al heredar el prototipo de la clase 'Objeto()' hereda también los métodos. Sí, un array que saluda y se despide.