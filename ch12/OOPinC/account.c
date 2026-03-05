#include "account.h"
#include <stdlib.h>

// Now we define the actual data structure
struct Account {
    double balance;
};

Account* create_account(double initial_balance) {
    Account* acc = malloc(sizeof(Account));
    acc->balance = initial_balance;
    return acc;
}

void deposit(Account* acc, double amount) {
    if (acc && amount > 0) {
        acc->balance += amount;
    }
}

double get_balance(Account* acc) {
    return acc ? acc->balance : 0.0;
}

void destroy_account(Account* acc) {
    free(acc);
}