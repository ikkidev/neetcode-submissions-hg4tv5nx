class MinHeap:  
    #Heap is usually implemented with an array
    #priority queue
    #Left child index = 2i
    #Right child index = 2i + 1
    #Parent index = i //2
    #Heap has 2 critical contstraints
    # 1) Structure has to be a complete binary tree
    #    aka only the last level is allowed to have gaps
    # 2) Order every value has to be less than the root node

    def __init__(self):
        #Put dummy value at index 0 to simplify math for getting child and parent index
        self.heap = [0]

    def percolateUp(self, cur):
        #Keep swapping value at cur if it's value
        #is smaller than it's parents or until we reach beginning of queue i.e root node
        parent = cur // 2
        while self.heap[cur] < self.heap[parent] and cur > 1:
            self.heap[cur], self.heap[parent] = self.heap[parent], self.heap[cur]
            cur = parent
            parent = cur // 2

    def push(self, val: int) -> None:
        #Add val to end of queue and keep swapping value up until heap min order 
        #structure is satisfied
        self.heap.append(val)
        lastIndex = len(self.heap) - 1
        self.percolateUp(lastIndex)

    def percolateDown(self,cur):
        #Keep swapping value at cur down if it's value
        #is bigger than any one of it's child
        #Remember that heap is not a Binary Search Tree, so we can't rely on the property that the left
        #subtree is always < root and right subtree > root
        #We need to potentially visit every child if necessary
        #The only guarantee we have in a min heap is that each value a the next level will be greater than 
        #the value at the current level 

        #Keep checking as long as there is still a child
        while 2 * cur < len(self.heap):
            left = 2 * cur
            right = left + 1
            smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[cur] <= self.heap[smallest]:
                break

            self.heap[cur], self.heap[smallest] = self.heap[smallest], self.heap[cur]
            cur = smallest


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1 

        if len(self.heap) == 2:
            lastNode = self.heap.pop()
            return lastNode

        #Remove root node
        #Put node at the end of the queue to the root node position
        #Keep swapping node down until heap min order structure is satisfied
        minValue = self.heap[1]
        lastNode = self.heap.pop()
        self.heap[1] = lastNode
        self.percolateDown(1)
        return minValue
        

    def top(self) -> int:
        #Peek at min value without removing it from heap
        top = self.heap[1] if len(self.heap) > 1 else -1
        return top
        

    def heapify(self, nums: List[int]) -> None:
        """Transforms a list into a heap in-place."""
        self.heap = [0] + nums
        for i in reversed(range(1, len(self.heap) // 2 + 1)):
            self.percolateDown(i)
        
        