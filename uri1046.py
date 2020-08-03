a,b = list(map(int,input().split()))
if a>=b:
    c=(24-a)+b
    print("O JOGO DUROU %d HORA(S)"%c)
else:
    d=b-a 
    print("O JOGO DUROU %d HORA(S)"%d)
       
