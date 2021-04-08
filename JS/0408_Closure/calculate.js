function sum(a,b) {
    return a+b;
 }
 
 function divide(a,b) {
    return a/b;
 }
 
function calculate(fn, prev) {
    return (v) => {
        return fn(prev,v)
    }
}
 
// sum100 = (v) => {
//     return sum(100,v)
// }

 
 const sum100 = calculate(sum, 100)
 const divide100 = calculate(divide, 100)
 sum100(20);  //120
 divide100(20); //5