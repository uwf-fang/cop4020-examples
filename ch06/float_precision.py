# Demonstrating Floating-Point Inaccuracy
val = 0.1
sum_val = 0.0

# Add 0.1 ten times
for i in range(10):
    sum_val += val

# Theoretically, sum_val should be 1.0
print(f"Calculated Sum: {sum_val:.20f}")

# Check equality
if sum_val == 1.0:
    print("Equal to 1.0")
else:
    print("Not equal to 1.0 due to precision loss")

# Output usually shows: 0.99999999999999988898
