from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            new_f0 = max(f0, f2 - prices[i])
            new_f1 = f0 + prices[i]
            new_f2 = max(f1, f2)
            f0, f1, f2 = new_f0, new_f1, new_f2
        return max(f1, f2)
