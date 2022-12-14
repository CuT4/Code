e=0
function Factorial(n) {
    if (n === 0) {
        return 1;
    }
    else {
        return n * Factorial( n - 1 );
    }
}
for (let i = 0; i < 10; i++) {
    e+=(1/Factorial(i));
}
document.write(e);