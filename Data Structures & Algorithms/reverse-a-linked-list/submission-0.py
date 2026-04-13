# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prevNode,curNode = None, head

        # Need to be careful with termination condition
        # First attempt I thought we had to do while curNode and curNode.next
        while curNode:
            #Need to save link to next node before we reverse the link
            tmp = curNode.next
            #Reverse current node link
            curNode.next = prevNode
            #Keep track of where we are for next iteration
            prevNode = curNode
            #Move on to the next node saved in tmp
            curNode = tmp

        return prevNode