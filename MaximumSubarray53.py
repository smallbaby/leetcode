class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr = res = nums[0]
        for i in nums[1:]:
            curr = max(i, curr + i)
            res = max(curr, res)
        return res