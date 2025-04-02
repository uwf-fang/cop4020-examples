/*
 * File:
 *    go_hello.go
 *
 * Purpose:
 *    Illustrate basic use of Go goroutines: create some threads,
 *    each of which prints a message.
 *
 * Input:
 *    none
 * Output:
 *    message from each thread
 *
 * Compile/Run:  go run thread_hello.go <thread_count>
 */

package main

import (
	"fmt"
	"os"
	"strconv"
	"sync"
)

const MAX_THREADS = 64

// Global variable: accessible to all goroutines
var threadCount int

func usage(progName string) {
	fmt.Fprintf(os.Stderr, "usage: %s <number of threads>\n", progName)
	fmt.Fprintf(os.Stderr, "0 < number of threads <= %d\n", MAX_THREADS)
	os.Exit(0)
}

// Thread function
func hello(rank int, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Printf("Hello from thread %d of %d\n", rank, threadCount)
}

func main() {
	// Get number of threads from command line
	if len(os.Args) != 2 {
		usage(os.Args[0])
	}

	var err error
	threadCount, err = strconv.Atoi(os.Args[1])
	if err != nil {
		usage(os.Args[0])
	}

	if threadCount <= 0 || threadCount > MAX_THREADS {
		usage(os.Args[0])
	}

	// Create a WaitGroup to wait for all goroutines to finish
	var wg sync.WaitGroup
	wg.Add(threadCount)

	// Launch goroutines
	for i := 0; i < threadCount; i++ {
		go hello(i, &wg)
	}

	fmt.Println("Hello from the main thread")

	// Wait for all goroutines to finish
	wg.Wait()
}