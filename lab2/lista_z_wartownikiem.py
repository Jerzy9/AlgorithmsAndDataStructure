class Lista_c:

    def __init__(self, size):
        self.head = Element(0)
        self.size = 0
        self.max_size = size

    def push(self, index, new_el):
        this_el = self.head
        next_el = None

        if self.size < self.max_size:
            self.size += 1

            if index == 0:
                if self.head is not None:
                    next_el = self.head.next.next
                self.head = new_el
                self.head.next = next_el
                return 1

            for i in range(0, index - 1):
                this_el = this_el.next

            if next_el is not None:
                new_el.next = next_el
            else:
                new_el.next = self.head
            this_el.next = new_el

            return 1

        print("Lista jest pełna")
        return 0

    def remove(self, index):
        this_el = self.head

        if index == 0 and self.head is not None:
            self.head = this_el.next
            self.size -= 1

            for i in range(0, self.size - 1):
                this_el = this_el.next
            this_el.next = self.head

            return 1
        else:
            for i in range(0, index - 1):
                this_el = this_el.next

            if this_el.next is not None:
                this_el.next = this_el.next.next
                self.size -= 1
                return 1

    def get_list(self):
        res = [0] * self.max_size
        index = 0
        next_el = self.head
        head = None

        while next_el is not None and next_el != head:
            res[index] = next_el.el
            next_el = next_el.next
            index += 1
            head = self.head
        return res

    def get_el(self, index):
        this_el = self.head

        for i in range(0, index):
            this_el = this_el.next

            if this_el is None:
                print("błędny index")
                break

        return this_el


class Element:

    def __init__(self, el):
        self.el = el
        self.next = None

lista = Lista_c(5)

lista.push(0, Element(1))
lista.push(1, Element(2))
lista.push(1, Element(3))
lista.push(2, Element(4))
lista.push(3, Element(5))
print(lista.get_list())
lista.remove(0)
print("\n" ,lista.get_list())

lista.remove(0)
print("\n" ,lista.get_list())

