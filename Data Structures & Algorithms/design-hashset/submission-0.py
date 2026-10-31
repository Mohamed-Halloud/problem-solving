class MyHashSet:

    def __init__(self):
        self.capacity = 100
        self.data = [[] for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        index = key % self.capacity
        if key not in self.data[index]:
            self.data[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.capacity
        if key in self.data[index]:
            self.data[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.capacity
        return key in self.data[index]