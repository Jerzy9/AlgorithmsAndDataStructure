
def cezar(input, shift):
    output = ""
    for i in input:
        output += (chr(ord(i) + shift))

    print(output)


cezar("ale ma kota a kot ma ale", 2)