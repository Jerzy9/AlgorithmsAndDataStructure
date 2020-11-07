def read_input(file_name, split_by):
    file = open(file_name, "r")
    numbers = file.readline()
    numbers = numbers.split(split_by)

    for i in range(0, len(numbers)):
        try:
            numbers[i] = float(numbers[i])
        except:
            numbers.pop(i)

    return numbers


def max_num(numbers_tab):
    max_number = 0
    for num in numbers_tab:
        if max_number >= num:
            continue
        max_number = num
    return max_number


def write_output(output, file_name):
    file = open(file_name, "w")
    file.write(str(output))
    file.close()


def main():
    input_numbers = read_input("max_input.txt", ";")

    max_number = max_num(input_numbers)

    write_output(max_number, "max_output.txt")

    print("output: ", max_number)


main()
