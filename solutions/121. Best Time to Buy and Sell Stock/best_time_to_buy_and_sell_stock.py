from typing import List

# Kadane's Algorithm

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 # harus diubah jadi min int kalau input bisa negatif
        current_buy = prices[0]
        current_profit = 0
        for i in prices:
            current_profit = i - current_buy
            if current_profit > max_profit:
                max_profit = current_profit
            if current_profit < 0:
                current_buy = i
        return max_profit
        
"""
Runtime: 988 ms, faster than 76.13% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.2 MB, less than 11.89% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""