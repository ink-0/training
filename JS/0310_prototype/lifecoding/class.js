class Person {
    constructor(name,first,second){

        this.name= name;
        this.first = first;
        this.second = second;
    }
    sum(){
        return this.first + this.second;
    }
}
class PersonPlus extends Person{
    constructor(name,first,second,third){
        super(name,first,second,third)
        this.third = third;
    }
    sum(){
        return super.sum()+this.third;
    }
    average(){
        return (this.first+this.second+this.third)/2;
    }
}

var kim = new PersonPlus('kim',10,20,30);
console.log('kim',kim.average());