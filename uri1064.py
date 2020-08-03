n=[]
count=0
sum=0.0
for i in range(6):
    t=float(input())
    n.append(t)
    if n[i]>0:
        sum=sum+n[i]
        count=count+1
        avg=(sum/count)
print("%d valores positivos"%count)
print("%.1lf"%avg)