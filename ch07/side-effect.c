int a = 5;

int fun1() {
    a = 17; // Side effect: modifies global 'a'
    return 3;
}

void main() {
    // If 'a' is fetched first (value 5), result is 5 + 3 = 8
    // If 'fun1()' is called first (sets a=17), result is 17 + 3 = 20
    a = a + fun1();
}