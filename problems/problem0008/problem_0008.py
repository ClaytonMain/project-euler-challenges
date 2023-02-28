# Project Euler: Problem 8 - Largest product in a series
# Difficulty rating: 5%
import os
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0008(n: str, substr_len: int = 13) -> int:
    prods = []
    for i in range(len(n) - substr_len - 1):
        substr = n[i : i + substr_len]
        if '0' in substr:
            continue
        prod = 1
        for x in substr:
            prod *= int(x)
        prods.append(prod)
    return max(prods)


def main():
    basepath = os.path.dirname(os.path.realpath(__file__))
    with open(f'{basepath}/the_number.txt', 'r') as f:
        n = f.read().replace('\n', '')

    ans = p0008(n)
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.060197s
# Avg. exec. time: 0.000602s
# Fastest: 0.000573s
# Slowest: 0.000867s

# *** Answer ***
# 23514624000
