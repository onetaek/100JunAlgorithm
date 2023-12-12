//거스름돈 구하는 문제
function solution(money){
    money = String(money)//각자리 수를 뽑기 쉽게 문자열 인덱싱사용
    count = 0
    for( i = 0 ; i < money.length ; i++ ){
        if(parseInt(money[i])>=5){//값이 5 이상이면 -4를 해서 더해준다.
            count += (parseInt(money[i]) - 4)
        }else{// 그게 아닐경우 그냥 더해준다.
            count += parseInt(money[i])
        }
    }
    return count
}
console.log(solution(12345))