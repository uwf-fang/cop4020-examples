#!/usr/bin/env node
/*
 * File:
 *    js_hello.js
 *
 * Purpose:
 *    Illustrate basic use of Node.js Worker Threads: create some threads,
 *    each of which prints a message.
 *
 * Input:
 *    none
 * Output:
 *    message from each thread
 *
 * Usage:    node thread_hello.js <thread_count>
 *
 * Note: This requires Node.js v10.5.0 or later for the worker_threads module
 */

const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');
const path = require('path');

const MAX_THREADS = 64;

// If this is a worker thread
if (!isMainThread) {
    const { rank, threadCount } = workerData;
    console.log(`Hello from thread ${rank} of ${threadCount}`);
    parentPort.postMessage('done');
    return;
}

// Main thread code
function usage(progName) {
    console.error(`usage: ${progName} <number of threads>`);
    console.error(`0 < number of threads <= ${MAX_THREADS}`);
    process.exit(0);
}

// Get number of threads from command line
const args = process.argv.slice(2);
if (args.length !== 1) {
    usage(process.argv[0]);
}

const threadCount = parseInt(args[0], 10);
if (isNaN(threadCount) || threadCount <= 0 || threadCount > MAX_THREADS) {
    usage(process.argv[0]);
}

// Track completed workers
let completedWorkers = 0;

// Launch worker threads
console.log("Hello from the main thread");

for (let i = 0; i < threadCount; i++) {
    const worker = new Worker(__filename, {
        workerData: {
            rank: i,
            threadCount: threadCount
        }
    });

    // Listen for worker completion
    worker.on('message', () => {
        completedWorkers++;
        if (completedWorkers === threadCount) {
            // All workers have completed
        }
    });

    worker.on('error', (err) => {
        console.error(`Worker error: ${err}`);
    });
}