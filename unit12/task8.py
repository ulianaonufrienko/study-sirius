n, m = map(int, input().split())
hall = [list(map(int, input().split())) for i in range(n)]
k = int(input())
ans = 0
flag = True
for i in range(n):
   if flag:
       for j in range(m-k+1):
           if hall[i][j:j+k] == [0]*k:
               ans = i + 1
               flag = False
print(ans)
