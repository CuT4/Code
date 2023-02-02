"use strict";

const request = window.indexedDB.open("miDB", 1); 
// abrimos la base de datos "miDB" con una versión de 1

request.onerror = function(event) {
  console.error("Error al abrir la base de datos"); 
  // en caso de un error al abrir la base de datos, mostramos un error en la consola
};

request.onsuccess = function(event) {
  console.log("Base de datos abierta con éxito"); // Mostramos un mensaje en la consola de que la base de datos se abrió con éxito
  const db = event.target.result; // Guardamos la base de datos en una variable llamada "db"

  const data = { id: 1, nombre: "Juan", apellido: "Pérez" };
  const data2={id: 2, nombre:"Alex", apellido: "Gómez", direccion: "Barcelona"} // Definimos los datos que queremos guardar en un objeto
  guardarDatos(db, data); // Llamamos a la función "guardarDatos" y le pasamos la base de datos y los datos que queremos guardar
  guardarDatos(db, data2);

  obtenerDatos(db); // Llamamos a la función "obtenerDatos" y le pasamos la base de datos
};


request.onupgradeneeded = function(event) {
  console.log("Actualizando la base de datos"); 
  // si es necesario actualizar la base de datos, mostramos un mensaje en la consola
  const db = event.target.result; 
  // guardamos la base de datos en una variable llamada "db"
  const objectStore = db.createObjectStore("personas", { keyPath: "id" }); 
  // creamos una "objectStore" llamada "personas" con la clave "id"
};

const guardarDatos = function(db, data) { 
  // definimos la función "guardarDatos" que acepta la base de datos y los datos que se van a guardar
  const transaction = db.transaction("personas", "readwrite"); 
  // abrimos una transacción en modo "readwrite" para la "objectStore" "personas"
  const objectStore = transaction.objectStore("personas"); 
  // obtenemos la "objectStore" "personas"
  objectStore.add(data); 
  // agregamos los datos a la "objectStore"
};

const obtenerDatos = function(db) { 
  // definimos la función "obtenerDatos" que acepta la base de datos
  const transaction = db.transaction("personas", "readonly"); 
  // abrimos una transacción en modo "readonly" para la "objectStore" "personas"
  const objectStore = transaction.objectStore("personas"); 
  // obtenemos la "objectStore" "personas"
  const request = objectStore.getAll(); 
  // hacemos una solicitud para obtener todos los datos de la "objectStore"
  request.onsuccess = function(event) {
    console.log(event.target.result); 
    // si la solicitud es exitosa, mostramos los resultados en la consola
  };
};

