import random
import time


class NQueen:
    def __init__(self, size=4):
        self.set_size(size)

    # set a board size of n by n
    def set_size(self, size):
        self.n = size
        self.grid = [[0 for i in range(size)] for i in range(size)]

    # randomly select initial queen placement and solve acordingly
    def solve(self):
        ret_val = 0
        visited = []
        while len(visited) < self.n and not ret_val:
            r_no = random.choice([i for i in range(0, self.n)
                                  if i not in visited])
            visited.append(r_no)
            self.grid[r_no][0] = 1
            self.show_frame()
            ret_val = self.path_finder(r_no, 0)
            if not ret_val:
                self.grid[r_no][0] = 0
                self.show_frame()
        return self.grid

    # recursively find next placement for queen and backtrack if no solution exists
    def path_finder(self, row, col):
        if col + 1 >= self.n:
            return 1
        for t_row in range(0, self.n):
            if not self.check_adjecent(t_row, col+1):
                self.grid[t_row][col+1] = 1
                self.show_frame()
                if self.path_finder(t_row, col+1):
                    return 1
                self.grid[t_row][col+1] = 0
                self.show_frame()

    # check diagonal/row/column if queen is present there or not
    def check_adjecent(self, row, col):
        dist = 1
        for t_col in range(col-1, -1, -1):
            if self.grid[row][t_col] == 1:
                return 1
            if (row - dist) >= 0:
                if self.grid[row - dist][t_col] == 1:
                    return 1
            if (row + dist) < self.n:
                if self.grid[row + dist][t_col] == 1:
                    return 1
            dist += 1
        return 0

    # show each step taken frame by frame to find solution
    def show_frame(self):
        for row in self.grid:
            print(row)
        print('---' * len(self.grid))
        time.sleep(0.0)
        # input()


if __name__ == "__main__":

    size = 8
    nqueen = NQueen(size)
    board = nqueen.solve()

    for row in board:
        print(row)
