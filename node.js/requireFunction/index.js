const { add, sub, mul, div} = require('./functions')

addResult = add(3,5);
subResult = sub(7,4);
mulResult = mul(6,2);
divResult = div(8,4);

console.log({
    'Add':addResult,
    'Substraction':subResult,
    'Multiplication':mulResult,
    'Division':divResult
})