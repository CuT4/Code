YT=window.open("https://youtube.com");
YT.close();
YT.closed();

aviso=confirm("Esto sirve para confirmar");
if(aviso){
    alert("Has confirmado");
}else{
    alert("No has confirmado");
}

alert(screenLeft);
alert(screenTop);
alert("Has hecho un scroll X de "+ toString(scrollX)+" y un scroll Y de "+scrollY);

