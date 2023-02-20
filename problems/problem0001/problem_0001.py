# Project Euler: Problem 1 - Multiples of 3 or 5
# Difficulty rating 5%
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0001(n1=3, n2=5, maxn=1000):
    # Basic principle of inclusion and exclusion.
    mult_sum = sum(range(n1, maxn, n1))
    mult_sum += sum(range(n2, maxn, n2))
    mult_sum -= sum(range(n1 * n2, maxn, n1 * n2))
    return mult_sum


def main():
    ans = p0001()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS):
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.000745s
# Avg. exec. time: 0.000007s
# Fastest: 0.000006s
# Slowest: 0.000018s

# *** Answer ***
# 233168
