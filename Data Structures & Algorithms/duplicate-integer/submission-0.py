from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = defaultdict(int)
        for num in nums:
            numDict[num] += 1
            if numDict.get(num) > 1:
                return True

        return False
