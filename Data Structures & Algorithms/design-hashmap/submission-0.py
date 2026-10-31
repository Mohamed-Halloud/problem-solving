class MyHashMap:

    def __init__(self):
        self.size = 100
        self.data = [[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = hash(key) % self.size
        data = self.data[index]

        for i, (k, v) in enumerate(data):
            if k == key:
                data[i] = (key, value)
                return

        data.append((key, value))

    def get(self, key: int) -> int:
        index = hash(key) % self.size
        data = self.data[index]

        for i, (k, v) in enumerate(data):
            if k == key:
                return v

        return -1
    def remove(self, key: int) -> None:
        index = hash(key) % self.size
        data = self.data[index]

        for i, (k, v) in enumerate(data):
            if k == key:
                data.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)