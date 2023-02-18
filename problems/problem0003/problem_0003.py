# Project Euler: Problem 3 - Largest prime factor
import helper_funcs as hfs
import math

# See problem_0003_scratch.py for notes on this solution and other
# attempted solutions.

TIME_FUNCTION = True


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

    if TIME_FUNCTION:
        hfs.time_function('p0003', 100)


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Answer ***
# 6857

# *** Time Stuff ***
# Executions: 100
# Total exec. time: 4.908501s
# Avg. exec. time: 0.049085s
