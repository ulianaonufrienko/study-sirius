n=int(input())
m=int(input())
x=int(input())
y=int(input())

if n>m:
    n,m=m,n

ans=x
if y<ans:
    ans=y

if n-x<ans:
     ans=n-x
if m-y<ans:
    ans=m-y
print (ans)
