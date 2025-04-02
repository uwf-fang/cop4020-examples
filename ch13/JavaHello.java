/*
 * File:
 *    JavaHello.java
 *
 * Purpose:
 *    Illustrate basic use of Java threads: create some threads,
 *    each of which prints a message.
 *
 * Input:
 *    none
 * Output:
 *    message from each thread
 *
 * Compile:  javac JavaHello.java
 * Usage:    java JavaHello <thread_count>
 */

public class JavaHello {
    private static final int MAX_THREADS = 64;

    // Global variable: accessible to all threads
    private static int threadCount;

    public static void main(String[] args) {
        // Get number of threads from command line
        if (args.length != 1) {
            usage(args.length > 0 ? args[0] : "JavaHello");
        }

        try {
            threadCount = Integer.parseInt(args[0]);
        } catch (NumberFormatException e) {
            usage("JavaHello");
        }

        if (threadCount <= 0 || threadCount > MAX_THREADS) {
            usage("JavaHello");
        }

        // Create thread objects
        Thread[] threads = new Thread[threadCount];

        // Start all threads
        for (int i = 0; i < threadCount; i++) {
            final int threadRank = i;  // Need final for lambda
            threads[i] = new Thread(() -> {
                System.out.println("Hello from thread " + threadRank + " of " + threadCount);
            });
            threads[i].start();
        }

        System.out.println("Hello from the main thread");

        // Wait for all threads to complete
        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                System.err.println("Thread interrupted: " + e.getMessage());
            }
        }
    }

    private static void usage(String progName) {
        System.err.println("usage: " + progName + " <number of threads>");
        System.err.println("0 < number of threads <= " + MAX_THREADS);
        System.exit(0);
    }
}