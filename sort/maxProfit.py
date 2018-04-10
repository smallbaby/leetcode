# -*- coding: utf-8 -*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        for i, j in enumerate(prices):
            if i == 0:
                left = prices[0]
                max = 0
                continue
            if j - left < 0:
                left = j
            else:
                max = j - left if j - left > max else max
        return max
