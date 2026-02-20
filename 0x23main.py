import time

def measure_time(original_function):
    def wrapper_function(*args, **kwargs):
        start = time.time()
        result = original_function(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
        return result
    return wrapper_function

@measure_time
def slow_function():
    time.sleep(1)
    print("Finished slow function")

slow_function()
