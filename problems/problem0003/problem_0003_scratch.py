from helperfuncs.helper_funcs import time_decorator
import math


# Preface: I don't intend to include detailed explanations or a log of
# solutions in all my problem folders, just ones I found more intriguing
# than others, or ones for which I took multiple approaches, or when I just
# feel like it.
#
# Anywho, preface is over now.
#
# So, finding all the primes less than 600851475143 (which I'll call
# "the prompt number/value/"), looping through those primes, attempting
# to divide the prompt number by said primes, then returning the
# largest one that was able to divide the prompt number would be really
# slow. And could also use a lot of memory if we were storing our primes in
# a list. So that route is right out.
#
# Instead, the approach I'm taking is:
#   1.  Get our smallest known prime (p) that we haven't used yet
#       (so, 2, initially).
#   2.  Let's call the original prompt number "n". Make a copy of n (copy_n).
#   3.  Try to divide copy_n by p. If p divides copy_n, overwrite copy_n
#       with copy_n/p, then go back to 2.
#   4.  After dividing copy_n by p as much as possible, set p to the next
#       largest prime greater than p.
#   5.  If p is now equal to copy_n, then we know there are no larger primes
#       to check, and copy_n is the largest prime that will divide n,
#       so return copy_n. Otherwise go back to 2.
#
#   This works because of dark sorcery. Or it works because when we divide
#   a number by its prime factors, starting with the smallest prime factor
#   and working our way up, then eventually we're just left with the largest
#   prime factor. This is pretty neat 'cause you can potentially *massively*
#   reduce the number of primes you need to check. So anywho, with this
#   approach in mind, here are the functions I wrote.


# Solution 1
@time_decorator()
def p0003_solution01(n=600851475143):
    '''
    I actually forgot to save my first solution, so I've defined this function
    in its memory. R.I.P. in peace, Problem 3 Solution 1. Nobody will miss
    or even remember you.
    '''


# Solution 2
@time_decorator()
def p0003_solution02(n=600851475143):
    # Alrighty, we're making a copy of n (though we could probably just use
    # n, honestly), and initializing an empty list to toss our primes into.
    copy_n = n
    primes = []
    # Also, we want a cap on the largest value our prime can be, so here.
    maxp = math.ceil(math.sqrt(copy_n)) + 1
    # Startin' our loop at 2 'cause it's just the littlest, most precious
    # prime ever. I know it looks like this could loop all the way up to
    # sqrt(n), which it will if n is prime, but usually the loop ends
    # much earlier than that because...
    for p in range(2, maxp):
        # ...we're checking if p == copy_n and stopping the loop if it is.
        if p == copy_n:
            break
        # So, since p is just generated from range(), we don't actually know
        # if p is prime or not, so gotta check that. This maxp here
        # is just going to help us avoid looping through primes more than
        # necessary.
        maxp = math.ceil(math.sqrt(p)) + 1
        isprime = True
        # Since we know all the values in primes < p, just loop through
        # them & see if any of them divide p. If not, p is prime.
        for prime in primes:
            if prime > maxp:
                break
            if not (prime % p):
                isprime = False
                break
        # And if it's not prime, go to the next loop.
        if not isprime:
            continue

        # But if it *is* prime, then add it to our list.
        primes.append(p)

        # And divide copy_n by p as much as possible. "while not (copy_n % p)"
        # is faster than "while copy_n % p == 0". Also, we've got this
        # "copy_n != p" check to handle situations where n is the square
        # of a prime. 'Cause otherwise the function would return 1. Ask me
        # how I know.
        while (not (copy_n % p)) and (copy_n != p):
            copy_n /= p
    # And finally, return copy_n. "int" isn't actually needed here, I just
    # wanted to use it here.
    return int(copy_n)


# So, solution 1 is actually the fastest of these functions for the problem
# value, but it's actually super inefficient for numbers with large prime
# factors (or for large primes).
# Here's its calculation times for:
# n = 600851475143 ... 0.029378s
# n = 1000000007 ..... 0.274852s
# n = 10000000019 .... 1.521634s
# It's... ok, but we can do better.


