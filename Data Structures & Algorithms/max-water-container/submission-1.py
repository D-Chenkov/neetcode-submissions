class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Another two pointer problem.
        #Width is len of elements -1 i.e. 1, 0, 1 is width 2
        #Height is the minimum of the two elements.
        
        #First Naive where we check every possible option
        maxWater = 0
        for i, height in enumerate(heights):
            for j, rheight in enumerate(heights[(i+1):], start= i+1):
                maxWater = max(((j-i)*min(height,rheight)), maxWater)
        return maxWater