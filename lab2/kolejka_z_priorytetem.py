class Queue:

    def __init__(self, size):
        self.Queue = [0]*size
        self.head = 0
        self.tail = 0
        self.size = size

    def euqueue(self, obj):
        self.tail += 1

        if self.tail > self.size-1:
            self.tail = 0

        if self.head == self.tail:
            self.tail -= 1
            print("Kolejka jest pełna")
            pass

        self.Queue[self.tail] = obj

        pre = self.tail
        while pre-1 > 0 and self.Queue[pre] < self.Queue[pre-1]:
            temp = self.Queue[pre]
            self.Queue[pre] = self.Queue[pre-1]
            self.Queue[pre-1] = temp

            pre -= 1

    def dequeue(self):
        if self.tail == self.head:
            print("Pusta kolejka")
            return 0

        head = self.Queue[self.head]
        self.Queue[self.head] = 0

        self.head += 1
        if self.head > self.size-1:
            self.head = 0

        return head


def main():
    q = Queue(10)
    print(q.dequeue())
    print(q.Queue)
    print(q.dequeue())
    print(q.Queue)

    q.euqueue(7)
    q.euqueue(8)
    q.euqueue(54)
    q.euqueue(12)
    print(q.Queue)
    print(q.head)
    print(q.dequeue())
    print(q.Queue)


main()



