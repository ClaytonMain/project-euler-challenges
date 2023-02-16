# Project Euler: Problem 2 - Even Fibonacci numbers
import helper_funcs as hfs


TIME_FUNCTION = True


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
    print(f'\n*** Answer ***\n> {ans}')

    if TIME_FUNCTION:
        hfs.time_function('p0002')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Answer ***
# 4613732

# *** Time Stuff ***
# Executions: 10000
# Total exec. time: 0.049899s
# Avg. exec. time: 0.000005s
