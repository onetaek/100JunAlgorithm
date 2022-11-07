function compare(a, b){
    /* (조건식)?(조건식이 참일경우):(조건식이 거짓일 경우) */
    /* 여기서는 a가 a이 아닐경우에는 2진수로바꾸고 1의 갯수를 구하라는 의미 */
    /* match안에 /1/gi는 나도 처음봐서 검색해보니까 gi는 정규식이라면서 
    g는 모든 검색 결과를 배열로 반환한다는 의미
    i는 영어 대소문자를 구분 않고 일치한다는 의미라고하네용
    https://heropy.blog/2018/10/28/regexp/ 여기들어가보세용
    */
    console.log()
    var aValue = a == 0 ? a : a.toString(2).match(/1/gi).length;
    var bValue = b == 0 ? b : b.toString(2).match(/1/gi).length;
    /* 여기오면 aValue와 bValue에는 a,b의 2진수일 때 1의 갯수를 가지고있겠죠?
    아제 1의갯수가 같으면 10진수일때의 작은 수가 앞에 나와야합니다.
    그러면 compare()함수의 값이 참이어야 교체가 되어야한다.
    쉽게설명: a-b가 참이다? -> a가 b보다크다 -> 앞에 것이 클때 교체해준다.
    */
    if(aValue == bValue){
      return a - b;
    }else{
    /* 그다음: 2진수일때 1의 갯수가 다르다?그러면 그냥 1의 갯수로 오름차순 정렬한다. */
      return aValue - bValue;
    }
  }
  
  function solution(A){
    return A.sort(compare);
    /* sort(함수)이런식으로 나오면
    함수의 값이 참이면 교체한다!
    */
  }
  
  console.log(solution([17,9,5,11]))