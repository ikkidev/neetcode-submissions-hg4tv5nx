class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        # Index represents length of container
        # Value represents heigth of container
        # Intuition: if height is fixed, max area
        # would be from the lenght of the container

        # 2 pointers to keep track of container length front 
        # decrease or increase pointer depending on who has 
        # smaller height

        front, back = 0, len(heights)-1

        while back > front:
            length = back - front
            height = 1
            if heights[back] < heights[front]: 
                height = heights[back]
                back -= 1

            elif heights[front] <= heights[back]: 
                height = heights[front]
                front += 1  
            area = length * height
            if area > maxArea:
                maxArea = area

        return maxArea
        