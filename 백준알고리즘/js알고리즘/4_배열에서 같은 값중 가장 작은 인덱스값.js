function solution(nums,n){
    idx_arr = []
    for(i = 0 ; i < nums.length ; i++ ){
        if(nums[i] == n){
            idx_arr.push(i)
        }
    }
    arr = []
    if(idx_arr == arr){
        return -1
    }else{
        return idx_arr[0]
    } 
}
console.log(solution([3,2,4,1,5,3,2,2],7))
console.log('test:'+ ([] == []))