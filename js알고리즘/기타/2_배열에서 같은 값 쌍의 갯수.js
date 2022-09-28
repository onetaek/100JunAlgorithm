function solution(nums){
    var answer = 0;
    var i;
    var j;
    for(i = 0 ; i < nums.length-1 ; i++){
        for(j = i + 1 ; j < nums.length ; j++){

            console.log("i: "+i)
            console.log("j: "+j)

            if(nums[i] == nums[j]){
                answer++;
            }
        }
    }
    return answer;
}
console.log(solution([2,5,6,3,2,6,6]))