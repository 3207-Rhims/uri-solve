name = input()
salary = float(input())
sell= float(input())
rate=float("{:.2f}".format(salary))
product=float("{:.2f}".format(sell))

tot = ((sell*0.15)+salary)

print("TOTAL = R$ %0.2f"%tot)