function solution(s){

    var answer = "";
    for(i = 0; i < s.length ; i++){
        if(s.charCodeAt(i)>=65 &&s.charCodeAt(i)<= 65+26){
            answer += s[i].toLowerCase()
        }else if(s.charCodeAt(i)>=97 &&s.charCodeAt(i)<= 97+26){
            answer += s[i].toUpperCase()
        }           
    }
    return answer;
}

console.log(solution("Naver"))