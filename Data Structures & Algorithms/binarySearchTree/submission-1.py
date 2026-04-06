class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def insertHelper(self, cur, key, val):
            #if key == self.key overwrite value, we don't allow for duplicate keys
            if key == cur.key :
                cur.val = val
                return 
            #if key < self.key, traverse left subtree
            elif key < cur.key:
                if cur.left is None:
                    cur.left = Node(key, val)
                    return 
                else:
                    self.insertHelper(cur.left, key, val)
            #if key > self,key, traverse right subtree
            elif key > cur.key:
                if cur.right is None:
                    cur.right = Node(key, val)
                    return
                else:
                    self.insertHelper(cur.right, key, val)
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:

        #Empty tree, just insert new node as root
        if self.root is None:
            self.root = Node(key, val)
            return

        self.insertHelper(self.root, key, val)



    def get(self, key: int) -> int:
        #Empty tree, don't think we really need this additional check though
        if self.root is None:
            return -1
        
        cur = self.root

        while cur is not None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else: #found the key
                return cur.val

        return -1 #Didn't find key in tree

    def getMin(self) -> int:

        if self.root is None:
            return -1

        #Smallest key should be in left subtree, so we just traverse to the left most node
        cur = self.root

        while cur is not None and cur.left is not None:
            cur = cur.left

        return cur.val


    def getMax(self) -> int:

        if self.root is None:
            return -1
        
        #Biggest key should be in right subtree, so we just traverse to the right most node
        cur = self.root

        while cur is not None and cur.right is not None:
            cur = cur.right

        return cur.val

    def findMinNode(self, node) -> Node:
        
        if node is None:
            return None

        #Smallest key should be in left subtree, so we just traverse to the left most node
        cur = node

        while cur is not None and cur.left is not None:
            cur = cur.left

        return cur

    def removeHelper(self, node, key):
        # Find node to replace the node to be removed

        # leaf node (aka no child) -> just remove
        # one child -> replace node with child
        # 2 child -> replace with inorder successor
        # smallest node in right subtree

        #First try to find the key to be removed
        if node is None:
            return None
        if key < node.key:
            node.left = self.removeHelper(node.left, key)
        elif key > node.key:
            node.right = self.removeHelper(node.right, key)
        else: #Found the key
            #Leaf node
            if node.left is None and node.right is None:
                return None
            #1 child node
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            #2 child nodes
            #Get the smallest node in right subtree
            replaceNode = self.findMinNode(node.right)
            node.key = replaceNode.key
            node.val = replaceNode.val
            #Delete the smallest node that we just found from the right subtree
            node.right = self.removeHelper(node.right , replaceNode.key)
        
        return node


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)


    def getInorderKeys(self) -> List[int]:
        #Print keys inorder using a stack for iterative approach
        result = []
        stack = []
        cur = self.root

        while cur is not None or stack:
            #Go all the way left
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            
            #visit node
            cur = stack.pop()
            result.append(cur.key)

            #visit right subtree 
            cur = cur.right

        return result


