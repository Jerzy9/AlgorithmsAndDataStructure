
def read_file(file_name):
    file = open(file_name, "r")
    input = file.readline()
    input = list(input)

    # for i in range(0, len(input)):
    #     if not input[i].isnumeric():
    #         continue
    #     input[i] = input[i]
    return input


def write_file(file_output, output):
    file = open(file_output, "w")
    file.write(str(output))
    file.close()


def get_key(dictionary, value):
    for key in dictionary:
        for val in dictionary.get(key):
            if val == value:
                return key


def onp(input):
    output = []
    stack = []
    levels = {
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }

    for i in input:
        if i.isnumeric():
            output.append(i)
            continue

        elif i == ")":
            for j in stack:
                if j != "(":
                    output.append(stack.pop(0))
                    continue
                stack.pop(0)
                break
            continue

            # if len(stack) != 0 or get_key(stack[len(stack)-1]) < get_key(i):
            #     stack.append(i)
            # else:
            #     output.append(i)

    for i in stack:
        output.append(i)


    return output


def main():
    levels = {
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }
    input = read_file("input.txt")
    print(input)
    print(onp(input))
    # print(get_key(levels, "+"))



main()
