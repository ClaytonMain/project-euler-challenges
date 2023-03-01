# Project Euler: Problem 10 - Summation of primes
# Difficulty rating: 5%
from math import ceil, sqrt
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0010(n=2000000):
    sieved = list(range(n))
    sieved[0:2] = [0, 0]
    for i in range(2, ceil(sqrt(n)) + 1):
        if sieved[i]:
            for j in range(i * i, n, i):
                sieved[j] = 0
    return sum(sieved)


def main():
    ans = p0010()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 36.051404s
# Avg. exec. time: 0.360514s
# Fastest: 0.338525s
# Slowest: 0.431340s

# *** Answer ***
# 142913828922
