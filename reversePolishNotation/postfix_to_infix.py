def read_file(file_name):
    file = open(file_name, "r")
    line = file.readline()
    file.close()

    input = line.split(" ")
    return input

def write_file(file_name, output):
    file = open(file_name, output)
    file.write(output)
    file.close()

def postfix_to_infix(input):
    output, stack = "", []

    #2 3 + 5 * 4 2 3 4 + 5 * + + +

    for i in input:
        if i.isnumeric:
            stack.append(i)
        elif len(output) < 0:
            output = "(", stack.pop(), i, stack.pop(), ")"
            # output.append(string)
        else:
            output = "(", output, i, stack.pop()
        print(output)




