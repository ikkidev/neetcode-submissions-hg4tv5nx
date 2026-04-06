class Node:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        
    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        self.tail.prev = new_node
        new_node.prev = last_node
        last_node.next = new_node
        new_node.next = self.tail
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.next = first_node
        first_node.prev = new_node
        new_node.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last_node = self.tail.prev
        prev_node = last_node.prev
        self.tail.prev = prev_node
        prev_node.next = self.tail
        return last_node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
            
        first_node = self.head.next
        next_node = first_node.next
        self.head.next = next_node
        next_node.prev = self.head
        return first_node.val
        


        
