s1=set(open("prime.txt").read().split())
s2=set(open("happynum.txt").read().split(","))
[print(i,end=" ") for i in list(s1.intersection(s2))]



