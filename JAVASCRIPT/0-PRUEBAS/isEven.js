const checkIfIsEven = (n)=>{
    /*
    The function isEven takes one parameter, a positive or negative
    integer. It returns 'true' if the number passed is even, otherwise
    it will return 'false'. 
    Lastly, if the value given is not an integer it will return "The value given is not an integer"
    */
    if(Math.round(n)!== n) return "The value given is not an integer"
    if(n===0) return true;
    if(n===1) return false;
    if(n<0) return checkIfIsEven(Math.abs(n));
    else{
        return checkIfIsEven(n-2)
    }
}
button=document.querySelector("#activar-function")
button.addEventListener("click", ()=>{
    console.trace(checkIfIsEven(29));
} )
