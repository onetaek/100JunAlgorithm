def solution(num_list):
    measure_list = []
    for num in num_list:
        temp_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                temp_list.append(i)
        measure_list.append(temp_list)
    #print(measure_list)

    same_measure_list = []
    for j in range(1, len(measure_list)):
        same_measure_list = [
            i for i in measure_list[0] if i in measure_list[j]
        ]
    #print(same_measure_list)
    return max(same_measure_list)



print(solution([30, 100, 10]))