// For better understanding, see Euclid's algorithm
const gcd = function(a, b) {
    if (!b) {
        return a;
    }

    return gcd(b, a % b);
};