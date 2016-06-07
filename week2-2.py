import sys
key=sys.argv[1]
s=raw_input("input text: ")
output=""
for i in s:
    if i.isalpha():
        in_alfabet= ord(i)+ int(key)
        if in_alfabet>ord("z") and i.islower()==True:
            in_alfabet=in_alfabet-26
        elif in_alfabet>ord("Z") and i.isupper()==True:
            in_alfabet=in_alfabet-26
        letter=chr(in_alfabet)
    output=output+letter
print output
