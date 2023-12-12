function solution(arr){
    odd_list = []
    for( i = 0 ; i < arr.length ;i++){
        if(arr[i]%2 == 1){
            odd_list.push(arr[i])
        }
    }

    for( i = 0 ; i < arr.length ;i++ ){
        if(odd_list.includes(arr[i])){
            arr.splice(i,0,arr[i])
            arr.pop()
            i++
        }
    }
    return arr
}

console.log(solution([0,2,1,4,3,0]))