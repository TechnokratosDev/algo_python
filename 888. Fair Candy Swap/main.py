# sum(A)-i+j = sum(B)+i-j
# sum(A) - sum(B) = 2i - 2j
# (sum(A) - sum(b))/2 = i - j
# i = (sum(A) - sum(b))/2 + j
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2

        setA = set(aliceSizes)
        for j in set(bobSizes):
            if diff+j in setA:
                return [diff+j, j]
