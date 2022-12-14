let cantidad=prompt("How many pupils are in this curse? ")
let totalAlumns=[]

for (i=0; i<cantidad; i++){
    totalAlumns[i]=[prompt("Alumn name"+(i+1)),0];
}

const Assistance=(nombre, position)=>{
    let presencia=prompt(nombre);
    if(presencia.toLowerCase()=="p"){
        totalAlumns[position][1]++;
    }
}

for (i=0; i<30; i++){
    for (alumno in totalAlumns){
        Assistance(totalAlumns[alumno][0], alumno);
    }  
}
for (alumno in totalAlumns){
    let result=`${totalAlumns[alumno][0]}:<br>
         Assistenced:${totalAlumns[alumno][1]}<br>
         Missed:${30-parseInt(totalAlumns[alumno][1])}
`;
    if(30-totalAlumns[alumno][1]>18){
        result+="<b style=`color:red`>FAILED DUE TO NOT ASSISTENCE</b><br><br>"
    }
    else{
        result+="<br><br>"
    }
    document.write(result)

}