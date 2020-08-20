n=[]
max=0
loc=0
for i in range(3):  
    r=int(input())
    n.append(r)
    if n[i]>max:
        max=n[i]
        loc=i
print(max) 
print(loc+1)     