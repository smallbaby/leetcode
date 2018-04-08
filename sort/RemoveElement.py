# -*- coding: utf-8 -*-
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        for i,j in enumerate(nums):
            if j != val:
                nums[res] = j
                res = res + 1
        return res