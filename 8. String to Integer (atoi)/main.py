class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        res = 0
        length = len(s)

        while i < length and s[i] == " ":
            i += 1

        if i < length and s[i] == "-":
            sign *= -1
            i += 1
        elif i < length and s[i] == "+":
            i += 1

        while i < length and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res = res * sign
        if res < -2 ** 31:
            return -2 ** 31
        elif res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return res
