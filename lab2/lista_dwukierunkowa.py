class Lista_d:

    def __init__(self, size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = size
        self.half_index = size/2

    def push(self, index, new_el):
        # if self.half_index > index:
        this_el = self.head
        next_el = None

        if self.size < self.max_size:
            if index == 0:
                if self.head is not None:
                    next_el = self.head.next
                self.head = new_el
                self.head.next = next_el
                self.size += 1
                return 1

            for i in range(0, index - 1):
                this_el = this_el.next

            new_el.next = next_el
            new_el.prev = this_el
            this_el.next = new_el

            if next_el is None:
                self.tail = new_el

            self.size += 1
            return 1

        print("Lista jest pełna")
        return 0

    def get_list(self):
        res = [0]*self.max_size
        index = 0
        next_el = self.head

        while next_el is not None:
            res[index] = next_el.el
            next_el = next_el.next
            index += 1
        return res

    def get_el(self, index):
        if self.half_index > index:
            this_el = self.head

            for i in range(0, index):
                this_el = this_el.next
                if this_el is None:
                    print("błędny index")
                    break

            return this_el
        else:
            this_el = self.tail

            for i in range(self.size-1, index, -1):
                print("i", i)
                this_el = this_el.prev
                if this_el is None:
                    print("błędny index")
                    break
            return this_el

    def remove(self, index):
        if self.half_index > index:
            this_el = self.head

            if index == 0 and self.head is not None:
                self.head = self.head.next
                self.size -= 1
                return 1

            for i in range(0, index - 1):
                this_el = this_el.next

            if this_el.next is not None:
                this_el.next = this_el.next.next
                self.size -= 1
                return 1
        else:
            this_el = self.tail

            if index == self.size-1 and self.tail is not None:
                self.tail = self.tail.prev
                self.tail.next = None

                self.size -= 1

                return 1

            for i in range(self.size-1, index, -1):
                this_el = this_el.prev

            if this_el.prev is not None and this_el.next is not None:
                this_el.prev.next = this_el.next
                this_el.next.prev = this_el.prev
                self.size -= 1
                return 1

    def search(self, value):
        this_el = self.head
        index = 0

        while this_el.el != value:
            this_el = this_el.next
            index += 1
            if this_el is None:
                print("Nie ma szukanego elementu na liście")
                return -1
        return index


class Element:

    def __init__(self, el):

        self.el = el
        self.next = None
        self.prev = None


lista = Lista_d(5)

lista.push(0, Element(1))
lista.push(1, Element(2))
lista.push(2, Element(3))
lista.push(3, Element(4))
lista.push(4, Element(5))

print(lista.get_list())
lista.remove(2)
print("")
print(lista.get_list())
print(lista.search(5))

