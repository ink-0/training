
function solution(n, arr1, arr2) {
    var answer = [];
    // return answer;
    for (let i = 0; i < n ; i++) {
     
        let dec2bin1 = arr1[i].toString(2).padStart(n,0)
        let dec2bin2 = ar r2[i].toString(2).padStart(n,0)
        let ans = '';
        console.log(dec2bin1)
        console.log(dec2bin2)
        
        for (let j=n-1 ; j>=0 ; j--){
            ans+=(dec2bin1[j]) | (dec2bin2[j])
        }
        console.log('-------',ans)

        
        
    }


}

