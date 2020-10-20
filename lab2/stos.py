class Stack:
    def __init__(self, size):
        self.Stack = []*size
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
        print(self.Stack)
        self.Stack[self.top_index] = 0
        self.top_index -= 1
        print(self.Stack)

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


def main():
    stack = Stack(10)
    stack.push(5)
    print(stack.top())
    stack.push(4)
    stack.push(3)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())



    # stack.push(stack)


main()
