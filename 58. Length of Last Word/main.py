class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_len = 0
        curr_len = 0

        for letter in s:
            if letter == " ":
                if curr_len != 0:
                    last_len = curr_len
                curr_len = 0
            else:
                curr_len += 1
        if curr_len != 0:
            last_len = curr_len

        return last_len
