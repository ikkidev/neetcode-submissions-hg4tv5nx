# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Intuition:
        # Keep 3 pointers
        # 2 pointers fast and slow to detect a cycle
        # Last slow pointer to find the head of the cycle
        # if there is one

        has_cycle = False
        slow, fast = head, head
        #Cycle detection, fast will intersect slow if there is one
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break
        

        #Slow and cycle_head will intersect at the beginning of the cycle
        if has_cycle:
            cycle_head = head    
            while cycle_head != slow:
                slow = slow.next
                cycle_head = cycle_head.next

        return has_cycle