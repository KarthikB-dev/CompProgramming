from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = []
        for cidx in range(len(words[0])):
            new_col = ""
            for ridx in range(len(words)):
                if cidx < len(words[ridx]):
                    new_col += words[ridx][cidx]
            cols.append(new_col)

        return cols == words