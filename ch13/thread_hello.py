#!/usr/bin/env python3
"""
File:
    thread_hello.py

Purpose:
    Illustrate basic use of Python threads: create some threads,
    each of which prints a message.

Input:
    none
Output:
    message from each thread

Usage:    python thread_hello.py <thread_count>
"""

import sys
import threading

MAX_THREADS = 64

# Global variable: accessible to all threads
thread_count = 0

def usage(prog_name):
    """Print usage message and exit"""
    sys.stderr.write(f"usage: {prog_name} <number of threads>\n")
    sys.stderr.write(f"0 < number of threads <= {MAX_THREADS}\n")
    sys.exit(0)

def hello(rank):
    """Thread function that prints a message"""
    print(f"Hello from thread {rank} of {thread_count}")

def main():
    global thread_count

    # Get number of threads from command line
    if len(sys.argv) != 2:
        usage(sys.argv[0])

    try:
        thread_count = int(sys.argv[1])
    except ValueError:
        usage(sys.argv[0])

    if thread_count <= 0 or thread_count > MAX_THREADS:
        usage(sys.argv[0])

    # Create thread objects
    threads = []
    for thread in range(thread_count):
        t = threading.Thread(target=hello, args=(thread,))
        threads.append(t)

    # Start all threads
    for t in threads:
        t.start()

    print("Hello from the main thread")

    # Wait for all threads to complete
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
