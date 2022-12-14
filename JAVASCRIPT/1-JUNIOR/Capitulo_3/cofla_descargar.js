class APP{
    constructor(descargas, puntuacion, peso){
        this.descargas=descargas;
        this.puntuacion=puntuacion;
        this.peso=peso;
        this.iniciada=false;
        this.instalada=false;
    }
    abrir(){
        if(this.iniciada==false && this.instalada==true){
            this.iniciada=true;
            alert("La app está abierta");
        }
    }
    cerrar(){
        if(this.iniciada==true && this.instalada==true){
            this.iniciada=false;
            alert("La app se ha cerrado");
        }
    }
    instalar(){
        if(this.instalada==false){
            this.instalada=true;
            if(this.instalada==true){
                alert("App installada correctamente");
            }else{
                alert("Ha habido un error con la instalación")
            }
        }
    }
    desinstalar(){
        if(this.instalada==true){
            this.instalada=false;
            if(this.instalada=false){
                alert("App desinstalada");
            }else{alert("Ha habido un error con la desinstalación")}
        }
    }
    appInfo(){
        return `
        Descargas: ${this.descargas}<br>
        Estrellas: ${this.puntuacion}<br>
        Peso: ${this.peso}<br>
        `
    }
}

app1=new APP("1.000.000", "5", "3472MB");
app2=new APP("16.000", "4", "300MB");
app3=new APP("15.000", "3.7", "900MB");
app4=new APP("16.000", "4", "900MB");
app5=new APP("34.000", "4.99", "690MB");
app6=new APP("22.000", "4", "846MB");
app7=new APP("1.000", "2.4", "340MB");

document.write(
    `${app1.appInfo()}<br>
    ${app2.appInfo()}<br>
    ${app3.appInfo()}<br>
    ${app4.appInfo()}<br>
    ${app5.appInfo()}<br>
    ${app6.appInfo()}<br>
    ${app7.appInfo()}<br>`
);

