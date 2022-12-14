let free=false;

const valueClient=(time)=>{
    let age=prompt("How old are you? ")
    if (age>=18){
        if (time>=2 && time<7 && free==false){
            alert("You can enter for free")
            free=true
        }
        else{
            alert("You can enter paying a ticket")
        }
        
    }
    else{
        alert("No eres admitido aquí.")
    }
}

valueClient(3)
valueClient(2)
valueClient(3)
