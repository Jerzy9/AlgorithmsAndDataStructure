def read_file(file_name):
    file = open(file_name, "r")
    input = file.readline()
    input = list(input)

    return input


def write_file(file_output, output):
    file = open(file_output, "w")
    string_output = ""

    for i in output:
        string_output = string_output + i + " "

    file.write(string_output)
    file.close()


def get_key(dictionary, value):
    for key in dictionary:
        for val in dictionary.get(key):
            if val == value:
                return key


def infix_to_postfix(input):
    stack, output = [], []
    levels = {
        0: ["("],
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }

    for i in input:
        # numbers
        if i.isnumeric():
            output.append(i)
            continue

        elif i in ["+", "-", "*", "/", "^"]:
            while stack and get_key(levels, stack[-1]) > get_key(levels, i):
                output.append(stack.pop())

            stack.append(i)

        elif i == "(":
            stack.append(i)

        elif i == ")":
            for j in stack:
                if stack[-1] != "(":
                    output.append(stack.pop())

                stack.pop()
                break

        # print("Input: " + i + " Stack: " + str(stack) + " Output: " + str(output))
    while stack:
        output.append(stack.pop())
    return output


def main():
    levels = {
        1: ["+", "-"],
        2: ["*", "/"],
        3: ["^"]
    }
    input = read_file("infix_to_postfix_input.txt")
    write_file("infix_to_postfix_output.txt", infix_to_postfix(input))


main()
