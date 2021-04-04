function Car(brand) {
    this.carname =brand;
}

Car.prototype.present = function(){
    return "I have a "+ this.carname;
}


function Model(brand,mod){
    Car.call(this,brand);
    this.model = mod;
}

Model.prototype = Object.create(Car.prototype);
Model.prototype.show = function(){
    return this.present()+ "and~~ it is a "+this.model;
}

const mycar= new Model("Ford","Mustang");
console.log(mycar.show());
mycar;
