//최대 공약수 구하는 문제
function solution(num_arr){
    let measure_arr = [] // 약수를 저장하는 배열(2차원 배열임)
    for(i = 0 ; i < num_arr.length ; i ++){
        temp_arr = [] // 한개의 수에 대한 약수들을 저장하기 위한 배열
        //measure_arr에 push하기 때문에 for문을 돌때 마다 초기화 시켜준다.
        for( j = 1 ; j <= num_arr[i] ; j++ ){
            if (num_arr[i] % j == 0){
                temp_arr.push(j)
            }
        }
        measure_arr.push(temp_arr)// 각각의 수에 대해서 measure_arr에 push해준다.
    }
    //console.log(measure_arr)

    same_measure_arr = []//대충 공약수라는 의미 -> max함수를 사용하여 최대 공약수를 찾을거당.

    for( i = 0 ; i < measure_arr.length ; i ++ ){
        //구글에 filter 함수랑 includes 함수를 사용하는 방법을 찾아 보면됨
        //대충 두개의 배열을 비교해서 같으 값만 고를 수 있는 방식이다.
        //measure_arr의 0번째 인덱스 배열과 1번째 인덱스를 비교하고 2번째..3번째...랑 계속 비교해주면
        //결국 모든 배열들의 공약수들을 구할 수 있다.
        same_measure_arr = measure_arr[0].filter  
        (measure => measure_arr[i].includes(measure))
    }
    //console.log(same_measure_arr)
    return Math.max(...same_measure_arr)//공약수중 최대값을 리턴!
}

console.log(solution([5,15,50]))