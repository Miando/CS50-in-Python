name=raw_input("print First name, Second name: ")
def inicials(s):
    list_names=s.split()
    inicials=""
    for i in list_names:
        inicials=inicials + i[0].upper()
    return inicials


print inicials(name)
