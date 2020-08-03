A,B,C = list(map(float,input().split()))
list=[A,B,C]
list.sort()
a=list[2]
b=list[1]
c=list[0]
a=float(a)
b=float(b)
c=float(c)
if a >= b+ c :
    print("NAO FORMA TRIANGULO")
elif a**2==b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2>b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:  
    print("TRIANGULO ACUTANGULO")
if a==b==c:
    print("TRIANGULO EQUILATERO")
if a==b!=c or b==c!=a or c==a!=b:
    print("TRIANGULO ISOSCELES")     
       
             
