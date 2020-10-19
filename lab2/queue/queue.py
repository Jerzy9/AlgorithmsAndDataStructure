class Queue:

    def __init__(self):
        self.Queue = [0,0,0,0,0,0]
        self.head = 0
        self.tail = 0
        self.size = 5

    def euqueue(self, obj):
        self.tail += 1

        if self.tail > 5:
            self.tail = 0

        if self.head == self.tail:
            self.tail -= 1
            print("Kolejka jest pełna")
            return 0

        self.Queue[self.tail] = obj

    def dequeue(self):
        self.head += 1
        if self.head > 5:
            self.head = 0

        if self.tail == self.head:
            print("Pusta kolejka")
        head = self.Queue[self.head]
        self.Queue[self.head] = 0

        return head


def main():
    q = Queue()
    q.euqueue(1)
    q.euqueue(2)
    q.euqueue(3)
    print(q.Queue)

    print(q.dequeue())
    print(q.Queue)
    print(q.dequeue())
    print(q.Queue)

    q.euqueue(7)
    q.euqueue(8)
    print(q.Queue)


main()



