def safe_operation(func, *args):
    try:
        return func(*args)
    except Exception as e:
        return f"Operation failed: {e}"

print(safe_operation(lambda x, y: x / y, 10, 2))
print(safe_operation(lambda x, y: x / y, 10, 0))
print(safe_operation(lambda x, y: x + y, "Hello, ", "World!"))
print(safe_operation(lambda x, y: x + y, 5, "five"))