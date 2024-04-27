from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for item in nums:
            num = abs(item)
            ind = num - 1

            if nums[ind] < 0:
                result.append(num)
            nums[ind] *= -1

        return result
