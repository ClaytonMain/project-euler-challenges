# Project Euler: Problem 4 - Largest palindrome product
# Difficulty rating: 5%
import helper_funcs as hfs

# See problem_0004_scratch.py for notes & thought processes!

TIME_FUNCTION = True


def p0004(digits=3):
    max_factor = 10**digits - 1
    min_factor = 10 ** (digits - 1)
    max_pali = 0
    for i in range(max_factor, min_factor, -1):
        if not (i % 10):
            continue
        for j in range(i, min_factor, -1):
            n = i * j
            if n < max_pali:
                if j == i:
                    return max_pali
                break
            if not (n % 10):
                continue
            str_n = str(n)
            if str_n == str_n[::-1]:
                max_pali = n
    return max_pali


def main():
    ans = p0004()
    print(f'\n*** Answer ***\n{ans}')

    if TIME_FUNCTION:
        hfs.time_function('p0004')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Answer ***
# 906609

# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.174974s
# Avg. exec. time: 0.001750s
