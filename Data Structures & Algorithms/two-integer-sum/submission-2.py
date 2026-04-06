class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0 , len(nums) - 1
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key = lambda x: x[0])

        while left < right:
            cur_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if cur_sum == target:
                if nums_with_index[left][1] < nums_with_index[right][1]: 
                    return [nums_with_index[left][1],nums_with_index[right][1]]
                else:
                    return [nums_with_index[right][1],nums_with_index[left][1]]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return None      
        