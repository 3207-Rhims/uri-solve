n=[]
count=0
for i in range(6):
    t=int(input())
    n.append(t)
    if n[i]>0:
        count=count+1
print("%d valores positivos"%count)

