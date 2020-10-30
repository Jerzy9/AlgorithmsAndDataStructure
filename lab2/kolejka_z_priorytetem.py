class QueueP:

    def __init__(self, size):
        self.Queue = [0]*(size+1)
        self.head = 0
        self.tail = -1
        self.size = size
        self.max_size = size

    def euqueue(self, obj):
        self.tail += 1

        if self.tail > self.size-1:
            self.tail = 0

        if self.head == self.tail+1 or (self.head == 0 and self.tail == self.size-1):
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
        if self.head > self.size-1:
            self.head = 0

        return head

        # if pre != 0:
        #     print("head: ", self.head, "   tail: ", self.tail )
        #     while pre-1 > 0 and self.Queue[pre] < self.Queue[pre-1]:
        #         temp = self.Queue[pre]
        #         self.Queue[pre] = self.Queue[pre-1]
        #         self.Queue[pre-1] = temp
        #
        #         pre -= 1


def main():
    q = QueueP(5)
    q.euqueue(1); q.euqueue(2); q.euqueue(3); q.euqueue(4); q.euqueue(5);
    print(q.Queue)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.Queue)
    q.euqueue(1);
    q.euqueue(2);
    q.euqueue(3);
    q.euqueue(4);
    q.euqueue(5);
    print(q.Queue)
    print()


main()



