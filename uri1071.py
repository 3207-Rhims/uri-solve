x=int(input())
y=int(input())
sum=0
for i in range(y+1,x):
    if i%2!=0:
        sum=sum+i
print(sum)        