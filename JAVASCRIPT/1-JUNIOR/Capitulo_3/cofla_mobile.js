//class mobile has color, weight, screen resolution, camara resolution, and RAM
//it can be switched on, switched off, reboot, take photos, and record.

class MOVIL{
    constructor(color, peso, rP, cR, ram){
        this.color=color;
        this.peso=peso;
        this.rP=rP;
        this.cR=cR;
        this.ram=ram;
        this.encendido=false;
        this.informacion=`Este móvil es de color <b>${this.color}</b>, 
        pesa <b>${this.peso}</b>, dispone de una resolución de pantalla de <b>${this.rP}</b>, 
        la resolución de su cámara es de <b>${this.cR}</b>, y tiene <b>${this.ram}</b><br>`;
    }
    SwichOnButton(){
        if (this.encendido==false){
            alert("Móvil encendido");
            this.encendido=true;
        }else{
            alert("Móvil apagado");
            this.encendido=false;
        }
    }
    reiniciar(){
        if(this.encendido==true){
            alert("Reiniciando...");
        }else{
            alert("No se puede reiniciar porque está apagado");
        }
    }
    tomarFoto(){
        alert(`Foto tomada en una resolución de ${this.cR}`);
    }
    grabarVideo(){
        alert(`Grabando video en resolución ${this.cR}`);
    }
    info(){
        document.write(this.informacion)
    }
}


// celular1=new MOVIL("rojo", "150g", "5 pulgadas", "full hd", "2GB");
// celular2=new MOVIL("amarillo", "120g", "5.4 pulgadas", "full hd", "3GB");
// celular3=new MOVIL("blanco", "150g", "5.7 pulgadas", "full hd", "1GB");

// celular1.info()
// celular2.info()
// celular3.info()

class SUPER_MOVIL extends MOVIL{
    constructor(color, peso, rP, cR, ram, rdce){
        super(color, peso, rP, cR, ram);
        this.resolucionDecamaraExtra=rdce;
    }
    grabarVideolento(){
        alert("Estás grabando en cámara lenta");
    }
    reconocimientoFacial(){
        alert("Escaneo facial en curso...");
    }
    infoAG(){
        return this.informacion+`Resolución de cámara trasera: <b>${this.resolucionDecamaraExtra}</b><br>`;
    }
}

celular1=new SUPER_MOVIL("rojo", "150g", "5 pulgadas", "4k", "2GB", "full hd");
celular2=new SUPER_MOVIL("negro", "140g", "6 pulgadas", "4k", "2GB", "hd");

document.write`${celular1.infoAG()}<br>${celular2.infoAG()}`


