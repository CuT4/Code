function findEvenIndex(arr) {
    // Loop over each element in the array
    for (let i = 0; i < arr.length; i++) {
      // Calculate the sum of the elements to the left of i
      const leftSum = arr.slice(0, i).reduce((acc, val) => acc + val, 0);
      // Calculate the sum of the elements to the right of i
      const rightSum = arr.slice(i + 1).reduce((acc, val) => acc + val, 0);
      // If the left and right sums are equal, return the current index i
      if (leftSum === rightSum) {
        return i;
      }
    }
    // If no index is found, return -1
    return -1;
  }


/*
The slice() method in JavaScript returns a new array containing a subset of the elements of the original array.

The slice() method takes two arguments:

The start index (inclusive), which is the index of the first element to include in the new array.
The end index (exclusive), which is the index of the first element to exclude from the new array. If this argument is omitted, slice() will include all elements up to the end of the array.

If we omit the second argument to slice(), we get all the remaining elements of the array
*/

/*
reduce() is a higher-order function in JavaScript that applies a callback function to each element of an array, accumulating a result based on the return value of the callback function. The result can be of any type (not necessarily an array).

The callback function passed to reduce() takes two arguments:

The accumulator (acc), which is the result of the previous invocation of the callback function. The initial value of the accumulator is either the first element of the array (if no initial value is provided) or the initial value passed as a second argument to reduce().
The current element (val), which is the current element of the array being processed.
*/