line=input().split(":")      
a,b,c=line
a=int(a)
b=int(b)
c=int(c)
one=input().split(" ")
k,j=one
j=int(j)
line=input().split(":")      
a1,b1,c1=line
a1=int(a1)
b1=int(b1)
c1=int(c1)

#if a==a1==b1==b==c1==c:
    #d,h,m,s=1,0,0,0
#else:
if j>=i:
    d=j-i
elif j<=i:
    d=0 
    
if a1>=a:
    h=a1-a
else:
    h=24 - abs(a1-a)
    d=d-1

if b1>=b:
    m=b1-b
else:
    m=60- abs(b1-b)
    h=h-1
    
    
    
if c1>=c:
    s=c1-c
else:
    s=60-abs(c1-c)
    m=m-1

             
print("%d dia(s)"%d)
print("%d hora(s)"%h)
print("%d minuto(s)"%m)
print("%d segundo(s)"%s)                

