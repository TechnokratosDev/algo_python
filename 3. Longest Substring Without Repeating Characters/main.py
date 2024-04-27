class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0
        left = 0
        letters = set()

        for i in range(len(s)):
            while s[i] in letters:
                letters.discard(s[left])
                left += 1

            k = max(k, i - left + 1)
            letters.add(s[i])

        return k
