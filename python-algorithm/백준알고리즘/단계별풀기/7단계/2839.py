N = int(input())
m_of_3 = [0]
m_of_5 = [0]

for i in range(1,N+1):
    if i%3 == 0 :
        m_of_3.append(i)
    if i%5 == 0 :
        m_of_5.append(i)

answer = []

for i in range(len(m_of_3)):
    for j in range(len(m_of_5)):
        if N == m_of_3[i] + m_of_5[j]:
           answer.append(i+j)

if len(answer)==0:
    print(-1)
else:
    print(min(answer)) 