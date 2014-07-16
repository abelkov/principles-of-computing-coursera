"""
A simple testing suite for 2048
Note that tests are not exhaustive and should be supplemented
"""

import poc_simpletest
from game import *

def run_test(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test merge
    line1 = [2, 0, 2, 2]
    line2 = [0, 0, 0, 0]
    line3 = [0, 16, 2, 0]
    line4 = [4, 4, 4, 4]
    line5 = [2, 16, 0, 16]
    line6 = [0, 0, 2]
    line7 = [0, 2, 0]

    suite.run_test(merge(line1), [4, 2, 0, 0], "Test #1a: merge")
    suite.run_test(merge(line2), line2, "Test #1b: merge")
    suite.run_test(merge(line3), [16, 2, 0, 0], "Test #1c: merge")
    suite.run_test(merge(line4), [8, 8, 0, 0], "Test #1d: merge")
    suite.run_test(merge(line5), [2, 32, 0, 0], "Test #1e: merge")
    suite.run_test(merge(line6), [2, 0, 0], "Test #1f: merge")
    suite.run_test(merge(line7), [2, 0, 0], "Test #1g: merge")

    # create a game
    game = game_class(3, 4)

    suite.run_test(game.get_grid_height(), 3, "Test #2a: get_grid_height")
    suite.run_test(game.get_grid_width(), 4, "Test #3a: get_grid_width")

    suite.run_test(game.initial_tiles[UP], [(0,0), (0,1), (0,2), (0,3)], "Test #3a: initial_tiles (up)")
    suite.run_test(game.initial_tiles[DOWN], [(2,0), (2,1), (2,2), (2,3)], "Test #3b: initial_tiles (down)")
    suite.run_test(game.initial_tiles[LEFT], [(0,0), (1,0), (2,0)], "Test #3c: initial_tiles (left)")
    suite.run_test(game.initial_tiles[RIGHT], [(0,3), (1,3), (2,3)], "Test #3d: initial_tiles (right)")

    game.set_tile(0, 0, 2)
    game.set_tile(0, 2, 2)
    game.set_tile(0, 3, 4)
    game.reset()
    suite.run_test(game.grid, [[0,0,0,0]]*3, "Test #4a: reset")


    game.set_tile(0, 0, 2)
    game.set_tile(0, 2, 2)
    game.set_tile(0, 3, 4)
    suite.run_test(game.get_tile(0, 0), 2, "Test #5a: get_tile")
    suite.run_test(game.get_tile(0, 1), 0, "Test #5b: get_tile")
    suite.run_test(game.get_tile(0, 3), 4, "Test #5c: get_tile")


    game.move(LEFT)
    print game
    game.move(UP)
    print game
    game.move(RIGHT)
    print game
    game.move(DOWN)
    print game


    # game.reset()
    # for _ in range(3*4):
    #     game.new_tile()
    #     print game


    # report number of tests and failures
    suite.report_results()



if __name__ == '__main__':
    run_test(TwentyFortyEight)