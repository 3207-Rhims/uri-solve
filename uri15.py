import math
l1 = input().split(" ")
l2 = input().split(" ")

x1, y1 = l1
x2, y2 = l2

x1=float(x1)
x2=float(x2)
y1=float(y1)
y2=float(y2)

#x1,y1=list(map(float,input().split()))
#x2,y2=list(map(float,input().split()))
distance = math.sqrt(((x2-x1)**2+(y2-y1)**2))
print("%0.4f"%distance)