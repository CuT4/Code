function sum(n1,n2){
    let result= n1+n2;
    return document.write(result+"<br>");
}

function say_hello(name){
    let sentence=`Hello ${name}!<br>How you doing?`;
    return document.write(sentence);
}

const hello=(person)=>{
    let sentence=`Hello ${person}!<br>How you doing?`;
    return document.write(sentence);
}

hello("Naranjo")