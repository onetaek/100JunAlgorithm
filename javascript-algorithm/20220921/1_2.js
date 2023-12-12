function len_fun(i,len,arr,len_arr){
    if(arr.length == 0){
        return 0
    }else if(arr.length ==1){
        return arr[0]
    }
    if(i == len_arr.length - 1 && arr[i]==1){
        console.log('i == len_arr.length - 1 && arr[i]==1,일때')
        len_arr.push(len)
        return Math.max(...len_arr)
    }else if(i==arr.length - 1){
        console.log('arr[i]==1,일때')
        return Math.max(...len_arr)
    }else if(arr[i]==1){
        console.log('arr[i]==1,일때')
        len += 1
    }else if(arr[i]==0){
        console.log('arr[i]==0,일때')
        len_arr.push(len);
        len = 0;
    }
    i++
    console.log(len_arr)
    return len_fun(i,len,arr,len_arr)
}
function solution(arr){
    i = 0
    len = 0
    len_arr = []
    return len_fun(i,len,arr,len_arr)
    
}

console.log(solution([1,0,1,1,1,1]))