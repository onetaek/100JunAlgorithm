function solution(arr,k){
    let sum = 0;
    city_men = parseInt(arr.length / k)
    console.log('city_men',city_men)
    arr.sort(function (a, b) {
        return a - b;
      });
    console.log('정렬된arr',arr)
    for(i=city_men-1;i<arr.length;i+=city_men){
        console.log('더할값',arr[i])
        sum += arr[i];
    }
    return sum
}
// console.log(solution([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],10))
console.log(solution([6,2,1,4,7,8],3))