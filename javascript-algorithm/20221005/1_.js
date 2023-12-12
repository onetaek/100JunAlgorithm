function solution(s){
    num_arr = [0,0,0,0,0,0,0,0,0,0]
    for( let i = 0 ; i < s.length ; i++){
        num_arr[s[i]]++;
    }
    console.log(Math.max(...num_arr))
    for( let i = 0 ; i < num_arr.length ; i++){
        if(num_arr[i]==Math.max(...num_arr)){
            return i
        }
    }
}
console.log(solution("104001100"))