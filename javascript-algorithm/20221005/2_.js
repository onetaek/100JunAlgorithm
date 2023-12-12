/* num(10진수)를 2진수로 바꾸고 1의갯수를 return */
function count_1(num){
    two_jin_soo = num.toString(2);
    cnt_1 = 0;
    for(let i = 0 ; i < two_jin_soo.length ; i++){
        if(two_jin_soo[i]=='1'){
            cnt_1++;
        }
    }
    return cnt_1
}

function solution(num_arr){
    two_jin_soo_count_arr = []
    let test = 10;
    let test_2 = test.toString(2);
    
    /* 함수를 사용해서 2진수일 대 1의 개수를 배열에 넣음 */
    for( let i = 0 ; i<num_arr.length; i++){
        two_jin_soo_count_arr.push(count_1(num_arr[i]))
    }
    
    
    count_arr = []
    for(let i = 0 ; i < two_jin_soo_count_arr.length;i++){
        temp = []
        temp.push(i)
        temp.push(two_jin_soo_count_arr[i])
        count_arr.push(temp)
    }


    
    count_arr.sort(function(a,b){
        return a[1] - b[1] ;
    })


    sort_num_arr = []
    for( let i = 0 ; i < num_arr.length ; i++){
        sort_num_arr.push(0)
    }

    for(let i = 0 ; i < count_arr.length ; i++){
        sort_num_arr[i] = num_arr[count_arr[i][0]]
    }

    for( let i = 0 ; i < sort_num_arr.length ; i++){
        for( let j = i+1 ; j < sort_num_arr.length  ; j++){
            if((count_1(sort_num_arr[i]) == count_1(sort_num_arr[j])) && (sort_num_arr[i] > sort_num_arr[j])){

                temp = sort_num_arr[i]
                sort_num_arr[i] = sort_num_arr[j]
                sort_num_arr[j] = temp
            }
        }
    }
    return sort_num_arr
}

console.log(solution([11,17,8,2,9]))