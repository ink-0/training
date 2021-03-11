var kim = {name: 'kim', first:10, second:20}
var lee = {name: 'lee', first:10, second:10}

//만약 lee의 부모를 kim으로 설정
// lee.__proto__=kim

function sum(prefix){
    return prefix +(this.first + this.second);
}
//sum 이라는 객체를 실행시키는 
//sum(); 모든 함수는 call이라는 메서드를 가지고 잇음 함수도 객체이기 떄문에 
// sum.call( )

console.log(sum.call(kim, "=>"));
console.log(sum.call(lee,":"));

var kimSum = sum.bind(kim,"->");
console.log(kimSum());