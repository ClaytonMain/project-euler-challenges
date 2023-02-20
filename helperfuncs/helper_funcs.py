# Just some functions I plan to use across multiple challenges.
from functools import wraps
import time


def time_decorator(nloops=100):
    def actual_time_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Could just shove these into a list, but want to save memory.
            time_total = 0
            time_fastest = 999999
            time_slowest = 0
            for _ in range(nloops):
                ts = time.time()
                result = func(*args, **kwargs)
                te = time.time()
                time_exec = te - ts
                time_total += time_exec
                time_fastest = min(time_exec, time_fastest)
                time_slowest = max(time_exec, time_slowest)
            print('\n*** Time Stuff ***')
            print(f'Executions: {nloops}')
            print(f'Total exec. time: {time_total:.6f}s')
            print(f'Avg. exec. time: {time_total/nloops:.6f}s')
            print(f'Fastest: {time_fastest:.6f}s')
            print(f'Slowest: {time_slowest:.6f}s')
            return result

        return wrapper

    return actual_time_decorator
