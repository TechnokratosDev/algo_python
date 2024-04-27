from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for item in nums:
            ind = abs(item)

            if nums[ind] < 0:
                return ind
            nums[ind] *= -1
