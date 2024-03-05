const getNumberSign = (number) => {
    // if number is positive, return positive
    // if number is negative, return negative
    // if number is zero, return zero
    if (number === 0) {
        return 'Zero';
    } else if (number > 0 ) {
        return 'Positive';
    } else {
        return 'Negative';
    } 
    }  

module.exports = getNumberSign;