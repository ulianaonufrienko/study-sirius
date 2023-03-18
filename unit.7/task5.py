s=input()
ans=""
for i in range (len(s)):
    j=s.rfind(s[i])+1
    if j-i>len(ans):
        ans=s[i:j]
print(ans)
        
        
    