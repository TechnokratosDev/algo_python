class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        bigint = ["Thousand", "Million", "Billion"]
        result = self.get_small_int(num % 1000)
        num //= 1000

        for i in range(len(bigint)):
            if num > 0 and num % 1000 > 0:
                result = self.get_small_int(num % 1000) + bigint[i] + " " + result
            num //= 1000

        return result.strip()

    def get_small_int(self, num):
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        ten_digits = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                      "Nineteen"]
        ten_strings = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        result = ""
        if num > 99:
            result = digits[num // 100] + " Hundred "

        num %= 100
        if num > 9 and num < 20:
            result += ten_digits[num - 10] + " "
        else:
            if num >= 20:
                result += ten_strings[num // 10] + " "
            num %= 10
            if num > 0:
                result += digits[num % 10] + " "

        return result
