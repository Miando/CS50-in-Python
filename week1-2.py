while True:
    c=raw_input("input number of piramyd: ")
    n=int(c)
    if n>23 or n<=0:
        True
    else:
        break
for i in range(1,n+1):
    print " "*(n-i)+"*"*(i+1)


#def mario():
