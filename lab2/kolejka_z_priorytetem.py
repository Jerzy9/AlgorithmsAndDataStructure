class QueueP:

    def __init__(self, size):
        self.Queue = [0]*(size+1)
        self.head = 0
        self.tail = -1
        self.size = size+1
        self.max_size = size

    def enqueue(self, obj):
        self.tail += 1

        if self.tail > self.size-1:
            self.tail = 0

        if self.head == self.tail+1 or (self.head == 0 and self.tail == self.size-1):
            self.tail -= 1
            print("Kolejka jest pełna")
            return 0

        self.Queue[self.tail] = obj

        pre = self.tail

        while True:

            if self.Queue[pre] == 0 or self.Queue[pre-1] == 0:
                break

            elif pre == 0:
                if self.Queue[pre] > self.Queue[self.size-1] != 0:
                    temp = self.Queue[pre]
                    self.Queue[pre] = self.Queue[self.size-1]
                    self.Queue[self.size-1] = temp

                    pre = self.size-1
                    continue

            elif self.Queue[pre] > self.Queue[pre - 1] != 0:
                temp = self.Queue[pre]
                self.Queue[pre] = self.Queue[pre - 1]
                self.Queue[pre - 1] = temp

                pre -= 1
            else:
                break

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


def main():
    q = QueueP(5)
    q.enqueue(1); q.enqueue(2);q.enqueue(3); q.enqueue(1); q.enqueue(2);q.enqueue(3);
    print(q.Queue)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(8)
    q.enqueue(9)
    q.dequeue()
    print(q.Queue)

main()



