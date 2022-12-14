array1=["maria","josefa","roberta"]
array2=["pedro","marcelo", array1]

for (let elemento in array2){
    if (elemento==2){
        for(let i of array1){
            document.write(i+"<br>")
        }
    }
    else{
        document.write(array2[elemento]+"<br>")
    }

}