day = "Monday" # Global variable

def tester():
    # Without this line, 'day' would be treated as a new local variable
    # and the print statement would fail (UnboundLocalError) because
    # assignment 'day = ...' makes it local by default.
    global day

    print("The global day is:", day)

    day = "Tuesday" # Modifies the global variable
    print("The new value of day is:", day)

tester()
# Output:
# The global day is: Monday
# The new value of day is: Tuesday