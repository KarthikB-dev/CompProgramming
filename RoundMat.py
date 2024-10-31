class Solution:
    def nums_to_str(self, row, col):
        return str(row) + str(col)

    def new_pos(self, row, col, dir):
        if dir == 'e':
            return row, col + 1
        elif dir == 's':
            return row + 1, col
        elif dir == 'w':
            return row, col - 1
        elif dir == 'n':
            return row - 1, col 
        else:
            return None, None
        
    def new_dir(self, dir):
        if dir == 'e':
            return 's'
        elif dir == 's':
            return 'w'
        elif dir == 'w':
            return 'n'
        elif dir == 'n':
            return 'e'
        else:
            return None, None

    def valid_pos(self, new_row, new_col, num_rows, num_cols):
        if new_row < num_rows and new_row >= 0:
            if new_col < num_cols and new_col >= 0:
                return True
        return False

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: # type: ignore
        row = 0
        col = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        marked = {}
        spiral = []
        dir = 'e'
        while self.nums_to_str(row, col) not in marked and self.valid_pos(row, col, num_rows, num_cols):
            spiral.append(matrix[row][col])
            marked[self.nums_to_str(row, col)] = True
            # look at next position
            # if not out of bounds and not marked
            # move row, col to this location
            new_row, new_col = self.new_pos(row, col, dir)
            if self.valid_pos(new_row, new_col, num_rows, num_cols) and self.nums_to_str(new_row, new_col) not in marked:
                row, col = new_row, new_col
            # otherwise, change direction and move in that new direction
            else:
                dir = self.new_dir(dir)
                row, col = self.new_pos(row, col, dir)
        return spiral

        