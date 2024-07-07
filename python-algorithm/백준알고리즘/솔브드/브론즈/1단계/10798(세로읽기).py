import sys

# sys.stdin = open('input.txt','r')

words = []
for i in range(5):  
  word = sys.stdin.readline().rstrip()
  words.append(word)


# [0][0] -> [1][0] -> [2][0] -> [3][0] -> [4][0]
# [0][1] -> [1][1] -> [2][1] -> [3][1] -> [4][1]
# 생략... 
#
# [i][j] 라고 했을 때
# 이중 for문의 바깥쪽(나중에 증가하는 값)은 j 이고
# 이중 for문의 안쪽(먼저 증가하는 값)은 i 이다
# 예외) 빈 값이 있으면 넘거가야한다.

for j in range(15):
  for i in range(5):
    if j < len(words[i]):
      print(words[i][j], end="")