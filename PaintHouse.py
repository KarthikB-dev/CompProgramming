class Solution:
    def get_min(house_costs):
        return min(min(house_costs[0], house_costs[1]), house_costs[2])

    def minCost(self, costs: List[List[int]]) -> int:
        # Goal: minimizes the cost for the first i houses
        # minimum cost for house i is cost(red) + min(cost(red previous), cost(green previous))
        # cost(green) + min(cost(blue previous), cost(green previous))
        # cost(blue) + min(cost(red previous), cost(green previous))
        # order is red, blue, green

        min_red = {0: costs[0][0]}
        min_blue = {0: costs[0][1]}
        min_green = {0: costs[0][2]}

        length = len(costs)

        for i in range(1, length):
            min_red[i] = costs[i][0] + min(min_blue[i - 1], min_green[i - 1])
            min_blue[i] = costs[i][1] + min(min_red[i - 1], min_green[i - 1])
            min_green[i] = costs[i][2] + min(min_blue[i - 1], min_red[i - 1])

        return min(min(min_red[length - 1], min_blue[length - 1]), min_green[length - 1])