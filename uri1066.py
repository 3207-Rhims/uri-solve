count1=0
count2=0
count3=0
count4=0
for i in range(5):
    t=float(input())
    if t%2==0:
        count1=count1+1
    if t%2!=0:
        count2=count2+1
    if t>0:
        count3=count3+1
    if t<0:
        count4=count4+1
print("%d valor(es) par(es)"%count1)
print("%d valor(es) impar(es)"%count2)
print("%d valor(es) positivo(s)"%count3)
print("%d valor(es) negativo(s)"%count4)
                
        
                    
    