
function solution(A) {
    P = A.length

    const getSumArr = (arr)=>arr.reduce((prev,curr)=>prev+curr)

    let ans = 1000
    for (let i=1 ; i< P ; i++){
        const first = A.slice(0,i)
        const second = A.slice(i,P+1)

        diff = Math.abs(getSumArr(first)-getSumArr(second))
        ans = Math.min (diff,ans)

    }
    return ans
}