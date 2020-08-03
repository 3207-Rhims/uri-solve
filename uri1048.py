n=float(input())
if n>=0 and n<=400:
    d=(n*(15/100))
    p=d+n
    print("Novo salario: %.2lf"%p)
    print("Reajuste ganho: %.2lf"%d)
    print("Em percentual: 15 %")
if 400.01<=n and n<=800:
    d=(n*(12/100))
    p=d+n
    print("Novo salario: %.2lf"%p)
    print("Reajuste ganho: %.2lf"%d)
    print("Em percentual: 12 %")
if 800.01<=n and n<=1200:
    d=(n*(10/100))
    p=d+n
    print("Novo salario: %.2lf"%p)
    print("Reajuste ganho: %.2lf"%d)
    print("Em percentual: 10 %")
if 1200.01<=n and n<=2000:
    d=(n*(7/100))
    p=d+n
    print("Novo salario: %.2lf"%p)
    print("Reajuste ganho: %.2lf"%d)
    print("Em percentual: 7 %")     
if n>2000:
    d=(n*(4/100))
    p=d+n
    print("Novo salario: %.2lf"%p)
    print("Reajuste ganho: %.2lf"%d)
    print("Em percentual: 4 %")        
    
     