a=list(map(int,input().split()))
h=int(input())
i=0
while i<len(a) and a[i]>=h:
    i+=1
print(i+1)
