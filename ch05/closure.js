function createCounter() {
  let count = 0; // The Variable & Binding

  return function() { 
    // This inner function is a Closure
    count++; 
    return count;
  };
}

const counter = createCounter(); 
// createCounter() has finished executing here. 
// Normally, 'count' would be gone.
// But the closure "captures" the binding.

console.log(counter()); // 1
console.log(counter()); // 2

// How it is implemented in V8 (or similar engine)
// When a variable is found out-lives its parent, it is moved to heap (from stack)