// 1. Static Variable
// Bound before execution, remains until program ends.
int globalVar;

void function() {
    // 2. Stack-Dynamic Variable (The default for locals)
    // Bound when declaration is reached; unbound when function exits.
    int stackVar = 10;

    // 3. Explicit Heap-Dynamic Variable
    // Nameless memory cell allocated explicitly by the programmer at runtime.
    // 'intnode' is a pointer (stack-dynamic) pointing to heap memory.
    int *intnode;
    intnode = new int;  // Allocation (bound to heap storage)

    *intnode = 5;

    delete intnode;     // Deallocation (unbound explicitly)
}
