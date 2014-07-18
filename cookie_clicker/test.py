import poc_simpletest
from cookie import ClickerState

suite = poc_simpletest.TestSuite()

clicker = ClickerState()

suite.run_test(clicker.get_cookies(), 0.0, "1a: get_cookies")
suite.run_test(clicker.get_cps(), 1.0, "2a: get_cps")
suite.run_test(clicker.get_time(), 0.0, "3a: get_time")
suite.run_test(clicker.get_history(), [(0.0, None, 0.0, 0.0)], "4a: get_history")

clicker.wait(-5)
suite.run_test(clicker.get_time(), 0.0, "3b: get_time")
clicker.wait(5.0)
suite.run_test(clicker.get_cookies(), 5.0, "1b: get_cookies")
suite.run_test(clicker.get_time(), 5.0, "3c: get_time")

suite.run_test(clicker.time_until(20), 15.0, "5a: time_until")
suite.run_test(clicker.time_until(19.5), 15.0, "5b: time_until")

clicker.buy_item("item1", 3.0, 1.5)
suite.run_test(clicker.get_cps(), 2.5, "2b: get_cps")
suite.run_test(clicker.get_cookies(), 2.0, "1c: get_cookies")
suite.run_test(clicker.get_history(), [(0.0, None, 0.0, 0.0), (5.0, "item1", 3.0, 5.0)], "4b: get_history")

clicker.wait(3.0)
suite.run_test(clicker.get_cookies(), 9.5, "1d: get_cookies")

suite.run_test(clicker, "Total cookies: 12.5\nCurrent cookies: 9.5\nTime: 8.0\nCps: 2.5", "6a: str")

suite.report_results()