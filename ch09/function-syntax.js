const numbers = [7-11];

// Passing a subprogram (arrow function) as a parameter to 'filter'
// Traditional C-style loops are replaced by functional pipelines.
const evens = numbers.filter(n => n % 2 === 0);

// Passing a subprogram to 'map'
const squared = evens.map(n => n * n);

console.log(squared); // Output: [10, 12]