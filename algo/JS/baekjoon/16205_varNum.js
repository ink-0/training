const fs = require('fs');

let [num, varName] = (fs.readFileSync('./test') + '')
  .toString()
  .trim()
  .split(' ');

let ans = [];

const getSnakeCase = (word) => {
  let wordArr = word.split('');
  let result = wordArr.map((word, idx) => {
    if (idx === 0) return word.toLowerCase();
    else if (word === word.toUpperCase() && word !== '_')
      return '_' + word.toLowerCase();
    else return word;
  });
  return result.join('');
};

const getCamelCase = (word) => {
  let wordArr = word.split('');
  let isNextUpper = false;
  let result = wordArr.map((word, idx) => {
    if (word === '_') {
      isNextUpper = true;
      return null;
    } else if (isNextUpper) {
      isNextUpper = false;
      return word.toUpperCase();
    } else if (idx === 0) return word.toLowerCase();
    else return word;
  });

  return result.join('');
};

const getPascalCase = (word) => {
  let wordArr = word.split('');
  let result = wordArr.map((word, idx) => {
    if (idx === 0) return word.toUpperCase();
    else if (word === '_') return null;
    else return word;
  });
  return result.join('');
};

// let varNameArr = varName.split('');
console.log(getCamelCase(varName));
console.log(getSnakeCase(varName));
console.log(getPascalCase(varName));
