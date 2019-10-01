f1=open("prime.txt")
f2=open("happynumber.txt")
s1=[]
s2=[]
def isprime(n):
    if n==1:
        return False
    for i in range(n):
        if i%n==0:
            return False
    return True
for i in range(1000):
    if isprime(i):
        s1.append(i)


