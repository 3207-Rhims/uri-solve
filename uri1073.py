n=int(input())
if n>5 and n<2000:
    for i in range(1,n+1):
        if i%2==0:
            d=i**2
            print("%d^2 = %d"%(i,d))