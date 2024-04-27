# [[1,2,3],[4,5,6],[7,8,9]]
# 0,0 | 0,1 1,0  | 0,2 1,1 2,0 | 2,1 1,2 | 2,2
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        nums_dict = defaultdict(list)

        for i, elem_list in enumerate(nums):
            for j, elem in enumerate(elem_list):
                nums_dict[i + j].append(elem)

        result = []
        for _, items in nums_dict.items():
            result.extend(reversed(items))

        return result
