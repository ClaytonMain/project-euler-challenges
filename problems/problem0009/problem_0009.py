# Project Euler: Problem 9 - Special Pythagorean triplet
# Difficulty rating: 5%
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0009(n=1000):
    # Start with n/3 + 2 since a < b < c.
    for c in range(n // 3 + 2, n):
        # The start & end values for this range again ensure a < b < c.
        for b in range((n - c) // 2 + 1, c):
            a = n - c - b
            # a * a is faster than a ** 2.
            if a * a + b * b == c * c:
                return a * b * c


def main():
    ans = p0009()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.103278s
# Avg. exec. time: 0.001033s
# Fastest: 0.001001s
# Slowest: 0.001197s

# *** Answer ***
# 31875000
