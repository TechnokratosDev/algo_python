class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        str_array = s.split()

        return len(str_array[-1])
