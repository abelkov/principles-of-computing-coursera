from __future__ import print_function
import poc_simpletest
from hw1 import *

# suite = poc_simpletest.TestSuite()

# suite.run_test(resources_vs_time(0.5, 5), [[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0]], "Test #1a: resources_vs_time")

p = resources_vs_time(1, 100)
for i in p:
  print(i, end="\n")