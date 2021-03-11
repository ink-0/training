function Person(name, first, second, third) {
    this.name= name;
    this.first = first;
    this.second = second;
}
//Person이라는 생성자 함수의 모든 객체에서 사용할 메서드 생성
Person.prototype.sum = function(){
    return 'prototype' + (this.first + this.second);
}


var kim = new Person('kim',10,20);
var lee = new Person('lee',10,10);
kim.sum = function(){
    return 'this'+(this.first + this.second);
}
console.log("kim.sun()",kim.sum());
console.log("lee.sun()",lee.sum());
