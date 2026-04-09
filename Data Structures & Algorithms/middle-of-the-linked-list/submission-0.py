# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Tortoise hare algo
        # Intuition: fast pointer twice as fast as the slow pointer
        # slow pointer will be at the middle of the linked list when 
        # fast pointer reaches the end of the linkedlist
        #
        # In case of ties, if question asks to return the first middle node
        # Start fast pointer one node ahead
        # Otherwise, this algorith will return the second middle node

        while fast and fast.next:
            slow , fast = slow.next , fast.next.next

        return slow

        