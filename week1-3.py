try:
    s = float(input('input number: '))
    s=s*100
    count=0
    while s>=25:
        count=count+1
        s=s-25
    while s>=10:
        count=count+1
        s=s-10
    while s>=5:
        count=count+1
        s=s-5
    while s>=1:
        count=count+1
        s=s-1
    print count
except NameError:
    print('It is not a number')
