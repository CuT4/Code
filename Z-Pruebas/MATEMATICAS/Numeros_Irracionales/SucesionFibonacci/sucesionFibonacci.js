let anterior=1;
let siguiente=1;
document.write(1+"<br>")
document.write(1+"<br>")

for (let i = 0; i < 1476 ; i++) {
    let a=anterior+siguiente;
    document.write(a+"<br>")
    anterior=siguiente;
    siguiente=a;
}
