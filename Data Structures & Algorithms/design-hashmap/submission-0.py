class MyHashMap:

    def __init__(self):
        # self.map = [-1, -1, -1, ....]
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # Set value at index [key]
        self.map[key] = value

    def get(self, key: int) -> int:
        # return value at index [key] if it's mapped
        # If map does not contain mapping at index [key], returns -1
        return self.map[key]

    def remove(self, key: int) -> None:
        # Remove by resetting value to -1
        self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)