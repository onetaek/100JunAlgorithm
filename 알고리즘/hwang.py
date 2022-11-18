import sys
sys.stdin = open("input.txt","r")
size, N = map(int,input().split())
class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.last_idx = 0

    def push(self,value):
        self.arr[self.last_idx] = value
        self.last_idx += 1
    def pop(self):
        if self.empty():
            # 둘중 하나 사용
            # raise Exception("Stack is empty.") 
            return None
        self.last_idx = self.last_idx - 1
        return self.arr[self.last_idx]

    def empty(self):
        if self.last_idx == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.empty() == 0:
            raise Exception("Stack is empty")
        return self.arr[self.last_index - 1]
    
for test_case in range(1,N+1):
    print(f"#{test_case} ",end="") 
    #input_list = list(map(int,input().split()))
    init_stack = Stack(size)
    input_list = list(map(int,input().split()))
    input_stack = Stack(size)
    for input in input_list:
        input_stack.push(input)
    print(init_stack.arr)
    print(input_stack.arr)
    
    # 주어진 숫자를 스태킹을 하여 끝까지 할 수 있는지를 확인하는 것
    # [4,3,2,1] 스택 그리고 받은 스택ex) [2,4,3,1] 두개가있다.
    # 문제를 요약하면 push, pop을 이용하여 init스택을 받은스택으로 만들 수 있는지를 확인하는 것이다.
    # 받을 수 없는 경우는 
     

    print("--------------")