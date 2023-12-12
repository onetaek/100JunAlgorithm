# 두개의 리스트를 비교해서 같은 값만 저장한 리스트를 반환하는 함수만들기!!
def same_value(list_1,list_2):
    same_list = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                same_list.append(list_1[i])
    return same_list
# 이거는 그냥 문제푸는 함수
def solution(num_list):
    measure_list = []
    for num in num_list:
        temp_list = []
        for i in range(1, num + 1):
            if num % i == 0:
                temp_list.append(i)
        measure_list.append(temp_list)

    same_measure_list = []
    for i in range(1, len(measure_list)):
        same_measure_list = same_value(measure_list[0],measure_list[i])
    return max(same_measure_list)

print(solution([15, 5, 50]))

