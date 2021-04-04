var superObj = {superVal:'super'}

// var subObj = {subVal :'sub'}
// subObj.__proto__ = superObj;

var subObj = Object.create(superObj);
subObj.subVal = 'sub';
debugger;
// console.log("sub의 subVal",subObj.subVal); //sub
// console.log("sub의 superVal",subObj.superVal); //super
// subObj.superVal = 'sub';
// console.log("super의 superVal",superObj.superVal); //super

kim = {
    name:'kim',
    first:10,
    second:20,
    sum: function(){return this.first +this.second;}
}

var lee = Object.create(kim);

lee.name = 'lee'
lee.first=10;
lee.second=10;

lee.avg = function(){return (this.first +this.second)/2;}
console.log("lee.sum()",lee.avg());
