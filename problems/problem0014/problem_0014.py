# Project Euler: Problem 14 - Longest Collatz sequence
# Difficulty rating: 5%
from helperfuncs.helper_funcs import time_decorator


# Obvious, but slow method. Takes about 22 seconds to run.
@time_decorator(1)
def p0014_slow(max_n: int = 1000000) -> int:
    max_seq_len = 0
    max_seq_gen_by = 0
    for n in range(2, max_n):
        copy_n = n
        seq_len = 0
        while n > 1:
            if not (n % 2):
                n /= 2
            else:
                n = 3 * n + 1
            seq_len += 1
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_gen_by = copy_n
    return max_seq_gen_by


# About 10 times faster than the above method, but still feels rather slow.
# I'll take it, though.
@time_decorator()
def p0014(max_n: int = 1000000) -> int:
    seq_lens = {1: 1}
    max_seq_len = 1
    max_seq_gen_by = 1

    def get_seq_len(n: int) -> int:
        if n in seq_lens:
            return seq_lens[n]
        if not n % 2:
            new_n = n // 2
        else:
            new_n = 3 * n + 1
        seq_lens[n] = get_seq_len(new_n) + 1
        return seq_lens[n]

    for n in range(2, max_n):
        seq_len = get_seq_len(n)
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_gen_by = n

    return max_seq_gen_by


def main():
    ans = p0014()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 286.563920s
# Avg. exec. time: 2.865639s
# Fastest: 2.755189s
# Slowest: 3.868556s

# *** Answer ***
# 837799
