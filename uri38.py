valores = input()
partes = valores.split()
x= int(partes[0])
y = int(input())
if x==1:
    print("Total: R$",float("%0.2f" % (4*y)))
if x==2:
    print("Total: R$",float("%0.2f" % (4.5*y)))
if x==3:
    print("Total: R$",float("{:.2f}".format(y*5.00)))
if x==4:
    print("Total: R$",float("{:.2f}".format(y*2.00)))
if x==5:
    print("Total: R$",float("{:.2f}".format(y*1.50)))                