// Loose Equality (==) allows coercion
if ("7" == 7) {
    // This executes because string "7" is coerced to number 7
    console.log("Equal with coercion");
}

// Strict Equality (===) disallows coercion
if ("7" === 7) {
    // This does NOT execute. Types (String vs Number) do not match.
    console.log("Strictly equal");
}