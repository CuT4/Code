const sum=(arr)=>{
    //It takes an array and sums all its terms
    let result = 0;
    for(let i=0; i<arr.length; i++){
        result+=arr[i];
    }
    return result
};
const range=(start, end)=>{
    //Returns and array with all the numbers between start and end, both included
    let result = [];
    for(let i=start; i<=end; i++){
        result.push(i);
    }
    
    return result
}
const reverseArray=(arr)=>{
    //REFACTOR
    const result=[];
    for(let i=-1; i>-arr.length; i){
        result.push(arr[i])
    }
    arr=result;
    return arr;
}