function solution(arr){
    let sum = 0
    arr.sort((a,b)=>b-a)
    sum = 0
    for(i = 1 ; i < 4 ; i++){
        sum += arr[i];
    }
    if(arr[0]>=sum){
        return 0
    }else{
        return sum + arr[0]
    }
}
console.log(solution([3,2,3,1]))