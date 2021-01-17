class Node:
    """Klasa Węzeł"""

    def __init__(self, dane=None, next_node=None):
        self.dane = dane
        self.next_node  = next_node
    def __str__(self):
        return str(self.dane)

class Queue:
    """Klasa Kolejka FIFO"""

    def __init__(self):
        self.size = 0
        self._head = None
        self._tail = None

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, dane):
        t=self._tail
        self._tail = Node(dane)
        if self.isEmpty() :
            self._head = self._tail
        else:
            t.next_node = self._tail
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise ValueError("Kolejka FIFO jest pusta!")
        self._head = self._head.next_node
        self.size -= 1
        if self.isEmpty():
            self._tail=None

    def first(self):
        if self.isEmpty():
            raise ValueError("Kolejka FIFO jest pusta!")
        return self._head.dane
