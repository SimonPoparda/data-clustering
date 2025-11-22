import time
from functools import wraps

def log_time(func):
    """Decorator that logs start, end, and duration of a method"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Rozpoczynam funkcję: {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Zakończono funkcję: {func.__name__}. Czas wykonania: {end - start:.4f} s")
        return result
    return wrapper
