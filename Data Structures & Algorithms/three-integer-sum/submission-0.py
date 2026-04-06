class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Intuition: Brute force compare 3 pairs -> O(n^3)
        #2nd Intuition: Sort nums and run 2 pointer algorithm on a fixed index
        #Same logic: If sum is too small increase left pointer
        #If sum is too large decrease right pointer

        #Setup vars
        targetSum = 0

        #O(nlogn)
        numsSorted = sorted(nums)

        res = []
        size = len(nums)

        #O(n)
        # Only need to move i up to the 3rd last element, since we need 3 elements to make up the sum
        for i in range(size-2): 
            j = i + 1
            k = size - 1
            #Advance i if we see duplicates
            #Key insight here is any duplicates will be it's adjacent element since the list is sorted 
            if i>0 and numsSorted[i] == numsSorted[i-1]:
                continue

            #O(n)
            while j < k:
                currentSum = numsSorted[i] + numsSorted[j] + numsSorted[k]

                if currentSum == targetSum:
                    res.append([numsSorted[i], numsSorted[j], numsSorted[k]])

                    #These inner while loops are bound by n 
                    #since we are not resetting j or k to it's initial value

                    #keep advancing j if we see duplicates
                    while j<k and numsSorted[j] == numsSorted[j+1]:
                        j+=1
                    #Keep moving k down if we see duplicates
                    while j<k and numsSorted[k] == numsSorted[k-1]:
                        k-=1
                    #Need to move both since nums is sorted
                    #Keeping k fixed while only moving j means the sum will be larger than the target
                    #Keeping j fixed while only moving k means the sum will be smaller than the target
                    j+=1
                    k-=1

                elif currentSum < targetSum:
                    j+=1

                else:
                    k-=1

        return res

        