# Project Euler: Problem 1 - Multiples of 3 or 5
import helper_funcs as hfs


TIME_FUNCTION = True


def p0001(n1=3, n2=5, maxn=1000):
    # Basic principle of inclusion and exclusion.
    mult_sum = sum(range(n1, maxn, n1))
    mult_sum += sum(range(n2, maxn, n2))
    mult_sum -= sum(range(n1 * n2, maxn, n1 * n2))
    return mult_sum


def main():
    ans = p0001()
    print(f'\n*** Answer ***\n> {ans}')

    if TIME_FUNCTION:
        hfs.time_function('p0001')


if __name__ == '__main__':
    main()

# Printed messages: (SPOILERS)
# *** Answer ***
# > 233168

# *** Time Stuff ***
# Executions: 10000
# Total exec. time: 0.071089s
# Avg. exec. time: 0.000007s
