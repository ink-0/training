const user = {name:'tami',age:'25'};
const user2 = user;



const user3 = {};

//old way
for(key in user){
    user3[key]=user[key];
}

//object.assign
const user4 = Object.assign({},user);
console.log(user4)

const fruit1 = {color:'red'};
const fruit2 = {color:'blue', size:'big'};
const mixed = Object.assign({},fruit1,fruit2);
console.log(mixed.color);
console.log(mixed.size);
