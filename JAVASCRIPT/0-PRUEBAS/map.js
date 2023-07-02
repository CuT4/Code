const map = (arr, funct) =>{
    let result = [];
    for(let i of arr){
        result.push(funct(arr[i]));
    }
    return result
}