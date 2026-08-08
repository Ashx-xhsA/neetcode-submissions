class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            p = prices[i]
            if p > min_price:
                res = max(res, -min_price+p)
            else:
                min_price = p
        return res
        