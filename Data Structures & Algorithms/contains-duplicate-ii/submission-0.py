class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Intuition 1: Brute force
        #Go through every index pair and check if they are equal
        #and their distance is <= k 
        #O(n2)
        
        #Intuition 2: Fixed sliding window ( window size is k basically)
        #Keep moving window through nums
        #check window fits criteria
        #If it doesn't slide window right until length-k

        L=0
        window = set()

        for R in range(len(nums)):
            if abs(L-R) > k :
                window.remove(nums[L])
                L+=1
            
            if nums[R] in window:
                return True

            window.add(nums[R])


        #Didn't find any that fits criteria
        return False





        