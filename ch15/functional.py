# 1. Recursion (Standard - Python lacks native tail-call optimization)
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

# 2. Higher-Order Functions (Map)
# Using a nameless function (lambda) to cube elements.
numbers = [1, 2, 3]
cube_all = list(map(lambda x: x**3, numbers))

# 3. List Comprehensions
# Mirrors the set notation found in Haskell.
even_cubes = [x**3 for x in range(1, 11) if x % 2 == 0]

print(f"Standard 5!: {factorial(5)}")
print(f"Mapped Cubes: {cube_all}")
print(f"Even Cubes: {even_cubes}")
