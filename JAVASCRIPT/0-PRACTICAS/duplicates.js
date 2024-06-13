function duplicateCount(str) {
    // Convert the input string to lowercase
    str = str.toLowerCase();
    // Create an object to keep track of character counts
    const charCounts = {};
    // Loop over each character in the string
    for (let i = 0; i < str.length; i++) {
      // If the character has already been counted, increment its count
      if (charCounts[str[i]]) {
        charCounts[str[i]]++;
      } else {
        // Otherwise, initialize its count to 1
        charCounts[str[i]] = 1;
      }
    }
    // Count the number of characters that have a count greater than 1
    let count = 0;
    for (const char in charCounts) {
      if (charCounts[char] > 1) {
        count++;
      }
    }
    return count;
  }