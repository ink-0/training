class Shape { 
    constructor(width, height, color) {
        this.width = width;
        this.height =height;
        this.color = color;
    }

    draw () {
        console.log(`drawing ${this.color} color of`);
    }

    getArea() {
        return width * this.height;
    }
}

class Rectangle extends Shape{
}

class Triangle extends Shape{
    draw(){
        console.log('▲')
    }
    //overiding
    getArea(){
        return (this.width * this.height)/2;
    }
    //overiding

    toString() {
        return `Triangle color : ${this.color}`;
    }
}

const rectangle = new Rectangle(20,20,'blue');
rectangle.draw();
const triangle = new Triangle(20,20,'red');
triangle.draw();

console.log(rectangle instanceof Rectangle); // True
console.log(triangle instanceof Rectangle); // False
console.log(triangle instanceof Triangle); // True
console.log(triangle instanceof Shape); // True
console.log(triangle instanceof Object); // True
console.log(triangle.toString()); 