x=int(input())
p=int(input())
y=int(input())
i=0
x=x*100
y=y*100
while x<y:
    x=x+x//100*p
    i+=1
print(i)
