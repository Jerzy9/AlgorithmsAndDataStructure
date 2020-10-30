class Queue:

    def __init__(self, size):
        self.Queue = [0] * (size + 1)
        self.head = 0
        self.tail = -1
        self.size = size
        self.max_size = size

    def enqueue(self, obj):
        self.tail += 1

        if self.tail > self.size - 1:
            self.tail = 0

        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size - 1):
            self.tail -= 1
            print("Kolejka jest pełna")
            return 0

        self.Queue[self.tail] = obj

    def dequeue(self):
        if self.tail+1 == self.head:
            print("Pusta kolejka")
            return 0

        head = self.Queue[self.head]
        self.Queue[self.head] = 0

        self.head += 1
        if self.head > self.size - 1:
            self.head = 0

        return head


def read_input(file_name):
    file = open(file_name, "r")
    numbers = file.readline()
    numbers = numbers.split(";")
    que = Queue(len(numbers))

    for i in range(0, len(numbers)):
        try:
            que.enqueue(float(numbers[i]))
        except:
            print("Błędny znak")

    print(que.Queue)

    return que

def main():
    q = read_input("input.txt")

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(8)
    q.enqueue(9)
    q.dequeue()
    print(q.Queue)

main()


