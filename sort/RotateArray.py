class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.nums = nums
        self.reverse(0, len(nums) - 1)
        self.reverse(0, k - 1)
        self.reverse(k, len(nums) - 1)

    def reverse(self,start, end):
        while start < end:
            self.nums[start], self.nums[end] = self.nums[end], self.nums[start]
            start  += 1
            end -= 1
