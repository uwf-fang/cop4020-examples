import asyncio

# Definition of a Coroutine
# 'async def' defines a subprogram that can be paused.
async def fetch_data(simulated_delay, task_name):
    print(f"Start: {task_name}")

    # Execution SUSPENDS here.
    # 'await' yields control back to the event loop while waiting.
    # This simulates a non-blocking I/O operation (e.g., DB query or API call).
    await asyncio.sleep(simulated_delay)

    # Execution RESUMES here once the wait is over.
    print(f"Finish: {task_name}")
    return f"{task_name} Result"

# Main Entry Point
async def main():
    print("--- Sequential Execution (Slow) ---")
    # Await pauses 'main' until fetch_data completes.
    await fetch_data(1, "Task A")
    await fetch_data(1, "Task B")

    print("\n--- Concurrent Execution (Fast) ---")
    # Schedule both coroutines to run on the event loop immediately.
    # They run "interleaved" (quasi-concurrency) as described in Source [3].
    task1 = fetch_data(1, "Task C")
    task2 = fetch_data(1, "Task D")

    # Wait for both to complete
    results = await asyncio.gather(task1, task2)
    print(f"Results: {results}")

if __name__ == "__main__":
    asyncio.run(main())