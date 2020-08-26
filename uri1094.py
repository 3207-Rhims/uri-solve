n=int(input())
sum=0
sum1=0
sum2=0
s=0
for i in range(1,n+1):
    var=input()
    #print(var[:2])
    if var[3:]=="C" or var[2:]=="C":
        sum=sum+int(var[:2])
        #print(sum)
    if var[3:]=="R" or var[2:]=="R":
        sum1=sum1+int(var[:2])
        #print(sum1)
    if var[3:]=="S" or var[2:]=="S":
        sum2=sum2+int(var[:2])
        #print(sum2)
s=sum+sum1+sum2 
avg=(sum/s)*100
av=(sum1/s)*100
a=(sum2/s)*100 
print("Total: %d cobaias"%s)          
print("Total de coelhos: %d"%sum)
print("Total de ratos: %d"%sum1)
print("Total de sapos: %d"%sum2)
print("Percentual de coelhos: %.2lf %%"%avg)
print("Percentual de ratos: %.2lf %%"%av)
print("Percentual de sapos: %.2lf %%"%a)