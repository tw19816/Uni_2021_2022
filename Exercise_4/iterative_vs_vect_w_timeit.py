from re import VERBOSE
import numpy as np
from time import perf_counter


rng = np.random.default_rng()


def timeit(func):
    def inner(*args, **kwargs):
        
        if "VERBOSE" in kwargs.keys():
            VERBOSE = kwargs["VERBOSE"]
            del kwargs["VERBOSE"]
        else:
            VERBOSE = False
        if "n_loops" in kwargs.keys():
            n = kwargs["n_loops"]
            del kwargs["n_loops"]
        else:
            n = 1
        start = perf_counter()
        for i in range(n):
            res = func(*args, **kwargs)
        end = perf_counter()
        time_ms = (end-start)*1000
        if VERBOSE == True:
            print("func:'{}' args:{} took: {:2.4f} ms to run {} times".format(
                func.__name__, args, time_ms, n))
            print(f"Avaerage time per call: {time_ms/n:2.4f} ms")
        return res, time_ms
    return inner

@timeit
def iterative(n, mean, std):
    out = np.zeros(n, dtype=float)
    for i in range(n):
        out[i] = rng.normal(mean, std)

@timeit
def vectorised(n, mean, std):
    out = rng.normal(mean, std, n)


iterative(1000, 5, 1, VERBOSE=True, n_loops=1000)
vectorised(1000, 5, 1, VERBOSE=True, n_loops=1000)


