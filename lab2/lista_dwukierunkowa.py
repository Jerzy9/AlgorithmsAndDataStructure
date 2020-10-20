class Lista_d:

    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = size
        self.half_index = size/2

    def push(self, index, new_el):
        if self.half_index > index:
            this_el = self.head
            next_el = None

            if self.size < self.max_size:
                if index == 0:
                    if self.head is not None:
                        next_el = self.head.next
                    self.head = new_el
                    self.head.next = next_el
                    return 1

                for i in range(0, index - 1):
                    this_el = this_el.next

                new_el.next = next_el
                this_el.next = new_el

                return 1

            print("Lista jest pełna")
            return 0

        this_el = self.tail
#         tail musi działać tak jak head

