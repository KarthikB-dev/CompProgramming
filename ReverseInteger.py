class Solution:
    def in_bounds(self, digits, is_neg):
        out_of_bounds = False
        upper_bound = "2147483647"
        lower_bound = "2147483648"

        if len(digits) > len(upper_bound):
            out_of_bounds = True
        elif len(digits) == len(upper_bound):
            for idx, digit in enumerate(digits):
                if is_neg:
                    if digit < lower_bound[idx]:
                        break
                    elif digit > lower_bound[idx]:
                        out_of_bounds = True
                        break

                else:
                    if digit < upper_bound[idx]:
                        break
                    elif digit > upper_bound[idx]:
                        out_of_bounds = True
                        break
        return out_of_bounds

    def reverse(self, x: int) -> int:
        digits = ""
        is_neg = False

        if x < 0:
            x *= -1
            is_neg = True
        elif x == 0:
            return 0

        while x > 0:
            last_digit = x % 10
            x = x // 10
            digits = digits + str(last_digit)

        out_of_bounds = self.in_bounds(digits, is_neg)

        if not out_of_bounds:
            int_ver = int(digits)

            if is_neg:
                int_ver *= -1

            return int_ver
        else:
            return 0
