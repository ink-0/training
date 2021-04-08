
let curry = (fn) => { 
    return function curryFn(...args1) {
        if (args1.length >= fn.length) {
            return fn(...args1);
        } else {
            return (...args2) => curryFn(...args1, ...args2);
        }
    }
}

function multiply(a, b, c){
    return a * b * c;
}

let curriedMultiply = curry(multiply);
let result = curriedMultiply(2,3)(4);
let result = curriedMultiply(2)(3,4);