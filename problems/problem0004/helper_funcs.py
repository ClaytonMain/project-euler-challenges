# Just some functions I plan to use across multiple challenges.
from timeit import timeit


def time_function(func_name, number=100):
    stmt = f'{func_name}()'
    setup = f'from __main__ import {func_name}'
    t = timeit(stmt, setup, number=number)
    print('\n*** Time Stuff ***')
    print(f'Executions: {number}')
    print(f'Total exec. time: {t:.6f}s')
    print(f'Avg. exec. time: {t/number:.6f}s')
