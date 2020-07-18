next=int(input())

#find hour
hour=(next/3600)
#remainig second
hour1=(next%3600)
#find minute
min=(hour1/60)
#reamining minute
sec1=(hour1%60)

m=sec1

print(int(hour),":",int(min),":",int(m),sep="")

