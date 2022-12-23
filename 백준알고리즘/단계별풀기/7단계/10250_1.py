n = int(input())
for _ in range(n):
    H,W,N = map(int,input().split())
    if N%H == 0:
        floor = H
    else:
        floor = N%H 
    
    part = 1

    while(True):
        if(N < part * (H * (H-1))):
            break
        part += 1

    ho = int(N/H)+1 + (H-1)*(part -1)
    
    print(f"{floor:01d}{ho:02d}")
    