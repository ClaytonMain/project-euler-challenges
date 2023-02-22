# Project Euler: Problem 6 - Sum square difference
# Difficulty rating: 5%
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0006(n=100):
    # I feel like list comprehensions are going to trivialize this.
    return sum(range(n + 1)) ** 2 - sum([x * x for x in range(n + 1)])
    # Yes, they are.


def main():
    ans = p0006()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.000829s
# Avg. exec. time: 0.000008s
# Fastest: 0.000007s
# Slowest: 0.000026s

# *** Answer ***
# 25164150
