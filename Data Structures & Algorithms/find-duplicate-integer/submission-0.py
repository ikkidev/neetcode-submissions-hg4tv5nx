class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Intuition:
        #usually will try to solve this with a hash map
        #to keep track of num frequency
        #but we're constrained to O(1) space

        #2nd intuition:
        #Sort array: O(nlogn) time
        #No extra space if we sort in place
        #Duplicate int will be next to each other

        #3rd intuition:
        #Need to do this in O(n) time and O(1) space
        #Can we use slow fast pointer algo to detect a duplicate ?

        has_cycle = False
        #Start at 0 because we're guaranteed that 0 is not part of the cycle
        slow , fast = nums[0], nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        has_cycle = True

        cycle = 0
        if has_cycle:
            while slow != cycle:
                slow = nums[slow]
                cycle = nums[cycle]

            return cycle
