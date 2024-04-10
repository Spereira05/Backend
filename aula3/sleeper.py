import time

def timer(func: callable):
    def wrapper (*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args}{kwargs} Took {total_time:} seconds')
        return time
    return wrapper


