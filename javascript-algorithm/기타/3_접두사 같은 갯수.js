function solution(array,s){
    var answer = 0;
    for(i = 0 ; i < array.length ; i++){
        if(array[i]==s.slice(0,array[i].length)){
            answer++;
        }
    }
    return answer;
}
console.log(solution(['n','nav','nev'],'naver'))