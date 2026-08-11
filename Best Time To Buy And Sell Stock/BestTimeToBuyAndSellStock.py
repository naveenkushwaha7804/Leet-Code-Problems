class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_ = 0
        for price in prices:
            min_ = min(price,min_)
            max_ = max(max_ , price-min_)
        return max_
        