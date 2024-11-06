import time

def validate_score(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result.score < 0 or result.score > 100:
            raise ValueError("Score must be between 0 and 100.")
        return result
    return wrapper

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Evaluation time: {end - start:.2f} seconds")
        return result
    return wrapper

