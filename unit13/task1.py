n=int(input())
a=[[ str(abs(i-j))for j in range(n)]
    for i in range(n)]
for row in a:
     print(' '.join(row))
        