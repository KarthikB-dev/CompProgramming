from typing import List


class Solution:
    def no_lzeros(self, int_1, int_2, int_3, int_4):
        nums_list = [int_1, int_2, int_3, int_4]
        for num in nums_list:
            if num[0] == '0' and len(num) > 1:
                return False
        return True
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4: # 1-3 digits x 4 groups = 4-12
            return []

        # (3)^4=81 possible partitions, as the length of each integer
        # is 1-3, and there are 4 integers
        # dictionary from idx (0-80) to either None or a valid IP
        # 1-1-1-1, 1-1-1-2, 1-1-1-3, 1-1-2-1, 1-1-2-2 ... is the ordering system

        ips = []
        for idx in range(81):
            # Lengths of each integer
            len_1 = idx // 27
            len_2 = (idx - len_1 * 27) // 9
            len_3 = (idx - len_1 * 27 - len_2 * 9) // 3
            len_4 = idx % 3

            len_1 += 1
            len_2 += 1
            len_3 += 1
            len_4 += 1

            # Constructing an IP address with those integer lengths

            # Check 1: Correct length
            if len_1 + len_2 + len_3 + len_4 == len(s):
                int_1 = s[0 : len_1]
                int_2 = s[len_1 : len_1+len_2]
                int_3 = s[len_1+len_2 : len_1+len_2+len_3]
                int_4 = s[len_1+len_2+len_3:]

                # Check 2: Leading Zeros
                if self.no_lzeros(int_1, int_2, int_3, int_4):
                    int_1 = int(int_1)
                    int_2 = int(int_2)
                    int_3 = int(int_3)
                    int_4 = int(int_4)

                    print([int_1, int_2, int_3, int_4])
                    # Check 3: Correct Range
                    if int_1 <= 255 and int_2 <= 255 and int_3 <= 255 and int_4 <= 255:
                        ips.append(str(int_1) + "." + str(int_2) + "." + str(int_3) + "." + str(int_4))

        return ips