
def wordback(s):
    a=s.split()
    print(a)
    x=""
    for i in a[::-1]:
        x+=i+" "
    print(x)
def letterback(s):
    a=list(s)
    x=""
    for i in a[::-1]:
        x+=i
    print(x)
a="Welcome to BMSCE"
wordback(a)
letterback(a)
