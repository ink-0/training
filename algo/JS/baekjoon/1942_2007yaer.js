const fs = require('fs');

let [x, y] = (fs.readFileSync('./test') + '').toString().trim().split(' ');

const day = new Date(2007, x - 1, y);
const week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
console.log(week[day.getDay()]);
