function earnings (name, wage= 8590, hours = 40){
    console.log(`#${name}님의 급여 정보`);
    console.log(`- 시급: ${wage}원`);
    console.log(`- 근무 시간: ${hours}시간`);
    console.log(`- 급여: ${wage * hours}원`);
    console.log('');
}

earnings('smith');
earnings('adam',10000);
earnings('tom',10000,52);