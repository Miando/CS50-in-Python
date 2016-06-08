import sys
key=sys.argv[1]
s=raw_input("input text: ")
key=str(key)*(len(s)/len(key)+1)

output=""
spases=0
iteratoin=0
for i in s:
    if i ==" ":
        spases=spases+1
        letter=" "
    elif i.isalpha():
        if key[iteratoin-spases].isupper()==True:
            in_alfabet= ord(i)+ord(key[iteratoin-spases])-65
            if in_alfabet>ord("Z"):
                in_alfabet=in_alfabet-26
        elif key[iteratoin-spases].islower()==True:
            in_alfabet= ord(i)+ord(key[iteratoin-spases])-97
            if in_alfabet>ord("z"):
                in_alfabet=in_alfabet-26
        letter=chr(in_alfabet)
    output=output+letter
    iteratoin=iteratoin+1
print output
