class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_x = str_x[::-1]
        return str_x == rev_x