const reduce = (arr, combine, start=0)=>{
    let current = start;
    for(let element of arr){
        current = combine(current, element)
    }
    return current
}