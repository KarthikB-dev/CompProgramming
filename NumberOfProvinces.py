from typing import List


class Solution:
    def set_cc_ids(self, cc_dict, isConnected, curr_node, cc_id, n):
        cc_dict[curr_node] = cc_id
        for other_node in range(n):
            if other_node not in cc_dict and isConnected[curr_node][other_node]:
                self.set_cc_ids(cc_dict, isConnected, other_node, cc_id, n)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cc_id = 0

        # key = node #, value = cc_id
        cc_dict = {} 

        n = len(isConnected)

        self.isConnected = isConnected

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i not in cc_dict:
                    # set the connected component
                    # id of that group with cc_id
                    # increment cc_id
                    self.set_cc_ids(cc_dict, isConnected, i, cc_id, n)
                    cc_id += 1

        for i in range(n):
            if i not in cc_dict:
                cc_id += 1
        return cc_id