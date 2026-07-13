class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        max_profit = 0

        for l in range(len(prices)):
            if prices[l] < low:
                low = prices[l]

            else:
                max_profit = max(max_profit, prices[l] - low)

        return max_profit
                