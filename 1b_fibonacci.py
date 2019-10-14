#programs generates fibonacci numbers till n
if __name__=="__main__" :
    n=int(input("Enter the number : "))
    a=[0]*n
    a[0]=1
    a[1]=1
    for i in range(2,n):
        a[i]=a[i-1]+a[i-2]
    for i in a:
        print(i,end=" ")
