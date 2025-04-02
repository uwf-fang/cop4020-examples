/*
 * File:
 *    thread_hello.cpp
 *
 * Purpose:
 *    Illustrate basic use of C++ threads:  create some threads,
 *    each of which prints a message.
 *
 * Input:
 *    none
 * Output:
 *    message from each thread
 *
 * Compile:  g++ -std=c++11 -Wall -pthread -o cpp_hello thread_hello.cpp
 * Usage:    ./cpp_hello <thread_count>
 */

#include <iostream>
#include <thread>
#include <vector>
#include <cstdlib>

const int MAX_THREADS = 64;

// Global variable: accessible to all threads
int thread_count;

void Usage(const char* prog_name) {
    std::cerr << "usage: " << prog_name << " <number of threads>" << std::endl;
    std::cerr << "0 < number of threads <= " << MAX_THREADS << std::endl;
    exit(0);
}

// Thread function
void Hello(long rank) {
    std::cout << "Hello from thread " << rank << " of " << thread_count << std::endl;
}

int main(int argc, char* argv[]) {
    // Get number of threads from command line
    if (argc != 2) Usage(argv[0]);

    thread_count = std::strtol(argv[1], NULL, 10);
    if (thread_count <= 0 || thread_count > MAX_THREADS) Usage(argv[0]);

    // Create a vector to store threads
    std::vector<std::thread> threads;

    // Launch threads
    for (long thread = 0; thread < thread_count; thread++) {
        threads.push_back(std::thread(Hello, thread));
    }

    std::cout << "Hello from the main thread" << std::endl;

    // Join threads (wait for them to finish)
    for (auto& t : threads) {
        t.join();
    }

    return 0;
}
