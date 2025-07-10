def compute(a, b, op):
    """
    Compute basic operations.
    'div' should return a float when there's no remainder,
    or raise ZeroDivisionError if b == 0.
    """
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        # BUG: uses integer division and swallows ZeroDivisionError
        try:
            return a / b
        except ZeroDivisionError:
            return None
    else:
        raise ValueError(f"Unknown operation: {op}")