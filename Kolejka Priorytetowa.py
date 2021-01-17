class PQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxx = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxx]:
                maxx = i
        return self.items.pop(maxx)
