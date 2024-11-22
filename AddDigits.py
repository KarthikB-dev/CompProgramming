class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            sum = 0
            for ch in str(num):
                sum += int(ch)
            if len(str(sum)) == 1:
                return sum
            num = sum
        return num