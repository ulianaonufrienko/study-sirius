s=int(input())
ans=0
s5=0
while s5 <=s:
  s1=s-s5
  ans+=(s1//2+1)*(s5//10+1)
  s5+=5
print(ans)
