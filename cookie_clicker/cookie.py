"""
Cookie Clicker Simulator
"""

#import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._time = 0.0
        self._cps = 1.0
        self._history = [(self._time, None, 0.0, self._total_cookies)]

    def __str__(self):
        """
        Return human readable state
        """
        state = "Total cookies: " + str(self._total_cookies) \
            + "\nCurrent cookies: " + str(self._current_cookies) \
            + "\nTime: " + str(self._time) \
            + "\nCps: " + str(self._cps)

        return state

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0

        difference = (cookies - self._current_cookies)
        seconds = difference / self._cps
        return math.ceil(seconds)

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """
        if time <= 0:
            return

        self._time += time
        self._current_cookies += time * self._cps
        self._total_cookies += time * self._cps

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_cookies:
            return

        self._current_cookies -= cost
        self._cps += additional_cps
        self._history.append( (self._time, item_name, cost, self._total_cookies) )


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """

    build = build_info.clone()
    clicker = ClickerState()

    while clicker.get_time() <= duration:
        time_left = duration - clicker.get_time()
        next_item = strategy(clicker.get_cookies(), clicker.get_cps(), time_left, build)

        if next_item == None:
            break

        cost = build.get_cost(next_item)
        time_needed = clicker.time_until(cost)

        if time_needed > time_left:
            break

        clicker.wait(time_needed)
        clicker.buy_item(next_item, cost, build.get_cps(next_item))
        build.update_item(next_item)

    time_left = duration - clicker.get_time()
    if time_left > 0:
        clicker.wait(time_left)

    return clicker


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
    return "Cursor"


def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None


def _strategy(compare, cookies, cps, time_left, build_info):
    """
    A higher-order function that abstracts strategy_cheap and strategy_expensive functions.
    """

    def criterion(shop):
        """
        Choose item based on compare function.
        """
        choice = shop[0]

        for item, cost in shop[1:]:
            if compare(cost, choice[1]):
                choice = (item, cost)

        return choice

    shop = []
    could_spend = cookies + time_left * cps

    for item in build_info.build_items():
        if could_spend >= build_info.get_cost(item):
            shop.append( (item, roi) )

    if shop == []:
        return None

    choice = criterion(shop)
    return choice[0]

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Always return the cheapest item.
    """
    return _strategy(lambda new, old: new < old, cookies, cps, time_left, build_info)


def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Always return the most expensive item.
    """
    return _strategy(lambda new, old: new > old, cookies, cps, time_left, build_info)


def strategy_best(cookies, cps, time_left, build_info):
    """
    This strategy function does its best to maximize _total_cookies. The algorithm is obvious: for every item, compute its return on investment, and choose the one with the biggest roi.
    """
    shop = []
    could_spend = cookies + time_left * cps

    for item in build_info.build_items():
        if could_spend >= build_info.get_cost(item):
            roi = build_info.get_cps(item) / build_info.get_cost(item)
            shop.append( (item, roi) )

    if shop == []:
        return None

    shop.sort(key=lambda pair: pair[1], reverse=True)
    return shop[0][0]

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    #run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    #run_strategy("Best", SIM_TIME, strategy_best)

#run()


