class ANIMAL {
    constructor(especie, edad, color){
        this.especie=especie;
        this.edad=edad,
        this.color=color
        this.info=`Animal: ${this.especie}<br>Edad:${this.edad}<br>Color:${this.color}<br><br>`
    }
    showInfo(){document.write(this.info);}
}

class PERRO extends ANIMAL{
    constructor(especie, edad, color, raza){
        super(especie, edad, color);
        this.raza="Pastor alemán";
        this.info=`Animal: ${this.especie}<br>Edad:${this.edad}<br>Color:${this.color}<br>Raza:${this.raza}<br><br>`;
    }

    
    // set setRaza(newRaza){
    //     this.raza=newRaza;
    // }
    // get getRaza(){
    //     return this.raza;
    // }
      
}




const perro=new PERRO("Draguer", 9, "Marrón");
const canario=new ANIMAL("Piolin", 1, "Amarillo");
const pulpo=new ANIMAL("Pol", 3, "Morado");

// PERRO.setRaza("Bulldog")
// document.write(perro.getRaza())

perro.showInfo();
canario.showInfo();
pulpo.showInfo();