# Solution 3
@time_decorator()
def p0003_solution03(n=600851475143):
    # So again, making a copy of n, but instead of making a list of primes,
    # we can make a *set* of composites.
    # "Why not primes?", you ask.
    # "How about you be patient?", I reply.
    # Anywho, we're using a set 'cause it's (generally) faster to check
    # if a set contains a given value than it is to check in a list.
    copy_n = n
    composites = set()
    # Also, we're bringing maxp back.
    maxp = math.ceil(math.sqrt(copy_n)) + 1
    # So again, same scenario. Looping through p values of unknown
    # primeatude, but usually reducing the number of values we gotta loop
    # through by...
    for p in range(2, maxp):
        # ...breaking the loop early if p >= copy_n.
        if p >= copy_n:
            break
        # Oh, and since we've got this handy set of composites, we can check
        # if p is in it. If it is, *hey, guess what*, it's a composite.
        # If it's composite, we don't care about it and we restart the loop.
        if p in composites:
            continue

        # Again, we're just dividing copy_n by p as much as possible.
        while (not (copy_n % p)) and (copy_n != p):
            copy_n /= p

        # Going to recalculate maxp as the sqrt of our current copy_n
        # value 'cause we want to cap how high the next bit has to loop.
        maxp = math.ceil(math.sqrt(copy_n)) + 1

        # Then we do this fanciness right here. We're taking all the
        # composites generated by p up to the square root of copy_n ('cause
        # we don't need to check higher than that, remember?), and adding
        # them to the set of composites for future reference. However,
        # this right here is why solution 1 is faster when n has relatively
        # small prime factors.
        composites.update(range(p * p, maxp, p))
    # And again, once done looping we just return copy_n.
    return int(copy_n)


# So accessing sets is pretty cool. Let's see some calculation speeds
# for various values of n.
# n = 600851475143 .... 0.049907s
# n = 1000000007 ...... 0.005378s
# n = 10000000019 ..... 0.017095s
# n = 100000000003 .... 0.057224s
# n = 1000000000039 ... 0.203317s
# To quote the great Lightning McQueen, "I am speed".
# "Ok, but why composites and not primes?", you ask again.
# Yeah, ok, about that...


# Solution 4
# I initially wanted to tackle solution 3 using a set of primes, but I
# figured the extra function calls would be too much overhead, so I just
# used composites in that solution. But more on that later.
@time_decorator()
def p0003_solution04(n=600851475143):
    # You know the deal with copy_n.
    copy_n = n
    # But now we're generating a set of potential primes & will remove
    # composites as we find them.
    maxp = math.ceil(math.sqrt(copy_n)) + 1
    primes = set(range(2, maxp))

    for p in range(2, maxp):
        if p >= copy_n:
            break
        # Pretty much the same as solution 3, but with primes.
        if p not in primes:
            continue

        while (not (copy_n % p)) and (copy_n != p):
            copy_n /= p

        maxp = math.ceil(math.sqrt(copy_n)) + 1
        # After I wrote solution 3, I found out about the difference_update
        # function, which seemed like it would be pretty useful and possibly
        # an efficient way to handle this.
        # But...
        primes.difference_update(range(p * p, maxp, p))
    return int(copy_n)


# ...it actually runs slower.
# n = 600851475143 .... 0.073095s
# n = 1000000007 ...... 0.006115s
# n = 10000000019 ..... 0.018486s
# n = 100000000003 .... 0.069313s
# n = 1000000000039 ... 0.228864s
# Guess the difference_update function has more overhead than just a regular
# update function. So anywho, ended up going with solution 3 in the final
# problem_0003.py file.


def main():
    test_cfgs = [
        {'func': p0003_solution02, 'testinds': [0, 1, 2]},
        {'func': p0003_solution03},
        {'func': p0003_solution04},
    ]
    all_testvals = [
        600851475143,
        1000000007,
        10000000019,
        100000000003,
        1000000000039,
    ]
    for cfg in test_cfgs:
        func = cfg['func']
        testinds = cfg.get('testinds')
        print(f'\n*****************************\n{func.__name__}:')
        testvals = all_testvals
        if testinds:
            testvals = [all_testvals[n] for n in testinds]
        for n in testvals:
            func(n)


if __name__ == '__main__':
    main()
