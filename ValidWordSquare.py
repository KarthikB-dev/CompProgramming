from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for cidx in range(len(words[0])):
            new_col = ""
            for ridx in range(len(words)):
                if cidx < len(words[ridx]):
                    new_col += words[ridx][cidx]
            if new_col != words[cidx]:
                return False

        return True