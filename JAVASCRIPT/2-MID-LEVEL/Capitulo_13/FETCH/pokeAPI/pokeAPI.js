const options={
    method:'GET'
};
pikachuData=fetch('https://pokeapi.co/api/v2/pokemon/charizard', options)
    .then(res=>res.text())
    .then(res=>document.write(res))
    .catch(err=>console.error(err));
;

/* De esta manera ya tienes todos los datos necesarios sobre lo que 
puedas necesitar pero, cabe decir, que aunque aquí parezca fácil, en 
las API protegidas vamos a tener que pasar en el options unos
headers específicos para que se verifique que tenemos acceso a dicha
API, los cuales varían dependiendo de cada una. Necesitaríamos una 
Api-Key específica*/

