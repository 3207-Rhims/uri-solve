te = int(input())

m = 0
o = 0

for i in range(te):
    v = int(input())
    if(v >= 10 and v <= 20):
        m += 1
    else:
        o += 1

print("%d in" %m)
print("%d out" %o)