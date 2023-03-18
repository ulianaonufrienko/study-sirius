n=int(input())
i=3
if  n%2==0:
    print(2)
else:
    while n%i!=0 and i*i <= n:   
        i+=2
    if i*i > n:
        print(n)
    else:
        print(i)
