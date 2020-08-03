line=input().split(" ")
a,b,c=line
a=float(a)
b=float(b)
c=float(c)
 # check condition  
if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
    d=0.5*(a+b)*c
    print("Area = %.1f"%d) 
    
else:
    p=a+b+c
    print("Perimetro = %.1f"%p)
    
        
        
        