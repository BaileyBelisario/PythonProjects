#define speed test decorator
from functools import wraps
from time import time
def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {t2 - t1}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(100000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(100000000)])


print(sum_nums_gen())
print(sum_nums_list())
