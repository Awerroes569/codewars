function NumberOperation(num,expr) {
    const expression = String(num) + expr;
    return new Function(`return parseInt(${expression})`)();
}
function processNumber(num, args) {
    if (args.length > 0) {
        return NumberOperation(num, args[0]);
    } else {
        return num;
    }
}
function zero() {
    return processNumber(0, arguments);
}
function one() { 
    return processNumber(1, arguments);
}
function two() { 
    return processNumber(2, arguments);
}
function three() {
    return processNumber(3, arguments);
 }
function four() {
    return processNumber(4, arguments);
 }
function five() { 
    return processNumber(5, arguments);
}
function six() {
    return processNumber(6, arguments);
 }
function seven() {
    return processNumber(7, arguments);
 }
function eight() { 
    return processNumber(8, arguments);
}
function nine() {
    return processNumber(9, arguments);
 }
function plus() {
    return '+'+String(arguments[0]);
 }
function minus() { 
    return '-'+String(arguments[0]);
}
function times() {
    return '*'+String(arguments[0]);
 }
function dividedBy() { 
    return '/'+String(arguments[0]);
}
