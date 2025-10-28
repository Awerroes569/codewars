var Morse = {};

Morse.alpha = {
    'A': '10111',
    'B': '111010101',
    'C': '11101011101',
    'D': '1110101',
    'E': '1',
    'F': '101011101',
    'G': '111011101',
    'H': '1010101',
    'I': '101',
    'J': '1011101110111',
    'K': '111010111',
    'L': '101110101',
    'M': '1110111',
    'N': '11101',
    'O': '11101110111',
    'P': '10111011101',
    'Q': '1110111010111',
    'R': '1011101',
    'S': '10101',
    'T': '111',
    'U': '1010111',
    'V': '101010111',
    'W': '101110111',
    'X': '11101010111',
    'Y': '1110101110111',
    'Z': '11101110101',
    '0': '1110111011101110111',
    '1': '10111011101110111',
    '2': '101011101110111',
    '3': '1010101110111',
    '4': '10101010111',
    '5': '101010101',
    '6': '11101010101',
    '7': '1110111010101',
    '8': '111011101110101',
    '9': '11101110111011101',
    '.': '10111010111010111',
    ',': '1110111010101110111',
    '?': '101011101110101',
    "'": '1011101110111011101',
    '!': '1110101110101110111',
    '/': '1110101011101',
    '(': '111010111011101',
    ')': '1110101110111010111',
    '&': '10111010101',
    ':': '11101110111010101',
    ';': '11101011101011101',
    '=': '1110101010111',
    '+': '1011101011101',
    '-': '111010101010111',
    '_': '10101110111010111',
    '"': '101110101011101',
    '$': '10101011101010111',
    '@': '10111011101011101',
    ' ': '' // Technically is 7 0-bits, but we assume that a space will always be between two other characters
};

Morse.convertCharToBits = function (char) {
    const chr = char.toUpperCase();
    return Morse.alpha[chr];
}

Morse.convertingStringToBits = function (str) {
    
    let result = '';
    for (let i = 0; i < str.length; i++) {
        let toAdd = Morse.convertCharToBits(str[i]);
        result += toAdd;
        //console.log('str',i,'is',str[i])
        if (str[i + 1] === undefined) {
            //console.log('undefined exit')
            break;
        }
        else if (str[i + 1] === ' ')  {
            //console.log('str is ', str[i+1])
            result += '0000000';
        } else if (result.slice(-3) !=='000') {
            result += '000';
        }
        
    }
    return result;
}

Morse.cuttingStringToPieces = function (string, length) {
    result = [];
    for (let i = 0; i < string.length; i += length) {
        let toAdd = string.slice(i, i + length);
        result.push(toAdd);
    }
    let lastElement = result.pop();
    const lacking = length - lastElement.length;
    lastElement += '0'.repeat(lacking);
    result.push(lastElement);
    
    return result;
}

Morse.convertStringTo32Integer = function (string) {
    let signed = (parseInt(string, 2) | 0);   // Output: -1
    return signed;
}

Morse.encode = function (message) {
    const asBytes = Morse.convertingStringToBits(message);
    console.log('as bytes', asBytes);
    const pieces = Morse.cuttingStringToPieces(asBytes, 32);
    console.log('as pieces of bytes', pieces);
    const result = [];
    for (let piece of pieces) {
        const asSignedInt = Morse.convertStringTo32Integer(piece);
        result.push(asSignedInt);
    }
    return result;

};


Morse.convert32IntegerToString = function (n) {
    return (n >>> 0).toString(2).padStart(32, '0');
}

Morse.decode = function (integerArray) {
    // ·–·–·– ·–·–·– ·–·–·–
};

//FINDING BITS USING CHAR
console.assert(Morse.convertCharToBits('A') === '10111','Test 1 failed');
console.assert(Morse.convertCharToBits('a') === '10111','Test 2 failed');
console.assert(Morse.convertCharToBits(',') === '1110111010101110111', 'Test 3 failed');
//CONVERTING STRING TO BYTES
console.assert(Morse.convertingStringToBits('aA') === '1011100010111', 'Test 4 failed');
console.assert(Morse.convertingStringToBits('a A') === '10111000000010111', 'Test 5 failed');
//CUTTING STRING TO PIECES
console.assert(Morse.cuttingStringToPieces('01234567890', 4)[0] === '0123', 'Test 6 failed');
console.assert(Morse.cuttingStringToPieces('01234567890', 4)[2] === '8900', 'Test 7 failed');
//CONVERTING STRING TO SIGNED INTEGER
console.assert(Morse.convertStringTo32Integer('10101010001000101110101000101110') === -1440552402, 'Test 8 failed');
console.assert(Morse.convertStringTo32Integer('10100011101110111000000010111011') === -1547992901, 'Test 9 failed');
//CONVERTING SIGNED INTEGER TO STRING
console.assert(Morse.convertStringTo32Integer( -1440552402) === '10101010001000101110101000101110', 'Test 10 failed');
console.assert(Morse.convertStringTo32Integer(-1547992901) === '10100011101110111000000010111011', 'Test 11 failed');

console.log(Morse.encode('HELLO WORLD'));
 //   10100011101110111000000010111011

//ENCODE
//1. find character  OK
//2. check what next: char or space   insert 000
//3. adjust to 32 bit
//4.cut to 32 bit
//5. convert to array of numbers

//DECODE
//1. CREATE ARRAY OF BYTES FROM SIGNED INTEGERS
//2. CUT ZEROS FROM END
//3. SPLIT BY 7 ZEROS TO ARRAY
//4 EVERY PIECE SPLIT BY 3 ZEROS
//5. FOR EVERY SUBPIECE DETECT CHR+ADDING SPACE
//6. CUT LAST SPACE
