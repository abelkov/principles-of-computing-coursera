from __future__ import print_function
import random

"""
Clone of 2048 game.
"""

#mport poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """

    result = [0] * len(line)
    cur = 0

    for num in line:
        if num == 0:
            continue

        if result[cur] == num:
            result[cur] *= 2
            cur += 1
        else:
            if result[cur] != 0:
                cur += 1
            result[cur] = num

    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width

        up_tiles = []
        down_tiles = []
        left_tiles = []
        right_tiles = []

        for col in range(grid_width):
            up_tiles.append( (0, col) )
            down_tiles.append( (grid_height-1, col) )

        for row in range(grid_height):
            left_tiles.append( (row, 0) )
            right_tiles.append( (row, grid_width-1) )

        self.initial_tiles = {
            UP: up_tiles,
            DOWN: down_tiles,
            LEFT: left_tiles,
            RIGHT: right_tiles
        }

        self.reset()


    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = []
        for dummy_row in range(self.grid_height):
          self.grid.append([0]*self.grid_width)



    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        res = ""

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                res  += "%4d" % self.grid[row][col]
            res += "\n"

        return res


    def get_grid_height(self):
        """
        Get the height of the board.
        """

        return self.grid_height


    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self.grid_width


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        initials = self.initial_tiles[direction]
        offset = OFFSETS[direction]
        grid_changed = False

        for tile in initials:

            (row, col) = tile
            line = []

            # 1: retrieve tiles to merge
            while (0 <= row < self.grid_height) and \
                  (0 <= col < self.grid_width):
                line.append(self.grid[row][col])
                row += offset[0]
                col += offset[1]

            # 2: merge them
            merged = merge(line)
            if merged != line:
                grid_changed = True

            # 3: update the grid
            (row, col) = tile
            for num in merged:
                self.grid[row][col] = num
                row += offset[0]
                col += offset[1]

        if grid_changed:
            self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        empties = []

        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 0:
                    empties.append( (row, col) )

        if not empties:
            return

        (row, col) = random.choice(empties)

        # 10% chance it's a 4, 90% chance it's a 2
        self.grid[row][col] = random.choice([4, 2, 2, 2,
                                                2, 2, 2,
                                                2, 2, 2])


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """

        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """

        return self.grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

