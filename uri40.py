Line=input().split(" ")
n1,n2,n3,n4=Line
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
n5=0
avg=(n1+n2+n3+n4)/4
print("Media: %.1f"%avg)
if avg>=7:
    print("Aluno aprovado.")
if avg<5:
    print("Aluno reprovado.")
if avg>=5 and avg<=6.9:
    print("Aluno em exame.")
    n5=float(input())
    print("Nota do exame: %.1f" %n5)
    avg1=(n5+avg)/2
    if avg1 >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" %avg1)            
            