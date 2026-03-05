#ifndef ACCOUNT_H
#define ACCOUNT_H

// Opaque struct: Users know it exists but not what's inside
typedef struct Account Account;

// Constructor/Destructor
Account* create_account(double initial_balance);
void destroy_account(Account* acc);

// Public Methods
void deposit(Account* acc, double amount);
double get_balance(Account* acc);

#endif