class MyHashSet:

    def __init__(self):
        self.cap = 100

        self.data = [[] for i in range(self.cap)]

    def add(self, key: int) -> None:
        index = key % self.cap

        if key not in self.data[index]:
            self.data[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.cap

        if key in self.data[index]:
            self.data[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.cap

        return key in self.data[index]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)