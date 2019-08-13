#program counts number of zeroes , negatives  and positives .
if __name__=="__main__" :
    a=[1,2,3,4,5,-1,2,3,0]
    cp,cn,cz=0,0,0
    for i in a:
        if i>0:
            cp+=1
        elif i==0:
            cz+=1
        else:
            cn+=1

    print("No. of negative integers : ",cn)
    print("No. of positive integers :", cp)
    print("No. of zeroes :", cz)
