//둥글게둥글게 문제
function solution(N,K){
    num_arr = []
    //[1,2,3,4,5,6,7] 배열을 N번 나열하는 for문
    for( i = 0 ; i < N ; i ++){
        for( j = 1 ; j <= N ; j ++){
            num_arr.push(j);
        }
    }
    while(true){
        //----제거하다보면 num_arr의 크기가 작아져서 27번째 줄에 num_arr[K-1]의
        //K-1인덱스가 없는 경우가 발생한다. 그래서 num_arr.length가 K보다 작으면 계속해서 값을 추가해준다.
        if( num_arr.length < K){ 
            num_arr_length = num_arr.length
            while( num_arr.length < K){
                for( i = 0 ; i < num_arr_length ; i++ ){
                    num_arr.push(num_arr[i])
                }
            }
        }

        //배열에 있는 값에 첫번째 값과 두번째 값이 같으면 같은 값만 있다는 의미다.
        if(num_arr[0] == num_arr[1]){
            return num_arr[0]
        }
        
        temp = num_arr[K-1]//제거할 값을 임시로 저장한다.
        num_arr = num_arr.splice(K-1)//K-1번째 인덱스 부터 끝까지 값을 num_arr에 저장한다.
        num_arr = num_arr.filter((element) => element !== temp );//temp를 제외하고 나머지 값만 배열로 반환해준다.
    }
}

console.log(solution(50,7))