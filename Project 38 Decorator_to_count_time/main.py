import time

def decorator_time_count(function):
    def wrapper_function():
        current_time=time.time()
        function()
        print(f"{function.__name__} Time Taken: {time.time()-current_time}")
    return wrapper_function

@decorator_time_count
def fast_function():
    for i in range(1000000):
        i*i

@decorator_time_count
def slow_function():
    for i in range(10000000):
        i*i
    
fast_function()
slow_function()
