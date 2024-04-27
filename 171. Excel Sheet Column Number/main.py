class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = (ord(columnTitle[0]) - ord('A') + 1)
        # ord(char) - ord('A') + 1

        for i in range(1, len(columnTitle)):
            result *= 26
            result += (ord(columnTitle[i]) - ord('A') + 1)

        return int(result)
