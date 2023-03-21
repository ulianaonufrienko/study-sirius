a=list(map(int,input().split()))
ans_i=0
ans_j=1
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j])<abs(a[ans_i]-a[ans_j]):
            ans_i=i
            ans_j=j
print(ans_i,ans_j)
