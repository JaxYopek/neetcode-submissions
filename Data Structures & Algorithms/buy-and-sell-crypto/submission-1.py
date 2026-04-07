class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")  # Track the lowest price
        max_profit = 0  # Track the maximum profit
        
        for price in prices:  # Iterate over prices
            buy = min(buy, price)  # Always find the lowest price
            max_profit = max(max_profit, price - buy)  # Update profit if selling at current price
            
        return max_profit