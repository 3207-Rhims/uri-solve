N=float(input())
if 0 <= N <= 1000000.00:
    first=int(N/100)
    first1=N%100
    first2 = float("%.2f" % first1)
    second=int(first2/50)
    second1=first2%50
    second2 = float("%.2f" % second1)

    third=int(second2/20)
    third1=second2%20
    third2 = float("%.2f" % third1)

    four=int(third2/10)
    four1=third2%10
    four2 = float("%.2f" % four1)

    five=int(four2/5)
    five1=four2%5
    five2 = float("%.2f" %five1)

    six=int(five2/2)
    six1=five2/2
    six2 = float("%.2f" % six1)

    p=(first*100)+(second*50)+(third*20)+(four*10)+(five*5)+(six*2)
    t=(N-p)
    seven=int(t/1)
    seven1=t%1
    seven2 = float("%.2f" % seven1)

    eight=int(seven1/0.50)
    eight1=seven1%0.50
    eight2 = float("%.2f" % eight1)

    nine=int(eight2/0.25)
    nine1=eight2%0.25
    nine2 = float("%.2f" % nine1)

    ten=int(nine2/0.10)
    ten1=nine2%0.10
    ten2 = float("%.2f" % ten1)

    eleven=int(ten2/0.05)
    eleven1=ten2%0.05
    eleven2 = float("%.2f" % eleven1)

    tweleve=int(eleven2/0.01)
    print("NOTAS:")
    print(first,"nota(s) de R$ 100.00")
    print(second,"nota(s) de R$ 50.00")
    print(third,"nota(s) de R$ 20.00")
    print(four,"nota(s) de R$ 10.00")
    print(five,"nota(s) de R$ 5.00")
    print(six,"nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(seven,"nota(s) de R$ 1.00")
    print(eight,"nota(s) de R$ 0.50")
    print(nine,"nota(s) de R$ 0.25")
    print(ten,"nota(s) de R$ 0.10")
    print(eleven,"nota(s) de R$ 0.05")
    print(tweleve,"nota(s) de R$ 0.01")
