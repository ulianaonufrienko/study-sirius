elem=int(input())
prev1=elem
prev2=elem
count=0
while elem!=0:
    if prev1 > prev2 and prev1 > elem:
        count+=1
    prev2=prev1
    prev1=elem
    elem=int(input())
    
print(count)
