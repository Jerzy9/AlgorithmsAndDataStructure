class Queue:

    def __init__(self, size):
        self.Queue = [0] * (size + 1)
        self.head = 0
        self.tail = -1
        self.size = size
        self.max_size = size

    def euqueue(self, obj):
        self.tail += 1

        if self.tail > self.size - 1:
            self.tail = 0

        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.size - 1):
            self.tail -= 1
            print("Kolejka jest pełna")
            return 0

        print("przypisz", obj, " na index: ", self.tail)
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


def main():
    q = Queue(5)
    print(q.dequeue())
    print(q.Queue)
    print(q.dequeue())
    print(q.Queue)

    q.euqueue(7)
    q.euqueue(8)
    q.euqueue(8)
    q.euqueue(8)
    print(q.Queue)


main()



