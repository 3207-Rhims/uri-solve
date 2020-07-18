line = str(input(""))

split = line.split(" ")
A = int(split[0])
B = int(split[1])
C = int(split[2])
D = int(split[3])

if B>C and D>A and int(C+D)>int(A+B) and C>0 and D>0 and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")                    