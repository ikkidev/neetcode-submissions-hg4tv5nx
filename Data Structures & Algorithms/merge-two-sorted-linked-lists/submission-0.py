# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Declare dummyNode so we don't have to handle edge case of inserting into an empty list
        dummyNode = cur = ListNode()

        #Merge two list, check val, smaller one goes first
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                cur.next = list2
                list2 = list2.next
            #Don't forget to move current after inserting nodes from list1 or list2
            cur = cur.next    

        #Now we handle case where one list is bigger than the other
        #Simply take the leftover and put it at the end of cur
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        #Head of merged list is dummyNode.next since the first node is a dummy node
        return dummyNode.next

        
         
        