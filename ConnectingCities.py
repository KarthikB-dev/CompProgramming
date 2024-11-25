from typing import List
from sortedcontainers import SortedDict

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        cost = 0

        edge_dict = SortedDict({})
        
        # Algo: sort edge_dict by cost
        for u, v, w in connections:
            if w not in edge_dict:
                edge_dict[w] = [(u, v), (v, u)]
            else:
                edge_dict[w].append((u, v))
                edge_dict[w].append((v, u))

        # Add an edge that connects a node in the mst
        # to a node out of it

        vert_groups = {} 
        group_idx = 0

        for weight, edges in edge_dict.items():
            for u, v in edges:
                # If neither is in a vertex group, create a new vertex
                # group for the both of them, update the 
                # group indices and total cost
                u_grouped = u in vert_groups
                v_grouped = v in vert_groups

                if not u_grouped and not v_grouped:
                    vert_groups[u] = group_idx
                    vert_groups[v] = group_idx
                    cost += weight
                    group_idx += 1

                # If one is in a vertex group, add reuse the vertex group
                elif u_grouped and not v_grouped:
                    u_group = vert_groups[u]
                    vert_groups[v] = u_group
                    cost += weight

                elif v_grouped and not u_grouped:
                    v_group = vert_groups[v]
                    vert_groups[u] = v_group
                    cost += weight
                         
                # If they're both grouped, but in different
                # groups, join them by combining their groups
                elif v_grouped and u_grouped:
                    if vert_groups[u] != vert_groups[v]:
                        # Overwrite u's group idx
                        # with v's
                        u_prev_group = vert_groups[u]
                        for vert in vert_groups:
                            if vert_groups[vert] == u_prev_group: 
                                vert_groups[vert] = vert_groups[v]
                        # Increment cost
                        cost += weight

        # Check if every vertex is in vert groups
        num_grouped = len(vert_groups)
        if num_grouped < n:
            return -1
        # Check if every vertex has the *same* vert group
        first_group = vert_groups[1]
        for __, group_val in vert_groups.items():
            if group_val != first_group:
                return -1
        return cost