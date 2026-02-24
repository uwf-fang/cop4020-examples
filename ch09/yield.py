def grep_coroutine(pattern):
    print(f"Looking for '{pattern}'...")

    # 1. First Entry Point: Function start
    while True:
        # 2. Multiple Entry/Exit Points :
        # The 'yield' keyword suspends execution here.
        # It waits to receive data from the caller.
        line = yield

        if pattern in line:
            print(f"Found '{pattern}' in: {line}")

# --- Caller Logic (Symmetric Control) ---

# Initialize the coroutine
search = grep_coroutine("error")

# "Prime" the coroutine
# (Executes until the first yield, then suspends)
next(search)

# The caller and callee now act as equals (Symmetric Control [1]):
# The caller sends data, and the coroutine resumes to process it.
print("Scanning log stream...")
search.send("System starting up")       # No match, coroutine suspends again
search.send("Connection error detected") # Match found! Prints message.
search.send("Retrying connection")      # No match
search.close() # Terminate the coroutine