function solution(n){
    let sum = []
    num = 1;
    while(Math.pow(max,3)<=n){
        max++;
    }
    console.log(num)
    return Math.pow(max-1 , 3 );
}
console.log(solution(15))