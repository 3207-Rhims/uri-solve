n=float(input())
if n>=0 and n<=2000:
    print("Isento")
elif n>=2000.01 and n<=3000:
    m=(n-2000)
    m1=m*(8/100)
    print("R$ %.2lf"%m1)
elif n>=3000.01 and n<=4500:
    m=(n-3000)
    m1=m*(18/100)+80
    print("R$ %.2lf"%m1)
elif n>4500:
    m=(n-4500)
    m1=m*(28/100)+350
    print("R$ %.2lf"%m1)    
        
       
            
