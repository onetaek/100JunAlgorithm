function solution(arr){
    if(arr.length<3){
        return 0
    }
    for(i = 0 ; i < arr.length ;i++){
        for(j = i+1; j < arr.length ; j++){
            if(arr[i] > arr[j]){
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
            }
        }
    }
    sum = 0
    for(i = 1 ; i < arr.length - 1; i++){
        sum += arr[i]
    }
    return parseInt(sum/(arr.length -2))
}

console.log(solution([5,3,1,3,3]))