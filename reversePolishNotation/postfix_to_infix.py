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

# def postfix_to_infix:
