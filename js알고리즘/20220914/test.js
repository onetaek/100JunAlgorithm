function solution(A) {
    let arr = []
    console.log(A.length)
    for(i=0;i<A.length; i++){       
        for(j=0; j<A[i]+1; j++){
            console.log(i,j)
            if(A[i]%j == 0){
                arr.push(j)     
            }
        }
    return arr
    }
}

console.log(solution([6, 10, 14]))
// js는 ctrl + alt + N 이 샐행