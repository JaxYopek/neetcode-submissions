class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        sell = -float("inf")
        for i in range(1,len(prices),1):

            sell = max(prices[i], sell)
            if buy > sell:
                buy = min(prices[i - 1], buy)
            print(buy, sell)

        return sell - buy