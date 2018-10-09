"""Run this script in terminal:

   1) By default arguments: python test_calculation.py
   2) With arguments: python test_calculation.py -num1 any_number -num2 any_number
"""
import argparse
import sys
from calculation import add, divine

from ats import aetest
from ats.aetest import test


class SmokeTest(aetest.Testcase):
    """Testing divine and add functions from calculation.py"""

    @test
    def test_divine_function(self, num1, num2):
        if num1 < 0 or num2 < 0:
            self.skipped("One of arguments < 0")

        try:
            divine(num1, num2)
        except ZeroDivisionError:
            self.passx('Division by zero', from_exception=ZeroDivisionError("Sorry, I can't do it!"))
        else:
            print('Result of divine function', divine(num1, num2))
            self.passed('passed!!!')

    @test
    def test_add_function(self, num1, num2):
        if num1 < 0 or num2 < 0:
            self.skipped("One of arguments < 0")
        else:
            print('Result of add function', add(num1, num2))
            self.passed("passed!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='standalone parser')
    parser.add_argument('-num1', dest='num1', type=int, required=False)
    parser.add_argument('-num2', dest='num2', type=int, required=False)

    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])
    first_num = 0 if args.num1 == 0 else 3
    second_num = args.num2 or 0
    aetest.main(num1=first_num, num2=second_num)

