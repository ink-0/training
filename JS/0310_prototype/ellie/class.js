'use strict';

class User {
    constructor(firstName, lastName,age) {
        this.firstName = firstName;
        this.lastName= lastName;
        this.age = age;
    }
    //getter
    get age() {
        return this._age;
    }
    //setter
    set age(value) {
        // if(value<0){
        //     throw Error ('age can not be negetive');
        // }
        this._age = value<0? 0:value;
    }

}

const user1 = new User('Steve','Job',-1);
console.log(user1.age);