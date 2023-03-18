s=input()
a=int(s[0])
for i in range(2,len(s),2):
    if s[i-1]=='+':
        a+=int(s[i])
    else:
        a-=int(s[i])
print(a)
