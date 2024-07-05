class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 0
        r = 1000000000
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2

            length = 0
            bouquets = 0
            for i in bloomDay:
                if i <= mid:
                    length += 1

                    if length >= k:
                        bouquets += 1
                        length = 0
                else:
                    length = 0

            if bouquets >= m:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1

        return ans
