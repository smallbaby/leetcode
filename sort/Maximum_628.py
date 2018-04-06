# -*- coding: utf-8 -*-

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        m1 = nums[0] * nums[1] * nums[2]
        m2 = nums[0] * nums[-1] * nums[-2]
        return m1 if m1 > m2 else m2

    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort(reverse = True)
        # m1 = nums[0] * nums[1] * nums[2]
        # m2 = nums[0] * nums[-1] * nums[-2]
        # return m1 if m1 > m2 else m2
        m1 = m2 = m3 = -1000 * 1000
        s1 = s2 = 1000 * 1000
        for num in nums:
            if num > m1:
                m3 = m2
                m2 = m1
                m1 = num
            elif num > m2:
                m3 = m2
                m2 = num
            elif num > m3:
                m3 = num
            if num < s1:
                s2 = s1
                s1 = num
            elif num < s2:
                s2 = num
            mm1 = m1 * m2 * m3
            mm2 = m1 * s1 * s2
            return mm1 if mm1 > mm2 else mm2

s = Solution()
a = [1,4,3,-1,-2,-5]
print s.maximumProduct1(a)