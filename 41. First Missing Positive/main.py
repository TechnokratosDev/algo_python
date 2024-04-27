from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n + 1:
                nums[i] = n + 1

        for item in nums:
            if abs(item) > n:
                continue

            ind = abs(item) - 1
            if nums[ind] > 0:
                nums[ind] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
