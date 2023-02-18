# Planning:
# Got a few ideas here. The obvious solution would be to start with
# 999*999 => check if pali. => store value if largest pali. => go to
# 999*998 => check if pali. => ...
# ...
# 999*100 => check if pali. => store value if largest pali. => go to
# 998*998 => check if pali. => etc.
# Could probably also skip a bunch of loops by breaking if the product of
# our two three digit numbers is less than our max palindrome.
# Wait. That doesn't sound half bad. I'll go with that.
def p0004(digits=3):
    # Not necessary to get our max and min factors this way since the problem
    # specifies three digit numbers. This way is more fun though.
    max_factor = 10**digits - 1
    min_factor = 10 ** (digits - 1)
    max_pali = 0
    for i in range(max_factor, min_factor, -1):
        # If i ends with 0, then i * j won't be a palindrome, so skip it.
        if not (i % 10):
            continue
        for j in range(i, min_factor, -1):
            # # Same thing for j.
            # if not (j % 10):
            #     continue
            n = i * j

            # No need to keep looping for the remaining j values if
            # n < max_pali since every j remaining in the loop is less than
            # the current j, so every future i * j for the current i loop
            # will be less than the current max_pali.
            if n < max_pali:
                # But if n is already less than the max_pali for the first
                # j value, then we can skip the rest of the i values
                # by following the same logic from above.
                if j == i:
                    return max_pali
                    # break_i_loop = True
                break
            # Numbers ending in 0 won't be palindromes here:
            if not (n % 10):
                continue

            # Alright, if we've made it this far, we need to check if n is
            # a palindrome or not. Make it a string 'cause that's going to
            # simplify the way we check.
            str_n = str(n)
            # Would it be faster to compare the full string to its reversed
            # order, compare the first half to the last half, or to iterate
            # through and compare individual characters? One way to find out.

            # Comparing full string to reversed full string:
            if str_n == str_n[::-1]:
                max_pali = n
            # Exec time: 0.001679s
            # *** Alright, seems this one here is the winner. ***

            # Comparing first half of str_n to reversed last half of str_n:
            # mid_ind = len(str_n) // 2
            # if str_n[:mid_ind] == str_n[: -mid_ind - 1 : -1]:
            #     max_pali = n
            # Exec time: 0.002461s

            # Looping through each ind (full string):
            # len_str_n = len(str_n)
            # for k in range(len_str_n):
            #     if str_n[k] != str_n[-k - 1]:
            #         break
            #     if k + 1 == len_str_n:
            #         max_pali = n
            # Exec time: 0.002705s

            # Looping through each ind (half string):
            # len_str_n = len(str_n)
            # mid_ind = len_str_n // 2
            # for k in range(mid_ind):
            #     if str_n[k] != str_n[-k - 1]:
            #         break
            #     if k + 1 == mid_ind:
            #         max_pali = n
            # Exec time: 0.002902s

    return max_pali
