

const maxNumber = (...numbers) =>{
    /**
    * @param  {...any} numbers The numbers to compare.
    * @returns {maxNumberFound} The maximun value from the given numbers.
    */
    let maxNumberFound = -Infinity;
    for(let i=0; i<numbers.length; i++){
        if(numbers[i]>maxNumberFound){
            maxNumberFound = numbers[i]
        }
    }
    return maxNumberFound;
}
const minNumber = (...numbers) =>{
    /**
    * @param  {...any} numbers The numbers to compare.
    * @returns {minNumberFound} The minimun value from the given numbers.
    */
    let minNumberFound = Infinity;
    for(let i=0; i<numbers.length; i++){
        if(numbers[i]<minNumberFound){
            minNumberFound = numbers[i]
        }
    }
    return minNumberFound;
}