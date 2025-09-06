from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        max_p=0
        for right in range(1, len(prices)):
            if(prices[left]>prices[right]):
                left=right
                continue
            max_p=max(max_p, prices[right]-prices[left])
        return max_p