class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Another two pointer problem.
        #Width is len of elements -1 i.e. 1, 0, 1 is width 2
        #Height is the minimum of the two elements.
        
        #First Naive where we check every possible option (n^2)
        #maxWater = 0
        #for i, height in enumerate(heights):
        #    for j, rheight in enumerate(heights[(i+1):], start= i+1):
        #        maxWater = max(((j-i)*min(height,rheight)), maxWater)
        #return maxWater

        #Now proper 2 pointers:
        maxWater = 0
        l = 0
        r = len(heights)-1
        while l<r:
            maxWater = max((r-l) * min(heights[l], heights[r]), maxWater)
            if (heights[l] < heights[r]):
                l+=1
            else:
                r-=1
        return maxWater
