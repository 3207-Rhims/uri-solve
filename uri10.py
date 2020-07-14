l1 = input().split(" ")
l2 = input().split(" ")

c1, q1, v1 = l1
c2, q2, v2 = l2
r=float(v1)
t=float(v2)

tot = (int(q1) *float("{:.2f}".format(r)) + (int(q2) *float("{:.2f}".format(t))))

print("VALOR A PAGAR: R$ %0.2f" %tot)