n = int(input())
arr = map(int, input().split())
    
ls = sorted(list(arr))
for i in range(-n + 1, 1):
    if ls[n-1] == ls[abs(i)]:
        continue
    elif ls[n-1] != ls[abs(i)]:
        print(ls[abs(i)])
        break
