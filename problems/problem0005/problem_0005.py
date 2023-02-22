# Project Euler: Problem 5 - Smallest multiple
# Difficulty rating: 5%
from helperfuncs.helper_funcs import time_decorator

# This one is pretty fun. Let's start with some examples.
#
# Suppose we want to find a number divible by both 2 and 3. Then 2 and
# 3 need to be factors of that number (obvs). It's simple enough to
# prove directly that 6 is the smallest number divisible by both 2
# and 3, and 6 = 2 * 3.
#
# Now, suppose we want to find a number divisible by 2, 3, and 4. Again,
# 2, 3, and 4 must be factors of this number. So would 2 * 3 * 4 = 24 be
# the smallest number divisible by these three numbers? Nope! 24 would
# be too high. The smallest number divisible by 2, 3, and 4 is actually
# 12. But why? Well, 2 * 3 is already divisible by 2. If we multiply
# this number by 2 again, we get 2 * 3 * 2 = 3 * 4 = 12, since 4 is
# just 2 * 2.
#
# So, essentially, in order to find the smallest number divisible by
# a set of numbers, s1, we need to come up with a set of numbers, s2,
# from which the numbers in s1 can be generated. Any composites in s2
# need to be reduced to their prime factors, and primes should only
# appear in s2 more than once if more than one of the same prime
# is needed to generate one of the numbers in s1.
#
# Alright, let's get to it.


@time_decorator()
def p0005(n=20):
    pfactors = {}
    composites = set()
    for i in range(2, n + 1):
        if i not in composites:
            pfactors[i] = 1
            composites.update(range(i * i, n + 1, i))
        else:
            for p in [x for x in pfactors if x * x <= i]:
                divcount = 0
                while (i > 1) & (not i % p):
                    divcount += 1
                    i /= p
                if divcount:
                    pfactors[p] = max(divcount, pfactors[p])
    ans = 1
    for k, v in pfactors.items():
        ans *= k**v
    return ans


def main():
    ans = p0005()
    print(f'\n*** Answer ***\n{ans}')


if __name__ == '__main__':
    main()

# Output (SPOILERS)
# *** Time Stuff ***
# Executions: 100
# Total exec. time: 0.002697s
# Avg. exec. time: 0.000027s
# Fastest: 0.000025s
# Slowest: 0.000051s

# *** Answer ***
# 232792560
