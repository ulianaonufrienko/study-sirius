

def IsPalindrome(S):
    a = S.lower()
    resultat=True
    for i in range (len(a)):
        if a[i-1]!=a[-i]:
            resultat=False
    return resultat

S = input()
if IsPalindrome(S):
    print('YES')
else:
    print('NO')
