# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def pivotPicker(self, start: int, mid:int, end:int, pairs:List[Pair]) -> int:
        x = pairs[start].key
        y = pairs[mid].key
        z = pairs[end].key

        if (y <= x <= z) or (z <= x <= y):
            return start
        elif (x <= y <= z) or (z <= y <= x):
            return mid
        else:
            return end

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(0, len(pairs)-1, pairs)
        return pairs
    
    def quickSortHelper(self, start : int, end: int, pairs: List[Pair]) -> None:
        if end - start + 1 <= 1:
            return

        mid = start + (end - start) // 2

        #Pick pivot
        #pivotIndex = self.pivotPicker(start, mid, end, pairs)

        #Using end as pivot to satisfy question
        pivotIndex = end
        pivot = pairs[pivotIndex].key

        #Move pivot to the end to simplify partitioning
        pairs[pivotIndex], pairs[end] = pairs[end], pairs[pivotIndex]
        cur = start

        #Partition
        for i in range(start,end):
            
            if pairs[i].key < pivot:
                pairs[cur], pairs[i] = pairs[i], pairs[cur]
                cur += 1
                
        # Move pivot to its final place 
        pairs[cur], pairs[end] = pairs[end], pairs[cur] 

        #Sort left
        self.quickSortHelper(start, cur-1, pairs)

        #Sort right
        self.quickSortHelper(cur+1, end, pairs)
        