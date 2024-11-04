from heapq import heapify, heappop, heappush
from typing import List
INF = 1e9

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Distances from k to a given node, dist(k, v) -> w, so dist[v] = w
        # Previous node used to achieve shortest path to v
        # q is the queue (min heap) used for selection of expansion points
        dist, prev, edges, edge_list, q, ver_set, dist_dict = [], {}, {}, {}, [], set(), {}

        for u_i, v_i, w_i in times:
            ver_set.add(u_i)
            ver_set.add(v_i)
            edges[(u_i, v_i)] = w_i
            if u_i in edge_list:
                edge_list[u_i].append(v_i)
            else:
                edge_list[u_i] = [v_i]
            
            if v_i not in edge_list:
                edge_list[v_i] = [] # Signifies no outgoing connections

        for ele in ver_set:
            if ele != k:
                dist.append((INF, ele))
                dist_dict[ele] = INF
            prev[ele] = -1 # Undefined

        if len(ver_set) < n: # Not all vertices provided
            return -1

        dist.append((0, k))
        dist_dict[k] = 0
        heapify(dist)

        while dist:
            top_val = dist.pop() 
            u = top_val[1]
            for v in edge_list[u]:
                alt = dist_dict[u] + edges[(u, v)] # Using this edge to get to v
                if alt < dist_dict[v]:
                    prev[v] = u 
                    dist_dict[v] = alt
                    heappush(dist, (alt, v))

        max_dist = -1 * INF # Minimum time is the maximum distance of any node
        for __, distance in dist_dict.items():
            if distance == INF:
                return -1
            elif distance > max_dist:
                max_dist = distance

        return max_dist