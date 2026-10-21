class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        minProfit = 0
        currentProfit = 0
        maxProfit = 0
        for i in range(len(prices)):
            currentProfit = prices[i] - minPrice
            if prices[i] < minPrice:
                minPrice = prices[i]
            if currentProfit > maxProfit: 
                maxProfit = currentProfit
        return maxProfit