# Project Euler: Problem 12 - Highly divisible triangular number
# Difficulty rating: 5%
from math import sqrt, log
from helperfuncs.helper_funcs import time_decorator


# The obvious (and *extremely* slow) solution. Takes over half an hour to
# complete.
@time_decorator(1)
def p0012_bad_solution(n_div: int = 500) -> int:
    tn = 0
    i = 0
    while True:
        i += 1
        tn += i
        count = 0
        for j in range(1, tn):
            if not (tn % j):
                count += 1
            # Since we're dealing with "highly-divisible" numbers, going to
            # skip numbers that aren't divisible by at least 5 numbers less
            # than 10. Does this generalize appropriately? Probably not.
            if (j == 10) & (count < 8):
                break
        if count > n_div:
            return tn


# This solution is significantly faster, though I'm sure it has room for
# improvement.
@time_decorator()
def p0012(n_div: int = 500) -> int:
    # Start by finding approximately the first n_div primes.
    # Probably shouldn't need more than that since we're dealing with
    # highly-divisible numbers.
    ub = int(n_div * log(n_div))
    sieve = list(range(ub))
    sieve[0:2] = [False, False]
    for i in range(int(sqrt(ub)) + 1):
        if sieve[i]:
            for j in range(i * i, ub, i):
                sieve[j] = False
    primes = [i for i in sieve if i]

    # Now, start looping through triangular numbers.
    tn = 0
    # Just choosing a really high number as the upper bound in our range.
    for i in range(1, n_div**5):
        tn += i
        # tn_copy is so we can keep dividing tn by prime numbers without
        # altering the current tn.
        tn_copy = tn
        n_factors = 1
        for p in primes:
            mult_by = 0
            if p >= tn:
                break
            while not (tn_copy % p):  # This is faster than tn % p == 0
                mult_by += 1
                tn_copy /= p
            n_factors *= mult_by + 1
        if n_factors > n_div:
            return tn


def main():
    ans = p0012()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 86.949034s
# Avg. exec. time: 0.869490s
# Fastest: 0.860600s
# Slowest: 0.899366s

# *** Answer ***
# 76576500
