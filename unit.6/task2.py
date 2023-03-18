a=int(input())
i=1
fi1=1
fi2=0
fi=0
while fi<a:
    fi=fi2+fi1
    i+=1
    fi2=fi1
    fi1=fi 
if a!=fi:
    print(-1)
else:
    print(i)
