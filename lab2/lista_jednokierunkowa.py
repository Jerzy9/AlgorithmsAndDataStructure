class Lista_j:

    def __init__(self, size):
        self.size = 0
        self.max_size = size
        self.head = None

    def push(self, index, new_el):
        this_el = self.head
        next_el = None

        if self.size < self.max_size:
            self.size += 1

            if index == 0:
                if self.head is not None:
                    next_el = self.head.next
                self.head = new_el
                self.head.next = next_el
                return 1

            for i in range(0, index-1):
                this_el = this_el.next

            new_el.next = next_el
            this_el.next = new_el

            return 1

        print("Lista jest pełna")
        return 0

    def get_list(self):
        res = [0] * self.max_size
        index = 0
        next_el = self.head

        while next_el is not None:
            res[index] = next_el.el
            next_el = next_el.next
            index += 1
        return res

    def remove(self, index):
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

    def get_el(self, index):
        this_el = self.head

        for i in range(0, index):
            this_el = this_el.next

            if this_el is None:
                print("błędny index")
                break

        return this_el

    def search(self, value):
        this_el = self.head
        index = 0

        while True:
            if this_el.el == value:
                return index
            if this_el.next == self.head:
                print("Nie ma elementu na liście")
                break
            this_el = this_el.next
            index += 1

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


lista = Lista_j(10)

lista.push(0, Element(2))
lista.push(1, Element(3))
lista.push(2, Element(4))
lista.push(3, Element(5))
lista.push(4, Element(6))
lista.push(5, Element(7))

lista.push(0, Element(90))

lista.remove(5)

print(lista.get_list())
print(lista.search(4))

# print(lista.get_el(4).el)


