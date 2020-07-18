t=int(input())
year=t/365
year1=t%365
month=year1/30
month1=(year1%30)
print(int(year),"ano(s)\n",int(month),"mes(es)\n",int(month1),"dia(s)",sep='')

