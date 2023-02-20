# Project Euler: Problem 3 - Largest prime factor
# Difficulty rating 5%
from helperfuncs.helper_funcs import time_decorator
import math

# See problem_0003_scratch.py for notes on this solution and other
# attempted solutions.


@time_decorator()
def p0003(n=600851475143):
    copy_n = n
    composites = set()
    maxp = math.ceil(math.sqrt(copy_n)) + 1
    for p in range(2, maxp):
        if p >= copy_n:
            break
        if p in composites:
            continue
        while (not (copy_n % p)) and (copy_n != p):
            copy_n /= p
        maxp = math.ceil(math.sqrt(copy_n)) + 1
        composites.update(range(p * p, maxp, p))
    return int(copy_n)


def main():
    ans = p0003()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 4.693884s
# Avg. exec. time: 0.046939s
# Fastest: 0.044662s
# Slowest: 0.067782s

# *** Answer ***
# 6857
