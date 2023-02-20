# Project Euler: Problem 2 - Even Fibonacci numbers
# Difficulty rating 5%
from helperfuncs.helper_funcs import time_decorator


@time_decorator(1000)
def p0002(n1=1, n2=2, maxn=4000000):
    # I know the problem tells us to start with 1 and 2, so this part is
    # a bit... extra, but I wanted to write a generalized function.
    fibsum = 0
    # "not (n1 % 2)"" is ever so slightly faster than "n1 % 2 == 0"
    if not (n1 % 2):
        fibsum += n1
    while n2 < maxn:
        if not (n2 % 2):
            fibsum += n2
        ntemp = n2
        n2 += n1
        n1 = ntemp
    return fibsum


def main():
    ans = p0002()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.000529s
# Avg. exec. time: 0.000005s
# Fastest: 0.000004s
# Slowest: 0.000018s

# *** Answer ***
# 4613732
