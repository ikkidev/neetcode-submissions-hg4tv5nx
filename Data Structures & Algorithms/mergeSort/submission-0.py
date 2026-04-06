# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeHelper(self, start: int, end: int, pairs: List[Pair]) -> List[Pair]:

        # Base case, 1 element don't need to sort
        #0-0+1 = 1
        if end - start + 1 <= 1:
            return pairs

        # Get middle index
        # Also avoid overflow, not really a problem in python though
        #mid = (start + end) // 2
        mid = start + ( end - start) // 2
        # Sort left half
        self.mergeHelper(start, mid, pairs)
        # Sort right half
        self.mergeHelper(mid+1, end, pairs)

        # Merge sorted half    
        self.merge(start, mid, end, pairs)

        return pairs

    def merge(self, start: int, mid: int, end: int, pairs: List[Pair]) -> None:
        leftArray = pairs[start:mid+1]
        rightArray = pairs[mid+1:end+1]

        left = 0 # index for left array
        right = 0 # index for right array
        ori = start # index for original array to be sorted

        while left < len(leftArray) and right < len(rightArray):
            if leftArray[left].key <= rightArray[right].key:
                pairs[ori] = leftArray[left]
                left += 1
            else:
                pairs[ori] = rightArray[right]
                right += 1
            ori += 1

        while left < len(leftArray):
            pairs[ori] = leftArray[left]
            left += 1
            ori += 1

        while right < len(rightArray):
            pairs[ori] = rightArray[right]
            right += 1
            ori += 1


    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        start = 0
        end = len (pairs) - 1

        return self.mergeHelper(start, end, pairs)


