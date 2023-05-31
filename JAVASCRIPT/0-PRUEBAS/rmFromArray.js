let fruits = ['apple', 'bannana', 'lemon', 'pomegrade', 'raspberry', 'orange', 'strawberry']

const removeElementfromArray = (array, value)=>{
    /**
     * The function removeElementfromArray takes two arguments: an array, and the value that
     * must be deleted from the array. If the value exist in the array, the function will return
     * a copy of the array given but without the value that was indicated in the second parameter.
     * 
     * If the first parameter is not an array or the second parameter is not found in the array,
     * it will return false.
     */
    if(!array.includes(value)){
        return false
    }
    return array.slice(0, array.indexOf(value)).concat(array.slice(array.indexOf(value)+1));
}
// removeElementfromArray()