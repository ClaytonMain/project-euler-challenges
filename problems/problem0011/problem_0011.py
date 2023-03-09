# Project Euler: Problem 11 - Largest product in a grid
# Difficulty rating: 5%
import os
from helperfuncs.helper_funcs import time_decorator


@time_decorator()
def p0011(n: str, prod_len: int = 4) -> int:
    vals = [[int(y) for y in x.split()] for x in n.split('\n')]
    max_prod = 0
    valslen = len(vals)
    diagstop = valslen - prod_len + 1
    for i in range(valslen):
        for j in range(len(vals[i]) - prod_len + 1):
            horiz = 1
            vert = 1
            diag1 = 1
            diag2 = 1
            for x in range(prod_len):
                iplusx = i + x
                jplusx = j + x
                iplusplminusx = i + prod_len - x - 1
                horiz *= vals[i][jplusx]
                vert *= vals[jplusx][i]
                if i < diagstop:
                    diag1 *= vals[iplusplminusx][jplusx]
                    diag2 *= vals[iplusx][jplusx]
            max_prod = max([max_prod, horiz, vert, diag1, diag2])
    return max_prod


def main():
    basepath = os.path.dirname(os.path.realpath(__file__))
    with open(f'{basepath}/the_number.txt', 'r') as f:
        n = f.read().replace('\n\n', '\n')
    ans = p0011(n)
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.079616s
# Avg. exec. time: 0.000796s
# Fastest: 0.000764s
# Slowest: 0.000974s

# *** Answer ***
# 70600674
