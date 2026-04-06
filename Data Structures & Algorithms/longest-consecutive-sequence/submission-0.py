from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #1st intuition, sort nums and start building sequence only if current element is exactly 1
        #greater than the previous element (Time : O(nlogn) / Space O(n))

        # 2nd intuition,
        # First populate nums into a hash set so we can easily lookup existing num in nums O(1) lookup
        # Find the start of a sequence. A num is a start of a sequence only if (n-1) doesn't exist in the hash set
        # Once we find the start keep looking in the hash set for next num in sequence and add them to an array of sequences
        # So for eg -> [[1,2,3],[,6,7,8,9]]
        # get length of longest array in sequences and return it

        num_set = set()
        longest = 0

        #O(n)
        for num in nums:
            num_set.add(num)
        
        sequence_map = defaultdict(set)        

        #O(n)
        for num in num_set:
            if (num-1) not in num_set:
                length = 1 
                sequence_map[num].add(num)

                #O(k) O(1)*k lookup to find next sequence in num_set
                while (num+length in num_set):
                    sequence_map[num].add(num+length)
                    length+=1
                longest = max(length, longest)
        print (sequence_map)

        return longest




    

