function solution(arr){
    len_arr = [];
    len = 0
    if(arr.length == 1){
        return arr[0]
    }else if(arr.includes(1)==false){
        return 0
    }else if(arr.includes(0)==false){
        return arr.length
    }
    count = arr.filter(element => 1 === element).length
    if(count == 1){
        return 1
    }
    for(i = 0 ; i < arr.length-1 ; i++ ){
        if( arr[i]!=arr[i+1] && arr[i+1]==1 ){
            len = 1   
        }else if(i==0 &&arr[0]==1&&arr[1] == 0){
            len_arr.push(1)
        }else if(arr[i]!=arr[i+1] && arr[i+1]==0 ){
                len_arr.push(len)      
        }else if((i+1) == arr.length-1){
            len_arr.push(len+1)
        }else if(arr[i]==arr[i+1] && arr[i]==1){
            len +=1
        }
    }
    return Math.max(...len_arr)
}
console.log(solution([1,0,0,0,0,0,0,0]))