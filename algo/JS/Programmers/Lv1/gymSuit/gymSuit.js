function solution(n, lost, reserve) {
  var answer = 0;
  n -= lost.length;
  let spareLost = [];
  lost.map((stu) => {
    if (reserve.includes(stu)) {
      reserve.splice(reserve.indexOf(stu), 1);

      n += 1;
    } else {
      spareLost.push(stu);
    }
  });

  spareLost.map((ele) => {
    if (reserve.includes(ele - 1)) {
      reserve.splice(reserve.indexOf(ele - 1), 1);

      n += 1;
    } else if (reserve.includes(ele + 1)) {
      reserve.splice(reserve.indexOf(ele + 1), 1);

      n += 1;
    }
  });
  return n;
}
//test case 12 불통
// function solution(n, lost, reserve) {
//   return n-lost.filter(lstu => {
//       const spareStu = reserve.find(rstu => Math.abs(rstu-lstu)<=1)
//       if(!spareStu) return true
//       reserve = reserve.filter(rstu => rstu!==spareStu)
//   }).length
// }
