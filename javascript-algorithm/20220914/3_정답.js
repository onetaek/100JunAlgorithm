function solution(N, K){
    var  arr = new Array(N);
    var number = 0;
  
    for(var i = 0; i < N; i++){
      arr[i] = i + 1;
    }
  
    for(var i = 0; i < N - 1; i++){
      number += (K - 1);
      console.log('K -1해준 nuumber값: ',number)
      number %= arr.length;
      console.log('%= 해준 number 값:  ',number)
      arr.splice(number, 1);
      console.log('splice 된 arr값 : ',arr)
    }
  
    return arr[0];
  }

  console.log(solution(7,3))