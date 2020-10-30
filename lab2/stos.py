class Stack:
    def __init__(self, size):
        self.Stack = [] * size
        self.size = 0
        self.max_size = size
        self.top_index = -1

    def top(self):
        if len(self.Stack) < 0:
            print("Pusty stos")
            return 0
        return self.Stack[self.top_index]

    def pop(self):
        top = self.top()

        if self.top_index < 0:
            print("Pusty stps")
            self.top_index = 0
            return 0

        self.Stack[self.top_index] = 0
        self.top_index -= 1

        return top

    def push(self, obj):
        self.size += 1
        self.top_index += 1

        if self.top_index >= self.max_size:
            print("Nie ma miejsca na stosie")
            self.top_index -= 1
            return 0
        self.Stack.append(obj)

        # self.Stack[self.top_index] = obj
        return 1


def read_input(file_name):
    file = open(file_name, "r")
    numbers = file.readline()
    numbers = numbers.split(";")
    stack = Stack(len(numbers))

    for i in range(0, len(numbers)):
        try:
            stack.push(float(numbers[i]))
        except:
            numbers.pop(i)

    print(stack.Stack)

    return stack


def main():
    stack = read_input("input.txt")


main()
