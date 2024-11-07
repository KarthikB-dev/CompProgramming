from typing import List


class Solution:
    # curr_room is the current room than can be accessed
    # it would start with 0

    def explore_rooms(self, rooms, curr_room, visitable_map):
        curr_keys = rooms[curr_room]
        visitable_map[curr_room] = True
        for key in curr_keys:
            if visitable_map[key] == False:
                # One function call per key that's been given in the input
                self.explore_rooms(rooms, key, visitable_map)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Keys and Rooms

        # O(n) time complexity has to initialize a map of size n
        visitable_map = {}
        num_rooms = len(rooms)
        for room_idx in range(num_rooms):
            visitable_map[room_idx] = False

        self.explore_rooms(rooms, 0, visitable_map)

        # Iterate over a map of size n
        for room_idx in range(num_rooms):
            if not visitable_map[room_idx]:
                return False
        return True