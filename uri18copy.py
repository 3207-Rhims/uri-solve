import math
inp=int(input())
print(inp)
t=inp/100
frac,whole=math.modf(t)
print(int(whole),"nota(s) de R$ 100,00")

t2= (inp-(whole*100))/50
one,two=math.modf(t2)
print(int(two),'nota(s) de R$ 50,00')

t3=(inp-(two*50+whole*100))/20
three,four=math.modf(t3)
print(int(four),"nota(s) de R$ 20,00")

t4=(inp-(two*50+whole*100+four*20))/10
five,six=math.modf(t4)
print(int(six),"nota(s) de R$ 10,00")

t5=(inp-(two*50+whole*100+four*20+six*10))/5
seven,eight=math.modf(t5)
print(int(eight),"nota(s) de R$ 5,00")

t6=(inp-(two*50+whole*100+four*20+six*10+eight*5))/1
nine,ten=math.modf(t6)
print(int(ten),"nota(s) de R$ 1,00")

t7=(inp-(two*50+whole*100+four*20+six*10+eight*5+ten*1))/0.50
eleven,tweleve=math.modf(t7)
print(int(tweleve,"nota(s) de R$ 0.50")

t8=(inp-(two*50+whole*100+four*20+six*10+eight*5+ten*1+tweleve*float(0.50))/0.20
thirteen,fourteen=math.modf(t8)
print(int(fourteen),"nota(s) de R$ 0.20")

t9=(inp-(two*50+whole*100+four*20+six*10+eight*5+ten*1+tweleve*0.50+fourteen*float(0.20)))/0.10
fifteen,sixteen=math.modf(t9)
print(int(sixteen),"nota(s) de R$ 0.10")

t10=(inp-(two*50+whole*100+four*20+six*10+eight*5+ten*1+teweleve*0.5+fourteen*0.20+sixteen*float(0.10)))/0.05
seventeen,eighteen=math.modf(t10)
print(int(eighteen),"nota(s) de R$ 0.10")

t11=(inp-(two*50+whole*100+four*20+six*10+eight*5+ten*1+teweleve*0.50+fourteen*0.20+sixteen*0.10+eighteen*float(0.10)))/0.01
nineteen,twenty=math.modf(t11)
print(int(twenty),"nota(s) de R$ 0.20")   



