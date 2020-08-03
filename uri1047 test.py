a,b,c,d = list(map(int,input().split()))
if a==b==c==d:
    h,m=24,0
else:
    if d>=b:
        m=d-b
    else:
        m=60- abs(d-b)
        c=c-1
    if c>=a:
        h=c-a
    else:
        h=24 - abs(c-a)    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h,m))    
    