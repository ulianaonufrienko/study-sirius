ans=0
count=0
elem=int(input())
while elem !=0:
    if count==0:
        ans=elem
        count=1
    elif elem==ans:
        count+=1
    else:
        count-=1
    elem=int(input())
print(ans)
