a=int(input())
b=int(input())
c=int(input())
d=int(input())
start=(a-c+d-1)//d*d+c
for i in range (start,b+1,d):
     print(i)
     