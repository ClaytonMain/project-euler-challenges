# Project Euler: Problem 13 - Large sum
# Difficulty rating: 5%
import os
from helperfuncs.helper_funcs import time_decorator


# Man, I'm sure this would be much more difficult in some other programming
# language. But hey! We're using Python!
@time_decorator()
def p0013(the_numbers: str, first_n_digits: int = 10) -> str:
    vals = [int(x) for x in the_numbers.split('\n')]
    return str(sum(vals))[:first_n_digits]


def main():
    basepath = os.path.dirname(os.path.realpath(__file__))
    with open(f'{basepath}/the_numbers.txt', 'r') as f:
        the_numbers = f.read().replace('\n\n', '\n')
    ans = p0013(the_numbers)
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.002383s
# Avg. exec. time: 0.000024s
# Fastest: 0.000022s
# Slowest: 0.000047s

# *** Answer ***
# 5537376230
