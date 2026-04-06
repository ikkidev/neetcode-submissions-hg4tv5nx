class HashTable:

    TOMBSTONE = object()  # unique marker for deleted entries
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = [None] * capacity

    def getIndex(self, key: int) -> int:
        index = key % self.capacity
        first_tombstone = None

        while self.hashmap[index] is not None:
            if self.hashmap[index] is self.TOMBSTONE:
                if first_tombstone is None:
                    first_tombstone = index
            else:
                existing_key, _ = self.hashmap[index]
                if existing_key == key:
                    return index
            index = (index + 1) % self.capacity

        return first_tombstone if first_tombstone is not None else index

    def insert(self, key: int, value: int) -> None:
        # Check if key exists (replace value)
        index = self.getIndex(key)
        if self.hashmap[index] is not None and self.hashmap[index] is not self.TOMBSTONE:
            self.hashmap[index] = (key, value)
            return

        
        index = self.getIndex(key)
        self.hashmap[index] = (key, value)
        self.size += 1

        # Resize if map reaches load factor ≥ 0.5
        if (self.size ) / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity

        while self.hashmap[index] is not None:
            if self.hashmap[index] is not self.TOMBSTONE:
                k, v = self.hashmap[index]
                if k == key:
                    return v
            index = (index + 1) % self.capacity

        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity

        while self.hashmap[index] is not None:
            if self.hashmap[index] is not self.TOMBSTONE:
                k, _ = self.hashmap[index]
                if k == key:
                    self.hashmap[index] = self.TOMBSTONE
                    self.size -= 1
                    return True
            index = (index + 1) % self.capacity

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        old_map = self.hashmap
        self.capacity *= 2
        self.hashmap = [None] * self.capacity

        for item in old_map:
            if item is not None and item is not self.TOMBSTONE:
                key, value = item
                index = key % self.capacity
                while self.hashmap[index] is not None:
                    index = (index + 1) % self.capacity
                self.hashmap[index] = (key, value)