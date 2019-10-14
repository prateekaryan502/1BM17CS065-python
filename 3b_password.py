import random as r
import string as s
x=""
a=s.printable[:62]+'@'
for i in range(10):
    x+=a[r.randint(1,63)]
print(x)

