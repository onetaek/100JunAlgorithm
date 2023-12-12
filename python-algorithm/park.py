mylist = [1,3,3,5]
mylist_cnt = [0,0,0,0,0,0]
for i in mylist:
    mylist_cnt[i]+=1
for i in range(1,len(mylist_cnt)):
    print("숫자",i,"는",mylist_cnt[i],"개 있다.")