class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.element_counter = 0
        self.dyn_array = [0] * self.capacity

    def get(self, i: int) -> int:
        if 0 <= i < self.element_counter:
            return self.dyn_array[i]
        else:
            raise IndexError("Index out of bounds")

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.capacity:
            self.dyn_array[i] = n
        else:
            raise IndexError("Index out of bounds")


    def pushback(self, n: int) -> None:
        if self.element_counter == self.capacity:
            self.resize()
        self.dyn_array[self.element_counter] = n
        self.element_counter+=1


    def popback(self) -> int:
        if self.element_counter > 0:
            last_element_index = self.element_counter - 1
            print(f"The last index is {last_element_index}")
            pop = self.get(last_element_index)
            self.dyn_array[last_element_index] = 0
            self.element_counter -= 1
            return pop 

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
