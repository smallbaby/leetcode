# -*- coding: utf-8 -*-
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return n
        res = 0
        for i in range(1, 33):
            res = res << 1
            if n & 1 == 1:
                res = res + 1
            n = n >> 1
        return res
