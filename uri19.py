next=int(input())
hour=(next/3600)
hour1=(next%3600)
sec=(hour1/60)
sec1=(hour1%60)
m=sec1
print(int(hour),":",int(sec),":",int(m),sep="")

