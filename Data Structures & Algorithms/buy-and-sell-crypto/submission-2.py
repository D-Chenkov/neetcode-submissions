class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        lowest = math.inf
        for i in range(len(prices)):
            if (maxProf < prices[i]-lowest):
                maxProf = prices[i]-lowest
            if (prices[i] < lowest):
                lowest = prices[i]
    
        return maxProf