var strStr = function (haystack, needle) {
  let needleLen = needle.length;

  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      if (haystack.substring(i, i + needleLen) === needle) return i;
    }
  }
};
