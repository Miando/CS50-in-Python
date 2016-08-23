lst=[5,2,7,4,0,9,8,6,5,7,8,6,5,4,6,2,7,8,5,4,1,5,6,6,-100]
k=0
n=1
while n<(len(lst)):
    while k<(len(lst)-n):
        if lst[k]>lst[k+1]:
            lst[k],lst[k+1]=lst[k+1],lst[k]
            print lst #
        k+=1
    k=0
    n+=1
