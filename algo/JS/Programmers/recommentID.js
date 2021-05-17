function solution(new_id) {
  var answer = '';

  new_id = new_id.toLowerCase();

  const checkEffectWord = (str) => {
    const effectWord = /[^(/-\/_\/.\a-z0-9)]/gi;
    if (effectWord.test(str)) {
      var newStr = str.replace(effectWord, '');
      return newStr;
    } else return str;
  };

  const checkPoint = () => {
    var newStr = str.replace('..', '.');
    return newStr;
  };
}

var temp = checkEffectWord(new_id);
