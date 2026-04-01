class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy_price = float('inf')
        for price in prices:
            buy_price = min(price, buy_price)
            ans = max(price-buy_price, ans)
        return ans
            
        