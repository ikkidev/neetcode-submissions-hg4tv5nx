class LinkedList:
    class Node:
        def __init__(self, val, next_node = None):
            self.next = next_node
            self.val = val

    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            #Out of bounds
            if cur is None:
                return -1
            else:
                cur = cur.next
        return -1 if cur is None else cur.val


    def insertHead(self, val: int) -> None:
        temp = self.Node(val, self.head)
        self.head = temp
        if self.tail is None:
            self.tail = temp

        print(self.head.val)

    def insertTail(self, val: int) -> None:
        new = self.Node(val)
        if self.tail is None:
            self.head = self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        print(self.tail.val)
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        
        cur = self.head
        prev = None
        
        for i in range(index):
            if cur is None:
                return False
            prev = cur
            cur = cur.next

        if cur is None:
            return False

        if prev is None:        # removing head
            self.head = cur.next
        else:
            prev.next = cur.next

        # FIX tail
        if cur == self.tail:
            self.tail = prev

        return True

    def getValues(self) -> List[int]:
        cur = self.head
        values = list()
        while cur is not None:
            values.append(cur.val)
            cur = cur.next
        return values
            
        
