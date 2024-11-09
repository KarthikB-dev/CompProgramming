class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # Length difference > 1 or same strings -> return False
        if abs(len(s) - len(t)) > 1 or s==t:
            return False

        # Replacement
        if len(s) == len(t):
            hamm_dist = 0
            for idx in range(len(s)):
                if s[idx] != t[idx]:
                    hamm_dist += 1
            return hamm_dist == 1

        # So do the following to check for insertion
        # Let b(ig) be the longer, l(ittle) be the shorter of the two strings
        # 1. Initialize some index to 0 (zero indexed)
        # 2. Iterate from left to right until l[idx] != b[idx]
        # 3. Check if b[idx + 1:] = l[idx:]. If they are equivalent,
        # then the edit distance is one

        b, l = "", ""
        if len(s) > len(t):
            b, l = s, t
        else:
            b, l = t, s

        for idx in range(len(l)):
            if l[idx] != b[idx]:
                return b[idx + 1:] == l[idx:]
        
        # First len(l) characters match, so by simply appending
        # the last character of s will work
        return True