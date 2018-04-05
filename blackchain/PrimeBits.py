# -*- coding: utf-8 -*-
# __author__ = 'kai.zhang01'
# create date = 2018/03/27
from ChrToOrd import *
import math
class Solution(object):

    @staticmethod
    def prime(code):
        if code == 1 or code  == 2:
            return True
        for i in range(2,int(math.sqrt(code))+1):
            if code%i == 0:
                return False
        return True
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # 6 10
        # 6 --> 0110
        # 7 --> 0111
        # 8 --> 1000
        # 9 --> 1001
        # 10 -->1010

        cnt = 0
        for i in range(L, R):
            n = i
            bits = 0
            while i > 0:
                bits += i & 1
                i >>= 1
            if Solution.prime(bits):
                cnt += 1
        return cnt

s = Solution()
print s.countPrimeSetBits(567, 607)