check=[]
with open("dictionaries/large", "r") as f:
    for i in f:
        if i!="":
            check.append(i.strip())
#print check
new=[]
ff = open('alice_words.txt','w')
with open("texts/alice.txt", "r") as c:
    for y in c:
        y=y.replace(","," ").replace("."," ").replace(":"," ").replace(")"," ").replace("("," ").replace(";"," ").replace("?","").replace("!"," ")
        y=y.replace("*"," ").replace("--"," ").replace("-"," ").replace('"',"").replace("''"," ").replace("["," ").replace("]"," ")
        y=y.replace("_"," ").replace("3"," ").replace("0"," ")
        f=y.split()
        for x in f:
            if x[0]=="'" :
                x=x[1:]
            elif x[-1]=="'" 
                x=x[:-1]
            x=x.lower()
            if x not in check:
                if x not in new:
                    new.append(x)
                    ff.write(x)
                    ff.write("\n")
