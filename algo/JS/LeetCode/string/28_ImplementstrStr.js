var strStr = function (haystack, needle) {
  let needleLen = needle.length;

  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      if (haystack.substring(i, i + needleLen) === needle) return i;
    }
  }

  const charToInt = (char) => char.charCodeAt() - 'a'.charCodeAt();
  if (needle.length === 0) return 0;
  if (haystack.length < needle.length) return -1;

  const base = 26;
  let nHash = 0;
  let hHash = 0;

  for (let i = 0; i < needle.length; i++) {
    nHash = nHash * base + charToInt(needle[i]);
    hHash = hHash * base + charToInt(haystack[i]);
    // console.log(i, nHash, hHash);
  }
  if (nHash === hHash) return 0;

  const highOrder = base ** needle.length;

  for (let j = 1; j < haystack.length - needle.length + 1; j++) {
    hHash =
      hHash * base -
      charToInt(haystack[j - 1]) * highOrder +
      charToInt(haystack[j + needle.length - 1]);
    // console.log(
    //   j,
    //   'j',
    //   hHash,
    //   haystack[j - 1],
    //   haystack[j + needle.length - 1]
    // );
    if (nHash === hHash) return j;
  }
  return -1;
};

console.log(strStr('hello', 'll'));
