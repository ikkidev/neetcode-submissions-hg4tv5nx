class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.element_counter = 0
        self.dyn_array = [0] * self.capacity

    def get(self, i: int) -> int:
        if self.capacity > 0 and i >= 0 and i < self.capacity:
            return self.dyn_array[i]


    def set(self, i: int, n: int) -> None:
        if self.capacity > 0 and i >= 0 and i < self.capacity:
            self.element_counter += 1
            self.dyn_array[i] = n 


    def pushback(self, n: int) -> None:
        if self.element_counter == self.capacity:
            self.resize()

        self.dyn_array[self.element_counter] = n
        self.element_counter +=1


    def popback(self) -> int:
        if self.element_counter > 0:
            return self.dyn_array[self.element_counter - 1]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(0, self.element_counter):
            new_array[i] = self.dyn_array[i]
        self.dyn_array = new_array
        

    def getSize(self) -> int:
        return self.element_counter
    
    def getCapacity(self) -> int:
        return self.capacity
