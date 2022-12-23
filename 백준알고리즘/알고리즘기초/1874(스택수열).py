import sys
sys.stdin = open("input.txt","r")
N = int(input())
input_list = []
for _ in range(N):
    input_list.append(int(input()))
print("input_list")
print(input_list)
my_list = []
stack_list = []
for i in range(N,0,-1):
    my_list.append(i)
print("my_list")
print(my_list)

for input_num in input_list:
    while input_num != my_list[len(my_list)-1]:
        
        
        pass    
