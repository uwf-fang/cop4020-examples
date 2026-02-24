// A function that simulates a network request (Coroutine behavior)
function fetchData() {
    return new Promise(resolve => setTimeout(() => resolve("Data Loaded"), 1000));
}

async function mainProcess() {
    console.log("1. Start");

    // Execution SUSPENDS here. Control returns to the system/event loop.
    // This is the "Resume" capability of coroutines.
    const result = await fetchData();

    // Execution RESUMES here when data is ready.
    console.log("2. " + result);
}

mainProcess();
console.log("3. I run while mainProcess is suspended");

// Output Order:
// 1. Start
// 3. I run while mainProcess is suspended
// (1 second delay)
// 2. Data Loaded