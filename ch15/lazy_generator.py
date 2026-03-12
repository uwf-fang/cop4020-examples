def infinite_integers():
    """A custom generator that counts from 0 to infinity."""
    n = 0
    while True:
        yield n
        n += 1

def is_perfect_square(target):
    # We initialize the generator
    numbers = infinite_integers()

    # We pull values from the generator one by one
    for n in numbers:
        square = n * n

        if square == target:
            return True

        # The "Safety Valve": stop if we pass the target
        if square > target:
            break

    return False

# Testing the logic
print(f"Is 16 a perfect square? {is_perfect_square(16)}") # True
print(f"Is 20 a perfect square? {is_perfect_square(20)}") # False
