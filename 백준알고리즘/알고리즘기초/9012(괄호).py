import sys
sys.stdin = open("input.txt","r")
T = int(input())








































# error_list = ["))","((","())(()"]


# for _ in range(T):
#     bracket_list = input()
#     is_no = False
#     print(bracket_list)
#     for error in error_list:
#         if error in bracket_list:
#             is_no = True
#             print("NO")
#         break
#     if is_no == True:
#         is_no = False
#         break
#     if bracket_list[0] == ")" or bracket_list[len(bracket_list)-1] == "(":
#         print("NO")
#     else:
#         open_cnt = 0
#         close_cnt = 0
#         for bracket in bracket_list:
#             if bracket == "(":
#                 open_cnt += 1
#             elif bracket == ")":
#                 close_cnt += 1
#         if open_cnt == close_cnt:
#             print("YES")
#         else:
#             print("NO")
            