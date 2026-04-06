class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1st intuition
        # Sort input array (nlogn) in decreasing order
        # Problem here is the number of elements can technically be unbounded
        # But k most frequent elements will be the first k number of elements in the array
        # So we just keep iterating through the array until we find k distinct elements

        # 2nd intuition
        # Key a hash map on the kth frequency 
        # Highest number of frequency is the length of nums (n)
        # i.e the same element appears n number of times in nums
        # Every time we encounter an element k number of times
        # We add it to the list of values for that key
        # Need to build a frequency index list too 

        count_map = {}
        freq_list = []

        #List for us to bucket sort without completely sorting through all n elements
        for i in range(len(nums)+1):
            freq_list.append([])

        #Build dictionary to count number of times num appear in nums
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        #Puts corresponding num into the correct frequency bucket in freq_list
        for key, val in count_map.items():
            freq_list[val].append(key)

        # Now we just iterate through the largest possible kth frequency
        res = []

        for i in range(len(freq_list)-1, 0, -1):
            # Grab the list of num in the ith frequency bucket
            for num in freq_list[i]:
                res.append(num)
            
                if len(res) == k:
                    return res


        

