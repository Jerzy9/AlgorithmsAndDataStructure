def read_file(file_name):
    file = open(file_name, "r")
    line = file.readline()
    file.close()

    input = line.split(" ")
    return input


def write_file(file_name, output):
    file = open(file_name, "w")
    file.write(str(output))
    file.close()


def postfix_to_infix(input):
    output, stack = "", []

    for i in input:
        if i.isnumeric():
            stack.append(i)
            continue
        else:
            output = stack[-2] + i + stack[-1]
            stack.pop()
            stack += ""
            stack[-1] = "(" + output + ")"

        print("el: ", i, " stack: ", stack, " output: ", output)
    return output


def main():
    input = read_file("postfix_to_infix_input.txt")
    output = postfix_to_infix(input)
    print(output)
    write_file("postfix_to_infix_output.txt", output)

main()

