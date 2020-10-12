
def read_file(file_name):
    file = open(file_name, "r")
    input = file.readline()
    input = list(input)

    for i in range(0, len(input)):
        if not input[i].isnumeric():
            continue
        input[i] = input[i]
    return input


def write_file(file_output, output):
    file = open(file_output, "w")
    file.write(str(output))
    file.close()


def get_key(dictionary, value):
    for key in dictionary:
        if val == value:
            return key


def onp(input):
    output = []
    signs = []
    levels = {
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }

    for i in input:
        if i.isnumeric():
            output.append(i)
            continue
        get_key(levels)
        signs.append(i)

    return output


def main():
    levels = {
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }
    # input = read_file("input.txt")
    # print(input)
    print(get_key(levels, "+"))


main()
