//1번째
// function solution(new_id) {
//   var answer = '';

//   new_id = new_id.toLowerCase();

//   const checkEffectWord = (str) => {
//     const effectWord = /[^-_.a-z0-9)]/gi;
//     if (effectWord.test(str)) {
//       var newStr = str.replace(effectWord, '');
//       return newStr;
//     } else return str;
//   };

//   const checkDoublePoint = (str) => {
//     var newStr = str.replace(/[.]{2,}/g, '.');
//     return newStr;
//   };

//   const checkStartPoint = (str) => {
//     var newStr = str.replace(/(^[.])|([.]$)/g, '');
//     return newStr;
//   };

//   var temp = checkStartPoint(checkDoublePoint(checkEffectWord(new_id)));
//   if (!temp) temp = 'a';
//   if (temp.length >= 16) temp = temp.slice(0, 15);
//   console.log('점전', temp);

//   if (temp.substr(temp.length - 1, 1) === '.')
//     temp = temp.substr(0, temp.length - 1);
//   console.log('점후', temp);
//   if (temp.length <= 2) {
//     var lastWord = temp.substr(temp.length - 1, 1);
//     while (temp.length < 3) {
//       temp += lastWord;
//     }
//   }

//   return temp;
// }
//2번재 20:00
function solution(new_id) {
  new_id = new_id
    .toLowerCase()
    .replace(/[^a-z0-9\_.-]/g, '')
    .replace(/\.{2,}/g, '.')
    .replace(/^\.|\.$/g, '')
    .replace(/^$/g, 'a')
    .slice(0, 15)
    .replace(/\.$/, '');
  if (new_id.length <= 2) {
    new_id = new_id.padEnd(3, new_id[new_id.length - 1]);
  }
  return new_id;
}
