def Capitalize(S):
    resultat=""
    ranshe_bila_bukva=False
    for i in S:
        if ranshe_bila_bukva==False:
            if 'a' <= i <= 'z':
                resultat+=chr(ord(i)-32)
            elif 'A' <= i <= 'Z':
                resultat+=i
            else:
                resultat+=i
        else:
            if 'a' <= i <= 'z':
                resultat+=i
            elif 'A' <= i <= 'Z':
                resultat+=chr(ord(i)+32)
            else:
                resultat+=i
        ranshe_bila_bukva=i.isalpha()
    return resultat



S = input()
B = Capitalize(S)
print (B) 
