#include <stdio.h>
#include "account.h"

int main() {
    Account* my_acc = create_account(100.0);

    deposit(my_acc, 50.0);

    // printf("%f", my_acc->balance); // THIS WOULD FAIL COMPILATION!
    printf("Balance: %.2f\n", get_balance(my_acc));

    destroy_account(my_acc);
    return 0;
}