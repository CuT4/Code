const primeFactors=(n)=>{
    let factors = [];
    let divisor = 2;
    if(n==1) return factors.push(n);
    while(n>=2){
        if(n%divisor==0){
            factors.push(divisor);
            n = n/divisor;
        }
        else{
            divisor++
        }
    }
    return factors
}

/*
let primeNumbers=[];
for(let i=0; i<=1000000; i++){
    if(primeFactors(i).length == 1) primeNumbers.push(primeFactors(i)[0])
    console.log(`primeFactors(${i}) => `, primeFactors(i));
}
console.log(primeNumbers);
*/



