function solution(arr){
    let sum = 0;
    arr.sort(function (a, b) {
        return a - b;
      });
    for(i=1;i<arr.length;i+=2){
        sum += arr[i];
    }
    return sum
}
console.log(solution([1,2,100,99]))