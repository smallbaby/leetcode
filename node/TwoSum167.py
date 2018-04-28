# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return numbers
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right = right - 1
            elif numbers[left] + numbers[right] < target:
                left = left + 1
            else:
                return [left + 1, right + 1]
