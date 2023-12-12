function solution(n){
    var arr = []
    while( n > 0 ){
        arr.push(n%2)
        n = parseInt(n/2)
    }
    var arr_idx = []

    for(i = 0 ; i < arr.length ; i++ ){
        if(arr[i] == 1){
            arr_idx.push(i)
        }
    }

    var max = 0
    for(i = 1 ; i < arr_idx.length ; i++){
        if( Math.abs(arr_idx[i] - arr_idx[i-1]) > max ) {
            max = Math.abs(arr_idx[i] - arr_idx[i-1])
        }
    }
    return max
}

solution(11)