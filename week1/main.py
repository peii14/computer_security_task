import sys

def bound_value(value: int, minimum_value: int = 0, maximum_value: int = 100) -> int:
    return max(minimum_value, min(value, maximum_value))


if __name__ == "__main__":
    value = int(sys.argv[1])
    min_val = int(sys.argv[2]) if len(sys.argv) > 2 else None
    max_val = int(sys.argv[3]) if len(sys.argv) > 3 else None

    args = [arg for arg in [value, min_val, max_val] if arg is not None]
    print(bound_value(*args))
    