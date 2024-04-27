from typing import List


class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        if not n:
            return []

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
                 "8": "tuv", "9": "wxyz"}
        res = []

        def recursion(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in phone[next_digits[0]]:
                recursion(combination + letter, next_digits[1:])

        recursion("", n)
        return res
