# Project Euler: Problem 7 - 10001st prime
# Difficulty rating: 5%
from helperfuncs.helper_funcs import time_decorator
from math import log, sqrt

# Hooray I get to make a sieve!


@time_decorator()
def p0007(n=10001):
    # pi(x) > x/log(x) according to:
    # https://en.wikipedia.org/wiki/Prime-counting_function
    # So we'll use this to find an upper bound for our sieve.
    ub = n * 2
    while n >= ub / log(ub):
        ub *= 2
    sieved = list(range(ub))
    sieved[0:2] = [0, 0]
    for i in range(int(sqrt(ub)) + 1):
        if sieved[i]:
            for j in range(i * i, ub, i):
                sieved[j] = 0
    return [p for p in sieved if p][n - 1]


def main():
    ans = p0007()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 2.400888s
# Avg. exec. time: 0.024009s
# Fastest: 0.023077s
# Slowest: 0.029690s

# *** Answer ***
# 104743
