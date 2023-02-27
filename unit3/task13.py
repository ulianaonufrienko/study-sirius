n=int(input())
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
ad=a-d
bc=b-c
res= ad**2+bc**2
print(res+1)
